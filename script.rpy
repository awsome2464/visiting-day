#####################################
## Visiting Day, © 2023 Good Tales ##
#####################################

## Characters #################################################################################################################
define an = Character("Anne", image="anne")
define a = Character("[aName]", image="ariel")
define b = Character("Boss", what_italic=True)
define c = Character("Charles", image="charles")
define g = Character("Gabe", image="gabe")
define ls = Character("Lucas", image="lucas")
define ly = Character("Lucy", image="lucy")
define m = Character("Michelle", image="michelle")
define mo = Character("Moss", image="moss")
define w = Character("Worker")


## Images #####################################################################################################################

# Character Blinks
image ariel_blink:
    "Characters/Ariel/Ariel Eyes 01.png"
    pause 3 + renpy.random.randint(0, 2) + renpy.random.random()
    "Characters/Ariel/Ariel Eyes 03.png"
    pause 0.05
    "Characters/Ariel/Ariel Eyes 04.png"
    pause 0.05
    "Characters/Ariel/Ariel Eyes 03.png"
    pause 0.05
    "Characters/Ariel/Ariel Eyes 02.png"
    pause 0.05
    repeat

image gabe_blink:
    "Characters/Gabe/Gabe Eyes 01.png"
    pause 3 + renpy.random.randint(0, 2) + renpy.random.random()
    "Characters/Gabe/Gabe Eyes 03.png"
    pause 0.05
    "Characters/Gabe/Gabe Eyes 04.png"
    pause 0.05
    "Characters/Gabe/Gabe Eyes 03.png"
    pause 0.05
    "Characters/Gabe/Gabe Eyes 02.png"
    pause 0.05
    repeat

# Character Sprites
image anne = Placeholder("girl")

layeredimage ariel:
    always:
        "Characters/Ariel/Ariel Base.png"
    group mouth:
        attribute grin:
            "Characters/Ariel/Ariel Mouth 01.png"
        attribute frown:
            "Characters/Ariel/Ariel Mouth 02.png"
        attribute scream:
            "Characters/Ariel/Ariel Mouth 03.png"
    always:
        "ariel_blink"
    group eyebrows:
        attribute sad:
            "Characters/Ariel/Ariel Eyebrows 01.png"
        attribute casual:
            "Characters/Ariel/Ariel Eyebrows 02.png"

image charles = Placeholder("boy")

layeredimage gabe:
    always:
        "Characters/Gabe/Gabe Base.png"
    group mouth:
        attribute grin:
            "Characters/Gabe/Gabe Mouth 01.png"
        attribute blank:
            "Characters/Gabe/Gabe Mouth 02.png"
    always:
        "gabe_blink"
    group eyebrows:
        attribute level:
            "Characters/Gabe/Gabe Eyebrows 01.png"
        attribute casual:
            "Characters/Gabe/Gabe Eyebrows 02.png"
        attribute raised:
            "Characters/Gabe/Gabe Eyebrows 03.png"

image lucas = Placeholder("boy")
image lucy = Placeholder("girl")
image michelle = Placeholder("girl")
image moss = Placeholder("boy")

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
define audio.loss = "audio/music/Loss.mp3"
define audio.norther_passage = "audio/music/Northern-Passage.mp3"
define audio.post_op = "audio/music/Post-Op_Looping.mp3"

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
style clipboard_hover:
    font "gui/fonts/CasualCursive-Regular.ttf"
    idle_color "#000000"
    hover_color "#006eb8"
    text_align 0.5
    size 45

style clipboard_idle:
    font "gui/fonts/CasualCursive-Regular.ttf"
    color "#000000"
    text_align 0.5
    size 45

style intro:
    font "gui/fonts/Abbasy Calligraphy Typeface.ttf"
    color "#65c8ff"
    text_align 0.5
    size 100
    outlines [(1.0, "#ffffff", 0.0, 0.0)]

style roomnumber:
    color "#0006ff"
    italic True


## Transforms #################################################################################################################
transform title:
    zoom 0.75
    xalign 0.95 yalign 0.05

transform middle:
    xalign 0.5 yalign 0.5

transform right:
    xalign 0.9 yalign 0.5

transform left:
    xalign 0.1 yalign 0.5

transform clipboard(delay):
    zoom 0.5
    alpha 0.0 ypos 150
    pause delay
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.5 ypos 0

transform clipboard_text(delay):
    alpha 0.0 ypos 150
    pause delay
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.5 ypos 0

transform black_background:
    alpha 0.0
    ease 0.5 alpha 0.75
    on hide:
        ease 0.5 alpha 0.0

transform confirm_clipboard:
    offscreenleft
    ease 0.5 xalign 0.25
    on hide:
        ease 0.5 offscreenleft

transform confirm_button:
    alpha 0.0
    xalign 0.8 yalign 0.5
    pause 0.5
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

