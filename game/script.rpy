# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# SORRY THIS IS SO DISORGANIZED PLEASE ORGANIZE AND MOVE THINGS AROUND HOWEVER YOU WANT!!
# i will probably separate these into different script files so that its easier to read
define p = Character("Placeholder")
define m = Character("Mika")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bathroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show charactertest at right

    # These display lines of dialogue.

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

    #first point and click screen
    call screen toothbrush_changer

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

    scene wake

    show charactertest at right

    p "here we are at the wake"
    p "look around before we move on"

    hide charactertest
    call screen wake_scene


#for the soap choice
label um_no:

    m "why would i want to brush my teeth with SOAP"
    m "freak"
    m "ok ill make u try again"

    #makes player restart point and click
    jump restart_choice

screen emotion_changer():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "orangesadface.png"
        hover "redsadface.png"
        action Jump("continue_on")

screen toothbrush_changer():
    imagebutton: #for toothbrush
    # using int for more precise placement
        xpos int(610) # reminder for mika higher value = move right/lower value = move left
        ypos int(593) # reminder for mika that higher value = lower placement/lower value = higher placement
        idle "toothbrush_idle.png"
        hover "toothbrush_hover.png"
        action Jump("continue_on")

    imagebutton: #for soap
        xpos int(1105)
        ypos int(860)
        idle "soap_idle.png"
        hover "soap_hover.png"
        action Jump("um_no")

# wake scene interactables ##################################################

screen wake_scene():
    imagebutton: #for casket
        xpos int(800)
        ypos int(178)
        idle "casket_idle"
        hover "casket_hover"
        action Jump("clicked_button")

    imagebutton: #for flowers
        #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
        xpos(75) # reminder for mika higher value = move right/lower value = move left
        ypos(2) # reminder for mika that higher value = lower placement/lower value = higher placement
        idle "flowers_idle"
        hover "flowers_hover"
        action Jump("clicked_button")

    imagebutton: #forchairs
        xpos int(487)
        ypos int(455)
        idle "chair_idle"
        hover "chair_hover"
        action Jump("clicked_button")

label clicked_button:
    m "ok what else do u wanna press"

    call screen wake_scene

