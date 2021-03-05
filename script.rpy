#####################################
## Visiting Day, © 2021 Good Tales ##
#####################################

## Characters #################################################################################################################
define a = Character("Anne", image="anne", what_prefix='"', what_suffix='"')
define b = Character("Boss", what_prefix='"', what_suffix='"', what_italic=True)
define c = Character("Charles", image="charles", what_prefix='"', what_suffix='"')
define g = Character("[g_name]", image="gabe", what_prefix='"', what_suffix='"')
define ls = Character("Lucas", image="lucas", what_prefix='"', what_suffix='"')
define ly = Character("Lucy", image="lucy", what_prefix='"', what_suffix='"')
define m = Character("[m_name]", image="mike", what_prefix='"', what_suffix='"')
define w = Character("Worker", what_prefix='"', what_suffix='"')


## Images #####################################################################################################################

# Character Sprites
image anne = Placeholder("girl")
image charles = Placeholder("boy")
image gabe = Placeholder("boy")
image lucas = Placeholder("boy")
image lucy = Placeholder("girl")
image mike = Placeholder("boy")

# Backgrounds
image bg black = "#000000"
image bg desk = "#aaaaaa"
image bg door = "#4a7f9c"
image bg hallway = "#3700ff"
image bg lobby = "#94bfd8"
image bg room = "#3cabe0"
image bg white = "#ffffff"

# Misc.
image goodtales = "Good Tales Transparent.png"
image goodtales_presents = Text("Good Tales presents", style="intro")
image logo = "gui/logo.png"
image logo_shine:
    "logo"
    pause 0.75
    "gui/logo shine/shine01.png"
    pause 0.04
    "gui/logo shine/shine02.png"
    pause 0.04
    "gui/logo shine/shine03.png"
    pause 0.04
    "gui/logo shine/shine04.png"
    pause 0.04
    "gui/logo shine/shine05.png"
    pause 0.04
    "gui/logo shine/shine06.png"
    pause 0.04
    "gui/logo shine/shine07.png"
    pause 0.04
    "logo"
    pause 0.04
    "gui/logo shine/shine08.png"
    pause 0.04
    "gui/logo shine/shine09.png"
    pause 0.04
    "gui/logo shine/shine10.png"
    pause 0.04
    "gui/logo shine/shine11.png"
    pause 0.04
    "logo"
    pause 3


## Audio ######################################################################################################################

# Audio Channels
init python:
    renpy.music.register_channel("sound2", mixer="sfx", loop=False)
    renpy.music.register_channel("ambience1", mixer="sfx", loop=True)
    renpy.music.register_channel("ambience2", mixer="sfx", loop=True)

# Music 
define audio.a_new_day = "<loop 3.73>audio/music/a_new_day.ogg"
define audio.autumn_leaves = "<loop 5.2>audio/music/Autumn-Leaves_Looping.mp3"
define audio.blue_ridge = "audio/music/Blue-Ridge_Looping.mp3"
define audio.delivering_the_goods = "audio/music/Delivering-the-Goods_Looping.mp3"
define audio.evening_stars_rising = "audio/music/Eveing-Stars-Rising.mp3"
define audio.far_away_puzzle_places = "audio/music/Far-Away-Puzzle-Places.mp3"
define audio.high_altitude_bliss = "audio/music/High-Altitude-Bliss.mp3"
define audio.norther_passage = "audio/music/Northern-Passage.mp3"

# Sound Effects
define audio.crowd_running = "audio/se/crowd_running.ogg"
define audio.crowd_talking = "<to 28 loop 1>audio/se/crowd_talking.ogg"
define audio.door = "audio/se/door.ogg"
define audio.elevator = "audio/se/elevator.ogg"
define audio.intercom = "audio/se/intercom.ogg"
define audio.knock = "audio/se/knock.ogg"
define audio.light_switch = "audio/se/light_switch.ogg"
define audio.running = "audio/se/running.ogg"


## Styles #####################################################################################################################
style intro:
    font "gui/fonts/Abbasy Calligraphy Typeface.ttf"
    color "#65c8ff"
    text_align 0.5
    size 100
    outlines [(1.0, "#ffffff", 0.0, 0.0)]


