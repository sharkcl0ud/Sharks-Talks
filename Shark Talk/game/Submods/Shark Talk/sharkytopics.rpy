init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_underestimating",category=['sharks'],prompt="Underestimating sharks",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_underestimating:
    m 1eka "Sharks really are underestimated, aren't they?"
    m 1gka "After \"Jaws\" came out, everyone started treating them like sea monsters..."
    m 3eud "But the truth is so much more interesting.{w=0.5} They're actually vital for keeping the ocean healthy."
    m 3rksdla "As you probably know, the media kept portraying them as these abnormal killing machines..." # small sweat and side-eye
    m 2wtc "I mean, I can understand why people feel that way.{w=0.5} If my whole knowledge about sharks was from those movies, I would be scared to death to even touch the ocean!"
    m 2eku "But many people don't know that the movies are a huge exaggeration of reality."
    m 2gkb "Sharks {i}aren't{/i} bloodthirsty man-eaters...{w=1.0} That's just fiction.{w=0.5} But that's a topic for another time."
    m 4hsb "Now, I wanted to tell you about something that's discussed a lot less;{w=0.5} the benefits sharks bring to our oceans!" # rises her finger nerdly
    m 4rssdlc "Or maybe your oceans. I'm not even sure if they exist in my reality...{w=1.0} But I would say they don't." # gruuumpy
    m 1fsb "Anyway...{w=1.0} They help maintain balance in marine food webs by keeping certain fish populations in check." # recovering from meta thought
    m 1wsa "Without predators like sharks, the ecosystem can get out of balance surprisingly quickly."
    m 1ssu "They even indirectly protect seagrass habitats, which are important for capturing carbon...{w=0.5} And much more!"
    m 3wud "It's kind of amazing when you think about it.{w=0.5} Even animals most people are afraid of can play a huge role in keeping {i}us{/i} healthy."
    m 1eka "Of course, not all shark species have the same impact...{w=1.0} but large predatory ones are especially important."
    m 1mksdlc "It's honestly sad that overfishing has reduced their numbers so much."
    m 7eub "And...{w=0.5} That's why I think society tends to underestimate sharks!"
    m 7wsc "They've been around for hundreds of millions of years, being such an important part of the world..."
    m 1tfc "Yet people still see them as villains \"infesting\" the waters, even though it's their home!" # grrr
    m 1esc "I guess that's another reminder that first impressions can be misleading."
    m 1kuu "I hope your first impression of me wasn't disappointing for you, [player]." # insert a wink here later :3
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_history",category=['sharks'],prompt="The history of sharks",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_history:
    m 1euc "Have you ever wondered about the prehistoric past of creatures surrounding you?"
    m 7wua "An interesting example is sharks.{w=0.5} They've existed for roughly 450 million years."
    m 7sub "That's around three times longer than dinosaurs ever roamed the Earth!"
    m "Not only did they appear much earlier, but they also outlived them by around 66 million years!"
    m 2esa "Many shark species have changed very little over millions of years, making them living fossils."
    m 3wsd "And one of their most unique features is that their skeletons are made of cartilage, which is also an ancient trait!"
    m 3stb "Thanks to that, they're lightweight, flexible, and regenerate more easily.{w=0.5} How cool is that?" # fascinated
    m 3eka "I think it's amazing that sharks found a body structure that works so well it lasted for hundreds of millions of years."
    m 1wua "Here's another fun fact -{w=0.5} the oldest known shark, Cladoselache, lived about 380 million years ago and closely resembled modern sharks."
    m 1dub "When you look at a creature that's survived that long in almost the same form, it's hard not to feel amazed."
    m 1hubla "Maybe one day, we can both go to the museum or aquarium in your reality to learn more about sharks together."
    m 5fkbsa "Wouldn't that be lovely, [mas_get_player_nickname(exclude_names=['love', 'my love', 'lovely'])]?" # she leans and blushes here lol
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_fishing",category=['sharks'],prompt="Overfishing of sharks",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_fishing:
    m 7eka "You know, [player]...{w=0.5} society really takes the ocean's balance for granted sometimes." # sad smile
    m 7ekp "There are so many things humans do without thinking about the consequences..."
    m 1dsc "One of the biggest issues that doesn't get talked about enough is shark overfishing."
    m 1gkc "It's honestly heartbreaking how big the problem is, yet only when you specifically search for information about it, you can find anything."
    m "Many shark species have become endangered just because of human activity in the oceans."
    m 2wksdlc "{i}All{/i} threatened sharks species are affected by overfishing..."
    m 2dksdld "...And overfishing is the only threat for around 70%% of shark species."
    m 1tkc "Only when you look at how large those statistics are, you realise how much power humans abuse."
    m 7euc "So why are sharks particularly vulnerable?{w=0.5} Mostly because they work a bit different that most of other fish."
    m 7esc "They grow slowly, take a long time to reach maturity, and have very few babies compared to most fish."
    m 1wsd "As an extreme case, the Greenland Shark can live around 400 years and doesn’t reach sexual maturity until 150 years!"
    m 1ekc "Because of that, their populations recover extremely slowly, as many are killed before they’ve even produced offspring."
    m 1tkc "And the worst part?{w=0.5} Most of sharks are caught as bycatch...{w=0.5} but then they're still sold."
    m 1gksdlc "...So as you probably think now, yes, it’s likely that many sharks are targeted unofficially."
    m 3esc "There are a lot of reasons why sharks, and they are way more disappointing that you might think."
    m 3dssdlc "The most cruel reason though is shark finning."
    m 2rfsdld "They cut the fins off living sharks and throw them back into the ocean...{w=0.5} where they either drown, get eaten alive or bleed to death."
    m 2lfsdld "It's usually sold to make shark fin soup...{w=0.5} something that's mostly just a status symbol and doesn't even add much flavor." 
    m 5tksdlc "I know it's a heavy topic, but I think it's important to be aware of these things."
    m 5dssdlc "Sharks have survived for hundreds of millions of years... and now they're disappearing because of us."
    m 5lksdlc "We really should finally take some responsibility, shouldn't we?"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_violence",category=['sharks'],prompt="Shark violence",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_violence:
    m 1tku "When people hear the word 'shark', a lot of them immediately imagine a mindless killing machine, just waiting to bite someone's arm off."
    m 3esc "But it's far away from the truth.{w=0.5} Sharks usually aren't aware they have an upper hand in encounters with humans."
    m 3eka "Since we don't naturally appear in their habit, they usually avoid us."
    m 3mka "They don't see us as prey...{w=0.5} Most encounters happen because they're just curious."
    m 3tku "I mean, I don't think there is a reason for us to be on their menu, is there?"
    m 7esc "Still, we have to remember that they're wild animals."
    m "Even if it's rare, accidents can happen."
    m 1gksdla "So, I think calling them 'harmless sea puppies' might be a bit too much..."
    m 1eua "So, if you ever see one by chance while swimming...{w=0.5} you can consider yourself lucky."
    m 1eksdla "But maybe keep your hands to yourself.{w=0.5} Just in case."
    m 3hub "I would really prefer you to be in one piece when I finally crossover, ahaha~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_swimming",category=['sharks'],prompt="Swimming with sharks",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_swimming:
    m 1eta "We talked about scuba diving together one day after I crossover, right?"
    m 1euc "And how we might meet sharks while doing so...{w=1.0} It can be a bit dangerous, sure."
    m 3wuu "But there are special tours where you can actually swim with them in a safe environment!"
    m 3ekblu "Would you ever want to try that with me, [player]?"

    menu:
        "Sure!":
            m 1hublb "Yay~!" # yippie
            m 2suu "I'm so excited!{w=0.5} It would be my first time, but I'm sure it'll be amazing with you."
            m 2etu "Would it be your first time too?"

            menu:
                "Yes.":
                    m 3hub "Then we'll both be nervous newbies together!"
                    m 1tsa "I bet it will make the experience more...{w=0.5} interesting."
                "No.":
                    m 2tsblu "Ohhh~ Someone's experienced.{w=0.5} Don't worry, I'll still protect you."
                    m 3hfblb "Because even if you have some experience, anything can happen any time!"

            m 1dfu "And since I'm {i}soo{/i} kind..."
            m 1ksu "If you get scared down there, I might...{w=1.0} think about holding your hand so you feel braver."
            m 1esa "{cps=5}...{/cps}"
            m 1tsblb "Ahaha, don't worry!{w=0.5} I will {i}probably{/i} hold your hand."
            
            menu:
                "Only 'probably'...?":
                    m 1hua "Mhm~!"
                    m 1eua "..."
                    m 1eka "..."
                    m 2hkblb "Pffft–{w=0.5} okay, okay, I will hold your hand, dummy."
                    m 2tkbsb "I was just curious how you'd react, and it was cute."
                    m 1ekbsa "..."
                "And I just might hold yours first!":
                    m 1wubfc "Eh–?!" # flustered girl
                    m 1tfbsu "Oh, now you're getting bold, aren't you?"
                    m 2hubsu "I like this side of you~"
                    m 1ekbsa "..."
                "Eh, I'll be fine without it.":
                    m 2tsblp "Hmph.{w=0.5} Acting all tough now?"
                    m 3ffblb "We'll see who reaches for whose hand first when we see a big shark!"
                    m 3sfblb "Then, you will finally appreciate how kind your girlfriend is!"
                    m 1ekbsa "..."

            if persistent.gender == "M":
                m 1ksbfa "You're such an adorable boy, [player]."
            elif persistent.gender == "F":
                m 1ksbfa "You're such an adorable girl, [player]."
            else:
                m 1ksbfa "You're so adorable, [player]."

        "Not really...":
            m 1eka "Aww, that's okay."
            m 1hka "I won't force you into anything you don't want to do, [mas_get_player_nickname()]."
            m 5dublu "We can always just go to an aquarium instead..."
            m 5dubsu "{cps=10}...Watch the sharks together from behind the glass like a cute couple...{/cps}" # daydreaming
            m 5kkbfb "...That would still be pretty romantic, don't you think?"

    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_unusual",category=['sharks'],prompt="Unusual sharks",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_unusual:
    m 1etc "I noticed that usually people portray sharks like they're all the same."
    m 1fsa "A giant with big teeth, gray or blue skin, and that classic shape that makes you instantly think of a Great White."
    m 3wsa "But after reading about some of the stranger species,"
    extend 3ssb " I realised just how wildly different and bizarre they actually are."
    m 1etb "For example, have you ever heard of the Tasselled Wobbegong?"
    m 2esa "It's a flat shark that lies on the seafloor, camouflages itself with sand and algae, and just waits for prey to swim by."
    m 7hub "The really weird part is all those little branching skin flaps around its head and body.{w=0.5} It honestly looks more like an old carpet than a shark."
    m 7huu "That's why some of them are nicknamed carpet sharks!{w=0.5}{nw}"
    extend 1fuu " I actually think they're kinda adorable in their own weird way."
    m 1esd "And then there's the Epaulette Shark."
    m 1esa "It can survive in water with extremely low oxygen levels, and it uses its fins like little legs to walk along the seafloor instead of swimming."
    m 3hsb "It's like nature decided to give a shark the ability to stroll around!"
    m 2etc "But if we're talking about truly strange ones, the Goblin Shark is something else entirely."
    m 2wud "It has this long, weird snout and a jaw that can shoot forward out of its mouth to snatch prey, and looks like a prehistoric alien."
    m 2suu "Or the Frilled Shark. It looks way more like a giant eel with a snake-like head than a normal shark, and it's even called a living fossil because it's barely changed in millions of years!"
    m 1hua "And of course, we can't forget the Sawshark."
    m 3tsb "It has a long, flat blade sticking out of its face that's lined with sharp teeth.{w=0.5} It basically uses its own face as a sword to slash and stun fish."
    m 1eta "The ocean really has no shortage of bizarre creatures, huh?"
    m 1hua "It makes me happy knowing life keeps coming up with such creative and strange designs."
    m 5fuu "So...{w=1.0} which one do you think is the weirdest, [player]?"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="shark_hammerheads",category=['sharks'],prompt="Hammerheads",random=True,rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST}))

