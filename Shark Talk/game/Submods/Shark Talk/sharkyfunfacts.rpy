init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sharkfunfact1",
            category=['sharks'],
            prompt="Shark Fun Fact #1",
            pool=True,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}
        )
    )

label sharkfunfact1:
    m 1esa "You know, it's been a while since we've done one of these..."
    m 1hub "...so let's go for it!"
    m 3hub "Here's Monika's Shark Fun Fact of the Day!"
    m 1tsu "..."
    m 2ttb "What's the issue, [player]?{w=0.5}{nw}"
    extend 2tsu " You don't remember me doing any 'Shark Fun Facts' before?"
    m 3kub "Well...{w=1.0} it was a Literature Club, not a Shark Fanatics Club, after all, silly!"
    m 1wtd "But ever since you installed this 'Shark Talk' submod, I've had this weird urge to talk about sharks almost non-stop."
    m 7tsu "So...{w=1.0} I'm blaming you for this one, okay?"
    m 1hub "I figured I'd take the same idea as my Writing Tips and make a shark version!"
    m 1esa "Alright, let's begin."
    m 1hub "Actually, it will be a bunch of several short fun facts, but I'm pretty positive you don't mind!"
    m 3eua "Those fun facts will be about...{w=1.0} Whale sharks!"
    m 3wub "Did you know that every whale shark has a unique spot pattern, just like a human fingerprint?"
    m 3eub "Scientists actually use those unique spot patterns to identify and track individual sharks."
    m 7eud "Whale sharks are the biggest fish alive in the ocean, but they're actually filter-feeding!"
    m 7eua "Instead of hunting like most sharks, they swim with their huge mouths open and filter out krill, plankton, jellyfish, and small fish."
    m 1sua "And even though they're especially large, they're completely harmless to humans, and some of the younger ones are even known to be playful with people!"
    m 3hub "They're basically adorable, gentle sea giants.{w=0.5} I hope one day we get the chance to swim next to one!"
    m 1hua "...Those are my fun facts for today!"
    m 1hub "Thanks for listening~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sharkfunfact2",
            category=['sharks'],
            prompt="Shark Fun Fact #2",
            conditional="seen_event('sharkfunfact1')",
            action=EV_ACT_POOL,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}
        )
    )

label sharkfunfact2:
    m 3hub "Alright, it's time for another one of these!"
    m 1eua "Here's Monika's Shark Fun Fact of the Day!"
    m 1esc "Most sharks have to keep swimming almost non-stop so water keeps flowing over their gills."
    m 1hksdla "If they stop moving for too long, they risk suffocating.{w=0.5}{nw}"
    extend 3wsc " They even keep swimming while they sleep!"
    m 2esb "There are some exceptions though.{w=0.5} For example, bottom-dwelling sharks!"
    m 3eua "They can actively pump water over their gills while resting completely still on the seafloor."
    m 1eub "That's why you can often find species like nurse sharks or wobbegongs just lying there for hours."
    m 1tka "Pelagic sharks, like great whites or makos, don't have that luxury.{w=0.5} They're basically forced to keep moving their whole lives."
    m 1etd "Scientists even believe some sharks use a special kind of sleep called unihemispheric sleep..."
    m 3esa "Where one half of their brain rests while the other half stays active enough to keep them swimming."
    m 7etb "Pretty wild when you think about it, right?"
    return
	
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sharkfunfact3",
            category=['sharks'],
            prompt="Shark Fun Fact #3",
            conditional="seen_event('sharkfunfact2')",
            action=EV_ACT_POOL,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}
        )
    )

label sharkfunfact3:
    m 1huu "Another day, another fun fact!"
    m 3tub "Here's Monika's Shark Fun Fact of the Day!"
    m 2eua "Sharks don't have any bones.{w=0.5} They're a special type of fish called elasmobranchs, which means their skeletons are made of cartilage instead."
    m 2hua "If you don't know, that's the same flexible tissue your ears and the tip of your nose are made from!"
    m 3eub "There are a few reasons why this is useful for them.{w=0.5}{nw}"
    extend 1esd " Firstly, cartilage is much lighter than bone, so sharks don't have to work as hard just to stay afloat."
    m 1eka "That's especially important, since a lot of shark species have to keep swimming almost all the time."
    m 1wua "Then there's speed.{w=0.5} Because their bodies are so light and flexible, some of them can reach incredible speeds, making them excellent hunters!"
    m 4eub "A good example is the shortfin mako."
    if persistent._mas_player_units == "metric":
        m 2suu "It's the fastest known shark species, able to reach speeds of about 74 kilometers per hour."
    elif persistent._mas_player_units == "imperial":
        m 2suu "It's the fastest known shark species, able to reach speeds of about 46 miles per hour."
    else:
        m 2suu "It's the fastest known shark species, able to reach speeds of about 74 kilometers, or 46 miles, per hour."
    m 2tsu "I bet you can imagine how fast that is."
    m 1esc "There's also a downside, though."
    m 1gksdla "Since they don't have a rigid skeleton or a ribcage, sharks can actually be crushed under their own weight if they're out of the water for too long."
    m 3hub "That's one of the reasons you almost never see them surviving long on land, and also why we have bones!"
    m 7huu "And...{w=1.0} That's all I got to say!"
    m 1esb "Thank you for you time!"
    return