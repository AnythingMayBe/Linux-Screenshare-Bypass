### Linux-Screenshare-Bypass
A simple bypass method for https://github.com/Rancio777/Linux-Minecraft-Screenshare-Tool, because they don't use variables :c

## How that works?
This script simply use a RegEx expression for finding the result file (`.*\.scan`), and edit it

## How to fix it?
Simpely use **variables**, not copy it in a file.
Example:
```bash
Detections="Check A" # It define the "Detections" variable to "Check A", it actually means we failed Check A.
NordVPN=true # It define the "NordVPN" variable to "true", it actually means we failed NordVPN's check
```
Also, I don't really know bash, so I maded an over-commented Python script, sorry.

## Disclaimer
That program don't works with the latest version of their software.
But, the **idea still works**, if you have a little knowledge of Python and Bash, you can easily make a bypass updated with their latest version.
I do not recommend to do that for bypassing reasons, do you cheat because you think that's fun or do you cheat because you want to test moderator's knowledge?
