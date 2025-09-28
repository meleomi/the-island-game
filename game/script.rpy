# The script of the game goes in this file.
Plug 'wakatime/vim-wakatime'

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("-")
define you = Character("Mr. Gagnon(you)")
define girl = Character("Ava")
define mom = Character("Harper")
define grandpa = Character("Lames")
define guy = Character("Oliver")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg black = im.Scale("bg black.png", 1920, 1080)
    image bg sea = im.Scale("bg sea.jpeg", 1920, 1080)

    scene bg black
    show you_sp at left
    you "For weeks, the sea had been both our guide and our grave, carrying us farther than any map dared to promise"


    with fade
    scene bg sea
    show you_sp at left
    you "I believed I had mastered the sea, that nothing could stand on the way. But when the storm came, our ship cracked apart under its rage."


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

   

    # These display lines of dialogue.


    # This ends the game.

    return
