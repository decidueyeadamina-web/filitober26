# SORRY THIS IS SO DISORGANIZED PLEASE ORGANIZE AND MOVE THINGS AROUND HOWEVER YOU WANT!!
# i will probably separate these into different script files so that its easier to read
define p = Character("Placeholder")
define m = Character("Mika")

#ok actual characters here
define ma = Character("Marisol")
define ma_i = Character(None, italics =True)
define mai = Character(None, italics =True)
define mom = Character("Mother")
define t = Character("Tin-Tin")

#may move to another script my life with c# is fucked everything is harder when calling a script from another script 
#all this to say im used to just keeping all variables ever on the same script...
#will organize this later...perchance...

#basically every point and click is going to have a value 0 is false and 1+ is true, and if all point and clicks are done they'll all be set to 1+
#meaning we can drop an if then statement to immediately call the next scene >:) easy check fuck yes

#Wake Check Variables
default wakeFlowers = 0
default wakeCasket = 0
default wakeChairs = 0

#Bedroom Check Variables
default bedroomNightstand = 0
default bedroomBed = 0
default bedroomMirror = 0

label start:

## BATHROOM SCENE

    #scene bathroom

    #show charactertest at right

    #p "Hi guys its me ur programmer for filitober 2026."

    #p "this is a prototype for all the main mechanics of the game."

    #p "mainly saying stuff for me but if someone else gets the file prototypes hi :)"

    #hide charactertest
    
    #p "check out this face that's gonna pop up behind me"

    #m "sorry it isnt a face anymore i made it toofbrush"

    #menu brush_teef:
    #    "wow mika thats awful"

    #    "you suck so bad":
    #        p "i cant believe you mika"

    #    "js a toofbrush no biggie":
    #        p "wow ur on his side?"

    #abel after_menu:
    #    "ok whatever move on to the next thing"

    # restart_choice for if player picks soap...freaks...
    #label restart_choice:
    #p "ok do u want to brush ur teeth yet go click the toothbrush (not the soap)"

    ## first point and click interaction
    #call screen toothbrush_changer

##for the soap choice
#label um_no:

    #m "why would i want to brush my teeth with SOAP"
    #m "freak"
    #m "ok ill make u try again"

    #makes player restart point and click
    #jump restart_choice

    #continuation of script
#label continue_on:
    
    #show charactertest at right
    #p "omg did u see that hover absolutely steller work."

    #am thinking of just making every interactable object an image button
    #that way every interactable thing can have a cool hover
    #or not lmfao either way i can pull up

    #ok i pull up hop out at the after partyyy
    #ya idgaf what u do lol u do u king

    #p "once i get dialogue and a scenes list ill do stuff ill do all the stuff"

    #p "adding this in as a check for changes?"

    #p "ok time to change scenes"

# dude you thought u were disorganized let me show u how insane it can get (AD)...
# literally breaking into ur files is insanely eye opening the first time i coded with renpy every single variable/ref was on the script.rpy document :')
# keeping everything above the line here that's old scenes so our new scenes start on kaleas actual document 
## WAKE SCENE

    scene wake
    with fade

    "In a room full of white flowers, decorations, and plastic chairs, a white casket sits in the middle.The world seems solemn and still, as if time had just stopped ticking." 
    queue sound "distorted_background_people_talking-spooktober_2026.ogg" loop fadein 1.0
    
    "The silence is broken as the wake begins and relatives start to trickle in. Most enter silently, some whispering, and a few talking loudly, as if they were simply meeting up."

    #starts the wake bg point and click
    call screen wake_scene

    #clicking flowers
    label wake_flowers:
        "Chrysanthemums, flowers of the dead. They always smell earthy and herbal, kind of like medicine."
        #adding 1 to show that it has been checked
        $ wakeFlowers += 1;
        #"[wakeFlowers] variable amount"

        #this is a check to see if all the things have been clicked!
        if (wakeFlowers >= 1 and wakeChairs >= 1 and wakeCasket >= 1):
            jump wake_continue1
        else:
            call screen wake_scene

    #clicking chairs
    label wake_chairs:
        "The men are playing Tong-its, the women are gossiping about useless rumors that are none of their business. Everyone is so loud."
        $ wakeChairs += 1;
        #"[wakeChairs] variable amount"
        
        if (wakeFlowers >= 1 and wakeChairs >= 1 and wakeCasket >= 1):
            jump wake_continue1
        else:
            call screen wake_scene

    #clicking casket
    label wake_casket:
        "Who’s gonna help his wife with the kids? Poor woman. He should have been more careful with his health."
        $ wakeCasket += 1;
        #"[wakeCasket] variable amount"
        
        if (wakeFlowers >= 1 and wakeChairs >= 1 and wakeCasket >= 1):
            jump wake_continue1
        else:
            call screen wake_scene
    


