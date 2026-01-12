# =================
# CHARACTERS           
# =================

# Important characters 
# Zuha character defined
define z = Character("Zuha", color="#6fa758")

#??? defined (noor)
define c = Character("????", color="#ddbf22")

#Noor character defined
define n = Character("Noor", color="#ddbf22")

#lg (little girl) character defined
define lg = Character("???", color="#b84756")


# NPC's 
#seesaw girl
define s = Character("???", color="#40c5c5")

#swing girl 
define h = Character("???", color="#c54040")
#fortune teller 

#bully 1

#bully 2


# =================
# CONSTANTS
# =================

init -1 python:        #init -1 loads before normal init blocks

    # Swing
    SWING_NOT_PLAYED = 0
    SWING_PLAYED = 1
    SWING_PLAYED_NOW_PLAYING_WITH_HAEUN = 2

    # Seesaw
    SEESAW_NOT_PLAYED = 0
    SEESAW_PLAYED = 1
    SEESAW_ASK_IF_PLAY_WITH_GIRL_A = 2
    SEESAW_AFTER_PLAYING = 3

    # Picnic 
    NO_MISSION_DONE = 0
    FIRST_MISSION_DONE = 1
    ALL_MISSIONS_DONE = 2

    # Cake stages
    CAKE_UNEATEN = 0
    CAKE_EATEN_NO_CUTLERY = 1   #short bad ending
    CAKE_EATEN_WITH_CUTLERY = 2

    #Are we still friends? turning point for a good or bad ending
    NOT_FRIENDS = 0
    STILL_FRIENDS = 1

    # Door / Safe
    LOCKED = 0
    UNLOCKED = 1

    # Fortune teller
    STARTING = 0
    FAILED = 1
    HALFWAY_PASSED = 2
    FULLY_PASSED = 3

    # Light switch
    OFF = 0   #bshort bad ending
    ON = 1

# =================
# PYTHON MODULES
# =================
init python:

    # Time module imported for: timer in snowball fight
    import time 

# =================
# OOP CLASSES
# =================

    #Item class for item objects 
    class Item:
        def __init__(self, name, description, icon=None):
            self.name = name
            self.description = description
            self.icon = icon

    #PlaygroundObject class for Playground objects
    class PlaygroundObject:
        def __init__(self, name, stage):
            self.name = name
            self.stage = stage



# =================
# VARIABLES
# =================



# Playground hotspot positions (fallback values)
default swing_x = 1050
default swing_y = 280
default swing_w = 160
default swing_h = 120

default seesaw_x = 800
default seesaw_y = 280
default seesaw_w = 160
default seesaw_h = 120

default picnic_x = 500
default picnic_y = 280
default picnic_w = 160
default picnic_h = 120

default cake_x = 400
default cake_y = 300
default cake_w = 120
default cake_h = 120

default safe_x = 600
default safe_y = 300
default safe_w = 120
default safe_h = 120

# =================
# OBJECTS 
# =================

# Dream realm - Items
define recorder = Item(
    "Recorder", 
    "An old recorder given by the swing girl. It recorded a fight between two bullies and the girl you saw in your dream. You also appear shortly in the recording, fighting the bullies and becoming friends with girl from your dream."
)

define hairpin = Item(
    "Hairpin", 
    "A small hairpin given by the seesaw girl. You believe you've bought this hairpin before but you can't recall why."
)

define cutlery = Item (
    "Cutlery",
    "Cutlery, consisting of two forks and knives, given by the seesaw girl. You believe that this item can be usefull"
)

define photo = Item(
    "Photo",
    "A photo celebrating the girl in your dream's and Noor's birthday, founded inside the cake. You see yourself, the dreamgirl, and Noor when you three were kids and based on the picture, you three seemed like great friends."
)

define friendship_bracelet = Item(
    "Friendship bracelet",
    "A friendship bracelet you found in the safe. Your, dreamgirl's and Noor's name are written on it."
)

define key = Item(
    "Key",
    "A key given by The Fortune Teller. You believe that you know where to use it"
)

define newspaper = Item(
    "Newspaper",
    "A Newspaper you found on the ground after witnessing the accident. It describes the unfortunat accident of a nine year old girl happened near a playground."
)


# Dream realm - PlaygroundObjects
define swing = PlaygroundObject("Swing", SWING_NOT_PLAYED)     #stage 0: didn't play with swing girl     stage 1: played with swing girl
define seesaw = PlaygroundObject("Seesaw", SEESAW_NOT_PLAYED)     #stage 0: first encounter     stage 1: after playing with swing girl     stage 2: after both girl swing and seesaw play together
define picnic = PlaygroundObject("Picnic Table", NO_MISSION_DONE)     #stage 0: didn't complete all missions     stage 2: completed first mission     stage 3: completed second mission (all)
define cake = PlaygroundObject("Cake", CAKE_UNEATEN)     #stage 0: uneaten     stage 1: eaten WITHOUT cutlery (bad ending)    stage 2: eaten WITH cutlery
define safe = PlaygroundObject("Safe", LOCKED)     #stage 0: locked     stage 1: unlocked
define fortune_teller = PlaygroundObject(" The Fortune Teller", STARTING)     #stage 0: quiz failed    stage 2: quiz passed midway     stage 3: quiz passed completely
define door = PlaygroundObject("Door", LOCKED)     #stage 0: locked     stage 1: unlocked
define lightswitch = PlaygroundObject("Switch", OFF)     #stage 0: failed to turn on switch (bad ending)     stage 2: turned on switch


