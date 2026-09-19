# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Placeholder")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgtest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show charactertest at right

    # These display lines of dialogue.

    p "Hi guys its me ur programmer for filitober 2026."

    p "this is a prototype for all the main mechanics of the game."

    p "mainly saying stuff for me but if someone else gets the file prototypes hi :)"
    
    p "check out this face that's gonna pop up behind me"

    hide charactertest

    call screen emotion_changer

    
label continue_on:
    
    show charactertest at right
    p "omg did u see that hover absolutely steller work."

    #am thinking of just making every interactable object an image button
    #that way every interactable thing can have a cool hover
    #or not lmfao either way i can pull up

    p "once i get dialogue and a scenes list ill do stuff ill do all the stuff"

    #p "adding this in as a check for changes?"

    p "ok bye :D"
    return


screen emotion_changer():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "orangesadface.png"
        hover "redsadface.png"
        action Jump("continue_on")


