# label wake_interact:


#code that controls point and click outlines/outcomes of each interaction
screen wake_scene_start():

    imagebutton: #for casket
        xpos int(800)
        ypos int(178)
        idle "casket_idle"
        hover "casket_hover"
        action Jump("casket_click")

    imagebutton: #for flowers
            #oh my god i didnt put int..no wonder it took so long to align. js dont touch this lol
        xpos(75) # reminder for mika higher value = move right/lower value = move left
        ypos(2) # reminder for mika that higher value = lower placement/lower value = higher placement
        idle "flowers_idle"
        hover "flowers_hover"
        action Jump("flowers_click")

    imagebutton: #forchairs
        xpos int(487)
        ypos int(455)
        idle "chair_idle"
        hover "chair_hover"
        action Jump("chairs_click")

        #Jump("clicked_button")]

#label used after clicking casket
label casket_click:
    p "He was nice I guess. I feel bad for his wife, who’s gonna help her with the kids?"
#sets variable to true
    $ casket_click = True
    call check_if_interacted

#label used after clicking flowers
label flowers_click:
    p "Chrysanthemums, flowers of the dead. They somehow always smell like chemicals."
#sets variable to true
    $ flowers_click = True
    call check_if_interacted

#label used after clicking chairs
label chairs_click:
    p "They’re playing Tong-its. I never really understood how the game works."
#sets variable to true
    $ chairs_click = True
    call check_if_interacted

#label used to click on other wake objects
label check_if_interacted:
    # checks if all conditions are true...allegedly
    if all([casket_click, flowers_click, chairs_click]):
        # changes to after wake_scene_start (back to main script)
        call end_wake_scene
    else: 
        # brings player back to point and click
        call screen wake_scene_start

# reads everything right until all variables are true
# like you can interact with objects multiple times UNTIL you interact with them all
# then it jumps from each object's dialogue and dialogue that should happen when you rejoin the main script
# idk what im doing wrong here king...delete and change whatever you need to