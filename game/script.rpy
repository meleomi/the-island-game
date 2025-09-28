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
    image bg island_p = im.Scale("bg island_peop.jpeg", 1920, 1080)

    # First opening scene
    scene bg black
    show you_sp at left:
        zoom 0.5
    you "For weeks, the sea had been both our guide and our grave, carrying us farther than any map dared to promise"


    # Sea opening scene
    with fade
    scene bg sea
    show you_sp at left:
        zoom 0.5
    you "I believed I had mastered the sea, that nothing could stand on the way. But when the storm came, our ship cracked apart under its rage."


    # Show the bg that people start going on the island
    scene bg island_p with fade
    #Text "all we have..."
    #Text "the first day"
    scene 
    #Text "We are running out of food"
    scene
    #Text "they all believe you"
    scene
    #show the poster I made with all the characters
    scene
  

    # These display lines of dialogue.


    # This ends the game.

    return
