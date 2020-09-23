
print("What will we be hacking today?\n1. Wii\n2. 3DS\n3. Switch\nI know I promised PSP and PS Vita, but those are WIP")
console = input()
print("Sounds good!")
if console == "1":
    import wiihax
elif console == "2":
    import 3dhax
elif console == "3":
    import switchitup
