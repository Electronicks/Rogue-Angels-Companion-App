# Declare characters used by this game. The color argument colorizes the
# name of the character.

define action = Character("Action:", color='#25ecec')
define o = Character("Overseer", color="#22FF22")
define enforcer = Character("Enforcer", color="#FF2222")
define guard = Character("Guard", color="#FF2222")
define umbrasius = Character("Umbrasius", color="#2277FF")
define bartender = Character("Bartender", color="#22FF22")
define aaron = Character("Aaron", color="#FF2222")
define camreal = Character("Camreal", color="#2277FF")
image bg vexation = "bg/vexation.png"
image bg base = "bg/base.png"
image bg bar = "bg/bar.png"
image bg map001 = Frame("map/map001.png")
image bg escape = "bg/escape.png"
image locked = "token/locked.png"
image poi = "token/poi.png"
image squad = "token/squad.png"
image turn = "token/turn.png"
image door = "token/door.png"
image console = "token/console.png"
image thug = "character/thug.png"
image ship = "token/ship.png"
image y1l = Text("Y1", color='#ebeb1f')
image y2l = Text("Y2", color='#ebeb1f')
image r1l = Text("R1", color='#eb1f1f')
image r2l = Text("R2", color='#eb1f1f')

label c1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg vexation with fade:
        fit "cover"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    # show eileen happy

    # These display lines of dialogue.

    " C1 – Credits and Brimstone" "Location: Vexation, Fury’s Fall, Brimstone Base.\nYear: 1001 ATA."
    
    "\[The main entrance to the scorching sulfur-engulfed hangar area shuts behind you.\]"
    
    show overseer at left 
    o "Ah, fresh meat! Welcome to Brimstone, outer suburb of hell and the closest viable settlement to the Burning Suns. Population: none of your damn business. If you'll step right along to the elevator, we can begin the process of getting you oriented"
    
    play sound "elevator_start.wav"

    o "People like you always seem to wind up here. Drifters and opportunists. Always looking for that one big score, right? Well, you've found the right place to look, if you don't play by Assembly rules."
    
    play sound "elevator_stop.wav"
    
    o "Speaking of rules, we do have a few. First and foremost, some security precautions. Can't be too careful when there's..."
    
    show guard at right
    guard "Step aside, spread out and don’t move."
    
    hide overseer
    guard "Hand over your identification and your weapons. We will withhold these till you leave this area of the base again."
    
    show enforcer at left
    enforcer "Delay that order. There will be no inspection for now. We have been ordered to permanently confiscate all weapons from all visitors, no exceptions."
    
    menu:
        action "Every player must put aside all their cards with weapon classification. They must not be used for now."
        "Done":
            enforcer "And any neomorph or champions are to hand over all their gear as well. We don't trust those warmongering snakes."
            
    menu:
        action "Every neomorph and champion player must also put aside all their gear cards. They must not be used for now."
        "Done":
            enforcer "Good. Now move along."
            
    hide guard
    hide enforcer
    show bg base
    show overseer at left
    o """
    Let me run you through how things work around here. Hellfires are top of the tree. What we say, goes, and what we want, we get.
    Below us, we have the traders and merchants. After them, the bounty hunters, and smugglers.
    
    And last of all, we have you, guns for hire. Now this is nothing personal, just simple rules in a galaxy full of rivaling species and ideologies.
    
    That concludes our welcome tour, so I'll leave you to entertain yourselves. Follow the arrows to the bar. Don't leave the leisure area, don't get cute with the guards, and don't start a fight.
    
    Like I said, simple rules. Break 'em, and we'll break you.
    """
    
    play music "callista.mp3" fadeout 1.0 fadein 5.0
    o "Enjoy your stay."
    
    scene bg bar with fade:
        fit "cover"
    "\[The noise from the speakers and crowds intensifies as you approach the bar area.\]"
    
    show bartender at right
    bartender "Welcome outlanders, what’ll it be? If you don’t mind a strong aftertaste, I have a newly imported Marauder rum from Hel’s Market on Asgard."
    
    "\[The bartender waves you to the bar again.\]"
    
    bartender "Here’s your drink."
    play sound "beep.wav"
    bartender "You have a personal call on the comm. Let me reroute it to your device, just a second."
    
    hide bartender
    show umbrasius at left
    umbrasius """
    Greetings, Commander. I’m pleased to hear you've already assembled a team. As you can imagine, with so many factions on the warpath, it is almost impossible to find unaffiliated agents through our regular channels.
    
    But let's get straight to business. The Neomorph Polity is deeply concerned by the Assembly’s failure to control the unprovoked aggression of our enemies.
    
    I’ve therefore been tasked with exploring "alternative strategies" to defend the Polity from all current and future foes. An exploration that has led me to this particular suburb of hell.
    """

