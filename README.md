### Linux-Screenshare-Bypass
A simple bypass method for https://github.com/Rancio777/Linux-Minecraft-Screenshare-Tool, because they don't use variables :c

## How that works?
This script simply use a RegEx expression for finding the result file (`.*\.scan`), and edit it

## How to fix it?
Simple use **variables**, not copy it in a file.
Example:
```bash
Detections="Check A" # It define the "Detections" variable to "Check A", it actually means we failed Check A.
NordVPN=true # It define the "NordVPN" variable to "true", it actually means we failed NordVPN's check
```
Also, I don't really know bash, so I maded an over-commented Python script, sorry.