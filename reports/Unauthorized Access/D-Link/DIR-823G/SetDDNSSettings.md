## Overview

- Manufacturer's website information：http://www.dlink.com.cn/
- Firmware download address ：http://www.dlink.com.cn/techsupport/ProductInfo.aspx?m=DIR-823G

## Affected version

DIR823G_V1.0.2B05_20181207

## Vulnerability details

An improper access control vulnerability exists in the web management interface of DIR823G_V1.0.2B05_20181207. By sending a specially crafted unauthenticated HTTP POST request to the `/HNAP1/` endpoint with the `SOAPAction` header set to `SetDDNSSettings `, an attacker can enable or disable the DDNS service of the device.

## POC

![image-20250408234242127](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250408234242127.png)

![image-20250408234256687](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250408234256687.png)