label c1_play:
    scene bg map001:
        fit "cover"
        xanchor 0 yanchor 0
        xpos 0 ypos 0 #zoom 0.83
        #linear 3.0 xpos 60 ypos 0
        
    action "Open the map book at map 001"
    
    menu:
        action "Take 3 Blocked Entrances, 1 POI, the player standees and the turn marker."
        "Done":
            window hide
            show locked as l1 with moveinbottom:
                xpos 0.26 ypos 0.525
            pause
            show locked as l2 with moveinbottom:
                rotate 90 xpos 0.494 ypos 0.362
            pause
            show locked as l3 with moveinbottom:
                rotate 90 xpos 0.422 ypos 0.645
            pause
            show poi with moveinbottom:
                xpos 0.465 ypos 0.18
            pause
            show squad with moveinbottom:
                xpos 0.135 ypos 0.185
            pause
    
    window show

label player_select:
    menu:
        action "How many players are there?"
        "2":
            window hide
            $ players = 2
            show turn with moveintop:
                xpos 0.76 ypos 0.915 # 3 turns
        "3":
            window hide
            $ players = 3
            show turn with moveintop:
                xpos 0.725 ypos 0.915 # 4 turns
        "4":
            window hide
            $ players = 4
            show turn with moveintop:
                xpos 0.69 ypos 0.915 # 5 turn
    pause
    
    window show
    show umbrasius at left
    umbrasius "Vexation is a wretched place to find yourself delayed, but that is the situation I find myself in. Rendezvous with me at my location and I'll explain further. Don't dally, Commander - I have no desire to stay in this garbage incinerator of a system a second longer than necessary."
    
    hide umbrasius
    hide squad
    
    menu:
        "Introduction note:" "a) Adjacent does not mean “on top of”, though it is legal with a borderless POI like here.\nb) In the beginning of each new mission, you always select a Commander. This player will call the shots when mutual agreements cannot be made, or in cases where the team must vote on decisions."
        
        "Success: Get the commander adjacent to the point of interest (POI)":
            jump c1_mu1
        "Failure: The turn token reaches 0":
            "Restarting the mission"
            jump c1_play
            
label c1_mu1:
    hide turn
    "Remove 1 POI and 1 Blocked Entrance"
    window hide
    hide poi with dissolve
    pause
    hide l1 with dissolve
    pause
    window show
        
    menu:
        action "Take 1 Door and 1 Console"
        "Done":
            window hide
            show door with moveinbottom:
                xpos 0.26 ypos 0.525
            pause 
            show console with moveintop:
                xpos 0.12 ypos 0.78
            pause
            if players >= 4:
                show turn with moveintop:
                    xpos 0.512 ypos 0.915 # 10 turn
            elif players == 3:
                show turn with moveintop:
                    xpos 0.584 ypos 0.915 # 8 turn
            else:
                show turn with moveintop:
                    xpos 0.655 ypos 0.915 # 6 turn
            pause
            
    window show
    show umbrasius at left
    umbrasius """
    Good to see you in person, Commander. My agent promised me a competent team, but let's not get ahead of ourselves. When I arrived, these Hellfire thugs confiscated my ship and equipment, and I now see they're doing it to everyone.
    
    Perhaps they're running low on resources? In any case, I’m not interested in their petty problems. If they want to steal my ship it'll be over my dead body… or more precisely, over a lot of other dead bodies.
    
    Get into their enclave and hack their console so that you’ll be able to retrieve our stuff. And don’t let anyone get in your way.
    """
    
    hide umbrasius
    menu:
        "Introduction note:" "Opening, disabling and hacking are all achieved by successfully interacting with the object in question."
        
        "Success: Open the door and disable the console.":
            play sound "open_safe.wav"
            jump c1_mu2
        "Failure: The turn token reaches 0":
            "Restarting the mission"
            jump c1_play
            
