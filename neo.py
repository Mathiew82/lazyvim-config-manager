from os import system

print(
    """
   Welcome to NeoVim config manager
    --------------------------------
    Select a option: (write a number and press enter)

 1. Install
 2. Update
 3. Uninstall
 4. Reinstall

    Press enter to exit
"""
)
selection = input("")

if selection == "1":
    system("git clone git@github.com:Mathiew82/lazyvim-config.git ~/.config/nvim")
    print(" Installation was successful!")
elif selection == "2":
    try:
        if system("sudo rm -r ~/.config/nvim") != 0:
            raise Exception("󱂷 ~/.config/nvim folder does not exist")
        print("󱥾 Deleted ~/.config/nvim folder...")
    except Exception as e:
        print(e)

    system("git clone git@github.com:Mathiew82/lazyvim-config.git ~/.config/nvim")
    print(" Update was successful!")
elif selection == "3":
    try:
        if system("sudo rm -r ~/.config/nvim") != 0:
            raise Exception("󱂷 ~/.config/nvim folder does not exist")
        print("󱥾 Deleted ~/.config/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/share/nvim") != 0:
            raise Exception("󱂷 ~/.local/share/nvim folder does not exist")
        print("󱥾 Deleted ~/.local/share/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/state/nvim") != 0:
            raise Exception("󱂷 ~/.local/state/nvim folder does not exist")
        print("󱥾 Deleted ~/.local/state/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.cache/nvim") != 0:
            raise Exception("󱂷 ~/.cache/nvim folder does not exist")
        print("󱥾 Deleted ~/.cache/nvim folder...")
    except Exception as e:
        print(e)

    print(" Uninstall was successful!")
elif selection == "4":
    try:
        if system("sudo rm -r ~/.config/nvim") != 0:
            raise Exception("󱂷 ~/.config/nvim folder does not exist")
        print("󱥾 Deleted ~/.config/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/share/nvim") != 0:
            raise Exception("󱂷 ~/.local/share/nvim folder does not exist")
        print("󱥾 Deleted ~/.local/share/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/state/nvim") != 0:
            raise Exception("󱂷 ~/.local/state/nvim folder does not exist")
        print("󱥾 Deleted ~/.local/state/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.cache/nvim") != 0:
            raise Exception("󱂷 ~/.cache/nvim folder does not exist")
        print("󱥾 Deleted ~/.cache/nvim folder...")
    except Exception as e:
        print(e)

    system("git clone git@github.com:Mathiew82/lazyvim-config.git ~/.config/nvim")
    print(" Uninstall and installation was successful!")

#
#
#
