# The script of the game goes in this file.
Plug 'wakatime/vim-wakatime'

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define capitan = Character("Mr. Gagnon")
define girl = Character("Ava")
define mom = Character("Harper")
define grandpa = Character("Lames")
define guy = Character("Oliver")
# --- 1) who is alive at the start ? ---
define survivors = ["Oliver", "Harper", "James", "Ava", "Yourself"]

# --- 2) quick helper ----------
init python:
def build_kill_menu():
# return a Ren'Py menu list [ (label, jump_target), … ]
items = []
for name in survivors:
items.append((name, "day_kill_" + name.lower()))
return items
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
    #the first day
   


#I don't know if this works
label day_loop:
python:
day = len(survivors) 
if day == 0:
renpy.jump("game_over")

# flavour text
scene bg inform with fade
"Day [day] – we are running out of food."
scene bg poster with fade
"Choose who dies today."

# build & show menu (only survivors)
call screen kill_menu_screen
# after jump the chosen name is removed inside the target label
jump day_loop # next day


# --- 4) one screen for all days ----------
screen kill_menu_screen():
tag menu
modal True
vbox:
text "Who do you want to kill?" xalign 0.5
hbox:
for name in survivors:
textbutton name action Jump("day_kill_" + name.lower())


# --- 5) one generic death label ----------
label day_kill_oliver:
scene bg death_oliver
"Oliver is gone…"
$ survivors.remove("Oliver")
return

label day_kill_harper:
scene bg death_harper
"Harper is gone…"
$ survivors.remove("Harper")
return

label day_kill_james:
scene bg death_james
"James is gone…"
$ survivors.remove("James")
return

label day_kill_ava:
scene bg death_ava
"You chose yourself…"
$ survivors.remove("Ava")
return

label day_kill_yourself:
scene bg death_you
"You chose yourself…"
$ survivors.remove("Yourself")
return