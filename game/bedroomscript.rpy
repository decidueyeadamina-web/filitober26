# this is the wake scene interactable stuff
define p = Character("Placeholder")
define m = Character("Mika")

label bedroom_interact:

    screen bedroom_scene():

        imagebutton: #for lamp
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(120) # reminder for mika higher value = move right/lower value = move left
            ypos(574) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "br_nightstand_idle"
            hover "br_nightstand_hover"
            action Jump("bedroom_nightstand")

        imagebutton: #for mirror
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(1430) # reminder for mika higher value = move right/lower value = move left
            ypos(80) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "br_mirror_idle"
            hover "br_mirror_hover"
            action Jump("bedroom_mirror")

        imagebutton: #for bed
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(245) # reminder for mika higher value = move right/lower value = move left
            ypos(385) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "br_bed_idle"
            hover "br_bed_hover"
            action Jump("bedroom_bed")

        #Jump("clicked_button")]

    screen bedroom_screenwindow():
        
        imagebutton: #for window
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
            xpos(592) # reminder for mika higher value = move right/lower value = move left
            ypos(60) # reminder for mika that higher value = lower placement/lower value = higher placement
            idle "br_window_idle"
            hover "br_window_hover"
            action Jump("bedroom_windowclicked")
