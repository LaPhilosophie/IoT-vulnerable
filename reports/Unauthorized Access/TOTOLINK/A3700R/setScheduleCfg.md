## Overview

- Manufacturer's website information：https://www.totolink.net/
- Firmware download address ：https://www.totolink.net/data/upload/20200728/311b3ec5b0a8e61af298aebda158ec9b.zip

## Affected version

A3700R V9.1.2u.5822_B20200513

## Vulnerability details

An improper access control vulnerability exists in the web management interface of A3700R V9.1.2u.5822_B20200513. By sending a specially crafted unauthenticated HTTP POST request to the `topicurl` endpoint with the header set to `setScheduleCfg`, an attacker can set the reboot schedule of the device.

## POC

![image-20250404204151196](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250404204151196.png)

![image-20250404204205302](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250404204205302.png)
