Title: Installing Oxygen OS on OnePlus One
Date: 2017-02-25 11:28
Category: Android
Tags: Android
Summary: How to install Oxygen OS on OnePlus One via Linux
Keywords: oneplus
          oneplus one
          oxygenos
          ubuntu
          linux
          adb
          fastboot


The official OnePlus One does not show how to install OxygenOS on OnePlus One using Linux OS.
So here is a summary on how to do it which take 15 mn.

**I believe you know what you are doing. Your data will be wiped out completely, so prepare a backup before doing any thing from this tutorial.**

Download required files as indicated [here][1] with instruction of Mac OS and OPO2.1.4_Patch_Mac.zip

Install Android development tools (android adb and fastboot):

```shell

    sudo apt-get update
    sudo apt-get install android-tools-adb android-tools-fastboot
```

Extract OPO2.1.4_Patch_Mac.zip and cd into it

```shell
  
  cd OPO2.1.4_Patch_Mac/  
```

Check Device Status:

```shell
  
  sudo fastboot devices
```

Unlock Bootloader:

```shell
  
  sudo fastboot oem unlock
```

Flash Oxygen Recovery and appsboot patch

```shell
  
  sudo fastboot flash recovery sys/recovery.img
  sudo fastboot flash aboot sys/emmc_appsboot.mbn
```

Boot into Recovery

```shell
  
  sudo fastboot boot sys/recovery.img
```

If the system don't go to recovery turn it of and press power+volumen down button again.

Then you can either follow the Mac instructions items from 11 or Wipe the cache and data and use USB install from the recovery, then you have to run this command of course with your phone connected via usb to your laptop/pc:

```shell

  sudo adb sideload ../OnePlus_Bacon_OxygenOS_201601190107.zip
```

Just wait until the install is done and then reboot the phone.
You have now successfully installed OxygenOS on your phone. 

[Credits][2]


[1]: https://forums.oneplus.net/threads/oxygenos-2-1-4-for-the-oneplus-one.425544/
[2]: https://forums.oneplus.net/threads/installation-on-linux.425650/#post-14427789