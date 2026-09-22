# the quiz part of the submod. never ever done that before :')
init 5 python:
    addEvent(
        Event(
            persistent._mas_game_database,
            eventlabel="sharky_quiz_start",
            prompt="Shark quiz",
            unlocked=True
        ),
        code="GME",
        restartBlacklist=True
    )

image greatwhite = "Submods/Shark Talk/images/greatwhite.jpg"
image greathammerhead = "Submods/Shark Talk/images/greathammerhead.jpg"
image goblin = "Submods/Shark Talk/images/goblin.jpg"
image epaulette = "Submods/Shark Talk/images/epaulette.jpg"
image blue = "Submods/Shark Talk/images/blue.jpg"
image blacktipreef = "Submods/Shark Talk/images/blacktipreef.jpg"
image bull = "Submods/Shark Talk/images/bull.jpg"
image lemon = "Submods/Shark Talk/images/lemon.jpg"
image leopard = "Submods/Shark Talk/images/leopard.jpg"
image oceanicwhitetip = "Submods/Shark Talk/images/oceanicwhitetip.jpg"
image tiger = "Submods/Shark Talk/images/tiger.jpg"
image frilled = "Submods/Shark Talk/images/frilled.jpg"
image thresher = "Submods/Shark Talk/images/thresher.jpg"
image shortfinmako = "Submods/Shark Talk/images/shortfinmako.jpg"
image whale = "Submods/Shark Talk/images/whale.jpg"



init python:
    import random
    shark_questions = [
        {"image": "greatwhite", "correct": "Great White Shark"},
        {"image": "greathammerhead", "correct": "Great Hammerhead Shark"},
        {"image": "goblin", "correct": "Goblin Shark"},
        {"image": "epaulette", "correct": "Epaulette Shark"},
        {"image": "blue", "correct": "Blue Shark"},
        {"image": "blacktipreef", "correct": "Blacktip Reef Shark"},
        {"image": "bull", "correct": "Bull Shark"},
        {"image": "lemon", "correct": "Lemon Shark"},
        {"image": "leopard", "correct": "Leopard Shark"},
        {"image": "oceanicwhitetip", "correct": "Oceanic Whitetip Shark"},
        {"image": "tiger", "correct": "Tiger Shark"},
        {"image": "frilled", "correct": "Frilled Shark"},
        {"image": "thresher", "correct": "Thresher Shark"},
        {"image": "shortfinmako", "correct": "Shortfin Mako Shark"},
        {"image": "whale", "correct": "Whale Shark"},
    ]

init python:
    correct_reactions = [
        "Correct!",
        "That's right!",
        "Yup!",
        "Good one!",
        "Exactly!",
        "Yes! That's the {correct}!"
    ]

    wrong_reactions = [
        "Nope… that was the {correct}.",
        "Aww, wrong. It was the {correct}.",
        "Not quite… that was the {correct}.",
        "Close, but no. It was the {correct}.",
        "Hmm, not that one. The correct answer is {correct}.",
        "Oops! That was actually the {correct}."
    ]

screen shark_image(img):
    add img:
        xalign 0.0
        yalign 0.38
        xoffset 40
        zoom 0.40
    zorder 300

label sharky_quiz_start:
    m 7hub "I'll show you a picture and you tell me which shark it is."
    m 1hua "Ready? Let's go!"

    show monika at t22 with move

    python:
        total_questions = 10
        score = 0
        questions = list(shark_questions)
        random.shuffle(questions)
        questions = questions[:total_questions]

    $ question_number = 0

    while question_number < total_questions:
        $ current = questions[question_number]
        $ correct = current["correct"]
        $ img = current["image"]

        python:
            wrong = [q["correct"] for q in shark_questions if q["correct"] != correct]
            num_wrong = min(3, len(wrong))
            wrong = random.sample(wrong, num_wrong)
            answers = wrong + [correct]
            random.shuffle(answers)

        $ question_number += 1

        show screen shark_image(img)

        m 1eua "Question [question_number] of [total_questions]!"
        m 1eua "What shark is this?"

        $ menu_choices = [(ans, ans) for ans in answers]
        $ chosen = renpy.display_menu(menu_choices)

        hide screen shark_image

        if chosen == correct:
            $ score += 1
            $ reaction = random.choice(correct_reactions).format(correct=correct)
            m 1eub "[reaction]"
        else:
            $ reaction = random.choice(wrong_reactions).format(correct=correct)
            m 1hksdlu "[reaction]"

    m 3fub "Okay, that's all of [total_questions] questions!"

    if score == total_questions:
        m 3sub "Perfect score!{w=0.5}{nw}"
        extend 2tsblu " Have you been practicing lately, [player]?{w=0.5} You know, trying to impress me and stuff..."
        m 1hua "Ahahaha, I'm just messing with you~.{w=0.5} Good job [mas_get_player_nickname()], I'm proud of you."
    elif score >= total_questions * 0.7:
        m 2hub "Almost perfect!{w=0.5} You never fail to impress me, [mas_get_player_nickname()]."
    elif score >= total_questions * 0.4:
        m 1eua "Not bad, [mas_get_player_nickname()].{w=0.5}{nw}"
        extend 7hub " Remember, practice makes perfect.{w=0.5} Never give up!"
    else:
        m 1ekb "Your score might not be perfect,"
        extend 1ksu " but you definitely are.{w=0.5} With a little bit of practice, you will crush the quiz with ease."

    m 1eta "Would you like to play again?"

    menu:
        "Yes":
            jump sharky_quiz_start
        "No":
            m 2ekb "Okay, let's play again someday, alright?"

    hide screen shark_image
    show monika at t11 with move
    return