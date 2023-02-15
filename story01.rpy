###############################
## Story 1: Charles Robinson ##
###############################

label story1:
    call storybegin
    window show
    ly "C'mon, Lucas! Can't you hurry it up??"
    ls "I can.{w=0.5}\nDoesn't mean I want to."
    play music delivering_the_goods
    play ambience1 crowd_talking
    scene bg lobby
    show lucy at middle
    with dissolve
    ly "Ugh!"
    ly "Mom, tell Lucas to hurry up!"
    "Resorting to getting help from Mother Dearest.{w=0.5}\nTypical."
    show lucy at right with easeinleft
    pause 0.1
    show anne at left with dissolve
    pause 0.1
    an "Come on, Lucas.{w=0.35} It's a big crowd in here, and I'd hate for you to get lost in it."
    ls "Fine, whatever you say, Mom."
    "It's not like I get much of a choice in anything I do, anyway."
    ly "So, how much longer until we'll be at the front of the line, Mom?"
    an "I'm not sure, Lucy.{w=0.5}\nThe workers seem to be moving fast, but we could still be dealing\nwith an hour or so of wait."
    ly "UGH!"
    an "Hey, we've waited 10 years to see your father; we can wait another couple hours."
    ly "I guess..."
    "If it were up to me, we wouldn't even be here right now."
    "But hey, whatever Lucy and Mom want, I have to want, too."
    window hide dissolve
    pause 0.5
    scene bg desk with fadepause
    window show dissolve
    w "Next!"
    show lucy at middle with dissolve
    ly "Finally!"
    "An hour and fifteen minutes.{w=0.5}\nNot bad, all things considered."
    $a_name = "Worker"
    hide lucy with dissolve
    pause 0.5
    show ariel casual grin at middle with dissolve
    pause 0.1
    a "Hello!{w=0.35} Welcome to the Beyond Suites!"
    a "What is the name of the person you're visiting today?"
    show ariel at right with easeinleft
    show anne at left with dissolve
    pause 0.1
    an "Charles Robinson."
    "The worker typed into the computer in front of her, silently mouthing my father's name."
    a "Date of birth?"
    an "November 25th, 1966."
    "More typing."
    a "Date of death?"
    an "August 3rd, 2010."
    a sad frown "Oh, my.{w=0.5}\nYou've been waiting quite a while then, huh?"
    an "Haha.{w=0.35} Yes, about as long as one could."
    a grin "And your relation to the Visited?"
    hide anne
    show lucy at left
    with dissolve
    pause 0.1
    ly "We're his family!"
    ls "Pretty sure Mom was going to say that, Lucy."
    ly "Well, maybe I wanted to say it!"
    hide ariel
    show anne at right
    with dissolve
    pause 0.1
    an "Both of you, please knock it off!"
    ly "But he--!"
    an "I don't care who started it!{w=0.5}\nKnock it off!"
    "Lucy crossed her arms in a pout and looked away."
    show lucy:
        ease 0.5 alpha 0.0
    show anne at left with easeinright
    hide lucy
    show ariel casual grin at right with dissolve
    an "I'm sorry about that."
    a sad "Oh, it's quite alright, Ma'am.{w=0.35}\nThis is a day full of emotions, after all."
    a casual "Anyway, the room number you're looking for is {=roomnumber}418211411{/}."
    "She handed Mom a card with the number on it."
    if first_story:
        call workerhelp
    a "Enjoy your visit!"
    an "Thank you, Miss."
    an "Alright, kids. Let's go."
    scene bg desk with dissolve
    pause 0.1
    "We stepped out of the line and towards the elevators along the outer wall."
    call elevator_ride
    show anne at middle with dissolve
    pause 0.1
    an "Alright, the room should be somewhere around here..."
    an "407...{w=1}\n409...{w=1}\nAh!{w=0.5} 411!"
    hide anne with dissolve
    pause 0.1
    "There it was."
    "Behind that door was my father, Charles Robinson."
    "Feels a bit surreal to think about, to be honest."
    show lucy at middle with dissolve
    play sound knock
    ly "Dad?{w=0.5}\nAre you in there?"
    "There were a few seconds of silence before we heard movement from inside."
    "And then..."
    play sound door
    hide lucy with dissolve
    pause 1
    show charles at middle with longdissolve
    pause 0.5
    play music high_altitude_bliss
    c "Lucy?"
    show charles at left with easeinright
    show lucy at right with dissolve
    ly "Dad!!"
    "She ran forward and hugged him tightly."
    ly "It's so nice to see you again!!"
    "A grin grew on his face as he wrapped his arms around her to return the hug."
    c "Yes, it is, sweetheart."
    "He then looked and saw that other people were here, as well."
    c "Anne!"
    hide lucy
    show anne at right
    with dissolve
    pause 0.1
    an "Hello, Charles."
    "He broke from the hug with Lucy and approached Mom."
    "I could see tears forming in both of their eyes."
    an "Oh, Charles..."
    an "It's so wonderful to hear your voice again."
    c "And it's wonderful to hear yours, Anne."
    hide charles
    hide anne
    with dissolve
    pause 0.1
    "The two then leaned in and gave each other a kiss."
    "I used all my willpower to not roll my eyes."
    "As much as I'm disgusted by the fact Mom would consider kissing him, I suppose he still is her former husband, after all."
    "Though why she insisted on staying committed despite that whole \"'Til death do us part\" thing, I'll never understand."
    c "And Lucas!"
    show charles at middle with dissolve
    pause 0.1
    "Ah.{w=0.35}\nHe finally noticed me."
    c "Wow..."
    c "Look at you.{w=0.5}\nYou're a grown man now."
    ls "..."
    c "..."
    c "Anyway, would you all like to come in?"
    show charles at right with easeinleft
    show lucy at left with dissolve
    pause 0.1
    ly "Sure!"
    hide lucy
    show anne at left
    with dissolve
    pause 0.1
    an "I would love to."
    ls "..."
    window hide dissolve
    stop music fadeout 3
    scene bg hallway with dissolve
    pause 0.5
    scene bg room with dissolve
    pause 0.5
    play music delivering_the_goods
    show lucy at middle with dissolve
    pause 0.1
    window show dissolve
    ly "Wow!{w=0.5}\nThis is a pretty nice room, Dad!"
    show lucy at left with easeinright
    show charles at right with dissolve
    pause 0.1
    c "Yes, I was quite impressed, myself!"
    c "I only get it for a day, but it's definitely accommodating!"
    hide lucy
    show anne at left
    with dissolve
    pause 0.1
    an "I can certainly see why this place is called the Beyond {i}Suites{/i}!"
    "Do the dead even need accommodations like this?"
    "I mean, it's better than a casket, but can they even, say, eat any of the fruit in the bowls here?"
    "I suppose I could try asking."
    hide anne
    show lucy at left
    with dissolve
    pause 0.1
    ly "Hey, Dad?"
    c "Yes?"
    ly "Where do you go when you're not here?"
    "And the subject is changed by the perfect little princess."
    c "You mean when it's not the Visiting Day?"
    ly "Yeah!{w=0.35}\nLike, is it anything like this?"
    c "Ahaha...{w=0.5}\nI'm afraid I can't answer that."
    ly "Huh?"
    c "That was the one rule about the Visiting Day:{w=0.5} {i}No talking about the Other Side.{/i}"
    c "They say it's to keep it a surprise for the living."
    ly "Oh, come on!{w=0.5} Can't you give a teensy-weensy hint?"
    c "Sorry, Lucy; I don't wanna push my luck and break the sole rule on my first Visiting Day."
    ly "Ugh."
    c "Besides, I'd rather use this time to catch up with you!"
    c "Look at you. You've graduated from a cute little toddler to a cute little teenager."
    c "You're 14 now, so you're in, what, 8th grade?"
    ly "I just graduated 8th grade!{w=0.5}\nThis fall, I'll be starting high school!"
    c "High school??"
    c "Heh. Someone needs to create a way to stop you from growing, young lady!"
    ly "Ahahaha!"
    c "So, if you're just now starting high school..."
    c "...then that means you're about to graduate high school soon, right Lucas?"
    ls "..."
    ls "...yeah.{w=0.5}\nI'll be a senior this fall."
    c "Man...{w=0.5}\nI really have missed both of your entire childhoods, haven't I...?"
    ls "That's accurate.{w=0.5}\nEven though you were alive for most of mine, you weren't really there."
    $renpy.music.set_pause(True)
    "Everyone in the room went silent."
    "In my defense, I wasn't wrong."
    "Dad then let out a sigh."
    c "No, I suppose I wasn't."
    hide lucy
    show anne at left
    with dissolve
    pause 0.1
    "I could see Mom giving me a death glare."
    "I suppose that's what she gets for dragging me along against my will to see a man I didn't want to ever see again."
    an "A-Anyway, Charles, it's been quite an interesting life without you there."
    $renpy.music.set_pause(False)
    c "Interesting?{w=0.5}\nIn what way?"
    a "Well, being a single mother is never easy in any circumstance..."
    c "You never remarried?"
    an "Why would I?{w=0.35}\nI never fell out of love with you."
    "A big mistake on your part."
    c "Anne..."
    "He grabbed her hand with a smile."
    c "I thought for sure that what happened to me would be the best thing in your life."
    an "No, Charles.{w=0.5}\nBeing with you was."
    an "Yes, we had our issues, but I made vows, and darn it, I stuck with them."
    stop music fadeout 3
    "His eyes started to water again."
    c "You..."
    "He took a deep breath."
    play music high_altitude_bliss
    c "...you have no idea how much that means to me."
    c "I wasn't a perfect husband or father."
    "Understatement of the century."
    c "So to hear you say that..."
    "He wiped his eye."
    c "Thank you, Anne."
    "He then kissed her again."
    "My urge to vomit was increasing."
    c "You know, I must admit that I was surprised that you guys showed up."
