#Python modules
init python:
    import time 

#Characters
# Zuha character defined
define z = Character("Zuha", color="#6fa758")


#??? defined (noor)
define c = Character("????", color="#ddbf22")

#Noor character defined
define n = Character("Noor", color="#ddbf22")

#lg (little girl) character defined
define lg = Character("???", color="#b84756")


# Variables
# Snowball fight
default last_mash_time = 0.0
default goal = 15
default mash_count = 0

# Dreamland - solved missions
default swing_solved = false
default seesaw_solved = false 
default picknick_table_solved = false 

# Dreamland - inventory 
default inventory = []


# Small shake transform
transform shake(amount=10):
    xoffset -amount
    linear 0.05 xoffset amount
    linear 0.05 xoffset 0

screen endless_button_mash():
    modal True

    # Background that shakes
    add "snowball fight" at shake(amount=5 if mash_count % 2 == 0 else -5)

    # Key prompt
    text "PRESS Q!" xpos 0.5 ypos 0.5 xanchor 0.5 size 50 bold True color "#ffffff"

    # Encouragement message with a timer
    timer 1.0 action Function(lambda: None) repeat True  # redraw screen every second
    if time.time() - last_mash_time > 15.0:
        text "Don't give up!" xpos 0.5 ypos 0.3 xanchor 0.5 color "#ff0000" size 40

    # Key press handling
    key "K_q" action [
        SetVariable("last_mash_time", time.time()),      # update timer
        SetVariable("mash_count", mash_count + 1),       # increment count
        If(mash_count + 1 >= goal, [Hide("endless_button_mash"), Jump("mash_success")])
    ]

# 

    
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
    "{cps=5}...........{/cps}"   
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
    call mash_event
    jump after_snowball_fight

label mash_event:
    scene black  # or your starting scene

    # Reset variables
    $ mash_count = 0
    $ last_mash_time = time.time()

    show screen endless_button_mash

    # Waiting until screen handles progression
    $ renpy.pause(3600.0, hard=True)

    return


label mash_success:

    scene snowball fight won
    play sound snowball volume 1.9

    z "Uhoh..."

    return 



label after_snowball_fight:

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
    "{cps=30}{i}I froze; it felt like my mouth was shut with wires, unable to utter a single word.{/i}{/cps}"
    c "{cps=30}It's all your fault{/cps}{nw}"
    c "{cps=30}If only if i was there on time{/cps}{nw}"
    c "{cps=30}If only \"xxxx\" had listened to me{/cps}{nw}"
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

    label question_classmate: 
        scene infirmary cheeky
        c "{cps=40}Ask away, it's not like we're skipping next lecture on {i}purpose{/i}{/cps}~"

        menu: 
            "What? we're skipping our lecture?? ":
                scene infirmary concerned 
                c "{cps=40}Woah, i knew you were a nerd, but being {i}that{/i} concerned for school?{/cps}"
                c "{cps=40}Relax, i was just kidding, its lunchbreak.{/cps}"
                z "{cps=40}Oh thank god, i thought you were serious..{/cps}"
                c "{cps=40}Heh, when have i ever been serious about school?~{/cps}"
                z "{cps=40}Never?{/cps}"
                scene infirmary cheeky
                c "{cps=40} Exactly{/cps}"
                call question_classmate

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
                call question_classmate

            "Why are we in the infirmary?":
                scene infirmary thinking
                n "{cps=40}you forgot THAT too? To think we had such an wholesome moment together, forgotten...{/cps}"
                z "{cps=30}Uhm{/cps}"
                z "{cps=15}What did we do....{/cps}"
                n "{cps=40}You came to my rescue when i collapsed and you brought me here!"
                n "{cps=40}Though i told you to just use my wheelchair and push me, but instead, you insisted to..{/cps}"
                z "{cps=15}Insisted what...{/cps}"
                scene infirmary cheeky
                n "{cps=40}To carry me.{/cps}"
                n "{cps=15}{i}Bridal style{/i}{/cps}"
                z "{cps=40}Nooo.....{/cps}"
                "{cps=40}{size=-5}Why did i do something so embarassing.....{/size}{/cps}"
                call question_classmate


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
        scene shes awake 
        n "{cps=40}So doc, figured it out yet?{/cps}"
        z "{cps=70}WAH!{/cps}"
        z "{cps=40}Oh my god, you scared me!{/cps}"
        n "{cps=40}I would say the same to you...{/cps}"

        "{cps=30}{i}You try to help her stand up{/i}{/cps}"
        scene standing up
        z "{cps=30}{i}Be carefull, watch your step{/i}{/cps}"
        n "{cps=30}{i}...Thank you{/i}{/cps}"
        n "{cps=30}{i}A little bit more and people'll think that we're a pair{/i}{/cps}"
        z "{cps=30}{i}Be serious..{/i}{/cps}"

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
                    n "{cps=40}So.. did you feel anything{/cps}"
                    z "{cps=40}..Only the element of surprise, fortunately{/cps}"
                    "{cps=20}{i}This girl definetely has a screw loose!{/i}{/cps}"
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
            "{cps=30}{i}You and Noor decide to give a closer look at our surroundings, the place resembles an eerie looking playground.{/i}{/cps}"
            "{cps=40}{i}There's ordinary playground equipment, such as swings, a seesaw and a picnic table, but you also see things that feel slightly off to be there.{/i}{/cps}"
            "{cps=40}{i}Things like a safe, cake, and worst of all, a door standing in the middle of nowhere are nearby the area.{/i}{/cps}"
            "{cps=30}{i}You also see Children that seem to be playing in the playground, well, most of them, some of them are just quiet, like theyre waiting for someone to play with them.{/i}{/cps}"

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
            z "{cps=40}What if - instead of my memories - this place is connected to that girl's memory?{/cps}"
            z "{cps=40}The fact that children are here, and that were in a playground, makes {i}this{/i} theory more.. well-founded!{/cps}"
            n "{cps=40}That does seem more likely - good job on figuring it out! Look's like your not entirely useless after all!{/cps}"
            z "{cps=40}What's that supposed to mean...{/cps}"
            n "{cps=40}Nevermind that, i think it's a good idea to explore the area, because i don't think that we'll be woken up anytime soon.{/cps}"
            n "{cps=40}And who knows, maybe our ticket out of here is that very obvious looking door with that kid guarding it.{/cps}"
            z "{cps=40}Heh, maybe.{/cps}"

            jump exploration_dream_realm


        label exploration_dream_realm:






















        

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.


    # "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
