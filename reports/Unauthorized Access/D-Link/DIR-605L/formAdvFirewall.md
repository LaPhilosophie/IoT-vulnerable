## Overview

- Manufacturer's website information：http://www.dlink.com.cn/
- Firmware download address ：https://www.dlink.com.cn/techsupport/ProductInfo.aspx?m=DIR-605L

## Affected version

DIR-605L C1 3.02

## Vulnerability details

An improper access control vulnerability exists in the web management interface of DIR-605L C1 3.02. By sending a specially crafted unauthenticated HTTP POST request to the `goform` endpoint with the header set to `formAdvFirewall`, an attacker can set the firewall and DMZ service of the device.

## POC

![image-20250308172946049](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250308172946049.png)

![image-20250308173004481](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250308173004481.png)
