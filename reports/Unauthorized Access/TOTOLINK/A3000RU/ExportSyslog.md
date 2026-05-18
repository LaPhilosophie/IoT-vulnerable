## Overview

- Manufacturer's website information：https://www.totolink.net/
- Firmware download address ：https://totolink.com.my/products/a3000ru/

## Affected version

A3000RU_Firmware V5.9c.5185

## Vulnerability details

In TOTOLINK A3000RU_Firmware V5.9c.5185, an attacker can obtain the apmib configuration file without authorization through /cgi-bin/ExportSyslog.sh. When making a request to `/cgi-bin/ExportSyslog.sh`, the attacker can obtain the `syslog` configuration file syslog--xxxxxxxx.dat without authorization.

## POC

```sh
#!/bin/sh
#output HTTP header
eval `flash get HARDWARE_MODEL`
dateStr=`date  '+%Y%m%d'`
filename=\"syslog-$HARDWARE_MODEL-$dateStr.dat\"

echo "Pragma: no-cache"
echo "Cache-control: no-cache"
echo "Content-type: application/x-targz"
echo "Content-Transfer-Encoding: gzip, deflate"
echo "Content-Disposition: attachment; filename=$filename"
echo ""
cat /var/log/messages 2>/dev/null

```

![image-20250317145523577](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250317145523577.png)