label wake_continue1:

    show marisol_tired
    with dissolve
    
    "A single woman stands silently in front of the casket, a weary expression on her face."    
    ma "..."

    ma_i "This isn’t fair."

    ma_i "She might still be out there and I’m stuck setting up someone else’s wake."

    ma_i "I need to find her."

    hide marisol_tired
    show marisol_tired at right
    show mother_serious at left

    mom "What are you doing standing around? Go greet your relatives. Don’t forget to bless them."
    
    ma "Ugh"

    mom "Don't be rude."

    ma "I don't feel well. I'm going home."

    hide mother_serious
    show mother_angry at left

    mom "Ungrateful child. No respect for your elders. Your father would be disappointed."

    hide marisol_tired
    show marisol_angry at right

    ma "Don’t talk about him just to put me down. It’s not my fault yo-"

    mom "Enough."

    ma "Fine. You want to go home? Go home and clean your room."

    ma "I’m tired of seeing your mess."

    hide mother_angry

    ma "...Whatever."

    ma "She always has something to nag about."

    ma "I should have ran when I had the chance."

    hide marisol_angry

label porchscene:
    
    scene porch
    with fade

    show marisol_tired

    queue sound "walking-spooktober_2026.ogg" fadein 0.5

    ma_i "I need to keep looking for her..."

    "CRASH"
    queue sound "crash-spooktober_2026.ogg"

    ma_i "What was that???"

    queue sound "door_open-spooktober_2026.ogg"

    "Suddenly, the door is swung open. Standing there with trays in her arms is a girl who looks a few years younger than her."

    hide marisol_tired
    show marisol_tired at right
    show tintin_confused at left

    t "Oh! Mari! What are you doing here?"

    ma_i "Oh, it's just Tin-Tin..."

    ma "I don't feel well."

    t "Did you get any medicine?"

    ma_i "Right. I forgot to stop somewhere...It’s too late now."

    ma "..."

    ma "Yeah."

    ma "Why are you still here?"

    hide tintin_confused
    show tintin_neutral at left

    "Tin-tin notices her hesitation but decides to ignore it."

    t "I had to come back for some stuff."

    ma "Do you need help?"

    t "No it’s okay. Get some rest."

    ma "Okay...See you later."

    t "Be careful okay?"

    ma "...I will. You too."

    hide tintin_neutral

    ma_i "Did she see through me?"

    ma_i "I don’t even care anymore."

    jump bedroomscene

label bedroomscene:
    
    scene bedroom
    with fade

    queue sound "crickets-spooktober_2026.ogg"

    ma_i "I guess it is kind of messy in here."
    
    call screen bedroom_scene

label bedroom_nightstand:
    ma_i "On my nightstand lays the books we read together. I never really cared much for reading until I met her. It’s crazy how much I’ve changed."
    $ bedroomNightstand += 1;
    
    if (bedroomNightstand >= 1 and bedroomBed >= 1 and bedroomMirror >= 1):
            jump bedroomscene_continue1
    else:
            call screen bedroom_scene

label bedroom_bed:
    ma_i "I’m so tired...I feel like I’m the only one looking for her. The only who still cares. Why does no one else care?"
    $ bedroomBed += 1;
    
    if (bedroomNightstand >= 1 and bedroomBed >= 1 and bedroomMirror >= 1):
            jump bedroomscene_continue1
    else:
            call screen bedroom_scene


label bedroom_mirror:
    ma_i "I don’t even want to look at myself right now. I know I look awful and messy. At least that’s what mother has been telling me."
    $ bedroomMirror += 1;
    
    if (bedroomNightstand >= 1 and bedroomBed >= 1 and bedroomMirror >= 1):
            jump bedroomscene_continue1
    else:
            call screen bedroom_scene

