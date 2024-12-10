# reverseKey

### Language

- [English](#english)
- [中文](#中文)

---

### English
#### AES

AES round key calculation, [Stark](https://github.com/SideChannelMarvels/Stark) implement with python

reverseKey can

* print all round keys from the AES key;
* print all round keys from any intermediate or final round key(s).

Usage:

```
reverseKey.exe AES_key_in_hex
reverseKey.exe Round_key(s)_in_hex Initial_round_key_number_between_0_and_10#11#13
```

The AES key size is deduced from the size of the parameter, so

* for AES-128, provide one round key and its index
* for AES-192, provide one round key concatenated with the first half of the next round key and the index of the starting round key
* for AES-256, provide two concatenated round keys and the index of the starting round key

Examples:

* AES-128: (provide 1 round key)

```
python reverseKey.py B1BA2737C83233FE7F7A7DF0FBB01D4A
python reverseKey.py 97F926D5677B324AC439D77C8B03FDF8 5
python reverseKey.py FAEF63792F9A97A1FB78C88C4CA7048F 10
```

* AES-192: (provide 1.5 round keys)

```
python reverseKey.py B1BA2737C83233FE7F7A7DF0FBB01D4A7835FA62BE9726A1
python reverseKey.py D42AAFEB1510F368D8AA1354A707697696D6CC20F7737995 5
python reverseKey.py 504B601C4EEB5C33B3D208B8E4966BA37B07118538961350 11
```

* AES-256: (provide 2 round keys)

```
python reverseKey.py B1BA2737C83233FE7F7A7DF0FBB01D4A7835FA62BE9726A1BB39F261BAC4729C
python reverseKey.py F2E96B6FD53C1BBB49D0990E6FF86927DF8F909C21310695C43D2751C133AC12 5
python reverseKey.py 4D69A4975189FCA00DB0AC8F686EE58C033BE6307A3C13C226DF38591EEAC857 13
```

---

### 中文

#### AES

AES 轮密钥计算, [Stark](https://github.com/SideChannelMarvels/Stark) 的 python 版本

reverseKey 功能

* 通过当前 AES 密钥输出所有轮密钥；
* 通过任意一轮密钥输出所有轮密钥；

用法:

```
python reverseKey.py AES_key_in_hex
python reverseKey.py Round_key(s)_in_hex Initial_round_key_number_between_0_and_10#11#13
```

AES密钥长度是通过参数的长度来决定的

* 对于 AES-128，提供 1 轮秘钥及其轮次
* 对于 AES-192，提供 1.5 轮秘钥及其轮次
* 对于 AES-256，提供 2 轮秘钥及其轮次

举例:

* AES-128: (提供1轮密钥)

```
python reverseKey.py B1BA2737C83233FE7F7A7DF0FBB01D4A
python reverseKey.py 97F926D5677B324AC439D77C8B03FDF8 5
python reverseKey.py FAEF63792F9A97A1FB78C88C4CA7048F 10
```

* AES-192: (提供1.5轮密钥)

```
python reverseKey.py B1BA2737C83233FE7F7A7DF0FBB01D4A7835FA62BE9726A1
python reverseKey.py D42AAFEB1510F368D8AA1354A707697696D6CC20F7737995 5
python reverseKey.py 504B601C4EEB5C33B3D208B8E4966BA37B07118538961350 11
```

* AES-256: (提供2轮密钥)

```
python reverseKey.py B1BA2737C83233FE7F7A7DF0FBB01D4A7835FA62BE9726A1BB39F261BAC4729C
python reverseKey.py F2E96B6FD53C1BBB49D0990E6FF86927DF8F909C21310695C43D2751C133AC12 5
python reverseKey.py 4D69A4975189FCA00DB0AC8F686EE58C033BE6307A3C13C226DF38591EEAC857 13
```

---

### 