## Transforms #################################################################################################################
transform title:
    zoom 0.75
    xalign 0.95 yalign 0.05

transform middle:
    xalign 0.5 yalign 0.5

transform right:
    xalign 0.8 yalign 0.5

transform left:
    xalign 0.2 yalign 0.5


## Transitions ################################################################################################################
define elevator_close = ImageDissolve("elevator.png", 1.0)
define elevator_open = ImageDissolve("elevator.png", 1.0, reverse=True)
define fadepause = Fade(1.0, 1.0, 1.0)
define iris = ImageDissolve("iris.png", 0.75)
define longdissolve = Dissolve(3.0)


## Variables ##################################################################################################################

# Standard
default first_story = True
default g_name = "Gabe"
default m_name = "New Guy"
default stories = {"story1": False, "story2": False, "story3": False, "story4": False, "story5": False}


# Splash ######################################################################################################################
label splashscreen:
    stop music
    scene bg black
    pause 1
    show goodtales with Dissolve(2)
    pause 1.5
    hide goodtales with Dissolve(2)
    pause 1
    return

label before_main_menu:
    scene bg black
    scene bg lobby with iris
    pause 1.0
    play music a_new_day
    show logo_shine:
        alpha 0.0
        middle
        yalign 0.4
        zoom 0.9
        parallel:
            ease 0.5 middle
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.5 zoom 1.0
    pause 3
    play music blue_ridge
    show logo:
        middle
        ease 1 title
    hide logo_shine
    pause 1
    return

