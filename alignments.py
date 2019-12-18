def character_alignment(name):
    if "Paladin" in name.char_class or "UAPaladin" in name.char_class:
        align_choices = ["Lawful Good"]
        return align_choices
    elif "Druid" in name.char_class:
        align_choices = ["True Neutral"]
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

def alignment_examples():
    alignments = {}
    alignments["Lawful Good"] = "Lawful Good characters obey the as they believe order is the key to prosperity and peace.\n" \
                                "Lawful Good characters can break laws they feel are cruel and unjust, however they will\n" \
                                "do persue deplomacy before transgression or aggression.  To the Lawful Good, order is \n" \
                                "peace and any law counter to that are questioned, but at first through civil channels.\n" \

    alignments["Neutral Good"] = "Neutral Good characters will work within, or outside of, the law in order to maintain an\n" \
                                "honorable and peaceful dispositon.  They will employ any and all questionable or reasonable\n" \
                                "methods to accomplish anything that they feel is truly for the betterment of their companions\n" \
                                "or community.  They see law or self importance as only tools and cna be employed whenever they \n" \
                                "desire a positive outcome.\n"

    alignments["Chaotic Good"] = "Chaotic Good characters abhor the law and generally consider it evil, or at least akin to it.\n" \
                                "Chaotic Good characters value their liberty as the engine of peace and propsperity and will \n" \
                                "have no problem breaking the law if necessary but generally will do it in a way with without \n" \
                                "danger to violence to innocent lives.  They will respect 'fair' laws but will seek civil ways\n" \
                                "To sobvert them.\n"

    alignments["Lawful Neutral"] = "Lawful Neutral characters obey the law as the abhor chaos.  Lawful Neutral characters \n" \
                                   "will rarely disobey any established law, even if the rest of their character dislikes it.\n" \
                                   "To the Lawful Neutral, order for the sake of order is paramount, and details can be bealt\n" \
                                   "within legal channels.  Civil unrest is not tolerated, although punishment is pragmatic.\n" \
                                   "Lawful Neutral characters might be conservative towards rule and order but are not especially\n" \
                                   "cruel.  Lawful Neutral may or may not feel keen on retribution, but will obey laws of the domain.\n"\

    alignments["True Neutral"] = "True Neutral characters accept Law, Chaows, Good and Evil as forces of the universe and each \n"\
                                "with its place.  They may or may not disagree with an evil character's motivations, but generally\n" \
                                "accept these motivations for what they are.  They will combat exceptional cruelty, especially in \n" \
                                "dealing with abhorrent unnatural beings that threaten the balance of their world.\n" \
                                "True Neutral characters will not join a crusade against the non-threatening and are unlikely to\n" \
                                "destroy natrual life without exceptional reason (especially so for Druids!).\n" \
                                "True Neutral characters are not exceptionally nature obsessed, but they are more focused on seeing\n" \
                                "that the world maintains its natural balance.  To a non Druid, this could include seeing that the\n" \
                                "world maintains a geopolitical status quo"

    alignments["Chaotic Neutral"] = "Chaotic Neutral characters disdain the law and would be more closely defined as pure anarchists\n" \
                                    "Chaotic Neutral characters have their own loose and fluid sense of order that is most importantly\n" \
                                    "derived purely by their own character and compass.\n" \
                                    "Chaotic Neutral characters could be, but are not necessarily untrustworthy or selfish, neither \n" \
                                    "vein nor cruel, they prefer to live their life as they see fit, whether it breaks a law or not \n" \
                                    "(although they do take particular joy in breaking laws.)\n"\
                                    "A Chaotic Neutral character could certainly steal from you but isn't likely to leave you desparate\n" \
                                    "and bleeding, nor would the slight be personal.  Chaotic Neutral value self-preservation the most.\n"

    alignments["Lawful Evil"] = "Lawful Evil characters are the mirror opposite of Lawful Good.  Lawful Evil characters use order and\n" \
                                "brutal rule over an obsessive and unquenchable thirst for control.  The rule under a Lawful Evil regime\n"\
                                "are devastating to the populace and always some form of extreme cult or authoratarian stete.\n"\
                                "Lawful Evil characters are typically at odds with other Evil characters finding them impossible\n"\
                                "to control.  In some manner, Lawful Evil characters are the least dangerous as their intent is generally\n" \
                                "known and they fallow a perverse path of honor.  Do not be fooled, nor take them lightly as they as \n" \
                                "they always rule by decree and change the laws to suit their need."

    alignments["Neutral Evil"] = "Perhaps the most dangers as they are the most unpredictable, Neutral Evil characters are the most \n" \
                                "though not guaranteed to be the most cruel or unrelenting.  Neutral Evil characters care only to further\n"\
                                "their needs through especially selfish means.  Law or Chaos doesn't matter, only their malicious intent.\n" \
                                "Lawful Evil characters are common amongst apocalyptic and nihilistic cults, using any means to simply\n" \
                                "bring the world to darkness.  They are the purest of evil, they do not reap shadaows among the world\n" \
                                "their only intent is to bring ruin, it is an obsession, the form it takes to enforce it, cruel reign\n" \
                                "or berzerker chaos, is not employed out of any desire other than utility."

    alignments["Chaotic Evil"] = "Arguably Neutral Evil, and certainly Lawful Evil characters can be 'reasoned' with.  Either character\n"\
                                 "generally have a specific, horrific, inner purpose, but within a system that may be comprehended.\n"\
                                 "They're obsessed with a god, they're obsessed with control, they're obsessed with ruin.\n"\
                                 "Chaotic Evil characters value exceptional cruelty, and murderous chaos, solely for the turmoil and\n"\
                                 "pain that it brings. They value anguish and ruin for the sense of control it brings them, and\n" \
                                 "unfathomable and exceptional cruelty to others.  The experience of bringing terror to others as well\n"\
                                 "destroying any comfort in order is their goal."

    alignments["Notes"] = "These are only one interpretation based on the PHB Alignment explanations with some more context.  These are not\n"\
                          "to be taken literally and are only meant to give some context to the motivation of a given alignment choice,\n"\
                          "It should be clear enough that Evil party characters especially will work best if they are able to keep a low\n"\
                          "profile and their proclivities kept in check where plausible.\n"\
                          "Not every Evil character (Especially Assassins) should be shunned if they can work out a code of conduct that\n"\
                          "reflects the philosphy of your choice while not instigating party conflict.  If you must play an Evil character\n"\
                          "work with the DM on how best to handle it and accept that it may not be allowed.\n"\
                          "Lawful Evil Assassin, Cleric or Monk, characters are usually \'trusted enough\' to blend with an otherwise secular\n"\
                          "(no Paladins orGood Clerics) and other alignment/class choices might conflict as well."