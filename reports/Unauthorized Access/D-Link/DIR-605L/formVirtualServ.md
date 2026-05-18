## Overview

- Manufacturer's website information：http://www.dlink.com.cn/
- Firmware download address ：https://www.dlink.com.cn/techsupport/ProductInfo.aspx?m=DIR-605L

## Affected version

DIR-605L C1 3.02

## Vulnerability details

An improper access control vulnerability exists in the web management interface of DIR-605L C1 3.02. By sending a specially crafted unauthenticated HTTP POST request to the `goform` endpoint with the header set to `formVirtualServ`, an attacker can set the virtual service of the device.

## POC

![image-20250308172036447](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250308172036447.png)

![image-20250309140247232](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250309140247232.png)