label c1_mu2:
    hide console
    hide door
    hide turn
    "\[As the console shuts down, you swiftly open the armored boxes containing your confiscated equipment.\]"
    play sound "cocking.mp3"
    menu:
        action "Every player gets all their weapon and gear cards back in hand and is now able to use them again."
        "Done":
            show umbrasius at left
            umbrasius "Their security system is compromised; I have access to their vault and my ship. I’ll pick up my crew members in the bar area and meet you onboard my ship."
            play sound "alarm.mp3"
            umbrasius "It seems that the Hellfires have been alerted to your presence. But I assume that you’re capable of dealing with such trifles."
            hide umbrasius
            
    play music "blazing skies.mp3" fadeout 1.0
    menu:
        action "Take 2 Thugs as Y1 and Y2 and 1 Guard as R1"
        "Done":
            window hide
            show thug as y1 with moveinbottom:
                xpos 0.05 ypos 0.185
            show y1l with moveinbottom:
                xpos 0.05 ypos 0.185
            pause
            show thug as y2 with moveinbottom:
                xpos 0.123 ypos 0.282
            show y2l with moveinbottom:
                xpos 0.123 ypos 0.282
            pause
            show guard as r1 with moveinbottom:
                xpos 0.398 ypos 0.779
                xsize 78 ysize 78
            show r1l with moveinbottom:
                xpos 0.398 ypos 0.779
            pause
    
    window show
    menu:
        action "Put the Apprehensive attack EBC on the red side on the table"
        "Done":
            window hide
            if players >= 4:
                show turn with moveintop:
                    xpos 0.62 ypos 0.915 # 7 turn
            elif players == 3:
                show turn with moveintop:
                    xpos 0.655 ypos 0.915 # 6 turn
            else:
                show turn with moveintop:
                    xpos 0.69 ypos 0.915 # 5 turn
            pause
            
    window show
    
    show aaron at right
    aaron "Who are you? What are you doing in a restricted area? Did you not understand the rules you were given? I guess I’ll have to get my guards to give you a little reminder."
    hide aaron
    
    menu:
        "Introduction note:" "Eliminating, killing and destroying are all achieved by using weapons or abilities that deal damage to the enemies in question.\nRemember: When enemies appear, they always go first after the mission has been updated."
        
        "Success: Eliminate all ennemies":
            jump c1_mu3
        "Failure: The turn token reaches 0":
            "Restarting the mission"
            jump c1_play
        "Failure: All players are unconscious":
            "Restarting the mission"
            jump c1_play
            
