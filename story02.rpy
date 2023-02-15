###############################
## Story 2: Michelle Sanders ##
###############################

label story2:
    call storybegin
    play music post_op
    play ambience1 crowd_talking
    scene bg lobby with longdissolve
    pause 0.1
    window show dissolve
    "I must admit, it's a bit weird attending the Suites under these circumstances."
    "I know I'm far from the only detective to do so, but in a way, it feels like...{w=0.5} cheating."
    "After all, part of reason I wanted this position was so I could use my brain to work out the answer logically."
    "But there's a saying about desperate times, I suppose..."
    w "Next!"
    pause 0.5
    scene bg desk with dissolve
    pause 0.5
    show ariel casual grin at middle with dissolve
    pause 0.1
    $a_name = "Worker"
    a "Hello!{w=0.35} Welcome to the Beyond Suites!"
    a "What is the name of the person you're visiting today?"
    mo "Michelle Sanders."
    "She then began typing at the computer in front of her."
    a "...Sanders..."
    a "Date of birth?"
    mo "May 31st, 1993."
    a "...ninety three..."
    a "Date of death?"
    mo "December 25th, 2016."
    show ariel sad frown
    "The worker froze for a second."
    a "A Christmas death?{w=0.5}\nHow terrible..."
    "I gave a small sigh."
    mo "Yes, it is."
    "The worker got back to typing."
    a grin "And what is your relation to the Visited?"
    mo "Well, uh...{w=0.5}\nWe're not exactly \"related\", per se."
    mo "In fact, we've never met."
    a casual frown "You haven't?"
    mo "No.{w=0.5}\nI'm the detective in charge of her murder case."
    a sad "Oh...!{w=1.0}\nI see..."
    "She was noticeably tense all of a sudden."
    "But she cleared her throat and resumed her more professional attitude."
    a grin "A-Anyway, the room number you are looking for is {=roomnumber}192012254{/}."
    "She handed me a card with the number written on it."
    if first_story:
        call workerhelp
    a casual "I hope your visit goes well."
    mo "As do I."
    hide ariel with dissolve
    pause 0.1
    "It took a bit of searching, but I was able to find the elevators I needed to get me to the right direction."
    call elevator_ride
    "I feel like I've been walking down these halls for hours."
    "I understand that the Suites are meant to accommodate trillions of guests and there are only so many ways to divide them up, but surely there must even more subsections they could add to make it easier."
    "Finally, though, I found it."
    "I took a deep breath."
    "I had practiced many times how this greeting would go, but my line of work has taught that the unexpected loves to show its head at any moment."
    play sound knock
    "I knocked on the door."
    m "Who is it?"
    "A young woman's voice replied.{w=0.5}\nShe almost sounded a bit cheerful."
    "Which is a bit weird, given the circumstances of how she ended up here."
    "But it was still a voice I recognized from videos I had listened to millions of times."
    mo "Ms. Sanders, my name is Detective Ted Moss.{w=0.5}\nMay I speak with you?"
    "..."
    "No response."
    mo "Ms. Sanders?"
    m "I..."
    m "Y-Yeah, of course."
    play sound door
    pause 1
    show michelle at middle with longdissolve
    pause 0.5
    m "Sorry about that.{w=0.35}\nPlease come in."