# =================
# INVENTORY
# =================

default inventory = []



# =================
# TRANSFORM
# =================

transform shake(amount=10):
    xoffset -amount
    linear 0.05 xoffset amount
    linear 0.05 xoffset 0


# =================
# SCREENS           
# =================
# A screen is a UI layer for = buttons, clickable areas, overlays

# Button smash for Snowball fight screen
screen mash_snowballfight():
    modal True

    # Background that shakes
    add "snowball fight" at shake(amount=5 if mash_count % 2 == 0 else -5)

    # Key prompt
    text "PRESS Q!" xpos 0.5 ypos 0.5 xanchor 0.5 size 50 bold True color "#334082"

    # Encouragement message with a timer
    timer 1.0 action Function(lambda: None) repeat True  # redraw screen every second
    if time.time() - last_mash_time > 5.0:
        text "Keep it up!" xpos 0.5 ypos 0.3 xanchor 0.5 color "#632727" size 40

    # Key press handling
    key "K_q" action [
        SetVariable("last_mash_time", time.time()),      # update timer
        SetVariable("mash_count", mash_count + 1),       # increment count
        If(mash_count + 1 >= goal, [
            Hide("mash_snowballfight"), 
            Jump("mash_success")])
    ]


screen playground:

    imagemap:
        ground "playground.png"

        # Swing hotspot
        hotspot (swing_x, swing_y, swing_w, swing_h):
            hovered Show("debug_hitbox_swing")
            unhovered Hide("debug_hitbox_swing")
            action [Hide("debug_hitbox_swing"), Jump("swing_scene")]

        # Seesaw hotspot
        hotspot (seesaw_x, seesaw_y, seesaw_w, seesaw_h):
            hovered Show("debug_hitbox_seesaw")
            unhovered Hide("debug_hitbox_seesaw")
            action [Hide("debug_hitbox_seesaw"), Jump("seesaw_scene")]

        # Picnic hotspot
        hotspot (picnic_x, picnic_y, picnic_w, picnic_h):
            hovered Show("debug_hitbox_picnic")
            unhovered Hide("debug_hitbox_picnic")
            action [Hide("debug_hitbox_picnic"), Jump("picnic_scene")]


screen debug_hitbox_swing:
    add Solid("#00ff0088") xpos swing_x ypos swing_y xsize swing_w ysize swing_h

screen debug_hitbox_seesaw:
    add Solid("#0000ff88") xpos seesaw_x ypos seesaw_y xsize seesaw_w ysize seesaw_h

screen debug_hitbox_picnic:
    add Solid("#ffff0088") xpos picnic_x ypos picnic_y xsize picnic_w ysize picnic_h



screen inventory_screen():
    tag menu

    frame:
        align (0.5, 0.5)
        padding (20, 20)

        vbox: 
            spacing 10

            text "Inventory"

            if inventory:
                for item in inventory:
                    text item.name
            else:
                text "Your inventory is empty."

            textbutton "Close" action Return()

# =================
# LABELS          
# =================

# mashing event (for snowballfight)
label mash_event_snowballfight:

    # Reset variables before starting
    $ mash_count = 0
    $ last_mash_time = time.time()
    $ goal = 10 

    # Show mash screen
    show screen mash_snowballfight
    # Wait until the screen signals the event is done
    $ renpy.pause()

    return


label mash_success:
    jump after_snowball_fight



# Change position of debug hitboxes 
label playground_hub:
    # Move swing a bit left
    $ swing_x = 1080
    $ swing_y = 280

    # Move seesaw a bit higher
    $ seesaw_x = 633
    $ seesaw_y = 450

    # Move picnic table
    $ picnic_x = 138
    $ picnic_y = 525


    call screen playground
    return