transform confirm_text:
    zoom 2
    offscreenleft
    ease 0.5 xalign 0.285
    on hide:
        ease 0.5 offscreenleft


## Transitions ################################################################################################################
init -999:
    define elevator_close = ImageDissolve("elevator.png", 1.0)
    define elevator_open = ImageDissolve("elevator.png", 1.0, reverse=True)
    define fadepause = Fade(1.0, 1.0, 1.0)
    define iris = ImageDissolve("iris.png", 0.75)
    define longdissolve = Dissolve(3.0)


## Variables ##################################################################################################################

# Config
define config.mouse = {"default": [("gui/mouse.png", 0, 0)]}

# Standard
default aName = "Newbie"
default currentName = ""
default firstStory = True
default stories = {"charles": False, "michelle": False, "gladys": False, "colin": False, "samantha": False}
default storyLabels = ["story1", "story2", "story3", "story4", "story5"]
default storyNo = 0
default surnames = ["Robinson", "Sanders", "Swan", "Green", "Crenshaw"]


## Screens ####################################################################################################################
screen clipboard_names():
    default delay = 0.0
    default fullName = ""
    hbox:
        spacing 128
        xalign 0.5 ypos 583
        $listPos = 0
        for x in stories:
            if stories[x] == False:
                $fullName = x.capitalize() + " " + surnames[listPos]
                frame:
                    background None
                    xysize(250, 200)
                    vbox at clipboard_text(delay):
                        xalign 0.5 yalign 0.0
                        spacing 10
                        text "Name:" style "clipboard_idle" xalign 0.5
                        textbutton "[fullName]" text_style "clipboard_hover" xalign 0.5 action [Play(channel="sound", file="audio/se/paper_1.ogg"), Show("confirm_story", story=x, fullname=fullName)]
                #$delay += 0.2
                $listPos += 1

screen clipboard_photos():
    default delay = 0.0
    hbox:
        spacing 20
        xalign 0.5 yalign 0.5
        for x in stories:
            if stories[x] == False:
                add "[x] photo.png" at clipboard(delay)
                #$delay += 0.2

screen clipboards():
    modal True
    default delay = 0.0
    hbox:
        spacing 20
        xalign 0.5 yalign 0.5
        for x in stories:
            if stories[x] == False:
                add "clipboard.png" at clipboard(delay)
                #$delay += 0.2

screen story_select():
    modal True
    default delay = 0.0
    use clipboards
    use clipboard_photos
    use clipboard_names

screen confirm_photos(photo):
    add "%s photo.png" % photo at confirm_clipboard

screen confirm_names(name, fullname):
    frame at confirm_text:
        background None
        xysize(250, 200)
        xalign 0.5
        vbox:
            xalign 0.5 ypos -30
            spacing 10
            text "Name:" style "clipboard_idle" xalign 0.5
            text fullname style "clipboard_idle" xalign 0.5

screen confirm_story(story, fullname):
    modal True
    add "bg black" at black_background
    add "clipboard.png" at confirm_clipboard
    use confirm_photos(story)
    use confirm_names(story, fullname)
    frame at confirm_button:
        padding(20, 10)
        vbox:
            xalign 0.5 yalign 0.5
            text "Visit %s?" % story.capitalize() xalign 0.5
            textbutton "Yes" xalign 0.5 action [Play(channel="sound", file="audio/se/paper_2.ogg"), Hide("confirm_story"), Jump(story)]
            textbutton "No" xalign 0.5 action [Play(channel="sound", file="audio/se/paper_2.ogg"), Hide("confirm_story")]

# Splash ######################################################################################################################
label splashscreen:
    $persistent.splash = True
    stop music
    scene bg black
    pause 0.5
    show goodtales at middle with Dissolve(2)
    pause 1
    return

label before_main_menu:
    scene bg black
    if persistent.splash:
        show goodtales:
            middle
            ease 0.75 alpha 0.0
    show bg lobby with iris
    pause 0.25
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
    $persistent.splash = False
    return


