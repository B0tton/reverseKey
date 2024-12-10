# -------------------------------------------------------------------------------
# Author:       Botton
# Date:         2024/12/5
# -------------------------------------------------------------------------------

import sys

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

Rcon = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)

roundMap = {16: 10, 24: 12, 32: 14}


def shiftRound(array, num):
    '''
    :param array: 需要循环左移的数组
    :param num: 循环左移的位数
    :return: 使用Python切片，返回循环左移num个单位的array
    '''
    return array[num:] + array[:num]


def g(array, round):
    # 首先循环左移1位
    array = shiftRound(array, 1)
    # 字节替换
    array = [Sbox[i] for i in array]
    # 首字节和rcon中对应元素异或
    array = [(Rcon[round] ^ array[0])] + array[1:]
    return array


def xorTwoArray(array1, array2):
    '''
    返回两个数组逐元素异或的新数组
    :param array1: 一个array
    :param array2: 另一个array
    :return:
    '''
    assert len(array1) == len(array2)
    return [array1[i] ^ array2[i] for i in range(len(array1))]


def showRoundKeys(roundKeys):
    for i in range(0, len(roundKeys), 4):
        if None in roundKeys[i:i + 4]:
            continue
        roundKey = sum(roundKeys[i:i + 4], [])
        print("K%02d: " % (i // 4) + "".join("%02X" % k for k in roundKey))


def keyExpand(roundKey, round):
    roundKey = list(bytes.fromhex(roundKey))
    roundCnt = roundMap[len(roundKey)]
    iterationSize = len(roundKey) // 4
    W = [None] * (roundCnt + 1) * 4
    W[round * 4:round * 4 + iterationSize] = [[roundKey[i], roundKey[i + 1], roundKey[i + 2], roundKey[i + 3]]
                                              for i in range(0, len(roundKey), 4)]
    # 防止超出范围
    W = W[:(roundCnt + 1) * 4]
    for idx in range(round * 4 + iterationSize, len(W)):
        if idx % iterationSize == 0:
            W[idx] = xorTwoArray(g(W[idx - 1], idx // iterationSize), W[idx - iterationSize])
        elif iterationSize == 8 and idx % iterationSize == 4:
            W[idx] = xorTwoArray([Sbox[b] for b in W[idx - 1]], W[idx - iterationSize])
        else:
            W[idx] = xorTwoArray(W[idx - 1], W[idx - iterationSize])

    for idx in range(round * 4 - 1, -1, -1):
        if idx % iterationSize == 0:
            W[idx] = xorTwoArray(g(W[idx + iterationSize - 1], (idx // iterationSize) + 1), W[idx + iterationSize])
        elif iterationSize == 8 and idx % iterationSize == 4:
            W[idx] = xorTwoArray([Sbox[b] for b in W[idx + iterationSize - 1]], W[idx + iterationSize])
        else:
            W[idx] = xorTwoArray(W[idx + iterationSize - 1], W[idx + iterationSize])

    showRoundKeys(W)

def is_valid_hex_string(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def main():
    if len(sys.argv) < 2:
        suffix = sys.argv[0].split('.')[-1]
        command = sys.argv[0]
        if suffix == 'py':
            command = 'python ' + command
        print(f"Usage:")
        print(f"{command} AES_key_in_hex")
        print(f"{command} Round_key(s)_in_hex Initial_round_key_number_between_0_and_10#11#13")
        print("Examples:")
        print("- AES-128: (provide 1 round key)")
        print(f"  {command} B1BA2737C83233FE7F7A7DF0FBB01D4A")
        print(f"  {command} 97F926D5677B324AC439D77C8B03FDF8 5")
        print(f"  {command} FAEF63792F9A97A1FB78C88C4CA7048F 10")
        print("- AES-192: (provide 1.5 round keys)")
        print(f"  {command} B1BA2737C83233FE7F7A7DF0FBB01D4A7835FA62BE9726A1")
        print(f"  {command} D42AAFEB1510F368D8AA1354A707697696D6CC20F7737995 5")
        print(f"  {command} 504B601C4EEB5C33B3D208B8E4966BA37B07118538961350 11")
        print("  Tip: check if the second half round key is the same as yours. If not => AES-256")
        print("- AES-256: (provide 2 round keys)")
        print(f"  {command} B1BA2737C83233FE7F7A7DF0FBB01D4A7835FA62BE9726A1BB39F261BAC4729C")
        print(f"  {command} F2E96B6FD53C1BBB49D0990E6FF86927DF8F909C21310695C43D2751C133AC12 5")
        print(f"  {command} 4D69A4975189FCA00DB0AC8F686EE58C033BE6307A3C13C226DF38591EEAC857 13")
        sys.exit(1)
    roundKey = sys.argv[1]
    if len(roundKey) not in (32, 48, 64):
        print("Error: AES_key must be 16, 24 or 32-byte long")
        sys.exit(1)

    if not is_valid_hex_string(roundKey):
        print("Error: AES_key contains invalid hex characters")
        sys.exit(1)

    round = 0
    if len(sys.argv) > 2:
        try:
            round = int(sys.argv[2])
        except ValueError:
            print("Error: Round must be an integer")
            sys.exit(1)

        if round < 0:
            print("Error: Round invalid")
            sys.exit(1)

        if len(roundKey) == 32 and round > 10:
            print("Error: Round must be less than or equal 10")
            sys.exit(1)
        elif len(roundKey) == 48 and round > 11:
            print("Error: Round must be less than or equal 11")
            sys.exit(1)
        elif len(roundKey) == 64 and round > 13:
            print("Error: Round must be less than or equal 13")
            sys.exit(1)

    keyExpand(roundKey, round)


if __name__ == '__main__':
    main()