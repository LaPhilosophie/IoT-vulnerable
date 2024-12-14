# IoT-vulnerable

- [Tenda Vulnerabilities](#Tenda)
- [TOTOLINK Vulnerabilities](#TOTOLINK)
- [TP-LINK Vulnerabilities](#TP-LINK)
- [D-Link Vulnerabilities](#D-Link)

## Tenda

We discover vulnerabilities in **30** different router product of **Tenda**, revealed **258 vulnerabilities** and obtained **232 CVEs**, which is listed below.

|     Tenda  Routers      |    Vulnerable  function    |      CVE       | Type of vulnerability |
| :---------------------: | :------------------------: | :------------: | :-------------------: |
|    A18 V15.13.07.09     |   fromSetWirelessRepeat    | CVE-2024-2546  |    Buffer Overflow    |
|  AC7V1.0 V15.03.06.44   |       formQuickIndex       | CVE-2024-2891  |    Buffer Overflow    |
|                         |         formSetCfm         | CVE-2024-2892  |    Buffer Overflow    |
|                         |     formSetDeviceName      | CVE-2024-2893  |    Buffer Overflow    |
|                         |       formSetQosBand       | CVE-2024-2894  |    Buffer Overflow    |
|                         |       formWifiWpsOOB       | CVE-2024-2895  |    Buffer Overflow    |
|                         |      formWifiWpsStart      | CVE-2024-2896  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-2897  |   Command Injection   |
|                         |     fromSetRouteStatic     | CVE-2024-2898  |    Buffer Overflow    |
|                         |   fromSetWirelessRepeat    | CVE-2024-2899  |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-2900  |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-2901  |    Buffer Overflow    |
|                         |   fromSetWifiGusetBasic    | CVE-2024-2902  |    Buffer Overflow    |
|                         |    GetParentControlInfo    | CVE-2024-2903  |    Buffer Overflow    |
|                         |       formexecommand       | CVE-2024-32281 |   Command Injection   |
|                         |      fromWizardHandle      | CVE-2024-32301 |    Buffer Overflow    |
|   AC8v4  V16.03.34.09   |   R7WebsSecurityHandler    | CVE-2024-4064  |    Buffer Overflow    |
|                         |     formSetRebootTimer     | CVE-2024-4065  |    Buffer Overflow    |
|                         |    fromAdvSetMacMtuWan     | CVE-2024-4066  |    Buffer Overflow    |
| AC10v4.0  V16.03.10.13  |     fromSetRouteStatic     | CVE-2024-2581  |    Buffer Overflow    |
|                         |       fromSetSysTime       | CVE-2024-2856  |    Buffer Overflow    |
|                         |  formWanParameterSetting   | CVE-2024-32317 |    Buffer Overflow    |
| AC10Uv1.0 V15.03.06.48  |      formSetSambaConf      | CVE-2024-2853  |   Command Injection   |
|                         |      addWifiMacFilter      | CVE-2024-2711  |    Buffer Overflow    |
|                         |         formSetCfm         | CVE-2024-2763  |    Buffer Overflow    |
|                         |     formSetPPTPServer      | CVE-2024-2764  |    Buffer Overflow    |
|                         |     formSetClientState     | CVE-2024-30612 |    Buffer Overflow    |
|                         |      fromWizardHandle      | CVE-2024-32306 |    Buffer Overflow    |
| AC10Uv1.0 V15.03.06.49  |     formSetDeviceName      | CVE-2024-2703  |    Buffer Overflow    |
|                         |     formSetFirewallCfg     | CVE-2024-2704  |    Buffer Overflow    |
|                         |       formSetQosBand       | CVE-2024-2705  |    Buffer Overflow    |
|                         |      formWifiWpsStart      | CVE-2024-2706  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-2707  |   Command Injection   |
|                         |       formexeCommand       | CVE-2024-2708  |    Buffer Overflow    |
|                         |     fromSetRouteStatic     | CVE-2024-2709  |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-2710  |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-32284 |   Command Injection   |
|    AC15 V15.03.05.18    |   R7WebsSecurityHandler    | CVE-2024-2815  |    Buffer Overflow    |
|                         |     fromSysToolReboot      | CVE-2024-2816  |         CSRF          |
|                         |   fromSysToolRestoreSet    | CVE-2024-2817  |         CSRF          |
|                         |   saveParentControlInfo    | CVE-2024-2850  |    Buffer Overflow    |
|                         |      formSetSambaConf      | CVE-2024-2851  |   Command Injection   |
|                         |  setSmartPowerManagement   | CVE-2024-30613 |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-30840 |    Buffer Overflow    |
|                         |      fromWizardHandle      | CVE-2024-32303 |    Buffer Overflow    |
|    AC15 V15.03.05.20    |      formSetSpeedWan       | CVE-2024-2805  |    Buffer Overflow    |
|                         |      addWifiMacFilter      | CVE-2024-2806  |    Buffer Overflow    |
|                         |     formExpandDlnaFile     | CVE-2024-2807  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-2808  |    Buffer Overflow    |
|                         |     formSetFirewallCfg     | CVE-2024-2809  |    Buffer Overflow    |
|                         |       formWifiWpsOOB       | CVE-2024-2810  |    Buffer Overflow    |
|                         |      formWifiWpsStart      | CVE-2024-2811  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-2812  |   Command Injection   |
|                         | form_fast_setting_wifi_set | CVE-2024-2813  |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-2814  |    Buffer Overflow    |
|                         |       fromSetSysTime       | CVE-2024-2855  |    Buffer Overflow    |
|                         |      formsetUsbUnload      | CVE-2024-30645 |   Command Injection   |
|    AC18 V15.03.05.05    |      formSetSpeedWan       | CVE-2024-2485  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-2486  |    Buffer Overflow    |
|                         |     formSetDeviceName      | CVE-2024-2487  |    Buffer Overflow    |
|                         |     formSetPPTPServer      | CVE-2024-2488  |    Buffer Overflow    |
|                         |       formSetQosBand       | CVE-2024-2489  |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-2490  |    Buffer Overflow    |
|                         |   R7WebsSecurityHandler    | CVE-2024-2547  |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-2558  |    Buffer Overflow    |
|                         |     fromSysToolReboot      | CVE-2024-2559  |         CSRF          |
|                         |   fromSysToolRestoreSet    | CVE-2024-2560  |         CSRF          |
|                         |      formSetSambaConf      | CVE-2024-2854  |   Command Injection   |
|                         |       fromAddressNat       | CVE-2024-28535 |    Buffer Overflow    |
|                         |    fromNatStaticSetting    | CVE-2024-28537 |    Buffer Overflow    |
|                         |      formsetUsbUnload      | CVE-2024-28545 |   Command Injection   |
|                         |     formSetFirewallCfg     | CVE-2024-28547 |    Buffer Overflow    |
|                         |     formExpandDlnaFile     | CVE-2024-28550 |    Buffer Overflow    |
|                         | form_fast_setting_wifi_set | CVE-2024-28551 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-28553 |    Buffer Overflow    |
|                         |      fromWizardHandle      | CVE-2024-32305 |    Buffer Overflow    |
|  AC500 V2.0.1.9(1307)   |     bsSecurityHandler      | CVE-2024-3905  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-3906  |    Buffer Overflow    |
|                         |         formSetCfm         | CVE-2024-3907  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-3908  |   Command Injection   |
|                         |       formexeCommand       | CVE-2024-3909  |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-3910  |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-32314 |   Command Injection   |
|                         |     fromDhcpListClient     | CVE-2024-32316 |    Buffer Overflow    |
|                         |      fromSetVlanInfo       | CVE-2024-32318 |    Buffer Overflow    |
|                         |      formSetTimeZome       | CVE-2024-32320 |    Buffer Overflow    |
|     AX1803 V1.0.0.1     |     formSetSysToolDDNS     | CVE-2024-4236  |    Buffer Overflow    |
|    AX1806  V1.0.0.1     |   R7WebsSecurityHandler    | CVE-2024-4237  |    Buffer Overflow    |
|                         |     formSetDeviceName      | CVE-2024-4238  |    Buffer Overflow    |
|                         |     formSetRebootTimer     | CVE-2024-4239  |    Buffer Overflow    |
|  F1202 V1.2.0.20(408)   |        fromNatlimit        | CVE-2024-3875  |    Buffer Overflow    |
|                         |       fromqossetting       | CVE-2024-3876  |    Buffer Overflow    |
|                         |       fromVirtualSer       | CVE-2024-3877  |    Buffer Overflow    |
|                         |  fromwebExcptypemanFilter  | CVE-2024-3878  |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30634 |    Buffer Overflow    |
|                         |         formSetCfm         | CVE-2024-30635 |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-30636 |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-30637 |   Command Injection   |
|                         |       fromAddressNat       | CVE-2024-30638 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30639 |    Buffer Overflow    |
|     F1203 V2.0.1.6      |   R7WebsSecurityHandler    | CVE-2024-2976  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-2977  |    Buffer Overflow    |
|                         |         formSetCfm         | CVE-2024-2978  |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-2979  |    Buffer Overflow    |
|                         |       formexecommand       | CVE-2024-32280 |   Command Injection   |
|                         |      fromWizardHandle      | CVE-2024-32310 |    Buffer Overflow    |
|                         |  formWanParameterSetting   | CVE-2024-32312 |    Buffer Overflow    |
|  FH1202 V1.2.0.14(408)  |       formexeCommand       | CVE-2024-2980  |    Buffer Overflow    |
|                         | form_fast_setting_wifi_set | CVE-2024-2981  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-2982  |   Command Injection   |
|                         |     formSetClientState     | CVE-2024-2983  |    Buffer Overflow    |
|                         |         formSetCfm         | CVE-2024-2984  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-2985  |    Buffer Overflow    |
|                         |      formSetSpeedWan       | CVE-2024-2986  |    Buffer Overflow    |
|                         |    GetParentControlInfo    | CVE-2024-2987  |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30583 |    Buffer Overflow    |
|                         |      formWifiBasicSet      | CVE-2024-30584 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30585 |    Buffer Overflow    |
|                         |      formWifiBasicSet      | CVE-2024-30586 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30587 |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-30588 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30589 |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-30590 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30591 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30592 |    Buffer Overflow    |
|                         |     formSetDeviceName      | CVE-2024-30593 |    Buffer Overflow    |
|                         |      addWifiMacFilter      | CVE-2024-30594 |    Buffer Overflow    |
|                         |      addWifiMacFilter      | CVE-2024-30595 |    Buffer Overflow    |
|                         |     formSetDeviceName      | CVE-2024-30596 |    Buffer Overflow    |
|                         |       formexecommand       | CVE-2024-32282 |   Command Injection   |
|                         |      fromWizardHandle      | CVE-2024-32302 |    Buffer Overflow    |
|                         |  formWanParameterSetting   | CVE-2024-32315 |    Buffer Overflow    |
|     FH1203 V2.0.1.6     |      fromRouteStatic       | CVE-2024-2988  |    Buffer Overflow    |
|                         |    fromNatStaticSetting    | CVE-2024-2989  |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-2990  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-2991  |   Command Injection   |
|                         |         formSetCfm         | CVE-2024-2992  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-2993  |    Buffer Overflow    |
|                         |    GetParentControlInfo    | CVE-2024-2994  |    Buffer Overflow    |
|                         |      formWifiBasicSet      | CVE-2024-30597 |    Buffer Overflow    |
|                         |      formWifiBasicSet      | CVE-2024-30598 |    Buffer Overflow    |
|                         |      addWifiMacFilter      | CVE-2024-30599 |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-30600 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30601 |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-30602 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30603 |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-30604 |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-30606 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30607 |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-32283 |   Command Injection   |
|                         |      fromWizardHandle      | CVE-2024-32299 |    Buffer Overflow    |
|                         |  formWanParameterSetting   | CVE-2024-32311 |    Buffer Overflow    |
|  FH1205 V2.0.0.7(775)   |      fromRouteStatic       | CVE-2024-3006  |    Buffer Overflow    |
|                         |    fromNatStaticSetting    | CVE-2024-3007  |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-3008  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-3009  |   Command Injection   |
|                         |         formSetCfm         | CVE-2024-3010  |    Buffer Overflow    |
|                         |       formQuickIndex       | CVE-2024-3011  |    Buffer Overflow    |
|                         |    GetParentControlInfo    | CVE-2024-3012  |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30622 |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-30623 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30624 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30625 |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-30626 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30627 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-30628 |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-30629 |    Buffer Overflow    |
|                         |   saveParentControlInfo    | CVE-2024-30630 |    Buffer Overflow    |
|                         |        setSchedWifi        | CVE-2024-30631 |    Buffer Overflow    |
|                         |      formWifiBasicSet      | CVE-2024-30632 |    Buffer Overflow    |
|                         |      formWifiBasicSet      | CVE-2024-30633 |    Buffer Overflow    |
|                         |       formexecommand       | CVE-2024-32279 |   Command Injection   |
|                         |      fromWizardHandle      | CVE-2024-32307 |    Buffer Overflow    |
|                         |  formWanParameterSetting   | CVE-2024-32313 |    Buffer Overflow    |
|    TX9  22.03.02.10     |         sub_42BD7C         | CVE-2024-4111  |    Buffer Overflow    |
|                         |         sub_42CB94         | CVE-2024-4112  |    Buffer Overflow    |
|                         |         sub_42D4DC         | CVE-2024-4113  |    Buffer Overflow    |
|                         |         sub_42C014         | CVE-2024-4114  |    Buffer Overflow    |
|   W9  V1.0.0.7(4456)    |  formQosManageDouble_user  | CVE-2024-4240  |    Buffer Overflow    |
|                         |  formQosManageDouble_auto  | CVE-2024-4241  |    Buffer Overflow    |
|                         |       formwrlSSIDget       | CVE-2024-4242  |    Buffer Overflow    |
|                         |       formwrlSSIDset       | CVE-2024-4243  |    Buffer Overflow    |
|                         |       fromDhcpSetSer       | CVE-2024-4244  |    Buffer Overflow    |
|  W15EV1.0 V15.11.0.14   |     formAddDnsForward      | CVE-2024-4115  |    Buffer Overflow    |
|                         |      formDelDhcpRule       | CVE-2024-4116  |    Buffer Overflow    |
|                         |     formDelPortMapping     | CVE-2024-4117  |    Buffer Overflow    |
|                         |      formIPMacBindAdd      | CVE-2024-4118  |    Buffer Overflow    |
|                         |      formIPMacBindDel      | CVE-2024-4119  |    Buffer Overflow    |
|                         |    formIPMacBindModify     | CVE-2024-4120  |    Buffer Overflow    |
|                         |       formQOSRuleDel       | CVE-2024-4121  |    Buffer Overflow    |
|                         |      formSetDebugCfg       | CVE-2024-4122  |    Buffer Overflow    |
|                         |     formSetPortMapping     | CVE-2024-4123  |    Buffer Overflow    |
|                         |   formSetRemoteWebManage   | CVE-2024-4124  |    Buffer Overflow    |
|                         |     formSetStaticRoute     | CVE-2024-4125  |    Buffer Overflow    |
|                         |       fromSetSysTime       | CVE-2024-4126  |    Buffer Overflow    |
|                         |    guestWifiRuleRefresh    | CVE-2024-4127  |    Buffer Overflow    |
|   W20EV4.0 V15.11.0.6   |   formSetRemoteWebManage   | CVE-2024-3874  |    Buffer Overflow    |
| W30Ev1.0 V1.0.1.25(633) |         formSetCfm         | CVE-2024-3879  |    Buffer Overflow    |
|                         |      formWriteFacMac       | CVE-2024-3880  |   Command Injection   |
|                         |       frmL7ProtForm        | CVE-2024-3881  |    Buffer Overflow    |
|                         |      fromRouteStatic       | CVE-2024-3882  |    Buffer Overflow    |
|                         |      formaddUserName       | CVE-2024-32285 |    Buffer Overflow    |
|                         |       fromVirtualSer       | CVE-2024-32286 |    Buffer Overflow    |
|                         |       fromqossetting       | CVE-2024-32287 |    Buffer Overflow    |
|                         |  fromwebExcptypemanFilter  | CVE-2024-32288 |    Buffer Overflow    |
|                         |       fromAddressNat       | CVE-2024-32290 |    Buffer Overflow    |
|                         |       formexecommand       | CVE-2024-32292 |   Command Injection   |
|                         |     fromDhcpListClient     | CVE-2024-32293 |    Buffer Overflow    |
|                         |     fromDhcpListClient     | CVE-2024-32294 |    Buffer Overflow    |
|                         |      fromWizardHandle      | CVE-2024-4171  |    Buffer Overflow    |
|   G3 15.11.0.17(9502)   | formModifyPppAuthWhiteMac  | CVE-2024-4164  |    Buffer Overflow    |
|                         |       modifyDhcpRule       | CVE-2024-4165  |    Buffer Overflow    |
|     4G300  V1.01.42     |         sub_41E858         | CVE-2024-4166  |    Buffer Overflow    |
|                         |         sub_422AA4         | CVE-2024-4167  |    Buffer Overflow    |
|                         |         sub_4260F0         | CVE-2024-4168  |    Buffer Overflow    |
|                         |   sub_42775C/sub_4279CC    | CVE-2024-4169  |    Buffer Overflow    |
|                         |         sub_429A30         | CVE-2024-4170  |    Buffer Overflow    |
|   i21 V1.0.0.14(4656)   |  formQosManageDouble_user  | CVE-2024-4245  |    Buffer Overflow    |
|                         |  formQosManageDouble_auto  | CVE-2024-4246  |    Buffer Overflow    |
|                         |     formQosManage_auto     | CVE-2024-4247  |    Buffer Overflow    |
|                         |     formQosManage_user     | CVE-2024-4248  |    Buffer Overflow    |
|                         |       formwrlSSIDget       | CVE-2024-4249  |    Buffer Overflow    |
|                         |       formwrlSSIDset       | CVE-2024-4250  |    Buffer Overflow    |
|                         |       fromDhcpSetSer       | CVE-2024-4251  |    Buffer Overflow    |
|                         |    formGetDiagnoseInfo     | CVE-2024-4491  |    Buffer Overflow    |
|                         |       formOfflineSet       | CVE-2024-4492  |    Buffer Overflow    |
|                         |      formSetAutoPing       | CVE-2024-4493  |    Buffer Overflow    |
|                         |     formSetUplinkInfo      | CVE-2024-4494  |    Buffer Overflow    |
|                         |    formWifiMacFilterGet    | CVE-2024-4495  |    Buffer Overflow    |
|                         |    formWifiMacFilterSet    | CVE-2024-4496  |    Buffer Overflow    |
|                         |       formexeCommand       | CVE-2024-4497  |    Buffer Overflow    |
|   i22 V1.0.0.3(4687)    |    formSetUrlFilterRule    | CVE-2024-4252  |    Buffer Overflow    |

## TOTOLINK

We discover vulnerabilities in **19** different router product of **TOTOLINK**, revealed **47 vulnerabilities** and obtained **44 CVEs**, which is listed below.
| TOTOLINK  Routers | Vulnerable function |      CVE       |  Type of vulnerability   |
| :---------------: | :-----------------: | :------------: | :----------------------: |
|      A3000RU      |     product.ini     | CVE-2024-7170  |   Hard-Coded Password    |
|      A3100R       |    setTelnetCfg     | CVE-2024-7158  |    Command Injection     |
|                   |    getSaveConfig    | CVE-2024-7157  |     Buffer Overflow      |
|      A3300R       |       shadow        | CVE-2024-7155  |   Hard-Coded Password    |
|                   | UploadCustomModule  | CVE-2024-7331  |     Buffer Overflow      |
|      A3600R       |     product.ini     | CVE-2024-7159  |   Hard-Coded Password    |
|                   |   NTPSyncWithHost   | CVE-2024-7171  |    Command Injection     |
|                   |    getSaveConfig    | CVE-2024-7172  |     Buffer Overflow      |
|                   |      loginauth      | CVE-2024-7173  |     Buffer Overflow      |
|                   |    setdeviceName    | CVE-2024-7174  |     Buffer Overflow      |
|                   |   setDiagnosisCfg   | CVE-2024-7175  |    Command Injection     |
|                   |    setIpQosRules    | CVE-2024-7176  |     Buffer Overflow      |
|                   |   setLanguageCfg    | CVE-2024-7177  |     Buffer Overflow      |
|                   |      setMacQos      | CVE-2024-7178  |     Buffer Overflow      |
|                   |  setParentalRules   | CVE-2024-7179  |     Buffer Overflow      |
|                   | setPortForwardRules | CVE-2024-7180  |     Buffer Overflow      |
|                   |    setTelnetCfg     | CVE-2024-7181  |    Command Injection     |
|                   |    setUpgradeFW     | CVE-2024-7182  |     Buffer Overflow      |
|                   |  setUploadSetting   | CVE-2024-7183  |     Buffer Overflow      |
|                   |  setUrlFilterRules  | CVE-2024-7184  |     Buffer Overflow      |
|                   |    setWebWlanIdx    | CVE-2024-7185  |     Buffer Overflow      |
|                   | setWiFiAclAddConfig | CVE-2024-7186  |     Buffer Overflow      |
|                   | UploadCustomModule  | CVE-2024-7187  |     Buffer Overflow      |
|      A3700R       |     wizard.html     | CVE-2024-7154  | Improper Access Controls |
|                   |  ExportSettings.sh  | CVE-2024-7156  |  Information Disclosure  |
|                   |      setWanCfg      | CVE-2024-7160  |    Command Injection     |
|                   |      loginauth      | CVE-2024-42543 |     Buffer Overflow      |
|                   |   setPasswordCfg    | CVE-2024-42544 |     Buffer Overflow      |
|                   |    setWizardCfg     | CVE-2024-42545 |     Buffer Overflow      |
|      A7000R       |      loginauth      | CVE-2024-7212  |     Buffer Overflow      |
|                   |    setWizardCfg     | CVE-2024-7213  |     Buffer Overflow      |
|     CA300-PoE     |      loginauth      | CVE-2024-7217  |     Buffer Overflow      |
|       CP450       |     product.ini     | CVE-2024-7332  |   Hard-Coded Password    |
|                   |      loginauth      | CVE-2024-7465  |     Buffer Overflow      |
|       CP900       | UploadCustomModule  | CVE-2024-7463  |     Buffer Overflow      |
|                   |    setTelnetCfg     | CVE-2024-7464  |    Command Injection     |
|       EX200       |      loginauth      | CVE-2024-7336  |     Buffer Overflow      |
|                   |    getSaveConfig    | CVE-2024-7335  |     Buffer Overflow      |
|      EX1200       |  setParentalRules   | CVE-2024-7338  |     Buffer Overflow      |
|                   |      loginauth      | CVE-2024-7337  |     Buffer Overflow      |
|       LR350       |      setWanCfg      | CVE-2024-7214  |    Command Injection     |
|      LR1200       |   NTPSyncWithHost   | CVE-2024-7215  |    Command Injection     |
|                   |       shadow        | CVE-2024-7216  |   Hard-Coded Password    |
|      N350RT       |    setWizardCfg     | CVE-2024-7462  |     Buffer Overflow      |
| AC1200 T8 |     setUpgradeFW     | CVE-2024-8574 |  Command Injection  |
|           | setIpPortFilterRules | CVE-2024-8576 |   Buffer Overflow   |
|           |  setStaticDhcpRules  | CVE-2024-8577 |   Buffer Overflow   |
|           |   setWiFiMeshName    | CVE-2024-8578 |   Buffer Overflow   |
|           |  setWiFiRepeaterCfg  | CVE-2024-8579 |   Buffer Overflow   |
|           |        shadow        | CVE-2024-8580 | Hard-Coded Password |


## TP-LINK

We discover vulnerabilities in **3** different router product of **TP-LINK**, revealed **6 vulnerabilities** and obtained **3 CVEs**, which is listed below.

| TP-LINK  Routers | Vulnerable function |      CVE       |  Type of vulnerability   |
| :---------------: | :-----------------: | :------------: | :----------------------: |
|    TL-WR841ND v11 | popupSiteSurveyRpm  |  CVE-2024-9284 |     Buffer Overflow      |
|    TL-WR941ND v6  | popupSiteSurveyRpm  | CVE-2024-46313 |     Buffer Overflow      |
|    TL-WR740N V6   | popupSiteSurveyRpm  | CVE-2024-46325 |     Buffer Overflow      |


## D-Link

We discover vulnerabilities in **4** different router product of **D-Link**, revealed **34 vulnerabilities** and obtained **32 CVEs**, which is listed below.

|    D-Link  Routers    | Vulnerable  function  |         CVE         | Type of vulnerability |
| :-------------------: | :-------------------: | :-----------------: | :-------------------: |
| DIR-605L 2.13B01 BETA |   formAdvanceSetup    |    CVE-2024-9532    |    Buffer Overflow    |
|                       |   formDeviceReboot    |    CVE-2024-9533    |    Buffer Overflow    |
|                       |  formEasySetPassword  |    CVE-2024-9534    |    Buffer Overflow    |
|                       | formEasySetupWWConfig |    CVE-2024-9535    |    Buffer Overflow    |
|                       | formEasySetupWizard   |    CVE-2024-9549    |    Buffer Overflow    |                  
|                       |    formLogDnsquery    |    CVE-2024-9550    |    Buffer Overflow    |
|                       |    formSetWanL2TP     |    CVE-2024-9551    |    Buffer Overflow    |
|                       |  formSetWanNonLogin   |    CVE-2024-9552    |    Buffer Overflow    |
|                       |   formdumpeasysetup   |    CVE-2024-9553    |    Buffer Overflow    |
|                       |  formSetEasy_Wizard   |    CVE-2024-9555    |    Buffer Overflow    |
|                       |  formSetEnableWizard  |    CVE-2024-9556    |    Buffer Overflow    |
|                       |    formSetWanPPPoE    |    CVE-2024-9557    |    Buffer Overflow    |
|                       |    formSetWanPPTP     |    CVE-2024-9558    |    Buffer Overflow    |
|                       |     formWlanSetup     |    CVE-2024-9559    |    Buffer Overflow    |
|                       |  formSetWAN_Wizard51  |    CVE-2024-9561    |    Buffer Overflow    |
|                       |    formSetWizard1     |    CVE-2024-9562    |    Buffer Overflow    |
|                       | formWlanSetup_Wizard  |    CVE-2024-9563    |    Buffer Overflow    |
|                       |  formWlanWizardSetup  |    CVE-2024-9564    |    Buffer Overflow    |
|                       |    formSetPassword    |    CVE-2024-9565    |    Buffer Overflow    |
|   DIR-619L B1 2.06    |   formDeviceReboot    |    CVE-2024-9566    |    Buffer Overflow    |
|                       |    formAdvFirewall    |    CVE-2024-9567    |    Buffer Overflow    |
|                       |    formAdvNetwork     |    CVE-2024-9568    |    Buffer Overflow    |
|                       |  formEasySetPassword  |    CVE-2024-9569    |    Buffer Overflow    |
|                       |  formEasySetTimezone  |    CVE-2024-9570    |    Buffer Overflow    |
|                       |  formEasySetupWWConfi |    CVE-2024-9782    |    Buffer Overflow    |
|                       |    formLogDnsquery   |    CVE-2024-9783    |    Buffer Overflow    |
|                       |   formResetStatistic |    CVE-2024-9784    |    Buffer Overflow    |
|                       |      formSetDDNS     |    CVE-2024-9785    |    Buffer Overflow    |
|                       |      formSetLog      |    CVE-2024-9786    |    Buffer Overflow    |
|                 |    formSetMACFilter     | CVE-2024-9908 |    Buffer Overflow    |
|                 |       formSetMuti       | CVE-2024-9909 |    Buffer Overflow    |
|                 |     formSetPassword     | CVE-2024-9910 |    Buffer Overflow    |
|                 |      formSetPortTr      | CVE-2024-9911 |    Buffer Overflow    |
|                 |       formSetQoS        | CVE-2024-9912 |    Buffer Overflow    |
|                 |      formSetRoute       | CVE-2024-9913 |    Buffer Overflow    |
|                 | formSetWizardSelectMode | CVE-2024-9914 |    Buffer Overflow    |
|                 |     formVirtualServ     | CVE-2024-9915 |    Buffer Overflow    |
