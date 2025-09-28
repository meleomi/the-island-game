# The script of the game goes in this file.
Plug 'wakatime/vim-wakatime'

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define capitan = Character("Mr. Gagnon")
define girl = Character("Ava")
define mom = Character("Harper")
define grandpa = Character("Lames")
define guy = Character("Oliver")

# The game starts here.

label start:

    # Show the first ocean background.
    scene bg ocean
    # Show the text "The storm came...".
    scene bg inform text 1 with fade
    # Show the bg that people start going on the island
    scene bg island with fade
    #Text "all we have..."
    scene bg inform with text 2 with fade
    #Text "the first day"
    scene 
    #Text "We are running out of food"
    scene
    #Text "they all believe you"
    scene
    #show the poster I made with all the characters
    #and then just keep going im just gonna make the menu whick is when the player can chhose
    "choose which person you want to kill":
        menu:
            "Oliver":
                jump #corresponding text
            "Harper":
                jump #corresponding text
            "James":
                jump #corresponding text
            "yourself":
                jump #corresponding text
    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
