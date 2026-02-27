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
    SEESAW_ASK_IF_PLAY_WITH_GIRL_A = 3
    SEESAW_AFTER_PLAYING = 4

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
# A screen is an UI layer for = buttons, clickable areas, overlays

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

# playground screen
screen playground():

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

#picnic table screen
screen picnic_imagemap():
    imagemap:
        ground "picnic table.png"
        hover "picnic table hover.png"

        #Cake spot
        hotspot (cake_x, cake_y, cake_w, cake_h):
            action Jump("cake_interaction")

        #Safe hotspot
        hotspot (safe_x, safe_y, safe_w, safe_h):
            action Jump("safe_interaction")
        
        #Optional: click outside to leave
        hotspot(0, 0, 1920, 1080):
            action Jump("playground_hub")



screen debug_hitbox_swing:
    add Solid("#00ff0088") xpos swing_x ypos swing_y xsize swing_w ysize swing_h

screen debug_hitbox_seesaw:
    add Solid("#0000ff88") xpos seesaw_x ypos seesaw_y xsize seesaw_w ysize seesaw_h

screen debug_hitbox_picnic:
    add Solid("#ffff0088") xpos picnic_x ypos picnic_y xsize picnic_w ysize picnic_h


# Inventory screen
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


# Safe screen
screen safe_keypad():
    #MOET NOG SAFE IMG MAKEN EN TOEVOEGEN
    add images/safe.png


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

    # swing.stage = 0
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
        $ inventory.append(recorder)
        z "Why are you giving me this?"
        s "Well the thing is that i heard about the incident from this old recorder, it kept replaying the same thing over and over again."
        s "I thought, why tell them when they can hear the real thing?"
        z "{cps=40}Ah, but i don't know what button to pre-{nw}{/cps}"
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
        s "Whuh? your the kid that beat that her up?? {size=-5}i..{/size}"
        n "......."
        z "What do you think Noor, you recognize someone in here too"
        n "N-no, not the slightest clue.."
        "Huh, it felt like she was gonna tell me something.. well whatever"
        z "Lets go explore the playground further, thanks for showing us this Seo-ah!"
        s "No problem, don't miss me too much now!"
        n "Heh, we won't.~"

        jump playground_hub

    #  seesaw.stage = 1 and swing.stage =  1
    elif seesaw.stage == SEESAW_PLAYED and swing.stage == SWING_PLAYED:
        "The girl is satisfied playing with you."

        "I should ask them..."

        menu:
            "I got a favor":
                "Hehe, i knew you guys missed me, but this early?"
                "Well, i'd rather put it differently"
                z"More like.... wanting a favor?"
                s "Wow, your gonna use the same tactic i did? touché"
                z "Well its not much, but we wanted to ask if you'd like to play with someone else this time."
                z "That girl over there, she want's to use the seesaw, but she doesnt have anybody to play with"
                s "Haven't you tried helping her out first? "
                n "Trust me, she did"
                z "Anyways... look like your up for the task?"
                s "Hmmm...."
                s "Eh, why not"
                s "But only because i've got nothing to do!"
                n "A win is a win"
                $ seesaw.stage = SEESAW_ASK_IF_PLAY_WITH_GIRL_A

        jump playground_hub


    # seesaw.stage = 3
    elif seesaw.stage == SEESAW_AFTER_PLAYING:
        "The whole playground is quiet."
        "It seems that they both left."
        jump playground_hub

    # swing.stage = 1
    elif swing.stage == SWING_PLAYED:
        "the girl is slowly pushing the swing on her own."
        "she seemes satisfied, but you get the feeling that she feels kind of lonely"
        z "{i}Is there something i can do?{/i}"
        jump playground_hub


