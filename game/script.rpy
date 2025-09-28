# The script of the game goes in this file.
Plug 'wakatime/vim-wakatime'

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Mr. Gagnon")
define girl = Character("Ava")
define mom = Character("Harper")
define grandpa = Character("Lames")
define guy = Character("Oliver")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg sea = im.Scale("bg sea.jpeg", 1920, 1080)
    scene bg sea

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    guy "You've created a new Ren'Py game."

    guy "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
