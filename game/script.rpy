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


    # Island scene
    scene bg island_p with fade
    show you_sp at left:
        zoom 0.5
    you "Five of us reached the island, but we brought almost nothing with us. We don’t have much food, and what little we saved is running out. We made a fire to stay warm. There is no signal,but we keep trying, holding it up and hoping it will connect soon and we will be saved."
    hide you_sp
    show girl_sp at right:
        zoom 0.5
    girl "Mom... i want to go home..."
    show mother_sp at left:
        zoom 0.5
    mom "I know... We just need stay here for a little bit, until we will bw rescuered"
    girl "I’m cold..."
    mom "I know. Stay close to the fire, it will keep you warm"
    pause
    #Text "all we have..."
    #Text "the first day"
    scene 
    #Text "We are running out of food"
    scene
    #Text "they all believe you"
    scene
    #show the poster I made with all the characters
<<<<<<< HEAD
=======
    #and then just keep going im just gonna make the menu whick is when the player can chhose
    #the first day
   


#I don't know if this works
label day_loop:
python:
day = len(survivors) 
if day == 2:
renpy.jump#jump to the scene where survive is here

# flavour text
scene bg inform with fade
"Day [day] – we are running out of food."
scene bg poster with fade
"Choose who dies today."
>>>>>>> 3460b76fdc1be79b48bce409eaddf58df855ee35

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