# swing_scene dream label
label swing_scene:
    scene swing_scene

    if swing.stage == SWING_NOT_PLAYED:
        "As you approach the swing, a young girl is swinging by herself. She looks up as you draw near."
        s "Hey there! you, with the dark hair!"
        z "Huh, me?"
        "Thinking that he called you over, you walk towards her."
        s "Say... can you do me a favor? I promise it'll be of your benefit if you wanna know something {i}juicy{/i}."
        s "The thing is, i know a secret that you don't know!~ and i'll only tell you if you push me while I'm on the swing!"
        n "What are you blabbering about? Don't think that Zuha will give her swing pushing services, cash-free!"
        z "My what."
        s "I promise it'll be worth it! i've heard that in this specific area, something hectic happened... an incident if you will"
        s "And because of that incident, no one else dares to play around here anymore."
        s "Well, except for me- because i don't get scared that easily."
        z "So what happened exactly?"
        s "That i will tell!- but only for the price of 1 minute continual pushes while i sit on the swing!"
        n "Well Zuha, that's how far my negotiating skills can go, i guess you'll have to give your swing pushing services for free this time."
        z "Why does this situation feel so similair..."
        z "*sigh*... okay, i'll do it."
        s "I knew you had it in you!"
        n "I knew that i could count on you!"
        z "..."
        "you push the girl in her swing, you feel like its been longer than three minutes."
        "you just hope that this'll end quickly..."
        
        $ swing.stage = SWING_PLAYED 
        s "Whoo! that was fun!!!"
        scene swing_scene
        z "Im.. happy you enjoyed it ....uhh"
        z "What's your name kid?"
        s "The name's Seo-ah!"
        n "Now Seo-ah, explain to us the what happened here."
        s "Okay, but i won't tell you- here!"
        "Seo-ah gives you an old recorder, it seems cracked from the outside and a little rusty."
        z "Why are you giving me this?"
        s "Well the thing is that i heard about the incident from this old recorder, it kept replaying the same thing over and over again."
        s "I thought, why tell them when they can hear the real thing?"
        z "{cps=40}Ah, but i don't really know what button to pre-{nw}{/cps}"
        s "Ill do it for you!~"
        "click"

        scene black
        "You hear the sound glitching at first, but it got slightly clearer. You and Noor both listen to the recording."
        "{size=-5}Get up!{/size} i said GET UP!"
        "kicking sound"
        "No! stop it!"
        "Why are you being so stubborn, people like me also want a turn on the swing!"
        "But i just got here! It hasn't even been 3 minutes!"
        "I mean sure, if you were {i}normal{/i}, i wouldve understand, but your a \"special case\". How are you even gonna push yourself with {i}those{i} legs?"
        "People like you shouldn't wait in line for something that isn't made for special cases to begin with!"
        "slap sound"
        "What the hell are you going on about- don't you dare lay a finger on her!"
        "...Hahaha"
        "Ohh i get it, YOUR gonna push her! because she obiously can't do it herself huh?"
        "Get out of my sigth before i'll tell the teacher on you. You don't know anything about her!"
        "Theres nothing more to know about her, just the label \"cripple\" is about enough to sum her up!"
        "!"
        "fighting/kicking noises"
        "You hear a dispute, judging by the audio, it seems like the bully and a girl standing up for the disabled girl are fighting eachother."
        "When suddenly, you hear someone running with full speed"
        "loud kicking noise"
        "!!!"
        "Ow!! Ow my face- who the heck are you!"
        "..."
        "I saw the whole thing go down. Are you that pathetic? Insulting a little girl, slapping her - just to sit on some measily swing?"
        "It's the other way around, people like YOU are the \"special cases's\", resorting to violence over one petty thing."
        "Worst of all, you chose her to be your puncing bag BECAUSE she's so called special, going after people weaker than you, tch- go for someone your own size."
        "!.. I- You-! Just wait 'till i get the teacher and my parents, they'll get you expelled!"
        "Running away noise"
        "{i}Hmmph, NOW she'll tell the teacher? she's the one who started it...{/i}"
        "Uhm.. excuse me?"
        "!!!"
        "Thank you for that, i thought she was gonna harass us again and go away after having the last word, but i guess i flipped her switch."
        "You shouldn't thank me, it just felt too unbearable - to just watch this all unfold. I had to do something!"
        "I'll tell the teacher immediatly about what happened, i hope you really don't get expelled over this.."
        "You really think im gonna get expelled? That girl was just bluffing, and even if she's not, ive got quite allot to say aswell."
        "Besides, my clean record and high grades make me a pretty hard student to expel."
        "Heheh, thanks nonetheless, what's your name by the way?"
        "... It's Zuha, what's your name?"
        "Oh, my name is-"
        "The rusty recorder crashes, hearing glitching noises and eventually, going quiet."

        scene swing_scene
        z "That, was me? and the girl i saw in my dream, i recognize her voice!"
        s "Whuh? your the kid that beat that her up?? {size=-5}you don't exactly look the part..{/size}"
        n "......."
        n "No way... it's he-" 
        z "What do you think Noor, you recognize someone in here too"
        n "!"
        n "N-no, not the slightest clue.."
        "Huh, it felt like she was almost gonna tell me something though.. well whatever"
        z "L-lets go explore the playground further, thanks for showing us this Seo-ah!"
        s "No problem, don't miss me too much now!"
        n "Heh, we won't!~"

        jump playground_hub

    elif swing.stage == SWING_PLAYED:
        "The girl is satisfied playing with you."

        "What do i do?"

        menu:
            "Play with her":
                "She smiles as i push her with all my might."
                "After a while, she seems happier."

                $ seesaw.stage = SEESAW_ASK_IF_PLAY_WITH_GIRL_A

                $ inventory.append(recorder)
                "The girl hands me a recorder, she lets me listen to it."
                "Maybe this girl would like to play with the girl at the seesaw."
                jump playground_hub


