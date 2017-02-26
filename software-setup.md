Software setup
=====

- Downloaded floob's [image of Retropie + Attract Mode](http://forum.attractmode.org/index.php?topic=705.0).
  - Hint: it's in /mnt/data/Backup/Operating Systems
  - Will need to update Retropie to 4.1 after installing to microSD 32GB on RPi3
- Already had a 0.155 ROM set - going to update it to 0.175 to use with Final Burn Alpha (lr-fbalpha 0.2.97.39)
  - Set up external HDD with NTFS partition
  - Copy over all ROMs and patch them
- dd Retroipe + Attract Mode image to 16GB microSD
    - dd bs=4M if=<the img file> of=/dev/sdd



First boot:
- Launch raspi-config to expand FS and set locale
- Started Emulation Station, launched Retropie option to configure wifi
- Update Retropie from Retropie > Retropie Setup
  - "Update all installed packages" -> auto-updates install script first
  - Also updating system packages as part of update
    - Took about 2.5 hours

- Using https://www.youtube.com/watch?v=-ssbyofbm4Q to help configure
- Set roms path for MAME (Adv) to /media/usb/roms_to_0.173
- Think it will be easiest to have dedicated romsets for each of the three emulators
  - Should have plenty of disk space at least!
- Start by creating a mame2003/MAME 0.78 directory on the HDD
- Followed clrmamepro tutorial on https://github.com/retropie/retropie-setup/wiki/managing-roms to create a 0.78 romset
  - This is going to take hours...


- symlink'd ~/roms/mame-libretro/roms to the mame2003 romset on the external HDD
- Generated romlist from dir
- Scrape artwork
- Some games work (not Neo Geo games?)
  - need to scan romset using clrmamepro to work out what's missing
  - a lot of missing/broken files; going to try reconstructing a 0.78 set from the 0.151 set rather than the multiple-patched 0.175 set

- Switch to robospin theme
    - Probably going to have to create a custom non-ugly theme based on robospin later


TODO
====
- Should download and use this theme: http://www.onyxarcade.com/nevato.html
