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

- Think it will be easiest to have dedicated romsets for each of the three emulators
  - Should have plenty of disk space at least!

TODO
====
- Should download and use this theme: http://www.onyxarcade.com/nevato.html
