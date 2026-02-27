label arrival_dreamspace:
    
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