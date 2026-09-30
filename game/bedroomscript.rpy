# this is the wake scene interactable stuff
define p = Character("Placeholder")
define m = Character("Mika")

label bedroom_interact:

    screen bedroom_scene():

        imagebutton: #for lamp
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(185) # reminder for mika higher value = move right/lower value = move left
            ypos(2) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "nightstand_idle"
            hover "nightstand_hover"
            action Jump("bedroom_nightstand")

        imagebutton: #for mirror
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(30) # reminder for mika higher value = move right/lower value = move left
            ypos(85) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "nightstand_idle"
            hover "mirror_hover"
            action Jump("bedroom_mirror")

        imagebutton: #for bed
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(400) # reminder for mika higher value = move right/lower value = move left
            ypos(150) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "bed_idle"
            hover "bed_hover"
            action Jump("bedroom_bed")

        #Jump("clicked_button")]

    screen bedroom_screenwindow():
        
        imagebutton: #for window
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(1500) # reminder for mika higher value = move right/lower value = move left
            ypos(50) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "window_idle"
            hover "window_hover"
            action Jump("bedroom_windowclicked")
