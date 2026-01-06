#Python modules
init python:
    import time 

#Characters
# Zuha character defined
define z = Character("Zuha", color="#6fa758")

#Noor character defined
define n = Character("Noor", color="#ddbf22")

#lg (little girl) character defined
define lg = Character("???", color="#b84756")


# Variables
default last_mash_time = 0.0
default goal = 15
default mash_count = 0

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
    z "{cps=35}Stealing my notebooks, sticking gum on my clothes and now my coat?{/cps}"
    z "{cps=35}Nevertheless, i also can't remember where i was planning to go.{/cps}"
    z "{cps=35}This isn't even the way back home.. where am i go-{/cps}"

    stop music fadeout 1.0

    scene shocked sideview
    play sound snowball volume 1.9

    z "{cps=90}Wha-{/cps}"

    scene black
    z "{cps=70}My head, something cold hit my head just now-{/cps}"

    lg "{cps=40}Bullseye! i knew i still got it in me!{/cps}"

    scene dream girl encounter with fade
    play music wind fadein 1.0

    lg "{cps=40}That was such a hard throw to pull off..{/cps}"
    lg "{cps=40}But i STILL did it! a HEADSHOT at that!!{/cps}"
    z "{cps=15}Uhm..{/cps}"
    lg "{cps=40}Oh, sorry, did I brag too much? It's just been ages since i've had aim this good-especially in a snowstorm like this?{/cps}"
    lg "{cps=40}You'd think im lying, but well, it's you that got hit, so you gotta, no HAVE to believe it!{/cps}"
    lg "{cps=40}Besides, we're bff's right? i wouldn't do that to just to any stranger!{/cps}"
    z "{cps=5}...{/cps}"
    z "{cps=15}Me..{/cps}"
    z "{cps=15}and YOU?{/cps}"
    lg "{cps=35}wh- come on! I know its hard to recognize me because of the mist, but you can't be this dense! Are you doing it on purpose??{/cps}"
    lg "{cps=35}..Hehe, or did i hit you'r head {size=+5}that{/size} hard?{/cps}"
    z "{cps=40}Look kid.. i don't know what you're babbling about, but i need to go home!{/cps}"
    lg "{cps=15}...{/cps}"
    lg "{cps=40}Assuming {i}those{/i} odds, there's only a one-in-a-million chance you'll get there{/cps}"
    lg "{cps=40}The other options are: A, slipping off the pavement and hitting you're head for real, or B, get into an accident.{/cps}"
    z "{cps=35}Well, then why are {i}you{/i} outside?? aren't you scared of that happening to you too?{/cps}"
    lg "{cps=35}...Hmm i'll tell ya..{/cps}"
    lg "{cps=35} IF you beat me on a one on one snowball fight!{/cps}"
    z "{cps=35}??? right NOW? you just said-{/cps}"
    lg "{cps=35}What? seems to me that your'e just too scared to lose!~{/cps}"
    lg "{cps=35}Don't worry, ill fake it and let you win, but only once!"
    z "{cps=35}I'm sorry, but i can't play with you. i'm even turning purple as we spe-"
    lg "{cps=75}After this i'll tell you the way to get back home, whether you lose or not!{/cps}"
    lg "{cps=35}I know my way around here better than you, heck - i'll even walk you to your place so options A and B don't happen!~"

    scene black 
    "{cps=35}...{/cps}"
    "{cps=40}{i}I don't trust this at all.{/i}{/cps}"
    "{cps=40}{i}First of all, why does she keep referring to us as bff's? I hardly even know her!{/i}{/cps}"
    "{cps=40}{i}and secondly, How does she know the way back to MY house?{/i}{/cps}"
    "{cps=40}{i}Is it possible that i do know her? maybe she's my neighbour or something?{/i}{/cps}"
    "{cps=40}{i}Strange things have been happening ever since ive been walking this neverending road..{/i}{/cps}"
    "{cps=40}{i}But this might be my only chance to get back home.{/i}{/cps}"

    
    z "{cps=40}Okay, fine. I'll play you're game, but you WILL show me the way alright?{/cps}"
    z "{cps=40}Also thank you, but you don't have to walk me back home. {size=-5}that'd just be embarassing..{/size}{/cps}"
    lg "{cps=40}YEAYAA!!!! You won't regret this!! trust me!~~{/cps}"
    z "{cps=15}I hope so..{/cps}"

label mash_event:
    scene black  # or your starting scene

    # Reset variables
    $ mash_distance = 0
    $ last_mash_time = time.time()

    show screen endless_button_mash

    # Waiting until screen handles progression
    $ renpy.pause(3600.0, hard=True)

    return


label mash_success:

    scene snowball fight won

    z "Uhoh..."

    return 


        

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    #z "Wow im alive!! Zuha Hassan in the {i}flesh!{/i}"
    # n "Uhh {size=+10}im{/size} here too yk..."
    # lg "Im the girl from your \"dream\" silly!"
    # lg "dont tell me you {color=#ff0000}{u}forgot{/u}{/color} anything... {size=-10}right?{/size}"
    #"You've created a new Ren'Py game."

    # "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