# seesaw_scene dream
label seesaw_scene:
    # show closeup seesaw after clicking
    scene seesaw_scene

    #seesaw.stage = 0
    if seesaw.stage == SEESAW_NOT_PLAYED:
        "You see a little girl sitting on the ground with her back laying on one end of the seesaw."
        "You and Noor notice the sad and hollow expression on the the girl's face. You try to cheer her up"

        n "Hello there! Mind telling me what's got you so lost in thought?"
        h "Uhm.. who are you.. two?"
        n "My name is Noor and this girl's name is Zuha!"
        n "We wanted to ask if everything's alright, you look like your gonna bore a hole in the ground just by staring there."
        z "{i}Why can't she show concern like a normal person..{/i}"
        h "No.. it's just that... i..."
        h "...I really want to play on the seesaw, but theres nobody here to play with."
        h "The only kid playing in the park is that girl over there, on the swing, but i don't think i should bother her..."
        z "So.. you just want someone to play with? What's your name?"
        h "yes... my name is Ha-eun."
        z "Ha-eun, i'd love to play with you if it helps cheer you up!"
        h "A-are you sure? don't you think that-"
        z "It's no big deal, don't worry! I used to love the seesaw too when i was your age, so i'm really doing this for the both of us!"
        h "Oh, okay..!"

        "The girl gets seated immediatly, waiting for you to also sit down on the other end."
        "The moment you put your full weight onto the seat, Ha-eun is lifted high into the air on her end of the seesaw, now dangling from that height - she looks down at you from above."
        "While your still below her, you get confused why your still below her, processing what happened so suddenly, and it finally hits you."
        z "Ah..."
        "{i}Your too heavy, so your still on the ground... {/i}"
        n "NO way.. "
        n "BAHHWHAHHAAHAHAAH"
        z "You realised you might be {i}too{/i} heavy to play on the seesaw afterall...theres a reason why they're made for {u}kids{/u} only."
        h "Uhmm miss, im feeling scared, im too high up!"
        z "O-oh yeah! im sorry, let me get you down!"
        "You stand up, bringing Ha-eun down - You notice she's in a much worser mood than before."
        h "Ugh.. now i'll never be able to play on the seesaw..."
        h "Nevertheless - thank you for trying miss, but i wish there was someone my age who could play with me.."
        z "{i}Hmm, what should i do to cheer her up...{/i}."

        $ seesaw.stage = SEESAW_PLAYED
        jump playground_hub

    # seesaw.stage = 1
    elif seesaw.stage == SEESAW_PLAYED: 
        "The girl wants to play with someone around her age."
        "She looks bored."

        "I think i know what i should do..."
        jump playground_hub 

    # seesaw.stage = 3
    elif seesaw.stage == SEESAW_ASK_IF_PLAY_WITH_GIRL_A:

        "What should i say?"
        menu:
            "Ask if she'd like to play with girl a on the seesaw":
                h "Huh? oh no- why did you ask her? i don't know her that well.."
                z "You didn't know me and Noor before too, but we still got along pretty well didnt we? Try to give them a chance, i think anyone'll like the company of a girl like you!"
                "Ha-eun gets flustered and hesitates a little but accepts your request."
                "Girl a appears from behind you and introduces herself to her"
                "Ha-eun replies and does the same, they begin to have a chat and sit on the seesaw"
                "The both of them were having a great time together while rocking the seesaw. Soon, laughter fills the playground."

                $ seesaw.stage = SEESAW_AFTER_PLAYING
                $ inventory.append(hairpin)
                $ inventory.append(cutlery)

                "Ha-eun seems satisfied and rushes over to you."
                h "Miss Zuha, thank you for encouraging me to give girl a a chance, i had a wonderfull time with her!"
                h "To express my gratitude, i'd like to give you something that may come handy to you in the future"
                "Got item \"Hairpin\""
                "Got item \"Cutlery\""
                "Ha-eun gives you a hairpin and cutlery before running off. You wonder where she found all these items but before you could ask her, she vanished with girl a."
                n "Soo... not only this place, but the items we keep getting are starting to creep me out."
                n "I mean, who in their right mind would just give us these forks and knives, along side a-"
                n "..."
                n "Hairpin..."
                "Both of you inspect the hairpin, it's feels like you've seen this item before."
                "You try to say something, but you look at Noor - who has a very disturbed look on her face."
                z "What is it?"
                n "..."
                n "I've seen this before, this hairpin."
                n "It feels so familiar and yet- i just can't remember where ive seen it..."
                z "That's what i was thinking too! I think ive seen this one for sale in a clothing store before..." 
                z "Is this.. maybe my hairpin?"
                n "You? I've never seen you with a hairpin before, and this one looks like it belongs to a kid."
                z "Huh... ill just keep it for now"
                "You put the items in you got in you pocket, still contemplating wether these items are usefull or not"
                jump playground_hub

            "Ask if she'd like to play with Inaya on the seesaw":
                n "Wow.. i knew you were gonna say something weird like that."
                n "Look kid, im sorry, but i can't play with you: me and Zuha have approximately the same bodyweight, and last time... "
                n "Well, let's just say the seesaw wasn't exactly balanced."
                z "We do?"
                n "Just go with it"
                jump seesaw_scene
                
    # seesaw.stage == 3
    elif seesaw.stage == SEESAW_AFTER_PLAYING:
    
        "The seesaw creaks quietly."
        "No one is here anymore."
        jump playground_hub



