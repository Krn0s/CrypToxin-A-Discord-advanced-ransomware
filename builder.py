import os

os.system("color 5")
os.system("cls")
print("""
 ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ███▄    █ 
▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒ ██ ▀█   █ 
▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▓██  ▀█ ██▒
▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▓██▒  ▐▌██▒
▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒██░   ▓██░
░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ▒░   ▒ ▒ 
  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░░ ░░   ░ ▒░
░          ░░   ░ ▒ ▒ ░░  ░░         ░      ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░ ░ 
░ ░         ░     ░ ░                           ░ ░   ░    ░   ░           ░ 
░                 ░ ░                                                       
""")

input("Press Enter to continue...")

os.system("color 5")
os.system("cls")

def main():
    choice = input("[1] Build Encryption Script\n[2] Build Decryption Script\n[Enter Choice]:> ")
    if choice == "1":
        os.system("pyinstaller --onefile --noconsole -n encrypt encrypt.py")
        print("[*] Successfully built the encryption script.")
    elif choice == "2":
        os.system("pyinstaller --onefile --noconsole -n decrypt decrypt.py")
        print("[*] Successfully built the decryption script.")
    else:
        print("[!] Invalid choice, please choose 1 or 2.")
        main()

    print("[*] Done.")
    print("[*] Check the following directory: [ {} ] for the built script.".format(os.path.dirname(os.path.realpath(__file__))))
    input("[*] Press enter to exit.")


if __name__ == "__main__":
    main()
