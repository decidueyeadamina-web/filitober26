# SORRY THIS IS SO DISORGANIZED PLEASE ORGANIZE AND MOVE THINGS AROUND HOWEVER YOU WANT!!
# i will probably separate these into different script files so that its easier to read
define p = Character("Placeholder")
define m = Character("Mika")

#ok actual characters here
define ma = Character("Marisol")
define ma_i = Character(None, italics=True)
define mai = Character(None, italics=True)
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

#Bathroom Check Variables
default bathroomToothbrush = 0
default bathroomSoap = 0

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
    #bruh my first renpy game...i cant even go back to make it better because everything is on the script.rpy too.
# keeping everything above the line here that's old scenes so our new scenes start on kaleas actual document 
## WAKE SCENE

    scene wake
    with fade

    "In a room full of white flowers, decorations, and plastic chairs, a white casket sits in the middle. The world seems solemn and still, as if time had just stopped ticking." 
    queue sound "background_people_talking-spooktober_2026.ogg" loop fadein 1.0
    
    "The silence is broken as the wake begins and relatives start to trickle in. Most enter silently, some whispering, and a few talking loudly, as if they were simply meeting up."

    #starts the wake bg point and click
    call screen wake_scene

    #clicking flowers
    label wake_flowers:
        "{i}Chrysanthemums, flowers of the dead. They always smell earthy and herbal, kind of like medicine.{/i}"
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
        "{i}The men are playing Tong-its, the women are gossiping about useless rumors that are none of their business. Everyone is so loud.{/i}"
        $ wakeChairs += 1;
        #"[wakeChairs] variable amount"
        
        if (wakeFlowers >= 1 and wakeChairs >= 1 and wakeCasket >= 1):
            jump wake_continue1
        else:
            call screen wake_scene

    #clicking casket
    label wake_casket:
        "{i}Who’s gonna help his wife with the kids? Poor woman. He should have been more careful with his health.{/i}"
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

    stop sound fadeout 5.0
    
    ma_i "{i}This isn’t fair.{/i}"

    ma_i "{i}She might still be out there and I’m stuck setting up someone else’s wake.{/i}"

    ma_i "{i}I need to find her.{/i}"

    hide marisol_tired
    show marisol_tired at right
    show mother_serious at left

    mom "What are you doing standing around? Go greet your relatives. Don’t forget to bless them."
    
    ma "Ugh."

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

    hide mother_angry with dissolve

    ma "...Whatever."

    ma "{i}She always has something to nag about.{/i}"

    ma "{i}I should have ran when I had the chance.{/i}"

    hide marisol_angry

label porchscene:
    
    scene porch
    with fade

    show marisol_tired with dissolve

    queue sound "walking-spooktober_2026.ogg" fadein 0.5

    ma_i "{i}I need to keep looking for her...{/i}"

    queue sound "crash-spooktober_2026.ogg"
    "CRASH"
    ma_i "{i}What was that???{/i}"

    queue sound "door_open-spooktober_2026.ogg"

    "Suddenly, the door is swung open. Standing there with trays in her arms is a girl who looks a few years younger than her."

    hide marisol_tired
    show marisol_tired at right
    show tintin_confused at left

    t "Oh! Mari! What are you doing here?"

    ma_i "Oh, it's just Tin-Tin..."

    ma "I don't feel well."

    t "Did you get any medicine?"

    ma_i "{i}Right. I forgot to stop somewhere...It’s too late now.{/i}"

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

    ma_i "{i}Did she see through me?{/i}"

    ma_i "{i}I don’t even care anymore.{/i}"

    jump bedroomscene

label bedroomscene:
    
    scene bedroom_van
    with fade

    queue sound "crickets-spooktober_2026.ogg"

    ma_i "{i}I guess it is kind of messy in here.{/i}"
    
    call screen bedroom_scene

