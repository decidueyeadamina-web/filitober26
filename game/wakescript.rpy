# this is the wake scene interactable stuff
define p = Character("Placeholder")
define m = Character("Mika")

label wake_interact:

    screen wake_scene():

        imagebutton: #for casket
            xpos int(800)
            ypos int(178)
            idle "casket_idle"
            hover "casket_hover"
            action Jump("wake_continue")

        imagebutton: #for flowers
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(75) # reminder for mika higher value = move right/lower value = move left
            ypos(2) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "flowers_idle"
            hover "flowers_hover"
            action Jump("wake_continue")

        imagebutton: #forchairs
            xpos int(487)
            ypos int(455)
            idle "chair_idle"
            hover "chair_hover"
            action Jump("wake_continue")

        #Jump("clicked_button")]


