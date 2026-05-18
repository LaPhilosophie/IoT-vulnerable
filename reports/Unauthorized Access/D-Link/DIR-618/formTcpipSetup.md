## Overview

- Manufacturer's website information：http://www.dlink.com.cn/
- Firmware download address ：https://www.dlink.com.cn/techsupport/ProductInfo.aspx?m=DIR-618

## Affected version

DIR-618 Bx 2.02

## Vulnerability details

An improper access control vulnerability exists in the web management interface of DIR-618 Bx 2.02. By sending a specially crafted unauthenticated HTTP POST request to the `goform` endpoint with the header set to `formTcpipSetup`, an attacker can set the tcpip service of the device.

## POC

![image-20250308165807625](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250308165807625.png)

![image-20250308165840179](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250308165840179.png)