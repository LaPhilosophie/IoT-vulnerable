## Overview

- Firmware download website: https://www.tenda.com.cn/download/detail-2079.html

## Affected version

FH1202 V1.2.0.14(408)

## Vulnerability details

An improper access control vulnerability exists in the web management interface of In FH1202 V1.2.0.14(408). By sending a specially crafted unauthenticated HTTP POST request to the `goform` endpoint with `AdvSetWrl `, an attacker can set the advance settings of the device.

## POC

![image-20250320155343662](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320155343662.png)

![image-20250320155355008](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320155355008.png)
