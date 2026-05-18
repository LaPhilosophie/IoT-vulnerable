## Overview

- Firmware download website: https://www.tenda.com.cn/download/detail-2079.html

## Affected version

FH1202 V1.2.0.14(408)

## Vulnerability details

In FH1202 V1.2.0.14(408), an attacker can obtain the configuration file without authorization through `/default.cfg`. When making a request to `/default.cfg` and `/nvram_default.cfg`, the attacker can obtain the configuration file `default.cfg` or `nvram_default.cfg` without authorization. The login password can be found in the decoded file in these parameters.

## POC

The default password is `12345678`

![image-20250320145919879](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250320145919879.png)
