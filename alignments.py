def character_alignment(name):
    if "Paladin" in name.char_class or "UAPaladin" in name.char_class:
        align_choices = ["Lawful Good"]
        return align_choices
    elif "Druid" in name.char_class:
        align_choices = ["True Neutral"]
        return align_choices
    elif "Cleric" in name.char_class:
        align_choices = ["Lawful Good", "Lawful Neutral", "Lawful Evil",
                         "Neutral Good", "Neutral Evil", "Chaotic Good",
                         "Chaotic Neutral", "Chaotic Evil"]
        return align_choices
    elif "Cavalier" in name.char_class:
        align_choices = ["Lawful Good", "Neutral Good", "Chaotic Good"]
        return align_choices
    elif "Monk" in name.char_class:
        align_choices = ["Lawful Good", "Lawful Evil", "Lawful Neutral"]
        return align_choices
    elif "Barbarian" in name.char_class:
        align_choices = ["Chaotic Good", "Neutral Good", "Chaotic Neutral", "True Neutral",
                         "Chaotic Evil", "Neutral Evil"]
        return align_choices
    elif "Ranger" in name.char_class:
        align_choices = ["Lawful Good", "Neugral Good", "Chaotic Good"]
        return align_choices
    elif "Thief" in name.char_class:
        if "Cleric" in name.char_class:
            align_choices = ["Neutral Good", "Neutral Evil", "Chaotic Evil", "Lawful Evil", "Lawful Neutral"]
            return align_choices
        else:
            align_choices = ["Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Evil", "Lawful Evil",
                             "Lawful Neutral"]
            return  align_choices
    elif "Assassin" in name.char_class:
        align_choices = ["Lawful Evil", "Neutral Evil", "Chaotic Evil"]
        return align_choices
    else:
        align_choices = ["Lawful Good", "Lawful Neutral", "Lawful Evil",
                         "Neutral Good", "True Neutral", "Neutral Evil",
                         "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        return align_choices

alignments = {}
alignments["Lawful Good"] = "\nLAWFUL GOOD:\n"\
                            "Lawful Good characters obey the Law as they believe order is the key to prosperity and peace.\n" \
                            "Lawful Good characters can break laws they feel are cruel and unjust.  They are strict but \n" \
                            "fair, their law and adherence to it intending to benefit others and bring oder, not fear and \n" \
                            "blind obedience.\n"

alignments["Neutral Good"] = "\nNEUTRAL GOOD:\n"\
                            "Neutral Good characters will work within, or outside of, the law in order to maintain an\n" \
                            "honorable and peaceful dispositon.  They will employ any and all questionable or reasonable\n" \
                            "methods to accomplish anything that they feel is truly for the betterment of their companions\n" \
                            "or community.  They see law or self importance as only tools and cna be employed whenever they \n" \
                            "desire a positive outcome.\n"

alignments["Chaotic Good"] = "\nCHAOTIC GOOD:\n"\
                            "Chaotic Good characters abhor the law and generally consider it evil, or at least akin to it.\n" \
                            "Chaotic Good characters value their liberty as the engine of peace and propsperity and will \n" \
                            "have no problem breaking the law if necessary but generally will do it in a way with without \n" \
                            "danger to violence to innocent lives.  They will respect 'fair' laws but will seek civil ways\n" \
                            "To sobvert them.\n"

alignments["Lawful Neutral"] = "\nLAWFUL NEUTRAL:\n"\
                               "Lawful Neutral characters obey the law as they abhor chaos.  Lawful Neutral characters \n" \
                               "will rarely disobey any established law, even if the rest of their character dislikes it.\n" \
                               "To the Lawful Neutral, is the foremost element to prosperity, and details otherwise are handledt\n" \
                               "within legal channels.  Civil unrest is not tolerated, although punishment is pragmatic.\n" \
                               "Lawful Neutral characters might be conservative towards rule and order but are not especially\n" \
                               "cruel.  Lawful Neutral may or may not feel keen on retribution, but will obey laws of the domain.\n"\

alignments["True Neutral"] = "\nTRUE NEUTRAL:\n"\
                            "True Neutral characters accept Law, Chaos, Good and Evil as forces of the universe and each \n"\
                            "with its place.  They may or may not disagree with an evil character's motivations, but generally\n" \
                            "accept these motivations for what they are.  They will combat exceptional cruelty, especially in \n" \
                            "dealing with abhorrent unnatural beings that threaten the balance of their world.\n" \
                            "True Neutral characters will not join a crusade against the non-threatening and are unlikely to\n" \
                            "destroy natrual life without exceptional reason (especially so for Druids!).\n" \
                            "True Neutral characters are not exceptionally nature obsessed, but they are more focused on seeing\n" \
                            "that the world maintains its natural balance.  To a non Druid, this could include seeing that the\n" \
                            "world maintains a geopolitical status quo.\n"

alignments["Chaotic Neutral"] = "\nCHAOTIC NEUTRAL:\n"\
                                "Chaotic Neutral characters disdain the law and would be more closely defined as pure anarchists\n" \
                                "Chaotic Neutral characters have their own loose and fluid sense of order that is most importantly\n" \
                                "derived purely by their own character and compass.\n" \
                                "Chaotic Neutral characters could be, but are not necessarily, untrustworthy or selfish, neither \n" \
                                "vein nor cruel, they prefer to live their life as they see fit, whether it breaks a law or not \n" \
                                "(although they do take particular joy in breaking laws.)\n"\
                                "A Chaotic Neutral character could certainly steal from you but isn't likely to leave you desparate\n" \
                                "and bleeding, nor would the slight be personal.  Chaotic Neutral value self-preservation the most.\n"

alignments["Lawful Evil"] = "\nLAWFUL EVIL:\n"\
                            "Lawful Evil characters are the mirror opposite of Lawful Good.  Lawful Evil characters use order and\n" \
                            "brutal rule over an obsessive and unquenchable thirst for control.  The rule under a Lawful Evil regime\n"\
                            "are devastating to the populace and always some form of extreme cult or authoratarian stete.\n"\
                            "Lawful Evil characters are typically at odds with other Evil characters finding them impossible\n"\
                            "to control.  In some manner, Lawful Evil characters are the least dangerous as their intent is generally\n" \
                            "known and they fallow a perverse path of honor.  Do not be fooled, nor take them lightly as they as \n" \
                            "they always rule by decree and change the laws to suit their need.\n"

alignments["Neutral Evil"] ="\nNEUTRAL EVIL:\n" \
                            "Perhaps the most dangers as they are the most unpredictable, Neutral Evil characters are the most \n" \
                            "though not guaranteed to be the most cruel or unrelenting.  Neutral Evil characters care only to further\n"\
                            "their needs through especially selfish means.  Law or Chaos doesn't matter, only their malicious intent.\n" \
                            "Lawful Evil characters are common amongst apocalyptic and nihilistic cults, using any means to simply\n" \
                            "bring the world to darkness.  They are the purest of evil, they do not reap shadaows among the world\n" \
                            "their only intent is to bring ruin, it is an obsession, the form it takes to enforce it, cruel reign\n" \
                            "or berzerker chaos, is not employed out of any desire other than utility.\n"

alignments["Chaotic Evil"] = "\nCHAOTIC EVIL:\n"\
                             "Arguably Neutral Evil, and certainly Lawful Evil characters can be 'reasoned' with.  Either character\n"\
                             "generally have a specific, horrific, inner purpose, but within a system that may be comprehended.\n"\
                             "They're obsessed with a god, they're obsessed with control, they're obsessed with ruin etc.\n"\
                             "Chaotic Evil characters value exceptional cruelty, and murderous chaos, solely for the turmoil and\n"\
                             "pain that it brings. They value anguish and ruin for the sense of control it brings them, and\n" \
                             "unfathomable and exceptional cruelty to others.  The experience of bringing terror to others as well\n"\
                             "destroying any comfort in order is their goal.\n"

alignments["Notes"] = "These are only one interpretation based on the PHB Alignment explanations with some more context.  These are not\n"\
                          "to be taken literally and are only meant to give some context to the motivation of a given alignment choice,\n"\
                          "These archetypes are only my interpretation designed to help build an understanding of your potential philosphy.\n" \
                          "They are meant to give more context to my interpretation of the PHB's samples, and how I read into them.\n" \
                          "It should be clear enough that Evil party characters especially will work best if they are able to keep a low\n" \
                          "profile and their proclivities kept in check where plausible.  If making an Evil characterd, discuss it with \n" \
                          "the DM to see how it will fit.\n" \
                          "Nominally, the alignments fall into two segments, your dispotion towards Good or Evil, combined with your \n " \
                          "disposition towards order or chaos.\n"


def choose_alignment(name):
    align_choices = character_alignment(name)
    print("Would you like to see some potential context and motivations for these Alignments?")
    choice = input("Y or N?")
    if choice.upper() == "Y".upper():
        print(alignments["Notes"])
        for a in alignments:
            if a != "Notes":
                print(alignments[a])
                choice = input("Enter for mor...")
    result = False
    while not result:
        iter = 1
        for i in align_choices:
            print(iter, i)
            iter += 1
        choice = input("Choose a NUMBER:")

        if choice.isdigit():
            if int(choice) in range(1, len(align_choices)+1):
                it = int(choice)-1
                print(align_choices[it])
                name.char_alignment = align_choices[it]
                return name