## Story ######################################################################################################################
label start:
    window hide
    stop music fadeout 3.0
    scene black
    with longdissolve
    pause 2
    window show
    "{i}{size=+10}\"Let there be light!\"{/size}{/i}"
    window hide
    play music autumn_leaves
    play sound light_switch
    scene bg desk with Dissolve(0.1)
    pause 3
    window show dissolve
    w "Gabe, must you always do that when you hit the lights?"
    show gabe at middle with dissolve
    pause 0.1
    g "Why not?{w=0.35}\nI gotta make things interesting around here!"
    w "It's the Visiting Day, Gabe; things are going to be interesting by default."
    g "And somehow they're less interesting when your downer mouth starts going off."
    w "Hmph."
    w "Say, why is that chair on the other side of you empty?"
    g "Huh.{w=0.5} Good question.{w=0.5}\nI heard it belongs to a new guy working the Visiting Day for the first time."
    w "Well, it's gonna be his last time if he doesn't--"
    $renpy.music.set_pause(True, "music")
    window hide
    play sound door
    pause 1
    play sound2 running
    show gabe:
        ease 0.5 left
    show mike:
        offscreenright
        ease 0.5 right
    m "{cps=*1.5}I'm here!!\nI'm sorry I'm late!!{/cps}"
    m "{cps=*1.5}I missed the bus that was supposed to take me here, so I had to decide if it was worth waiting for the next one or finding some other mode of transportation...{/cps}"
    m "{cps=*1.5}...but by the time I settled on the latter, the next bus had arrived, but then I missed that, too, and--{/cps}!"
    g "Whoa, whoa!{w=0.35} Settle down, partner!"
    g "You're here now, and there's still time before the day begins.{w=0.5}\nNo need to panic."
    m "A-Ah, right.{w=0.35} Of course."
    $renpy.music.set_pause(False, "music")
    m "I'm Mike, by the way. Pleased to meet you."
    g "Name's Gabe. The feeling is mutual."
    $m_name = "Mike"
    g "So, word on the street is that this is your first time working during the big Day, eh?"
    m "Well, the word would be correct.{w=0.5}\nTo be honest, I'm quite nervous."
    g "Ah, there's no need to be nervous, Mike."
    g "Trust me, I've been working at the desk for a little over a thousand years now, and I promise that it's as simple as it gets."
    g "They did tell you what the job entails, right?"
    m "Yes, of course."
    m "When the human approaches, you ask them for the name, date of birth, and date of death of the person they wish to visit, as well as the reason for the visit."
    m "From there, you search for the file of the Visited, find their room number, and give it to the Visitors."
    g "Well, well. I'm glad management is still properly training the newbies.{w=0.5}\nI'd say you have nothing to worry about."
    m "You say that, but I still can't help but feel nervous about how I'll react to some of these humans."
    m "I know 10 years is nothing for us, but for them, it's one eighth of their life!{w=0.5}\nA tenth, if they're lucky!"
    m "So the emotions they must be feeling about waiting that long {i}at most{/i} to see someone they cared about..."
    g "Oh, I assure you that the tissue boxes on the desks aren't for taking care of a stuffy nose."
    g "But it's all a part of the job.{w=0.5}\nIf it reassures you, they're tears of happiness, not sorrow."
    m "I suppose that's true..."
    g "Just sit back and relax, Mike.{w=0.35} You'll do fine, I promise."
    window hide dissolve
    play sound intercom
    stop music fadeout 3
    pause 1
    hide mike
    hide gabe
    with dissolve
    pause 2
    window show dissolve
    b "Attention, Beyond Suites employees!{w=0.35}\nThe 2020 Visiting Day is about to begin momentarily!"
    b "If you are not at your station, please head there now so that we may begin without any issues."
    b "It's estimated that this will be a record-breaking attendance this year, so please perform at your absolute best as to assure all may see their Visited!"
    b "Thank you, and be sure to put on a smile!"
    pause 0.5
    show gabe at left
    show mike at right
    with dissolve
    pause 0.1
    g "Alright, Mike.{w=0.35} Time to get to work!"
    g "Still nervous?"
    m "Yes.{w=0.5} Very much so."
    g "I'm telling you, you'll be fine."
    g "Although you {i}may{/i} wanna brace yourself for the stampede."
    m "The what?"
    window hide dissolve
    pause 0.5
    play ambience1 crowd_running fadein 1
    play ambience2 crowd_talking fadein 1
    pause 2
    scene bg lobby with dissolve
    pause 1
    # Crowd silhouettes fade in
    pause 2
    scene bg desk
    show gabe at left
    show mike at right
    with dissolve
    pause 0.1
    window show dissolve
    m "O-Oh my!"
    g "The Boss wasn't kidding; that crowd seems larger than ever before!"
    g "I guess that's all the more reason to keep your nerves calm and head focused.{w=0.5}\nCan you do that, Mike?"
    m "I don't believe so, but I'll certainly do my best!"
    g "That'll have to do."
    window hide dissolve
    pause 1
    scene bg lobby
    #show crowd
    with dissolve
    pause 1
    play music blue_ridge
    pause 1
    #Scene pans up to show ceiling
    pause 2
    show goodtales_presents at middle with dissolve
    pause 3
    hide goodtales_presents with dissolve
    pause 1
    show logo at middle with dissolve
    pause 4
    stop music fadeout 5
    stop ambience1 fadeout 5
    stop ambience2 fadeout 5
    scene black with longdissolve
    pause 4

label story_select:
    play music far_away_puzzle_places
    scene bg desk with longdissolve
    pause 1
    window show dissolve
    w "Next!"
    window hide dissolve
    menu:
        "Charles Robinson" if not stories["story1"]:
            jump story1

    return

label workerhelp:
    m "Follow the signs around the lobby; they'll lead you in the direction you need to go."
    m "Or you may receive help from the workers spread along the floor."
    $first_story = False
    return

# Save for a scene between stories

    # g "But I can tell you right now that you don't have to stress too much about the \"why\" of the visit; it's mainly for statistics and stuff."
    # g "99\% of the time, it's friends or family coming to see them, but you tend to get your general curve ball in there."
    # m "Curve ball?{w=0.5} Like what?"
    # g "Well, there's a rumor floating around that in the European district one year, a French woman was visited by an amateur artist because he saw a painting of her and wanted to make his own."
    # m "Well, that's kinda sweet."
    # g "I should probably mention that it was a nude painting."
    # m "Oh."
    # g "Again, though, just a rumor."
    # g "Besides, the odds of something like that happening here are next to none. Expect to hear \"I'm her daughter!\" or \"We grew up together in the 50's!\"."