label picnic_scene:
    scene picnic table prototype

    "You notice strange items on the picnic table, and wonder who put them there."
    z "Why is there a safe and a cake here?"
    n "Huh, Maybe these items have a deeper meaning, disguised as random objects."
    n "Or maybe there's more than meets the eye..."
    z "How so?"
    n "Maybe this is our wake-up call to not take anything here too seriously."
    n "To stop with questioning everything and just go with the flow."
    z "I hardly think that's the case..."
    z "Lets just... take a closer look before we decide on anything."

    call screen picnic_imagemap
    return


label cake_interaction:
    "You inspect the cake, it's lit with nine cadles precisely."
    "You see that theres something written on the cake, but some of the words are smeared away, probably because of the icing."
    "It reads the following:"
    "{i}Happy 9nth birthday xxx AND xxx!{/i}"
    z "Hmm... so this is a birthday cake, but here? Whose birthday is it anyways?"
    z "It's impossible to make out who it was meant for.. but it does look delicous.."
    z "It's a strawberry shortcake at that, i'm not a sweettooth, but!~"
    n "..."
    z "..Uh, nevermind that - do you have any idea whose name it could be?"
    n "...It looks exactly like——"
    n "!"
    n "..."
    "Unexectedly, it looks like she cut herself off."
    "You question the sudden change of mood, and find the silence not so pleasant."
    z "I've got no clue of what to make of those cleared out words."
    z "And the cake is showing sings of melting... a cake - going to waste just like that..."
    n "Sigh."
    n "Just get this over with and eat it."
    z "Wha? no, i couldn't! it's clearly made for someone else and i.. shouldnt... "
    n "Come on, were in a dream right? you can practically do whatever you want."
    n "Besides, i've had enough of these weird things we've been encountering nonstop."
    "What should i do?"
    menu:
        "Eat the cake":
            if cutlery in inventory:
                z "It seems the cutlery we got actually did come in handy..."
                z "I mean, who would want to eat cake with their barehands?"
                n "I bet you'd actually do that, given how your eating {i}someone elses{/i} birthday cake."
                z "Didnt you just say i had freewill..."
                n "I mean.. it comes to a certain point."
                z "We'll eat this together though, im not finishing the whole thing."
                n "..."
                z "Come on, just taste it! i'll go first and let you know if its any good."
                n "....."
                n "if it means getting out of here faster.."

                "you use the cutlery that you got from Ha-eun to make even pieces."
                "You gave a fork to Noor and use one yourself, you take the first bite and...."
                "It's delicious! You finish it in one sitting, however, you give a glance on Noors face..."
                "She doesn't really seem to enjoy it that much."

                n "Of all things, there HAD to be jam inside..."
                z "Uh, but don't cakes normally get filled with jam? it's pretty common."
                n "That's the point, i dont like jam at all. Never been a fan of it."
                z "Well atleast you tried it?"
                n "Whatever, if your done we should go ahead."
                z "Hold up, just let me finish and..."
                z "?"
                z "Whats that... weird thing inside? in the middle?"
                "You see something crumpled up like a ball - and around it there are..."
                z "Glass shards?"
                z "Wha-- why are there shards placed inside the cake??"
                z "But i didn't feel anything sharp in my throat, even while chewing."
                n "I guess we were lucky we didnt begin eating in the middle."
                n "I told you to calm it down a notch, you were planning on eating the whole thing, werent you?"
                n "Not even that - if you decided it to eat it with your bare hands, you would've definetly gobbled that piece up without knowing."
                n "I knew it, i knew this place was weird from the beginning."
                z "But whats that crumpled thing in the middle, though?"
                z "It kind of looks like paper.."
                "You try to pry the crumpled up object out of the inside of the cake with your fork."
                "Eventually, you take it out, and it seems to be made of paper."
                "Trying to straighten the paper, you see it for what it actually is:"
                z "This is.. a photo."
                #scene birthday photo 
                "Giving it another look, you see three young girls smiling for the photo, two with partyhats and.."
                z "Wait- thats me!"
                z "You see yourself standing next to the girl, who's in the middle"
                z "Why am i in this photo? and the girl next to me, she looks awfully allot like the girl from my dream."
                n "...What do you mean, your saying you saw HER in your dream?"
                n "This doesn't make any sense, out of everyone.."
                n "Why would she.."
                "What, she knows this girl too?"
                "Why is she acting so secretive about it?"
                n "Besides that, this photo.. why is this here?"
                z "Well, most importantly, why are we in this photo in the first place?"
                "Thinking back, that girl did ask you if you remembered her."
                "Did you really know her all this time?"
                "You try to examine the surroundings within the photo, giving a closer look at the items that are present."
                # ADD A IMAGEMAP WHERE THE PLAYER CAN POINT OUT WEIRD THINGS, LIKE THE CAKE, PIN AND BIRTHDATE
                "You notice the same strawberry shortcake in the photo, with the names now being visible:"
                "{i}Happy 9nth birthday Inaya AND Noor!{/i}"
                z "Hmm, guessing by the girls wearing a partyhat, i assume the girl from my dream is named Inaya"
                z "The other girls name on the other hand... "
                z "That's strange, the other girls name is Noor?"
                z "Wow, what a coincidence.. am i right?"
                n "You... can't be that oblivious."
                n "Thats me." 
                z "??? {i}THAT's{/i} you????"
                n "What are you trying to say."
                z "Well, its just that..."
                z "You both dont look the same!!"
                z "At al!!"
                n "...People change you know, not that much of a shock in my opinion."
                z "Hmm, when you put it that way, i guess your right."
                n "! That's strange, that pin."
                z "What? Oh, that girl is wearing the same pin i got from Eun-hae earlier!"
                z "It seems that item is connected to her in some way."
                z "But where did Eun-hae find this pin? i guess logic doesnt exist in a dream."
                n "Didn't you say that you remember seeing this somewhere?"
                n "I think this pin doubles as a birthday gift, it looks clean in the photo and is too flashy for daily wear"
                z "Oh, that's possible, maybe i got this hairpin way back then for her birthday!"
                n "Yup, atleast that's what i think.."
                z "But still, i think we should answer the elephant in the room."
                z "...Stating the obvious here, but how come you and this \"Inaya\" have the same birthdate??"
                z "This can't be a coincidence, right???"
                n "It's not, we celebrated both our birthday's on the same day because it was the weekend."
                n "My birthday wasn't on the weekend, while that girl's was, so we planned our birthday on the same day so that everyone in the neighbourhood could come."
                z "Huh, really? It's strange that i can't recall any of that, only the pin is what slighlty stuck with me"
                z "But i should be able to remember this. I didn't know we had some type of history together, along with this Inaya girl."
                z "Childhood friends.. i can't believe we were like that, we look so happy!"
                n "Yeah, probably 'cause its a party idiot."
                n "... But still, we really were that close, always just the three of us."
                n "I still remember those days crystal clear, it was my whole childhood afterall - every vacation was spent playing at the park with you guys." 
                n "Those moments of us were the higlight of when i was a kid, along with another memory i'd rather forget." 
                "? another memory?"
                "I want to know what, but i think i shouldn't pry too much."
                "It's not like we're friends {i}now{/i} anyway."
                jump safe_interaction

            else:
                z "Let me just have a little piece, i want to know if i can taste stuff in a dream in general"
                z "This is a experiment! Science!"
                n "Whatever rows your boat i guess..."
                
                "You try the icing, theres jam coming out of the piece you made with your own hands."
                "It's delicious, sweet and savo-"
                # weird glass/crunch noise
                "ry?"
                # breathing noise - gasp of air
                "Wha- what is in my mouth? So sharp.."
                "I feel like i cant breathe, my pipe is damaged"
                #cg art of where zuha's mouth blood is coming out

                jump game_over

        "Don't eat the cake":
            z "I should leave it for later, you should always save the best for last!"
            n "So your insinuating that your still gonna eat it?"
            z "Well, i mean... i wanna know how cake tastes in a dream."
            z "Aren't you getting hungry from all this running around, we should have a break soon."
            n "If you wanna gobble that up, then be my guest..."
            jump safe_interaction
        