label bedroom_nightstand:
    ma_i "{i}On my nightstand lays the books we read together. I never really cared much for reading until I met her. It’s crazy how much I’ve changed.{/i}"
    $ bedroomNightstand += 1;
    
    if (bedroomNightstand >= 1 and bedroomBed >= 1 and bedroomMirror >= 1):
            jump bedroomscene_continue1
    else:
            call screen bedroom_scene

label bedroom_bed:
    ma_i "{i}I’m so tired...I feel like I’m the only one looking for her. The only who still cares. Why does no one else care?{/i}"
    $ bedroomBed += 1;
    
    if (bedroomNightstand >= 1 and bedroomBed >= 1 and bedroomMirror >= 1):
            jump bedroomscene_continue1
    else:
            call screen bedroom_scene


label bedroom_mirror:
    ma_i "{i}I don’t even want to look at myself right now. I know I look awful and messy. At least that’s what mother has been telling me.{/i}"
    $ bedroomMirror += 1;
    
    if (bedroomNightstand >= 1 and bedroomBed >= 1 and bedroomMirror >= 1):
            jump bedroomscene_continue1
    else:
            call screen bedroom_scene

label bedroomscene_continue1:
    
    call screen bedroom_screenwindow

    label bedroom_windowclicked:

        show bedroom_novan

        queue sound "Van_start-spooktober_2026.ogg"

        ma_i "{i}What was that van doing outside of my house?{/i}"

        ma_i "{i}Now that I think about it...I’ve been seeing that van around often.{/i}"

        stop sound fadeout 2.0

        ma_i "{i}I better keep an eye out. I know other people have been going missing as well.{/i}"

        ma_i "..."
        
        ma_i "{i}I guess I should clean my room before mother gets home and yells at me again.{/i}"

        ma_i "{i}Should I...{/i}"

        menu branchingEnding:
            "Organize my nightstand?":
                jump shelf_route

            "Put my clothes away":
                jump clothes_route
                
    label shelf_route:
        
        ma_i "{i}I should get rid of some of these books. It does feel a bit too cluttered.{/i}"

        "{i}Marisol picks up a book and looks at it for a while with a look of contemplation.{/i}"

        "{i}She then opens it, flipping to her favorite part of the story.{/i}"

        mai "{i}I didn’t know she annotated it for me...{/i}"

        "{i}She flips the page and a letter falls out, floating like a feather to the ground.{/i}"

        "{i}Tears begin to fall from her eyes as she picks the familiar letter up off of the ground.{/i}"

        mai "{i}I remember every single word in this letter. It’s the last one she ever wrote to me.{/i}"

        "{i}Marisol opens the letter, scanning the familiar words on the delicate white paper.{/i}"

        mai  "{i}I can almost hear her reading it out to me.{/i}"

        "{i}She folds the letter back up, carefully following the creases, and gently places it back into the book, just as she had found it.{/i}"

        mai "{i}I don’t deserve the warmth and comfort of her sweet words. Not after I failed her.{/i}"

        mai "{i}I can’t believe she’s gone. It’s all my fault. If I wasn’t so unsure of myself I could have been there with her.{/i}"
        
        mai "{i}Or if I just kept everything to myself we wouldn’t even be in this mess.{/i}"

        mai "{i}We could’ve been happy here. She didn’t have to do all this for me.{/i}"

        mai "{i}It’s all my fault.{/i}"

        "{i}Marisol puts the book back onto her nightstand and falls lifelessly into her bed with a defeated sigh.{/i}"

        mai "{i}I don’t want to clean right now. I’ll probably yelled at regardless. Whatever.{/i}"

        mai "{i}I can’t stop thinking about her. I don’t even know if she’s still alive.{/i}"

        mai "{i}Everyone says she’s probably gone. I don’t want to believe it but as more time passes, the more I lose hope.{/i}"

        "{i}Marisol lays in bed, wishing that her lover was laying there next to her.{/i}"

        mai "{i}I don’t know what to do anymore. I don’t know where she could be...{/i}"

        "{i}She drifts to sleep with tear stained cheeks. Her heart is still full of worry and guilt but her body just can’t keep up.{/i}"

        scene black
        with fade

        #play music "spooky" fadein 0.5

        ##IDK IF SPOOKY IS IN THE GAME FILES FAAAAAWK

        mai "{i}Where am I? What are those voices? Everything seems so loud.{/i}"

        mai "{i}Everyone is always so loud.{/i}"

        queue sound "distorted_background_people_talking-spooktober_2026.ogg" loop fadein 5.0

        mai "{i}This is just like the wake from this morning...All my relatives chatting and gossiping. I thought that wakes were supposed to be a time of grief and mourning.{/i}"

        mai "{i}Instead, they treat it like a place to socialize and catch up with others.{/i}"

        mai "{i}They all act so casually. It isn’t fair.{/i}"

        mai "{i}They get to laugh and play games while the families cry and suffer.{/i}"

        mai "{i}I don’t understand how they can be so casual about death.{/i}"

        mai "{i}Do they know what it’s like to lose someone they care about?{/i}"

        #supposedly distorted talking sfx here

        mai "{i}It’s. Not. Fair.{/i}"

        stop sound fadeout 3.0

        mai "{i}They’re lucky to even have a wake for their loved ones.{/i}"

        mai  "{i}...I can’t even give her a proper burial. I can’t do anything.{/i}"

        queue sound "woman_scream1-spooktober_2026.ogg"

        "{i}A loud scream cuts through Marisol’s thoughts, though she can’t tell where it came from.{/i}"

        stop sound fadeout 3.0

        queue sound "woman_crying-spooktober_2026.ogg" loop fadein 2.5 

        "{i}The sound of a crying woman echoes in the distance. Her sobs seem strange, yet somehow familiar.{/i}"

        mai "{i}What is that? Is someone crying?{/i}"

        "{i}Marisol attempts to walk towards the sound but finds herself unable to move. She attempts to speak but no words leave her throat.{/i}"

        "{i}It’s as if her soul was trapped in a realm of darkness, unable to escape or scream for help.{/i}"

        show lourdes_full 
        with fade

        "{i}All of a sudden, a figure appears in front of her. Her features appear distorted, making her unidentifiable.{/i}"

        "{i}However, Marisol feels deep within that she recognizes the person standing there.{/i}"

        "{i}She wants to call out to her. She wants to scream her name. All she can muster is a single word, despite the strain and hoarseness.{/i}"

        mai "{i}...Hello?{/i}"

        stop sound

        "{i}No one answered. Instead, the woman stopped crying entirely. Everything fell uncomfortably silent. The darkness surrounding her became increasingly apparent.{/i}"
        
        #uh we need a heartbeat sfx here :' )

        "{i}The sound of Marisol’s heart beating loudly and rapidly signified that she was still there.{/i}"

        mai "{i}Maybe this is my punishment. My personal purgatory. Trapped all alone, forced to spend an eternity with the person I hate the most.{/i}"

        queue sound "woman_scream2-spooktober_2026.ogg"

        mai "{i}I wish I could scream until my vocal chords rip out of my throat. I wish I could cry until the water in my body depletes.{/i}"

        #stop sound "heartbeat"

        scene bedroom
        play music "Guilt_Route.ogg" loop fadein 5.0
        #play sound "crickets-spooktober_2026" loop fadein 2.0

        "{i}Marisol jolts awake from her horrific dream, gasping for air and her heart beating out of her chest.{/i}"

        show marisol_angry
        
        ma "{i}Lourdes!{/i}"

        "{i}As she notices her surroundings, she realizes she must have been dreaming. Although what she had was far from a dream.{/i}"

        ma "..."

        ma "{i}I can’t imagine how much she must have suffered because of me.{/i}"

        ma "{i}I couldn’t be there for her in her final moments. I wanted to protect her like she always did for me.{/i}"

        ma "{i}In the end, I was useless after all. I guess my mother was right about something.{/i}"

        "{i}Marisol lays back down and stares at the ceiling. She remembers the promises they swore to never break.{/i}"

        ma "{i}We were supposed to grow old together...{/i}"

        ma "{i}Ironic isn’t it? She died because of me. Because I hesitated and left her waiting for me. Even after all she did for me.{/i}"

        "{i}After her nightmare, Marisol began to feel a type of pain she had never experience before. There was an aching pain within her, yet somehow she felt dull and lifeless at the same time.{/i}"

        ma "{i}Somehow this feeling of nothingness is even worse. I just feel so empty. The numbness surrounds my body and envelops my mind while I just lay here, waiting for my suffering to end.{/i}"

        ma "{i}Maybe feeling an overwhelming sense of guilt would have been better than the nothingness I feel right now.{/i}"

        ma "{i}Or maybe I’m just getting exactly what I deserve...{/i}"

        hide marisol 
        with dissolve

        stop sound fadeout 2.0
        stop music fadeout 5.0
        return

    label clothes_route:

        mai "{i}I guess I can start with picking my clothes up off of the floor.{/i}" 

        "{i}Marisol starts grabbing her clothes, lazily throwing them into her arms.{/i}"

        "{i}A thick square of paper falls out and lands face down on the floor.{/i}"

        "{i}She picks the paper up and turns it around, surprised by the photograph printed on the other side.{/i}"

        mai "{i}How did this get here?{/i}"

        "{i}A photograph of her stares back at her. Tears sting at her eyes, threatening to fall onto the paper sitting delicately in her hand.{/i}"

        mai "{i}She looks so beautiful in this picture. I miss her so much.{/i}"

        mai "{i}I need to see her again. I have to find her.{/i}"

        mai "{i}I don’t care what they say. I know she’s out there somewhere. She wouldn’t just leave me like that.{/i}"

        mai "{i}...Right?{/i}"

        mai "{i}She wouldn’t leave me all alone right? I don’t think she would.{/i}"

        mai "{i}But what if she...{/i}"

        mai "{i}No. I know she loves me. Why else would she plan to run away with me?{/i}"

        mai "{i}Maybe I’ll stop by her house again tomorrow.{/i}"

        mai "{i}I know mother doesn’t want me going over there anymore but how can I not?{/i}"

        "{i}Marisol flops down onto her bed with a thud, the photograph still in her hand and her arm stretched in front of her.{/i}"

        mai "{i}I should get some rest before tomorrow. I have to leave early so nobody sees me leave.{/i}"

        mai "{i}They haven’t let me leave the house since they last caught me sneaking out...At least not until the wake today.{/i}"

        mai "{i}Marisol falls asleep with the photograph laying on her chest as it rises and falls slowly and steadily.{/i}"

        mai "{i}Her mind is surprisingly empty as she falls into her much needed slumber.{/i}"

        scene bedroom
        with dissolve

        #play music "spooky" fadein loop
        #idk drop that spooky beat

        queue sound "crash-spooktober_2026.ogg"
        "{i}CRASH{/i}"

        "{i}Marisol is woken up by a sudden, loud crash. She jolts awake and scans the room, looking for the source of the noise.{/i}"

        ma "{i}What was that?{/i}"

        "{i}It’s a bit hard to tell in the dark but nothing seems out of the ordinary.{/i}"

        ma "{i}Maybe it was just my dream? Did I even have a dream?{/i}"

        "{i}Already partially awake, she gets up to use the comfort room. She stumbles over to the bathroom across the hall.{/i}"

        ma "{i}I just need to wash my face and clear my mind. Everything is okay.{/i}"

        scene bathroom

        show marisol_reflection
        with dissolve

        "{i}Marisol briefly looks at herself in the mirror, her focus shifting to the water faucet in front of her.{/i}"

        call screen toothbrush_changer

    label bathroom_toothbrush:
        "{i}I didn’t brush my teeth before falling asleep last night. It’s not like I ate anything anyways. I’ll just brush them in the morning.{/i}"
        $ bathroomToothbrush += 1;

        if (bathroomToothbrush >= 1 and bathroomSoap >= 1):
            jump bathroom_continue1
        else:
            call screen toothbrush_changer

    #kept the soap bc it already has a hover for the faucet dialogue
    label bathroom_soap:
        "{i}The cold water feels so refreshing on my warm skin. The sweat on my face washes away into the sink.{/i}"
        $ bathroomSoap += 1;
        
        if (bathroomToothbrush >= 1 and bathroomSoap >= 1):
            jump bathroom_continue1
        else:
            call screen toothbrush_changer

    label bathroom_continue1:
        
        "{i}Marisol uses her hands to fan her face dry.{/i}"

        #drop that knocking sfx here
        #play sound "knocking.ogg"
        "{i}A series of light knocks sound on the door. No one else should be awake right now.{/i}"

        "{i}She decides to ignore it, assuming it was just her imagination.{/i}"

        play sound "door_open-spooktober_2026.ogg"
        play sound "creaking-spooktober_2026.ogg"

        ma "{i}Huh? That could not have been a dream that time.{/i}"

        show lourdes_fullbathroom
        with dissolve

        play sound "woman_crying-spooktober_2026"

        "{i}Marisol stares at the reflection of the figure behind her in shock.{/i}"

        ma "{i}...Lourdes?{/i}"

        ma "{i}Where have you been? Are you okay?{/i}"

        call screen bathroom_ghost

    label bathroom_ghostclick:
        
        ma "{i}The cold water feels so refreshing on my warm skin. The sweat on my face washes away into the sink.{/i}"

        # JUMPSCARE HERE figure out how to set a timer for that but it should be a show then hide but like if then with it
        #sorry mika if ur reading this that might have made all the sense or been some bulshit

        play sound "woman_scream2-spooktober_2026.ogg"
        
        hide marisol_reflection
        show marisol_angry
        with dissolve

        ma "{i}What was that? Where did she go?{/i}"

        hide marisol_angry

        scene bedroom_novan
        play music "Denial_Route.ogg" loop fadein 5.0
        play sound "crickets-spooktober_2026.ogg" loop

        show marisol_angry
        with dissolve

        "{i}Marisol runs back to her room in disbelief, wondering where Lourdes ran off to.{/i}"

        ma "{i}She looked hurt. I have to help her. I can’t lose her again.{/i}"

        "{i}A voice in the back of her mind wonders if what she saw was real, but she dismisses the idea just as quickly as it enters her mind.{/i}"

        ma "{i}Why would she run away from me? I hope she didn’t hit her head.{/i}"

        "{i}Although she wants to help, she can’t seem to shake a certain feeling of uneasiness and dread.{/i}"

        ma "{i}Where could she have gone? There’s no way she went home.{/i}"

        ma "{i}Wherever she went, I need to find her. It’s too dangerous for her to be out there all alone at this time.{/i}"

        ma "..."

        ma "{i}I can’t let myself make the same mistake again. She needs me.{/i}"

        ma "{i}I don’t know what she experienced or the pain she suffered but all I can do is hope she can trust me to help her.{/i}"

        ma "{i}I just hope she can forgive me. I hope I can redeem myself and earn her trust back.{/i}"

        ma "{i}I will do anything to be with her again.{/i}"

        stop sound fadeout 2.0
        stop music fadeout 5.0
        return

#RUNNING LIST OF ALL SPRITE NAMES:
#marisol_tired
#marisol_angry
#marisol_reflection
#mother_serious
#mother_angry
#tintin_confused
#tintin_neutral
#lourdes_full
#lourdes_fullbathroom

#RUNNING LIST OF ALL SCENE NAMES:
#bedroom 
#bedroom_novan
