## Overview

- Firmware download website: https://www.tenda.com.cn/download/detail-2079.html

## Affected version

FH1202 V1.2.0.14(408)

## Vulnerability details

An improper access control vulnerability exists in the web management interface of In FH1202 V1.2.0.14(408). By sending a specially crafted unauthenticated HTTP POST request to the `goform` endpoint with `qossetting `, an attacker can set the qos settings of the device.

## POC

![image-20250320161041568](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320161041568.png)

![image-20250320161033140](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320161033140.png)
