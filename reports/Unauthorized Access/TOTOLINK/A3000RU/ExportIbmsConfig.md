## Overview

- Manufacturer's website information：https://www.totolink.net/
- Firmware download address ：https://totolink.com.my/products/a3000ru/

## Affected version

A3000RU_Firmware V5.9c.5185

## Vulnerability details

In TOTOLINK A3000RU_Firmware V5.9c.5185, an attacker can obtain the ibms configuration file without authorization through /cgi-bin/ExportIbmsConfig.sh. When making a request to `/cgi-bin/ExportIbmsConfig.sh`, the attacker can obtain the `ibms` configuration file ibms_config-xxxxxxxx.tar.gz without authorization.

## POC

```sh
#!/bin/sh
#output HTTP header
dateStr=`date  '+%Y%m%d'`
filename=\"ibms_config-$dateStr.tar.gz\"

echo "Pragma: no-cache"
echo "Cache-control: no-cache"
echo "Content-type: application/x-targz"
echo "Content-Transfer-Encoding: gzip, deflate"
echo "Content-Disposition: attachment; filename=$filename"
echo ""

cd /mnt
tar -cf /tmp/ibms_config.tar ibms_config
cd /tmp
gzip ibms_config.tar

cat /tmp/ibms_config.tar.gz 2>/dev/null

```

![image-20250317145251793](https://raw.githubusercontent.com/abcdefg-png/images2/main/image-20250317145251793.png)