label safe_interaction:    
    z "I think questioning why there's a safe and why it's here is just going to waste our time, so let's just figure out how to open this."
    n "Hmm, we finally agree on something for once."
    z "Though we don't have a key or something to open this up."
    z "Can't we just throw it hard on the ground and see if it breaks?"
    z "Andd i take it back, how about we actually use our brains instead of relying on brawn? Look, we don't even need something physical to open this up."
    n "It has a keypad built in, it says it requires a four digit code."
    z "Hmm, i think i've seen something before with that amount of numbers..."
    n "See? lets crack this thing!"

    #FAKE MENU/PLACEHOLDER FOR SAFE_KEYPAD!!!!!!!!!
    menu:
        "try to open the safe":
            "You somehow guess the code."
            jump safe_open

label safe_open:
    "The safe clicks open"
    "Inside lies a colourful bracelet, the beads each have a letter written, intrigued, you take a look."
    #show bracelet cg art
    z "This bracelet, it has our names written!"
    "Your name, Noor's and Inaya's name are spelled on the bracelet, this reminds you of having something similair."
    n "... the pin, and now the bracelets?"
    z "This one rings a bell.."
    z "Like with the hairpin, i think i've seen this bracelet before."
    n "You sure? Aren't you mistaking this with something else?"
    #show inventory screen and let player click the old rusty bracelet

    #FAKE MENU/PLACEHOLDER FOR INVENTORY_SCREEN
    menu:
        "choose the item that's most identical":
            "Old rusty bracelet":
                "You choose the old rusty bracelet and compare both items with eachother"
                "Their almost identical, other than yours being a little faded, the colours, beads and string match completely."
                jump bracelet_reconciliation

label bracelet_reconciliation:
    n "No way, it's exactly-"
    z "The same thing! I knew it, i knew i saw this bracelet somewhere!"
    n "But how? these are so old, we made these way back then."
    n "Even i lost mine for some time now, but you still had yours all this time?"
    z "Well to be honest, i didn't really remember who the other names were supposed to be."
    z "I can't really recall my childhood past, i don't know why, but its been like that since forever."
    z "I didn't even know i had friends, close ones at that, but weirdly enough, time being spent with you in this weird space.."
    z "it makes me somewhat happy i got to know you, because of all this, i get to see little fragments of what that part of my life was like"



                




    # if cutlery in inventory:
    #     "You use the cutlery to eat the cake properly."
    #     $ cake.stage = CAKE_EATEN_WITH_CUTLERY
    #     jump playground_hub

    # else: 
    #     "You stare at the cake, it has nine candles on it"
    #     "It looks very delicous, you get to urge to eat it"
    #     "But- theres no way you're eating cake with your barehands!"
    #     "You feel like you're missing something."
    #     z "{i}Lets head back for now..{/i}"
    #     jump playground_hub



    
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

    call snowball_dream
    call infirmary
    call arrival_dreamspace








    return
