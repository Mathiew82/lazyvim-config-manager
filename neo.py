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
    system("git clone https://github.com/Mathiew82/lazyvim-config.git ~/.config/nvim")
    print("\N{heavy check mark} Installation was successful!")
elif selection == "2":
    try:
        if system("sudo rm -r ~/.config/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.config/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.config/nvim folder...")
    except Exception as e:
        print(e)

    system("git clone https://github.com/Mathiew82/lazyvim-config.git ~/.config/nvim")
    print("\N{heavy check mark} Update was successful!")
elif selection == "3":
    try:
        if system("sudo rm -r ~/.config/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.config/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.config/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/share/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.local/share/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.local/share/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/state/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.local/state/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.local/state/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.cache/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.cache/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.cache/nvim folder...")
    except Exception as e:
        print(e)

    print("\N{heavy check mark} Uninstall was successful!")
elif selection == "4":
    try:
        if system("sudo rm -r ~/.config/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.config/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.config/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/share/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.local/share/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.local/share/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.local/state/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.local/state/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.local/state/nvim folder...")
    except Exception as e:
        print(e)

    try:
        if system("sudo rm -r ~/.cache/nvim") != 0:
            raise Exception(
                "\N{heavy multiplication x} ~/.cache/nvim folder does not exist"
            )
        print("\N{heavy check mark} Deleted ~/.cache/nvim folder...")
    except Exception as e:
        print(e)

    system("git clone https://github.com/Mathiew82/lazyvim-config.git ~/.config/nvim")
    print("\N{heavy check mark} Uninstall and installation was successful!")

#
#
#