# seesaw_scene dream
label seesaw_scene:
    # show closeup seesaw after clicking
    scene seesaw_scene

    #AFTER YOU PLAY WITH HER, SEESAW_STAGE IS + 1 
    if seesaw.stage == SEESAW_NOT_PLAYED:
        "You see a little girl sitting on the ground with her back laying on one end of the seesaw."
        "You and Noor notice the sad and hollow looking expression on the the girl's face,. You get an idea to try and cheer her up"

        n "Hello there young girl! Mind telling me what's got you so lost in thought?"
        h "Uhm.. who are you.. two?"
        n "My name is Noor and this girl's name is!"
        n "...uh"
        z "...It's Zuha"
        n "In any case, we wanted to ask if everything's alright, you look like your gonna bore a hole in the ground just by staring there for too long."
        z "Noor... why can't you show concern like a normal person."
        h "wha- no.. it's just that... i..."
        n "mhm?"
        h "...I really want to play on the seesaw, but theres nobody here to play with."
        h "The only kid playing in the park is that girl over there, on the swing, but i don't think i should bother her..."
        z "So.. you just want someone to play with? What's your name dear?"
        h "yes... my name is Ha-eun."
        z "Ha-eun, i'd love to play with you if it helps cheer you up!"
        h "A-are you sure? don't you think that-"
        z "It's no big deal, don't worry! I used to love the seesaw too when i was your age, so i'm really doing this for the both of us!"
        h "Oh, okay..!"

        "The girl gets seated immediatly, waiting for you to also sit down on the other end."
        "The moment you put your full weight onto the seat, Ha-eun is lifted high into the air on her end of the seesaw, now dangling from that height - she looks down at you from above."
        "While your still below her, you get confused why your still below her, processing what happened so suddenly, and it finally hits you."
        z "Ah..."
        "{i}You now realize what Ha-eun was trying to say.{/i}"
        n "NO way.. "
        n "BAHHWHAHHAAHAHAAH"
        z "You get flushed, realising you might be {i}too{/i} heavy to play on the seesaw afterall...theres a reason why they're made for {u}kids{/u} only."
        h "Uhmm miss, im feeling scared, im too high up!"
        z "O-oh yeah! im sorry, let me get you down!"
        "You stand up, bringing Ha-eun down - You notice she's in a much worser mood than before."
        h "Ugh.. now i'll never be able to play on the seesaw..."
        h "But still - thank you for trying miss, but i wish there was someone my age who could play with me.."
        z "Hmm, i think i know what i should do."
        n "... I have a bad feeling i know where this is going."

        $ seesaw.stage = 1 
        jump playground_hub

    # After YOU play with girl b at swings
    elif seesaw.stage == SEESAW_PLAYED: 
        "The girl wants to play with someone around her age."
        "She looks bored."

        "Maybe i should come back later..."
        jump playground_hub 

    # After you play with girl at the swings
    elif seesaw.stage = SEESAW_ASK_IF_PLAY_WITH_GIRL_A:

        "What should i say?"
        menu:
            "Ask if she'd like to play with girl a on the seesaw":
                h "Huh? oh no - why did you ask her? i don't know her that well.."
                z "You didn't know me and Noor before too, but we still got along pretty well didnt we? Try to give them a chance, i think anyone'll like the company of a girl like you!"
                "Ha-eun gets flustered and hesitates a little but accepts your request."
                "Girl a appears from behind you and introduces herself to her"
                "Ha-eun replies and does the same, they begin to have a chat and sit on the seesaw"
                "The both of them were having a great time together while rocking the seesaw. Soon, laughter fills the playground."

                $ seesaw.stage = 3
                $ inventory.append(hairpin)
                $ inventory.append(cutlery)

                "Ha-eun seems satisfied after all that playing and rushes over to you."
                h "Miss Zuha, thank you for encouraging me to give girl a a chance, i had a wonderfull time with her!"
                h "To express my gratitude, i'd like to give you something that may come handy to you in the future"
                "Ha-eun gives you a hairpin and cutlery before running off. You wonder where she found all these items but before you knew it, she vanished with girl a."
                n "Soo... not only this place, but the items we keep getting are very questionable huh"
                n "I mean, who in their right mind would just give us these forks and knives, along side a-"
                n "..."
                n "Hairpin..."
                "The both of you inspect the hairpin, trying to examine every small detail given to it."
                z "{cps=40} Wait a minute - i feel like i've seen this hairpin befo-{nw}{/cps}"
                n "This hairpin! i remember somebody wearing this all the time!"
                z "...As i was saying."
                z "The hairpin feels strangely nostalgic. i don't know why, but i think ive seen one like this for sale in a clothing store before..." 
                z "Is this.. maybe my hairpin?"
                n "You? I've never seen you with a hairpin before, and this one looks like it belongs to a kid, not a 17 year old like yourself."
                jump playground_return

            "Ask if she'd like to play with Inaya on the seesaw":
                n "Wow.. making big decisions all on your own huh?"
                n "How about asking the person involved first before telling her what to do?"
                "I'm still not gonna play with her even if you ask nicely - don't wanne be in your place like last time."

                jump seesaw_scene
                

    elif seesaw.stage == SEESAW_AFTER_PLAYING:
    
        "The seesaw creaks quietly."
        "No one is here anymore."
        #jump playground_return

    label picnic_scene:
    scene bg pincic

    if seesaw.stage < 2:
        # MOET MEER TOEVOEGEN, HEB VOOR NU NIET GEADD!
        "Theres cake and a safe on the picnic table."
        "But you won't eat the cake, even if it's your favourite type It;s because you REFUSE to eat cake with you you need a fork {bold}"
        "I feel like i'm missing something."
        #jump playground_return




    
# Handy writing tips:
# quotation marks: \"hehe\"
# underline: {u}hehe{/u}
# bold: {b}hehe{/b}
# italics: {i}hehe{/i}
# make size text bigger: {size=+10}biggie{/size}
# make size text smaller: {size=-10}smol{/size}


# transition tips:
# scene snowydream with vpunch

# label: gives a section code a name
# jump: use jump with name of label you want to jump to (e.g: jump end)
# call: jump to a statement and then jumpback= use call statement with label name: this is done for repititius action/figuring out a variable 
# return: use return statement after a section of code
# menu: for user choices, quotation marks and : is writing for options