label bedroomscene_continue1:
    
    call screen bedroom_screenwindow

    label bedroom_windowclicked:

        queue sound "Van_start-spooktober_2026.ogg"

        ma_i "What was that van doing outside of my house?"

        ma_i " Now that I think about it...I’ve been seeing that van around often."

        ma_i "I better keep an eye out. I know other people have been going missing as well."

        ma_i "..."
        
        ma_i "I guess I should clean my room before mother gets home and yells at me again."

        ma_i "Should I..."

        menu branchingEnding:
            "Organize my nightstand?":
                jump shelf_route

            "Put my clothes away":
                jump clothes_route
                
    label shelf_route:
        
        ma_i "I should get rid of some of these books. It does feel a bit too cluttered."

        "Marisol picks up a book and looks at it for a while with a look of contemplation."

        "She then opens it, flipping to her favorite part of the story."

        mai "I didn’t know she annotated it for me..."

        "She flips the page and a letter falls out, floating like a feather to the ground."

        "Tears begin to fall from her eyes as she picks the familiar letter up off of the ground."

        mai "I remember every single word in this letter. It’s the last one she ever wrote to me."

        "Marisol opens the letter, scanning the familiar words on the delicate white paper."

        mai  "I can almost hear her reading it out to me."

        "She folds the letter back up, carefully following the creases, and gently places it back into the book, just as she had found it."

        mai "I don’t deserve the warmth and comfort of her sweet words. Not after I failed her."

        mai "I can’t believe she’s gone. It’s all my fault. If I wasn’t so unsure of myself I could have been there with her."
        
        mai "Or if I just kept everything to myself we wouldn’t even be in this mess. "

        mai "We could’ve been happy here. She didn’t have to do all this for me."

        mai "It’s all my fault."

        "Marisol puts the book back onto her nightstand and falls lifelessly into her bed with a defeated sigh."

        mai "I don’t want to clean right now. I’ll probably yelled at regardless. Whatever."

        mai "I can’t stop thinking about her. I don’t even know if she’s still alive."

        mai "Everyone says she’s probably gone. I don’t want to believe it but as more time passes, the more I lose hope."

        "Marisol lays in bed, wishing that her lover was laying there next to her."

        mai "I don’t know what to do anymore. I don’t know where she could be..."

        "She drifts to sleep with tear stained cheeks. Her heart is still full of worry and guilt but her body just can’t keep up."

    label clothes_route:

        mai "I guess I can start with picking my clothes up off of the floor." 

        "Marisol starts grabbing her clothes, lazily throwing them into her arms."

        "A thick square of paper falls out and lands face down on the floor."

        "She picks the paper up and turns it around, surprised by the photograph printed on the other side."

        mai "How did this get here?"

        "A photograph of her stares back at her. Tears sting at her eyes, threatening to fall onto the paper sitting delicately in her hand."

        mai "She looks so beautiful in this picture. I miss her so much."

        mai "I need to see her again. I have to find her."

        mai "I don’t care what they say. I know she’s out there somewhere. She wouldn’t just leave me like that."

        mai "...Right?"

        mai "She wouldn’t leave me all alone right? I don’t think she would."

        mai "But what if she..."

        mai "No. I know she loves me. Why else would she plan to run away with me?"

        mai "Maybe I’ll stop by her house again tomorrow."

        mai "I know mother doesn’t want me going over there anymore but how can I not?"

        "Marisol flops down onto her bed with a thud, the photograph still in her hand and her arm stretched in front of her."

        mai "I should get some rest before tomorrow. I have to leave early so nobody sees me leave."

        mai "They haven’t let me leave the house since they last caught me sneaking out...At least not until the wake today."

        mai "Marisol falls asleep with the photograph laying on her chest as it rises and falls slowly and steadily. "

        mai "Her mind is surprisingly empty as she falls into her much needed slumber. "






#RUNNING LIST OF ALL SPRITE NAMES:
#marisol_tired
#marisol_angry
#mother_serious
#mother_angry
#tintin_confused
#tintin_neutral

#RUNNING LIST OF ALL SCENE NAMES:
#bedroom 