label c1_mu3:
    hide turn
    hide y1
    hide y1l
    hide y2
    hide y2l
    hide r1
    hide r1l
    show umbrasius at left
    umbrasius """
    We’re ready for take-off from hangar 17. Unfortunately, we have a situation here, as the Hellfires have locked the gangway door and placed our ship on a tractor beam.
    
    We won’t be going anywhere unless you can dispose of the pirates or disable the tractor beam from the control room. How you deal with it, is up to you.
    """
    hide umbrasius
    action "Remove 2 Blocked Entrances"
    window hide
    hide l2 with dissolve
    pause
    hide l3 with dissolve
    pause
    window show
    menu:
        action "Take the ship box, 1 Door and 1 Console"
        "Done":
            window hide
            show ship with moveinleft:
                xpos 0.825 ypos -0.185 rotate 90
            pause
            show door with moveinleft:
                xpos 0.92 ypos 0.18
            pause
            show console with moveinleft:
                xpos 0.885 ypos 0.67
            pause

    menu:
        action "Take 2 Thugs as Y1 and Y2 and 2 Guards as R1 and R2"
        "Done":
            window hide
            show thug as y1 with moveinbottom:
                xpos 0.82 ypos 0.67
            show y1l with moveinbottom:
                xpos 0.82 ypos 0.67
            pause
            show thug as y2 with moveinbottom:
                xpos 0.68 ypos 0.085
            show y2l with moveinbottom:
                xpos 0.68 ypos 0.085
            pause
            show guard as r1 with moveinbottom:
                xpos 0.05 ypos 0.375
                xsize 78 ysize 78
            show r1l with moveinbottom:
                xpos 0.05 ypos 0.375
            pause
            show guard as r2 with moveinbottom:
                xpos 0.121 ypos 0.182
                xsize 78 ysize 78
            show r2l with moveinbottom:
                xpos 0.121 ypos 0.182
            pause
    menu:
        action "Put the Disorganized attack EBC on the red side on the table"
        "Done":
            window hide
            if players >= 4:
                show turn with moveintop:
                    xpos 0.407 ypos 0.915 # 13 turn
            elif players == 3:
                show turn with moveintop:
                    xpos 0.477 ypos 0.915 # 11 turn
            else:
                show turn with moveintop:
                    xpos 0.547 ypos 0.915 # 9 turn
            pause
            
    window show
    show aaron at right
    aaron "OK... for better or worse you now have my full attention, and you won’t be going anywhere when I’m through with you. You'll be an example for everyone to see of why you don't screw with the Hellfires."
    hide aaron
    
    menu:
        "When enemies appear, they always go first after the mission has been updated.\nThe ship is part of the map and can be boarded/exited by players only. Enemies will not move towards, or target, players already onboard the ship."
        "Success: Open the door, disable the console, and get all players on board the ship.":
            jump c1_mu4a
        "Success: Eliminate all enemies.":
            jump c1_mu4b
        "Failure: The turn token reaches 0.":
            "Restarting the mission"
            jump c1_play
        "Failure: All players are unconscious.":
            "Restarting the mission"
            jump c1_play
    
label c1_mu4a:
    scene bg escape with fade:
        fit "cover"
    play sound "spaceship.wav"
    "\[As the ship escapes the atmosphere of Fury’s Fall, it all becomes quiet for a while as you settle down.\]"
    show camreal at right
    camreal "We’re in neutral space far from Fury’s Fall, no pursuers. Stand down from action stations. I'm plotting a route through the shadows of the planets in the habitable zone to screen any radiation bursts from the Suns. Should cut down the debris bump as well."
    show umbrasius at left
    umbrasius """
    You and your team certainly didn’t disappoint, Commander. We’re in for a long and demanding undertaking, but your performance gives me confidence that we’ll be able to pull it off.
    
    Let's get the debrief over with, so we can continue the conversation about more important matters and get you all settled on the ship.
    """
    
    hide camreal
    hide umbrasius
    menu:
        "Did the team eliminate 1 or more enemies in last mission segment?"
        "Yes":
            jump end
        "No":
            action "Everyone paints +1 in their legacy folder next to Hellfires."
    jump end
    
label c1_mu4b:
    scene bg escape with fade:
        fit "cover"
    play sound "spaceship.wav"
    "\[Leaving the gravitational pull of Fury’s Fall, everything becomes quiet as the cold dark space wraps around the ship.\]"
    show camreal at right
    camreal "This is the pilot speaking, we’re in neutral space with no pursuers, you may step down from your action stations. For the next several hours we’ll be cruising in the shadows of the planets in the habitable zone to avoid any sporadic radiation burst from the Suns."
    show umbrasius at left
    umbrasius """
    This is certainly one way to handle it, and your team did not disappoint on the scale of bloodshed. I’m confident that your skills will be a fine addition to my crew’s portfolio.
    
    Let’s get through the debrief, so we can continue the conversation about more important matters and get you all settled more permanently on the ship.
    """
    
    hide umbrasius
    hide camreal
    menu:
        action "Everyone paints -1 in their legacy folder next to Hellfires."
        "Done":
            jump end

label end:
    "Mission Successful"
    # jump c2 # c2 Digital Blood
    "Thank you for checking out this demo of Rogue Angel on Ren'Py!"
    return