#variables made outside game with variable name: default/define question_tally = 0
#or within the game: $ question_tally = ehe

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    play music wind

    "{cps=15}Its so cold.. for how long have i been walking?{/cps}"
    "{cps=15}The weather this season is no joke. i feel like i'll collapse any second..{/cps}"
    
    scene dream forest with fade 
    "{i}Winter, 20XX{/i}"
    z "{cps=35}I was almost going to call in sick for today, if only if it werent for that biology test.{/cps}"
    z "{cps=35}No i mean, school is important - no matter what kind of weather condition.{/cps}" 
    z "{cps=35}I shouldn't just skip school because theres a snowstorm - with the risk of slipping off the pavement, getting into an accident, and..{/cps}"
    "{cps=15}...{/cps}"
    z "{cps=35}I'm so glad i pulled that allnighter though! I thought i was a goner for sure.{/cps}"
    z "{cps=35}I mean, passing every test with high grades and then flunking the last one?{/cps}"
    z "{cps=35}..with a 70%%?{/cps}"
    z "{cps=35}I could never let that happen, even if it killed me!{/cps}" 
    
    z "{cps=15}..Hahaha{/cps}"  
    "{cps=5}......{/cps}"   
    z "{cps=35}Ugh.. its no use{/cps}"
    z "{cps=35}I'm trying so hard to distract myself from these heavy gusts...{/cps}"
    z "{cps=30}and its not even working!{/cps}"
    z "{cps=35}It's like im not even wearing a-"
    z "{cps=15}..."
    z "{cps=15}..coat...{/cps}"
    
    scene sideview with fade
    z "{cps=35}How could i forget something so important?{/cps}"
    z "{cps=35}..I must've ran off in a fit of anger, because of {i}them{/i}.{/cps}"
    z "{cps=35}{i}They're{/i} such a pain, i dont want to complain to the counsellor either. Too much of a hassle.{/cps}"
    z "{cps=35}The worst part is that i'm not even aware of who's been behind it all.{/cps}"
    z "{cps=35}Stealing my notebooks, sticking gum onto my clothes and now my coat?{/cps}"
    z "{cps=35}Nevertheless, i also can't remember why i'm outside in the first place, was i going home from school?{/cps}"
    z "{cps=35}This isn't even the way back home.. where am i go-{/cps}"

    stop music fadeout 1.0

    scene shocked sideview
    play sound snowball volume 1.9

    z "{cps=90}Wha-{/cps}"

    scene black
    z "{cps=70}My head, something cold hit my head just n-{/cps}"

    lg "{cps=40}Bullseye!!{/cps}"

    scene dream girl encounter with fade
    play music wind fadein 1.0

    lg "{cps=40}That was such a hard throw to pull off..{/cps}"
    lg "{cps=40}But i STILL did it! a HEADSHOT at that!!{/cps}"
    z "{cps=15}Uhm..{/cps}"
    lg "{cps=40}Oh, sorry, did I brag too much? It's just been ages since i've had aim this good - especially in a snowstorm like this?{/cps}"
    lg "{cps=40}You'd think im lying, but well, it's you that got hit, so you gotta, no HAVE to believe it!{/cps}"
    lg "{cps=40}Besides, we're bff's right? i wouldn't do that to just to any stranger!{/cps}"
    z "{cps=5}...{/cps}"
    z "{cps=15}Me..{/cps}"
    z "{cps=15}and YOU?{/cps}"
    lg "{cps=35}wh- come on! I know its hard to recognize me because of the mist, but you can't be this dense! Are you doing it on purpose??{/cps}"
    lg "{cps=35}..Hehe, or did i hit you'r head {size=+5}that{/size} hard?{/cps}"
    z "{cps=40}Look kid.. i don't know what you're babbling about, but i need to get home!{/cps}"
    lg "{cps=15}...{/cps}"
    lg "{cps=40}Assuming {i}those{/i} odds, there's only a one-in-a-million chance you'll get there{/cps}"
    lg "{cps=40}The other options are: A, slipping off the pavement and hitting you're head for real, or B, get into an accident.{/cps}"
    z "{cps=35}Well, then why are {i}you{/i} outside?? aren't you scared of that happening to you too?{/cps}"
    lg "{cps=35}...Hmm i'll tell ya..{/cps}"
    lg "{cps=35} IF you beat me on a one on one snowball fight!{/cps}"
    z "{cps=35}??? right NOW? you just said-{/cps}"
    lg "{cps=35}What? seems to me that your'e just too scared to lose!~{/cps}"
    lg "{cps=35}Don't worry, ill fake it and let you win, but only once!"
    z "{cps=35}I'm sorry, but i can't play with you. I really need to get home and so do yo-"
    lg "{cps=75}After this i'll tell you the way to get back home, whether you lose or not!{/cps}"
    lg "{cps=35}I know my way around here better than you, heck - i'll even walk you to your place so options A and B don't happen!~"

    scene black 
    "{cps=35}...{/cps}"
    "{cps=40}{i}I don't trust her at all.{/i}{/cps}"
    "{cps=40}{i}First of all, why does she keep referring to me as her bff? I hardly even know her!{/i}{/cps}"
    "{cps=40}{i}and secondly, How does she know the way back to MY house?{/i}{/cps}"
    "{cps=40}{i}Is it possible that i know her? maybe she's my neighbour or something?{/i}{/cps}"
    "{cps=40}{i}Strange things have been happening ever since ive been walking this neverending road..{/i}{/cps}"
    "{cps=40}{i}But this might be my only chance to get back home.{/i}{/cps}"

    
    z "{cps=40}Okay, fine. I'll play you're game, but you WILL show me the way alright?{/cps}"
    z "{cps=40}Also thank you, but you don't have to walk me back home. {size=-5}that's kind of embarassing..{/size}{/cps}"
    lg "{cps=40}YEAYAA!!!! You won't regret this!! trust me!~~{/cps}"
    z "{cps=15}I hope so..{/cps}"
    
    call mash_event_snowballfight from _call_mash_event_snowballfight
    jump after_snowball_fight


