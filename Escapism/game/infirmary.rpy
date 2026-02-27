
label infirmary:
    stop sound 
    scene stare with vpunch
    c "HEY!"
    z "!!!"
    c "{cps=30}Oh, finally! I thought you were faking it for sure{/cps}"
    z "{cps=30}Hold on? ..Aren't you?{/cps}"
    c "{cps=30}I?? aren't i what?{/cps}"
    "{cps=30}Huh.. was i dreaming? Did she wake me up just now?{/cps}"
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
