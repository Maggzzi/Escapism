label snowball_dream:
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
    return 