label after_snowball_fight:

    scene snowball fight won
    play sound snowball volume 1.9

    z "Uhoh..."
    
    scene black
    play sound thud volume 1.9
    "{cps=40}!{/cps}"
    z "{cps=40}Hey kid are you okay?{/cps}"
    "{cps=40}{i}I ran as fast i could to her, checking if she was alright{/i}{/cps}"
    z "{cps=40}Hey.. are you still there? Im sorry! i should've checked how hard i was throwing!{/cps}"
    "{cps=40}{i}Im getting scared.. did she faint?{/i}{/cps}"
    "{cps=40}{i}I was checking her pulse, she's luckily still breathing and surprisingly felt warm to the touch{/i}{/cps}"
    "{cps=40}{i}I picked her up, shaking her a little, in the hope she would open her eyes.{/i}{/cps}"

    scene checking with vpunch
    z "Wake up.. wake up!!"
    play sound shaking 
    "{cps=40}No matter how many times i shake her, she won't open her ey-{/cps}"
    "..."
    "{cps=15}{i}Huh..{/i}{/cps}"
    "{cps=40}{i}Since when did she get so large? i could've sworn she had the body of a little kid...{/i}{/cps}"
    "{cps=40}{i}Her hair also seems longer than before, what's going on?{/i}{/cps}"
    "{cps=40}{i}I gave a closer look at her, her face was covered by her bangs.{/i}{/cps}"

    #wind
    stop music fadeout 1.0

    scene checking changed 
    with vpunch 
    play sound reveal 
   

    play music ominous
    c "{cps=30}You...{/cps}"
    "!"
    c "{cps=40}Why do you never leave us alone? Acting like your so innocent.{/cps}"
    c "{cps=40}I knew that deep down, she was right all along.{/cps}"
    c "{cps=40}Your scum. That's what you are.{/cps}"
    c "{cps=40}Just like the rest of those two-faced morons{/cps}"
    "{cps=30}{i}I.. {/i}{/cps}"
    c "{cps=30}It's all your fault{/cps}{nw}"
    c "{cps=30}If only if i was there on time{/cps}{nw}"
    c "{cps=30}If only \"!?!?\" had listened to me{/cps}{nw}"
    c "{cps=30}This wouldn't have happened if-{/cps}{nw}"
    stop music fadeout 1.0


    scene horrifying with pixellate
    play sound thud 

    play sound horrifying_noise
    "{cps=30}I feel sick to my stomach, like im gonna hurl any moment{/cps}"
    z "{cps=30}Why am i feeling hot and cold at the same time??{/cps}"
    z "{cps=30}What's happening today? Ever since ive been walking, weird things keep on happening{/cps}"
    c "{cps=30}Hey.. you there?{/cps}"
    z "{cps=30}I don't care anymore!! i just wanna go home!{/cps}"
    c "{cps=30}Can you here me??{/cps}"
    z "{cps=30}Please, somehow! Let me escape this realit-{nw}{/cps}"

    stop sound 
    scene stare with vpunch
    c "HEY!"
    z "!!!"
    c "{cps=30}Oh, finally! I thought you were faking it for sure{/cps}"
    z "{cps=30}Wait what? ..Aren't you?{/cps}"
    c "{cps=30}I?? aren't i what?{/cps}"
    "{cps=30}Wait.. was i dreaming? Did she wake me up just now?{/cps}"
    c "{cps=25}Haa..{/cps}"

    c "{cps=40}Damn.. your really out of it.. {/cps}"
    c "{cps=40}You look like you've seen a ghost{/cps}"
    "{cps=40}The girl, who was staring right into my soul, decided to sit back{/cps}"
    "{cps=40}{size=-5} (i guess she realized how dumbfounded i seemed){/size}{/cps}"

    scene infirmary concerned with pixellate
    "{cps=30}{i}I take a good look at my surroundings, i think i recognize this place{/i}{/cps}"
    "{cps=30}{i}The school infirmary!{/i}{/cps}"
    "{cps=30}{i}Though that's odd.. what am i doing here?{/i}{/cps}"
    "{cps=30}{i}Especially with this girl.. I don't even know her name!..{/i}{/cps}"
    "{cps=30}{i}...But i did see her in my dream just now.{/i}{/cps}"
    c "{cps=30}So are you gonna stay quiet the whole time or what? Aren't you gonna ask me why i woke you up in the first place?{/cps}"
    "{cps=40}{i}Oh right! Seems like a good oppurtunity to ask her...{/cps}"

    jump question_classmate
    

