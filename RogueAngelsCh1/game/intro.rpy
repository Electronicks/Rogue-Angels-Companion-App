
image bg intro1 = Frame("intro/intro1.png")
image bg intro2 = Frame("intro/intro2.png")
image bg intro3 = Frame("intro/intro3.png")
image bg intro4 = Frame("intro/intro4.png")
image bg intro5 = Frame("intro/intro5.png")
image bg intro6 = Frame("intro/intro6.png")
image bg intro7 = Frame("intro/intro7.png")
image bg intro8 = Frame("intro/intro8.png")

label intro:
    play music "andromeda.mp3"
    scene bg intro1:
        fit "cover"
        xpos -0.7 ypos 0 zoom 3
        linear 6.0 xpos 0 ypos 0 zoom 1
    
    "For a thousand years, the Galactic Assembly of Soverign Civilizations has governed the Burning Suns."

    scene bg intro2:
        fit "cover"
        xpos -0.5 ypos -1.0 zoom 2
        linear 6.0 xpos 0 ypos -1.0

    "By providing a forum for cooperation between the most advanced species of the galaxy, the longest peace in galactic history was achieved; a truly golden age of harmony and prosperity."
    
    scene bg intro3:
        fit "cover"
    
    """
    Unfortunately, however well-intentioned their foundation, however principled its leaders, no civilization can endure forever.
    
    Eventualy - inevitably - the Assembly failed.
    """
    
    scene bg intro4:
        fit "cover"
    
    """
    War is now spreading like wildfire.
    
    Stifled by the bureaucracy and paralysed by insurrection, The Assembly desperately tries to keep old grudges and new rivalries at bay. But unchecked greed, overweening pride, and perhaps something yet darker threaten to consume the galaxy.
    """
    
    scene bg intro5:
        fit "cover"
    
    """
    As the member civilizations draw their battle lines and stake their claim to stars and systems, lives and loyalties are torn asunder.
    
    From Eva Arielle to Panacea, from Nominus to Modeus, people who have only ever known peace and privilege must reckon with the new, harsh truth that the galaxy isn't as safe a place as they had believed...
    """
    
    scene bg intro6:
        fit "cover"
    
    """
    Beyond the Assembly's control, though, an uncertain life is business as usual.
    
    For the freelancers and free spirits of Brimstone base, home of the Hellfire pirates, risk is all in a day's existance.
    """
    
    scene bg intro7:
        fit "cover"
    
    """
    A little too close to the galaxy's incandescent heart, Vexation is a toxic superheated mess of a system, a perfect mess in which to disappear.
    
    Brimstone, buried deep beneath the sulfurous surface of Fury's Fall, is a lodestone for the dissaffected: bounty hunters and runaways, thieves and smugglers, slaves and slavers; those for whom the Suns don't shine.
    """
    
    scene bg intro8:
        fit "cover"
    
    """
    It's a dangerous place; violence decides the pecking order.
    
    But someone always has a job for an enterprising mercenary - or a desperate one - and if your skill and luck hold, there's a lot of credit to be made, particularly now.
    
    War, after all is good for business.
    """
    
    return