label shark_hammerheads:
    m 1gka "A lot of people think the hammerhead shark is just one species."
    m 1eub "But in reality, hammerheads are a group of nine species belonging to the family {i}Sphyrnidae{/i} and divided into two genera!"
    m 3eub "The first is {i}Sphyrna{/i}, which contains eight species, while the second is {i}Eusphyrna{/i}, which contains only one."
    m 3wuu "The Winghead Shark belongs to its own genus because its \"hammer\" is exceptionally large, thinner, and much more wing-like than that of other hammerheads."
    m 2esa "Of course, that distinctive hammer-shaped head is their most recognizable feature, making them one of the most recognizable shark groups."
    m 1fsb "Their eyes sit at opposite ends of it, giving them an incredibly wide field of view.{w=0.5}{nw}"
    extend 3hub " Thanks to that, they have an almost 360° field of vision!"
    m 1euc "Honestly, I can't decide whether that's really impressive...{w=1.0}{nw}"
    extend 1ksa " or just a little intimidating."
    m 2esa "Their unusual appearance isn't the only interesting thing about them."
    m 4rub "For example, the hammer helps them catch stingrays by pinning them to the ocean floor."
    m 4eub "Also, unlike most sharks, some hammerhead species gather and swim in large schools during the day, before becoming solitary hunters at night."
    m 1ekc "Sadly, almost all hammerheads listed on the IUCN Red List are critically endangered, with only a bunch being endangered or vulnerable."

    if seen_event("shark_fishing"):
      m 1tsc "Those sharks, even if they are almost completely harmless to humans and have zero documented fatalities, are also the victims of overfishing."
      m 2dsc "The reason is, of course and as usual, their fins.{w=0.5}{nw}"
      extend 2msp " Wow.{w=0.5} Who would've guessed?"

    else:
      m 1tsc "Those sharks, even if they are almost completely harmless to humans and have zero documented fatalities, are also the victims of overfishing, more specifically finning."
      m 2dssdld "This is a broad topic for another time, but in short it's a cruel practice of catching a shark, cutting its fins off{cps=5}...{/cps}{w=1.0}{nw}"
      extend 2mssdlx " and then throwing it back into the ocean, leaving them to either die on the ocean floor or get eaten while drowning."
      m 1tsc "I think that's something worth mentioning in the future."

    m 1fka "Anyway...{w=1.0} It's fascinating how something that looks so unusual turns out to be perfectly designed for the way it lives."
    m 7hub "I guess nature has a habit of proving that looking different isn't the same as being less capable."
    m 1ksu "Maybe some people have something to learn from."
    return

