#p for player soz 
#any .rpy files ive mentioned are under the game folder
define p = Character("Mc")
define m = Character("Mother")
define c = Character("Cousin")

label start:

    # sorry i lowk couldnt figure out how else to make sure the player interacted with everything before moving on
    $ casket_click = False
    $ flowers_click = False
    $ chairs_click = False

    scene wake 

    "In a room full of white flowers, decorations, and plastic chairs, a white casket sits in the middle."
    "The world seems solemn and still, as if time had just stopped ticking."
    "The silence is broken as the wake begins and relatives start to trickle in. Most enter silently, some whispering, and a few talking loudly, as if they were simply meeting up."

    # wake_scene is controlled by wakescript.rpy
    call screen wake_scene_start

#label after player interacts with all wake objects, continuation of main script
label end_wake_scene:

    scene wake

    m "you are back in the main script"

    show charactertest at right #show mc sad/tired

    "A single woman stands silently in front of the casket, a weary expression on her face."

    p "..."
    p "This isn't fair."
    p "She might still be out there and I’m stuck setting up someone else\s wake."
    p "I need to find her"

    # show mc sad/tired, show mother neutra/serious
    
    m "What are you doing standing around? Go greet your relatives. Don\t forget to bless them."

    p "Ugh."

    m "Don't be rude."

    p "I don’t feel well. I’m going home."

    # show mc sad/tied, show mother angry

    m "Ungrateful child. No respect for your elders. Your father would be disappointed."

    # show mc angry, show mother angry

    p "Don\t talk about him just to put me down. It\s not my fault yo-"

    m "Enough"
    m "Fine. You want to go home? Go home and clean your room."
    m "I'm tired of seeing your mess."

    # show mc angry
    
    p "...Whatever."
    p "She always has something to nag about."
    p "I should have ran when I had the chance."


    # show fade

    jump porch_scene


    # PORCH SCENE HERE

label porch_scene:

    scene porch

    p "I need to keep looking for her..."

    "*CRASH*"

    p "What was that???"

    #replace mc name here
    "Suddenly, the door is swung open. Standing there with trays in her arms is a girl who looks a few years younger than MC." 

    # show mc sad/tired, show cousin confused

    c "Oh! What are you doing here?"

    p "I don\t feel well."

    c "I\m sorry...Did you get any medicine?"

    # italicize here
    p "Right. I forgot to stop somewhere...It\s too late now."

    "MC pauses for a moment to think."

    p "Yeah."
    p "Why are you still here?"

    #replace cousin name here
    "Cousin notices her hesitation but decides to ignore it."

    # show mc sad/tired, show cousin neutral
    
    c "I had to come back for some stuff."

    p "Do you need help?"

    c "No it\s okay. Get some rest."

    p "Okay...See you later."

    c "Be careful okay?"

    p "...I will"

    # show mc sad/tired

    p "Did she see through me?"
    p "I don\t even care anymore."

