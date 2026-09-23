# this is the bathroom scene interactable stuff

define p = Character("Placeholder")
define m = Character("Mika")


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

screen emotion_changer():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "orangesadface.png"
        hover "redsadface.png"
        action Jump("continue_on")