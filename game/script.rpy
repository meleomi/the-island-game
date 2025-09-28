# --- Characters ---
define e = Character("")
define you = Character("Mr. Gagnon (you)")
define girl = Character("Ava")
define mom = Character("Harper")
define grandpa = Character("James")  # match survivors
define guy = Character("Oliver")
define rescue = Character("Rescue team")

# --- Survivors (use default so we can change the list) ---
default survivors = ["Oliver", "Harper", "James", "Ava", "yourself"]

init python:
    def build_kill_menu():
        return [(name, "day_kill_" + name.lower()) for name in survivors]

# --- Screen ---
screen kill_menu_screen():
    tag menu
    modal True
    vbox:
        xysize (300, 200)
        text "{b}Who do you want to kill?{/b}":
            xalign 0.5 # Centers the text horizontally
            yalign 0.5 # Centers the text vertically
            color "#000000" # Sets the text color to red (hex code)
            size 40 # Sets the font size
        style_prefix "choice"
        xalign 0.5  # horizontal center
        yalign 0.5  # vertical center (optional)
        spacing 15
        for name in survivors:
            textbutton name action Jump("day_kill_" + name.lower())

# --- Start ---
label start:
    image bg black = im.Scale("bg black.png", 1920, 1080)
    image bg sea = im.Scale("bg sea.jpeg", 1920, 1080)
    image bg island_p = im.Scale("bg island_peop.jpeg", 1920, 1080)
    image bg island = im.Scale("bg island.jpeg", 1920, 1080)
    image bg poster = im.Scale("bg poster.jpg", 1920, 1080)
    image bg poster = im.Scale("bg poster.jpg", 1920, 1080) 
    image bg boat = im.Scale("bg boat.jpeg", 1920, 1080)
    # opening scenes …
    scene bg black
    show you_sp at left:
        zoom 0.5
    you "For weeks, the sea had been both our guide and our grave, carrying us farther than any map dared to promise."

    with fade
    scene bg sea
    show you_sp at left:
        zoom 0.5
    you "I believed I had mastered the sea, but when the storm came, our ship cracked apart under its rage."

    scene bg island_p with fade
    show you_sp at left:
        zoom 0.5
    you "Five of us reached the island, but we brought almost nothing with us. We don’t have much food, and what little we saved is running out. We made a fire to stay warm. We have sent the help signal, but aid will not arrive soon..."
   
   
    hide you_sp
    show girl_sp at right:
        zoom 0.5
    girl "Mom... i want to go home..."
    show mother_sp at left:
        zoom 0.5
    mom "I know... We just need stay here for a little bit, until we will be rescuered"
    girl "I’m cold..."
    mom "I know. Stay close to the fire, it will keep you warm"
    hide mother_sp
    show grandpa_sp at left:
        zoom 0.5
    grandpa "It may be cold now, but morning always comes."
    hide grandpa_sp
    hide girl_sp
    show son_sp at left:
        zoom 0.5
    guy  "Do not worry, the help will come soon."
    hide son_sp

    jump day_loop

# --- Loop ---
label day_loop:
    play music "sad-documentary-background-music-365827.mp3" loop
    # stop if only 2 survivors left
    if len(survivors) <= 2:
        jump end_game

    $ day = 5 - len(survivors)
    scene bg island_p with fade
    "Day [day+1] – We are running out of food."
    scene bg poster with fade
    "Choose who dies today."
    scene bg poster 
    pause 
    call screen kill_menu_screen
    jump day_loop

# --- Death labels ---
label day_kill_oliver:
    scene bg island
    you "Oliver is gone…"
    $ survivors.remove("Oliver")
    show you_sp at left:
        zoom 0.5
    you "I am so sorry, my dear son. I did not have any other choice. You will be remembered as a brave, honest person."
    hide you_sp
    jump day_loop

label day_kill_harper:
    scene bg island
    you "Harper is gone…"
    $ survivors.remove("Harper")
    if "Ava" in survivors:
        show girl_sp at left:
            zoom 0.5
        girl "Mother... I... I can’t... live without you… Why would you go..."
        hide girl_sp
    jump day_loop

label day_kill_james:
    scene bg island
    you "James is gone…"
    if "Harper" in survivors:
        show mother_sp at left:
            zoom 0.5
        mom "I am sorry, father... I did not know it would be like that..."
        hide mother_sp
    if "Ava" in survivors:
        show girl_sp at right:
            zoom 0.5
        girl "Grandaddy... Can you stay...I'll miss you so much"
        hide girl_sp
    $ survivors.remove("James")
    jump day_loop

label day_kill_ava:
    scene bg island
    you "Ava is gone…"
    if "Harper" in survivors:
        show mother_sp at left:
            zoom 0.5
        mom "My sweet little angel... No..I can not believe that happend to you... You will rest in peace in god's hands. I am so sorry"
        hide mother_sp
    $ survivors.remove("Ava")
    jump day_loop

label day_kill_yourself:
    scene bg island
    you "I chose myself…"
    you "I will never know what will happen to others, but I hope they will be saved..."
    $ survivors.remove("yourself")
    return

# --- Ending ---
label end_game:
    scene bg island with fade
    $ last_two = " and ".join(survivors)
    show you_sp at left:
        zoom 0.5
    rescue "Over here! We’ve found them!"
    scene bg boat with fade
    e "When the rescue team came only two of people remain: [last_two]."
    return