label question_classmate: 
    scene infirmary cheeky
    c "{cps=40}Ask away, it's not like we're skipping next lecture on {i}purpose{/i}{/cps}~"

    menu: 
        "What? we're skipping our lecture??":
            scene infirmary concerned 
            c "{cps=40}Woah, i knew you were a nerd, but being {i}that{/i} concerned for school?{/cps}"
            c "{cps=40}Relax, i was just kidding, its lunchbreak.{/cps}"
            z "{cps=40}Oh thank god, i thought you were serious..{/cps}"
            c "{cps=40}Heh, when have i ever been serious about school?~{/cps}"
            z "{cps=40}Never?{/cps}"
            scene infirmary cheeky
            c "{cps=40} Exactly{/cps}"
            jump question_classmate

        "Who are you again?":
            scene infirmary thinking
            c "..."
            c "{cps=40}Your serious..?{/cps}"
            scene infirmary concerned
            c"{cps=40}We're in the same class!{/cps}"
            z "{cps=40}...{/cps}"
            c "{cps=40}I gave you my gum!{/cps}"
            z "{cps=40}Hmm...{/cps}"
            c  "{cps=40}I'm the new transfer student...{/cps}"
            z "{cps=40}Oh! is your name Noor by any chance?{/cps}" 
            n "{cps=40}..Wow, now i know what it feels like to just be remembered by a label. {/cps}"
            z "{cps=40}..Sorry{/cps}"
            scene infirmary cheeky
            n "{cps=40}It's okay, i did the same thing when trying to remember you too{/cps}"
            z "{cps=40}..Wow..{/cps}"
            jump question_classmate

        "Why are we in the infirmary?":
            scene infirmary thinking
            n "{cps=40}you forgot THAT too? To think we had such an wholesome moment together, forgotten...{/cps}"
            z "{cps=30}Uhm{/cps}"
            z "{cps=15}What did we do....{/cps}"
            n "{cps=40}You came to my rescue when i collapsed and you brought me here!"
            n "{cps=40}Though i told you to just use my wheelchair, but instead, you insisted to..{/cps}"
            z "{cps=15}Insisted what...{/cps}"
            scene infirmary cheeky
            n "{cps=40}To carry me.{/cps}"
            n "{cps=15}{i}Bridal Carry Style{/i}{/cps}"
            z "{cps=40}Nooo.....{/cps}"
            "{cps=40}{size=-5}Why did i do something so embarassing.....{/size}{/cps}"
            jump question_classmate


        "Did you hear me talking in my sleep?":
            scene infirmary thinking
            z "{cps=40}Did i say something weird? I think i was having a nightmare{/cps}"
            z "{cps=40}..and i saw you taunting me in my sleep..{/cps}"
            z "{cps=40}It was probably when you were trying to wake me up tho, so it might not be that important.. but still.{/cps}"
            z "{cps=40}It seemed like you wanted to tell me something, like i was being blamed for.. {/cps}"
            scene infirmary concerned
            "..."
            z "{cps=40}Nevermind it's probably nothing...{/cps}"
            n "{cps=40}Yeah, don't think too much about it.{/cps}"
            n "{cps=40}You were giving me the creeps back there, i was almost gonna...{/cps}"
            scene infirmary thinking
            n "{cps=40}Nevermind.{/cps}"

            jump dozing_off

label dozing_off:
    "{cps=30}{i}You talk with Noor for a while, asking what she thinks about the school{/i}{/cps}"
    "{cps=30}{i}She says that she chose to come here specifically for a \"special\" person{/i}{/cps}"
    "{cps=30}{i}... You sensed a bad feeling{/i}{/cps}"
    "{cps=30}{i}Your chat goes on for quite a while, {i}so{/i} long that you feel kind of tired..{/i}{/cps}"
    "{cps=30}{i}The both of you felt incredibly sleepy, like you two hadn't slept for days{/i}{/cps}"

    scene sleepy
    z "{cps=40}Hey... are you dozing off? We can't sleep here you know..{/cps}"
    n "{cps=40}I'm not...  don't worry. Rather, worry about yourself, your yawning every five seconds.{/cps}"
    z "{cps=40}Oh.. really, i didn't know...{/cps}"
    z "{cps=15}that..{/cps}" 
    play sound thud
    scene black with vpunch
    "{cps=30}{i}You both go in a deep sleep, you feel like you've never been this tired before...{/i}{/cps}"

    scene horrifying
    play sound horrifying_noise
    z "{cps=40}Huh.. what's this feeling...{/cps}"
    z "{cps=40}I feel like i've felt this way before..{/cps}"
    z "{cps=40}When was that again..?{/cps}"
    
    scene noor sleepy with fade
    z "{cps=40}!!!{/cps}"
    z "{cps=40}What? why am i here... again?{/cps}"
    z "{cps=40}Hey are you there?{/cps}"
    z "{cps=40}Oh no, is she breathing properly?{/cps}"
    "{cps=40}{i}You try to check her pulse.{/i}{/cps}"
    "{cps=30}{i}You can't feel any movement.{/i}{/cps}"
    z "{cps=30}No way.. is she really?{/cps}"
    "{cps=30}{i}You lay your head on her chest, trying to hear her heartbeat{/i}{/cps}"
    "{cps=15}...{/cps}"
    scene shes awake 
    n "{cps=40}So, figured it out yet?{/cps}"
    z "{cps=70}WAH!{/cps}"
    z "{cps=40}Oh my god you scared me!{/cps}"
    n "{cps=40}I would say the same to you...{/cps}"

    "{cps=30}{i}You try to help her stand up{/i}{/cps}"
    scene standing up
    z "{cps=30}{i}Be carefull, watch your step{/i}{/cps}"
    n "{cps=30}{i}...Thank you{/i}{/cps}"

    "{cps=30}{i}Both you and Noor look up, trying to firgure out where they just landed{/i}{/cps}"

    scene playground with fade
    "{cps=30}{i}This place reminds you of the same place as in your dream{/i}{/cps}"
    "{cps=30}{i}Snowy, trees everywhere, but it seems like youre at a playground.. kind of atleast.{/i}{/cps}"
    z "{cps=30}This is! This is the same type of place i saw in my dream earlier!{/cps}"
    n "{cps=30}...Your joking{/cps}"
    z "{cps=30}Why am i back here again... Why do i have to relive this...{/cps}"
    z "{cps=30}What has this got to do with you too, Why are you here??{/cps}"
    n "{cps=30}Calm down man, you're overthinking it. If what you saying is true, then doesn't that mean that we're in a dream rightnow?{/cps}"
    z "{cps=20}Hmm.. yeah obviously.{/cps}"
    n "{cps=30}Look, let's try to confirm if this is a dream, just to be certain.{/cps}"
    z "{cps=30}I.. guess so.{/cps}"
    jump confirming_dream

