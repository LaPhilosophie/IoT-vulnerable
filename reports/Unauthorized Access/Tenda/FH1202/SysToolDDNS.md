## Overview

- Firmware download website: https://www.tenda.com.cn/download/detail-2079.html

## Affected version

FH1202 V1.2.0.14(408)

## Vulnerability details

An improper access control vulnerability exists in the web management interface of In FH1202 V1.2.0.14(408). By sending a specially crafted unauthenticated HTTP POST request to the `goform` endpoint with `SysToolDDNS `, an attacker can set the DDNS settings of the device.

## POC

![image-20250320161324947](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320161324947.png)

![image-20250320161313708](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320161313708.png)