## Story ######################################################################################################################
label start:
    window hide
    stop music fadeout 3.0
    scene black
    with longdissolve
    pause 2
    window show
    "{i}{size=+10}Let there be light!{/size}{/i}"
    window hide
    play music autumn_leaves
    play sound light_switch
    scene bg desk with Dissolve(0.1)
    pause 3
    window show dissolve
    w "Must you always do that when you hit the lights?"
    show gabe casual grin at middle with dissolve
    pause 0.1
    g "Why not?{w=0.35}\nI gotta make things interesting around here!"
    w "It's the Visiting Day, Gabe; things are going to be interesting by default."
    g level blank "And somehow they're less interesting when your downer mouth starts going off."
    w "Hmph."
    w "Say, why is that chair on the other side of you empty?"
    g raised "Huh.{w=0.5} Good question.{w=0.5}\nI heard it's for someone working the Visiting Day for the first time."
    w "Well, it's gonna be their {b}last{/b} time if they don't--"
    $renpy.music.set_pause(True, "music")
    window hide
    play sound door
    pause 1
    play sound2 running
    show gabe casual:
        ease 0.5 left
    show ariel sad scream:
        offscreenright
        ease 0.5 right
    a "{cps=*1.5}I'm here!!\nI'm sorry I'm late!!{/cps}"
    show ariel:
        linear 0.075 xalign 0.91
        block:
            linear 0.15 xalign 0.89
            linear 0.15 xalign 0.91
            repeat
    a "{cps=*1.5}I missed the bus that was supposed to take me here, so I had to decide if it was worth waiting for the next one or finding some other mode of transportation...{/cps}"
    a "{cps=*1.5}...but by the time I settled on the latter, the next bus had arrived, but then I missed that, too, and--{/cps}!"
    g raised grin "Whoa, whoa!{w=0.35} Settle down, partner!"
    g "You're here now, and there's still time before the day begins.{w=0.5}\nNo need to panic."
    show ariel grin:
        linear 0.075 right
    a "A-Ah, right.{w=0.35} Of course."
    $renpy.music.set_pause(False, "music")
    a casual "I'm Ariel, by the way. Pleased to meet you."
    g level "Name's Gabe. The feeling is mutual."
    $aName = "Ariel"
    g "So, word on the street is that this is your first time working the big Day."
    a sad frown "Well, the word would be correct.{w=0.5}\nTo be honest, I'm quite nervous."
    g casual "Ah, there's no need to be nervous, Ariel."
    g "Trust me, I've been working at the desk for a little over a thousand years now, and I promise that it's as simple as it gets."
    g "They did tell you what the job entails, right?"
    a casual grin "Yes, of course."
    a "When the human approaches, you ask them for the name, date of birth, and date of death of the person they wish to visit, as well as their relation to them."
    a "From there, you search for the file of the Visited, find their room number, and give it to the Visitors."
    g raised "Well, well. I'm glad management is still properly training the newbies.{w=0.5}\nI'd say you have nothing to worry about."
    a sad frown "You say that, but I still can't help but feel nervous about how I'll react to some of these humans."
    a "I know 10 years is nothing for us, but for them, it's one eighth of their life!{w=0.5}\nA tenth, if they're lucky!"
    a "So the emotions they must be feeling about waiting that long {i}at most{/i} to see someone they cared about..."
    g level blank "Oh, I assure you that the tissue boxes on the desks aren't for taking care of a stuffy nose."
    g grin "But it's all a part of the job.{w=0.5}\nIf it reassures you, they're tears of happiness, not sorrow."
    a "I suppose that's true..."
    g "Just sit back and relax, Ariel.{w=0.35} You'll do fine, I promise."
    window hide dissolve
    play sound intercom
    stop music fadeout 3
    pause 1
    hide ariel
    hide gabe
    with dissolve
    pause 2
    window show dissolve
    b "Attention, Beyond Suites employees!{w=0.35}\nThe 2020 Visiting Day is about to begin momentarily!"
    b "If you are not at your station, please head there now so that we may begin without any issues."
    b "It's estimated that this will be a record-breaking attendance this year, so please perform at your absolute best as to assure all may see their Visited!"
    b "Thank you, and be sure to put on a smile!"
    pause 0.5
    show gabe level grin at left
    show ariel casual frown at right
    with dissolve
    pause 0.1
    g "Alright, Ariel.{w=0.35} Time to get to work!"
    g "Still nervous?"
    a sad "Yes.{w=0.5} Very much so."
    g casual "I'm telling you, you'll be fine."
    g level "Although you {i}may{/i} wanna brace yourself for the stampede."
    a casual "The what?"
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
    show gabe casual blank at left
    show ariel sad scream at right
    with dissolve
    pause 0.1
    window show dissolve
    a "O-Oh my!"
    g "The Boss wasn't kidding; that crowd seems larger than ever before!"
    g raised grin "I guess that's all the more reason to keep your nerves calm and head focused.{w=0.5}\nCan you do that, Ariel?"
    a grin "I don't believe so, but I'll certainly do my best!"
    g level "That'll have to do."
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
    show screen story_select
    pause
    return

label storybegin:
    stop music fadeout 5
    scene bg black
    hide screen story_select
    with longdissolve
    pause 4
    $aName = "Worker"
    return

label workerhelp:
    a "Follow the signs around the lobby; they'll lead you in the direction you need to go."
    a "Or you may receive help from the workers spread along the floor."
    $firstStory = False
    return

label elevator_ride:
    window hide dissolve
    pause 0.5
    stop music fadeout 3
    stop ambience1 fadeout 3
    play sound elevator
    scene bg black with elevator_close
    pause 1
    scene bg hallway with elevator_open
    pause 0.5
    window show dissolve
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