label confirming_dream:
    n "{cps=30}Let's confirm it{/cps}"

    menu:
        "Ask her to slap you":
            z "{cps=30}Look, i know this seems crazy of me to ask, but slap me.{/cps}"
            z "{cps=30}I believe that if your in a dream, you can't feel pain right?{/cps}"
            z "{cps=30}I know that this seems crazy, but i want to try out every possibility to figure out if we're in this shared dre-{/cps}{nw}"
            play sound faceslap
            z "!!!"
            "..."
            n "{cps=40}So.. did you feel anything?{/cps}"
            z "{cps=40}..Only the element of surprise, fortunately{/cps}"
            z "{cps=20}{i}This girl definetely has a screw loose!{/i}{/cps}"
            jump dream_confirmed

        "Ask her what she remembers":
            z "{cps=30}Just to check if we both remember what happened, what can you recall up untill now?{/cps}"
            n "{cps=30}I remember waking you up from your earlier nightmare..{/cps}"
            z "{cps=30}Yeah..{/cps}"
            n "{cps=30}then talking with you for quite a bit..{/cps}"
            z "{cps=30}Uh huh..{/cps}"
            n "{cps=30}and we both felt sleepy and dozed off!{/cps}"
            z "{cps=30}Yeah! I think that's about right!{/cps}"
            jump dream_confirmed

label dream_confirmed:
    z "{cps=30}Hmm, so we're really in a dream afterall.{/cps}"
    n "{cps=30}Yeah, now that that's settled, we still have to figure out the \"why\" to this.{/cps}"
    "{cps=30}{i}You decide to give a closer look at your surroundings, the place resembles an eerie looking playground.{/i}{/cps}"
    "{cps=40}{i}There's ordinary playground equipment, such as swings, a seesaw and a picnic table, but you also see things that feel slightly off to be there.{/i}{/cps}"
    "{cps=40}{i}Things like a safe, cake, and worst of all, a door standing in the middle of nowhere are nearby the area.{/i}{/cps}"
    "{cps=30}{i}You also see Children that seem to be playing in the playground, well, most of them, some of them are just.. sitting.. alone.{/i}{/cps}"

    n "{cps=40}Hey, i can be wrong, but this place, does it remind you of somewhere you've been before?{/cps}"
    z "{cps=40}What? no, not really.. this place is just giving me the creeps!{/cps}" 
    n "{cps=40}Hmm, seems like my theory was incorrect then.{/cps}"
    z "{cps=40}Huh, what theory?{/cps}"
    n "{cps=40}...Well, i presume were stuck in your dream right now - because earlier you told me that this dream looked allot like the first dream you had.{/cps}"
    n "{cps=40}And if that's true - I thought, \"is it possible that we're seeing something from your point of view of something? like a fond memory?\"{/cps}"
    z "{cps=40}Oh wow, now that i think about it.. that does make sense!{/cps}"
    z "{cps=40}One thing im certain of, is that this place reminds me allot of the dream i had earlier; same snowy conditions, the same tall dark trees, things like that.{/cps}"
    z "{cps=40}i was being forced to play with this little girl in my dream, and after i misjudged my strength and tried to check on her she...{/cps}"
    z "{cps=40}!{/cps}"
    z "{cps=40}What if - instead of MY memories - this place is connected to that GIRL'S memory?{/cps}"
    z "{cps=40}The fact that children are here, and that were in a playground, makes {i}this{/i} theory more.. well-founded!{/cps}"
    n "{cps=40}That does seem more likely - good job on figuring it out! Look's like your not entirely useless after all!{/cps}"
    z "{cps=40}What's that supposed to mean...{/cps}"
    n "{cps=40}I think that it's a good idea to explore the area because i don't think that we'll wake up anytime soon.{/cps}"
    n "{cps=40}And who knows, maybe our ticket out of here is that very obvious looking door with the kid guarding it.{/cps}"

    jump playground_hub






    return
