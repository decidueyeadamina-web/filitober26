# SORRY THIS IS SO DISORGANIZED PLEASE ORGANIZE AND MOVE THINGS AROUND HOWEVER YOU WANT!!
# i will probably separate these into different script files so that its easier to read
define p = Character("Placeholder")
define m = Character("Mika")

label start:

## BATHROOM SCENE

    scene bathroom

    show charactertest at right

    p "Hi guys its me ur programmer for filitober 2026."

    p "this is a prototype for all the main mechanics of the game."

    p "mainly saying stuff for me but if someone else gets the file prototypes hi :)"

    hide charactertest
    
    p "check out this face that's gonna pop up behind me"

    m "sorry it isnt a face anymore i made it toofbrush"

    menu brush_teef:
        "wow mika thats awful"

        "you suck so bad":
            p "i cant believe you mika"

        "js a toofbrush no biggie":
            p "wow ur on his side?"

    label after_menu:
        "ok whatever move on to the next thing"

    # restart_choice for if player picks soap...freaks...
    label restart_choice:
    p "ok do u want to brush ur teeth yet go click the toothbrush (not the soap)"

    # first point and click interaction
    call screen toothbrush_changer

#for the soap choice
label um_no:

    m "why would i want to brush my teeth with SOAP"
    m "freak"
    m "ok ill make u try again"

    #makes player restart point and click
    jump restart_choice

    #continuation of script
label continue_on:
    
    show charactertest at right
    p "omg did u see that hover absolutely steller work."

    #am thinking of just making every interactable object an image button
    #that way every interactable thing can have a cool hover
    #or not lmfao either way i can pull up

    #ok i pull up hop out at the after partyyy
    #ya idgaf what u do lol u do u king

    p "once i get dialogue and a scenes list ill do stuff ill do all the stuff"

    #p "adding this in as a check for changes?"

    p "ok time to change scenes"

## WAKE SCENE

    scene wake

    show charactertest at right

    p "here we are at the wake"
    p "look around before we move on"

    hide charactertest

    #starts the wake bg point and click
    call screen wake_scene

label wake_continue:

    show charactertest at right
    p "ok next we need to make sure the player clicks all 3 before moving on"
