## Overview

- Manufacturer's website information：http://www.dlink.com.cn/
- Firmware download address ：http://www.dlink.com.cn/techsupport/ProductInfo.aspx?m=DIR-878

## Affected version

DIR-878 HW:A1 FW:1.03

## Vulnerability details

An improper access control vulnerability exists in the web management interface of DIR-878 HW:A1 FW:1.03. By sending a specially crafted unauthenticated HTTP POST request to the header set to `dllog.cgi`, an attacker can view the device log.

## POC

![image-20250105234627422](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250105234627422.png)
