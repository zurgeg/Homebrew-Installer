print("First off, which OS do you use:\n1. Windows\n2. macOS/Linus")
os = input()

if os == "1":
    print("Good choice! I've always liked Windows.")
    print("Unfourtantly, wii.guide (the source we download everything we need from) doesn't allow us to download the required files on Windows!\nFollow wii.guide instead")
elif os == "2":
     print("Good choice! Linux is awesome!")
     print("Let's get to it, shall we?")
     import os
     os.system("curl -A "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36" -o priiloader.zip https://wii.guide/assets/files/Priiloader_v0_9.zip")
     print("Priiloader is downloaded!, now on to the next step!")
     # I got tired of downloading assets from wii.guide, this step is WIP.
     # TO DO: Download Open Shop Channel
     # TO DO: Download RC24/BC24
     # TO DO: Extract OSC, RC24, and Priiloader. Wii need a way to run RC24 patcher on Linux! :)