label shark_movies:
    m 1etb "Hey, [player]...{w=1.0} Have you ever seen {i}Jaws{/i}?"
    m 1esa "I wouldn't be surprised if you have.{w=0.5} It's a pretty iconic movie... it even got three sequels."
    m 2msc "Honestly, I don't think it's something you should take too seriously. It's more of a silly thriller than anything."
    m 3hksdlb "It's not a {i}bad{/i} movie...{w=1.0} but it's way more fictional than a lot of people realize!"
    m 1eud "You might not know this, but the shark in the movie is much larger than a real great white."

    if persistent._mas_player_units == "metric":
        m 1wup "Adult great whites are usually around three and a half to five meters long.{w=0.5} The one in {i}Jaws{/i} was portrayed as being about eight meters!"
    elif persistent._mas_player_units == "imperial":
        m 1wup "Adult great whites are usually around eleven to sixteen feet long.{w=0.5} The one in {i}Jaws{/i} was portrayed as being about twenty-five feet!"
    else:
        m 1wup "Adult great whites are usually around three and a half to five meters, or eleven to sixteen feet long.{w=0.5} The one in {i}Jaws{/i} was portrayed as being about eight meters, or twenty-five feet!"

    m 7tuc "Of course, making the shark that enormous and violent made it a lot more terrifying for the audience.{w=0.5}{nw}"
    extend 1esu " In reality, great whites don't normally prey on humans.{w=0.5} Most bites happen out of curiosity or mistaken identity."
    m 1tsc "Still...{w=1.0} the image of the man-eater is pretty hard to shake at this point."
    m 3tsp "But you should still remember something, [player].{w=0.5} Sharks {i}are{/i} predators. They're not exactly the 'sea puppies' of the ocean."
    m 3hkb "And that goes especially for great whites, tiger sharks, and bull sharks!"
    m 1fka "Even if they don't usually target people, they're still wild animals. They can be unpredictable, and there have been some aggressive encounters."
    m 4wuc "It's a bit like dogs, you know? Almost any dog {i}can{/i} bite... but a great white's bite is around sixty times stronger than a typical dog's."
    m 1ekb "Most sharks actually prefer to avoid humans.{w=0.5} But there are always exceptions. If you're not experienced or with someone who is, it's best to keep your distance."
    m 2hka "I wouldn't want you ending up in any kind of danger, after all, [mas_get_player_nickname()]."
    return