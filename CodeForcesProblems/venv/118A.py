string = input().lower()
notvowl = ".".join([c for c in string if not c in "aoyeui"])

print("." + notvowl)