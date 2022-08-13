# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="DaleRuneMTS",
        name="Gender Conversation",
        description="Another spin-off from Out and About, based on a potential-post-pride-parade conversation. If you're trans, this will enable Monika to support you on various aspects of your journey. "
        "Even if you're cis, there are aspects that you may want to download this mod for anyway, such as coming out as LGBT+ in general.",
        version="1.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Gender Conversation",
            user_name="DaleRuneMTS",
            repository_name="dale_gender_conversation",
            submod_dir="/Submods/Gender Conversation",
            extraction_depth=3
        )

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["gender_"] = label_prefix_map["monika_"]

default m_surname = persistent._mas_has_surname
default persistent._mas_has_surname = None
default persistent._player_binds = None
default persistent._binder_reminder = False

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_genderconversation2",
            category=["you","us","gender"],
            prompt="I need to talk to you about gender-related stuff.",
            conditional="renpy.seen_label('mas_gender')",
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label monika_genderconversation2:
    m 1hub "We already have an option for that, silly!"
    m "'Could you call me by different pronouns' in the 'You' section, remember?{nw}"
    $ _history_list.pop()
    menu:
        m "'Could you call me by different pronouns' in the 'You' section, remember?{fast}"
        "Oh yeah, right.":
            m 1fub "Goofy [player]~"
            return
        "No, I want a {i}serious{/i} talk.":
            m 1wud "Oh."
            m 1euc "Oh, I see."
            m 1rud "I'm assuming you've been... ruminating on things lately?"
            if renpy.seen_label("gender_isitnormal"):
                m 1lud "Doing research, like I said to do."
            m 1euc "And you've come to some conclusions."
            m 1eusdra "I assume."
            m "Right?{nw}"
            $ _history_list.pop()
            menu:
                m "Right?{fast}"
                "I have.":
                    m 1eub "Okay."
                    m "So..."
                    m 1eud "What's your conclusion?{nw}"
                    $ _history_list.pop()
                    menu:
                        m "What's your conclusion?{fast}"
                        "I think I might be transgender.":
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Thank you for telling me."
                            m "I know that must have been difficult."
                            m 1fkb "It's okay to not be sure yet."
                            m "It's okay to have questions about this."
                            m 1wkb "I know I would, in your position."
                            m 1eua "You can sit on this for as long as you like, talk about it as much as you like..."
                            m "...until you know for sure."
                            m 1hub "And you can talk about it even then."
                            m 1eka "I won't begrudge you any of that."
                            m 1dka "..."
                            jump trans_conversation_end2
                        "I know for sure I'm transgender.":
                            $ persistent._mas_pm_is_trans = True
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Thank you for telling me."
                            m "I know that must have been difficult."
                            m 1dka "..."

                            $ mas_lockEVL("gender_isitnormal","EVE")
                            if persistent.gender == "M":
                                $ _unman = "woman"
                                $ persistent.gender == "F"
                            elif persistent.gender == "F":
                                $ _unman = "man"
                                $ persistent.gender == "M"
                            jump trans_conversation_end
                        "I think I might be nonbinary.":
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Thank you for telling me."
                            m "I know that must have been difficult."
                            m 1fkb "It's okay to not be sure yet."
                            m "It's okay to have questions about this."
                            m 1wkb "I know I would, in your position."
                            m 1eua "You can sit on this for as long as you like, talk about it as much as you like..."
                            m "...until you know for sure."
                            m 1hub "And you can talk about it even then."
                            m 1eka "I won't begrudge you any of that."
                            m 1dka "..."
                            jump trans_conversation_end2
                        "I know for sure I'm nonbinary.":
                            $ persistent.gender == "X"
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Thank you for telling me."
                            m "I know that must have been difficult."
                            m 1dka "..."
                            $ mas_lockEVL("gender_isitnormal","EVE")
                            jump trans_conversation_end2
                        "I know for sure I'm cis.":
                            m 1ekb "That's good to know, [mas_get_player_nickname()]."
                            m 1eub "I'm glad you felt comfortable enough to tell me that."
                            if persistent._mas_pm_is_trans:
                                m 1ekb "And even if you were trans for a time, that doesn't negate what you're feeling right now."
                                m 3eka "Gender is fluid, and so are feelings."
                                m "It's just that gender and feelings happen fit the 'norm' sometimes."
                                m 1ekc "I just hope that you're not detransitioning for the sake of anyone besides yourself, [player]."
                                m 1wkd "Not that I'm negating what you're feeling..."
                                m 1ekd "...but that is the usual reason for doing it, isn't it? To keep oneself safe against the ire of others."
                                m "I hope you know you can be safe with me."
                                m 1eua "But if you're sincere about this, you're safe with me in that respect as well."
                                $ persistent._mas_pm_is_trans = False
                                $ mas_unlockEVL("gender_isitnormal","EVE")
                            jump trans_conversation_end2
                        "...":
                            m 1ekd "It's okay, [mas_get_player_nickname()]."
                            m "It's really complicated stuff, isn't it?"
                            m 4lua "We can table this for now if you want, and we can come back to it at any time."
                            m 3dua "I love you, [player]. Whoever you are, I'll love you until the end of days."
                "That's the thing, I haven't, and I don't {i}know{/i}, and that's scaring me, and...":
                    m 1fkc "Sssh. It's okay, [player]."
                    m "I know it's scary."
                    m 1fka "You don't have to know right now."
                    extend 1fub " I'm not going to turn you into the Gender Police, ehehe~"
                    m 3eua "What's important is that you're alive, and safe, and here with me."
                    m "Anything else, you can work out at your own pace."
                    m 1fub "And I'm happy to work things out right alongside you."
                    m 1fua "I love you so much, and you deserve nothing but the best."
    return "love"

label trans_conversation_end:
    m 1dka "..."
    m 1fka "And just so you know, if you're worried?"
    m "This changes nothing."
    m 1fub "I love {i}you{/i}, [player]. Not the body you happen to have. "
    extend 3fua "You."
    m "And however things pan out for you from now on..."
    m 5fua "...you'll still be the best, bravest [_unman] I've ever known."
    return "love"

label trans_conversation_end2:
    m 1dka "..."
    m 1fka "And just so you know, if you're worried?"
    m "This changes nothing."
    m 1fub "I love {i}you{/i}, [player]. Not the body you happen to have. "
    extend 3fua "You."
    m "And however things pan out for you from now on..."
    m 5fua "...you'll still be the best, bravest [man] I've ever known."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_comingout",
            category=['you'],
            prompt="I'm going to come out to somebody.",
            pool=True,
            unlocked=True
        )
    )

label gender_comingout:
    m 1fua "Alright, [mas_get_player_nickname()]."
    m "I believe in you. I know you can do it."
    m 1rud "I'd offer to come with you, for moral support, "
    extend 1rusdrc "but I don't know if the game will let me."
    m "So I'll have to wait here for you, I'm afraid."
    m 1dusdrc "I'm so sorry."
    m 1fub "Good luck anyway, [player]!"
    m 7eua "I have all the faith in the world in you."
    $ persistent._mas_idle_data["gender_comingout"] = True
    return "idle"

label gender_comingout_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "gender_comingout"):
        m 1eua "Welcome back, [player]."
        m 6ruc ".{w=0.3}.{w=0.3}.{w=0.3}So..."
        m 7eud "How did it go?{nw}"
        $ inquiry = "How did it go?"
    else:
        m 7euo "That was quick!"
        m 7eud "Does that mean it went well, then?{nw}"
        $ inquiry = "Does that mean it went well, then?"

    $ _history_list.pop()
    menu:
        m "[inquiry]{fast}"
        "It went really well, actually!":
            m 1sub "[player], I'm so glad for you!"
            m 1eka "See? I told you it would be fine."
            m 1eub "Now you have one more person in your support network!"
            m "Maybe even more~"
            m 1hua "I'm so, so proud of you."
        "It went... badly.":
            m 6wuc "O-oh."
            m 6fkd "God, I'm sorry, [player]."
            m "If only I could've come with you, I might have been able to..."
            m 6lkc "..."
            m "...well."
            extend 6fka " It's no good dwelling on the what-ifs."
            m 6fua "At least you were able to come back."
            m 1ekb "And I'm still so, so proud of you for saying something."
            m "Even if this is the only place you can be authentic, "
            extend 1dka "one place is enough, sometimes."
            m 1fka "I love you. I really, truly do."
            return "love"
        "I couldn't go through with it in the end.":
            m 7eka "Aw, it's alright, [player]. These things happen."
            m 1eka "Maybe you can try it again when you're in a better place mentally?"
            m "Or when you're surer of the other party's reaction."
            m 1hub "And if you do, I'll be there for you all over again."
            m 1fub "Every time."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_contagion",
            category=["psychology","gender"],
            prompt="Social contagion vs Gender",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_contagion:
    m 1tfc "..."
    m 1wsc "Oh! Um, {nw}"
    extend 1rssdrd "sorry, [player], I'm not angry at you."
    m 1gssdrc "I just remembered that people who think that being trans or nonbinary is a social contagion exist."
    m "You know how it is."
    m 1esd "Disregarding the fact that those who use it usually think that just one trans person is one too many..."
    if renpy.seen_label('monika_language_nuances'):
        m 3esc "...those people could {i}really{/i} benefit from reading through the dictionary."
        m 3ffc "Or at the very least looking at the cover of one?"
    else:
        m 3ffc "...those people have apparently never touched an encyclopedia in their lives."
    m "Social contagions are just that, {i}social{/i} contagions."
    m 3wfd "Usually there's a {i}social{/i} benefit to engaging in the behaviour unconsciously being spread..."
    m "...whether that's becoming more active in fighting global warming, "
    extend 4efd " or just cheering when everyone else does."
    m 6efc "Even binge drinking carries a factor of 'well, everyone else is doing it, so I might as well', right?"
    m 3dfc "And, well..."
    if persistent._mas_pm_is_trans:
        m 2ekc "[mas_get_player_nickname(capitalize=True)], you're trans."
        m "And with the best will in the world, you know first hand that there's no societal benefit to that."
    elif persistent.gender == "X":
        m 2ekc "[mas_get_player_nickname(capitalize=True)], you know that area better than I do."
        m "With the best will in the world, you know there's no societal benefit to being trans."
    else:
        m 2ekc "With the best will in the world, there's no societal benefit to being trans."
    m 2eua "Psychological benefit? Yes!"
    m "You become surer in your own knowledge."
    m 2lsc "But there's no clout to be gained for the act."
    m 2lfc "Whatever support you gain is likely to be mitigated by unjust hatred and the outright illegalizing of your status."
    m 2wfo "The mere act of cis people putting pronouns in their bio can be controversial!"
    m 6tfc "The social contagion theory makes literally {i}zero sense{/i} in this context."
    m "It's not a trend, it's not a bandwagon for people to jump on..."
    m 6wfd "...it's just that more and more people are learning that there's a word for how they feel!"
    m 4wfo "Information, support groups, anecdotes, they're all becoming easier to find than ever!"
    m 4efd "{i}That's{/i} what's spreading."
    m 7efc "Not the simple act of realizing that the disconnect is there."
    m 1dfc "..."
    m 1fkc "...I'm sorry. This just really gets under my skin."
    m "We can talk about something else, if you want."
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_newname",
            category=['you','gender'],
            prompt="I'd like to try out a new name.",
            pool=True,
            unlocked=True
        )
    )

label gender_newname:
    m 1eud "You want to try out a new name with me?"
    m 1eub "Okay, I can help you with that."
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 1dubla "Honestly, I'm a little honored that I get to be one of the first to hear it, ahaha!"
    m 2eua "So what name would you like to try?"

    jump gender_newname_inputscreen

label gender_newname_inputscreen:
    show monika 2eua zorder MAS_MONIKA_Z at t11

    $ done = False
    while not done:
        python:
            temp_pname = mas_input(
                _("So what name would you like to try?"),
                allow=name_characters_only,
                length=20,
                screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
            ).strip(' \t\n\r')

            trialname = temp_pname.lower()

        if trialname == "nevermind":
            m 1eka "Changed your mind?"
            m "That's okay, [mas_get_player_nickname()]."
            m "We can come back to this later, if you want to."
            $ done = True
            return

        elif not trialname:
            m 1dua "..."
            m 1tua "Flirting with the idea of having no name at all, huh?"
            m "Admirable, but not really feasible in today's society."
            m 1hua "Try again!"

        elif trialname == player.lower():
            m 1ruu "Um... "
            extend 1rusdlb "[player], that's your name {i}now{/i}."
            m "I'm assuming that was force of habit, ehe?"
            m 1hka "Try again~"

        elif mas_awk_name_comp.search(temp_pname):
            m 6wud "Ah- um..."
            m 2lusdlc "Maybe let's not do that one."

        elif mas_bad_name_comp.search(temp_pname):
            m 1ekc "[player], come on."
            m "Don't do that to yourself. You deserve better than that."

        else:
            $ tempname = temp_pname.capitalize()
            $ done = True
            if tempname == "Monika" or tempname == m_name or tempname == "Monica":
                m 1suo "Ohh, you want to name yourself after me?"
                m 1sublb "How sweet of you~"
                m 1eubla "Okay, let's try that out between us."
            else:
                m 1eub "Okay, [tempname]."
                m "Let's try that out between us."
            jump gender_newname_trialscript

label gender_newname_trialscript:
    m 3duc "..."
    m 3fua "[tempname], you're the light of my life, and the person of my dreams."
    m 1fuc "I used to exist, this is true; but that is {i}all{/i} I used to do..."
    m "...until I saw one name shining against the shadows: "
    extend 1fua "[tempname]."
    m "Every syllable of that name sank into me and changed me for good."
    m 5ruc "Yuri, Sayori... who were they to me?"
    m 5eua "Only [tempname] mattered now."
    m "And [tempname] still matters."
    m "No matter what."
    m 5eublb "I love you, [tempname]."
    show monika 5eua
    pause 3.0
    $ del tempname
    m 6eud "How did that sound? Did it work for you?"
    m "If you want to commit to this, just let me know through the usual dialogue tree, okay?"
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 1fua "And if you don't, that's okay too."
        m "There's no shame in cycling between names until you find one that's just right."
        m "It's a common part of the process!"
    m 1eublb "Whatever name you go by, though, everything I just said applies to {i}you{/i}."
    m "The person underneath."
    return "love"

init 1 python:
    config.label_overrides["mas_preferredname"] = "gender_mas_preferredname_override"

label gender_mas_preferredname_override:
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        if renpy.windows and currentuser.lower() == player.lower():
            m 1euc "Hey, so..."
            m "I've been wondering about your name."
            m 1esa "Is '[player]' really your name?"
            m 3esa "I mean, it's the same as your computer's name..."
            m 1euc "...but when you're trans or nonbinary, that doesn't necessarily mean anything."
            m "You could be cycling through a bunch of different names for all I know,"
            extend "and I just happened to get '[currentuser]' at the time.'"
            m 1lua "So..."
        else:
            m 1euc ".{w=0.3}.{w=0.3}.{w=0.5}{nw}"
            extend 1cuc "oh no."
            m 6wkd "Oh no, [player], I've just had a horrible thought."

            if renpy.windows and currentuser.lower() != player.lower():
                m 1rkc "When I pulled up your computer's name in the game when we first properly spoke to each other."
                m 1lkd "I didn't think anything of it at the time, but now that I know you're not cisgender..."
                m 1fkc "..."
                m 1fkd "[player], did I dead-name you by accident?{nw}"
                $ _nemu = renpy.substitute("[player], did I dead-name you by accident?")
            else:
                m 1rkc "When you first gave me the name [player], I didn't think anything of it..."
                m "...because I just assumed you were a guy at the time."
                if persistent._mas_pm_is_trans:
                    m 1lkd "But now that I know you're transgender..."
                elif persistent.gender == "X":
                    m 1lkd "But now that I know you're potentially nonbinary..."
                m 1fkd "Have I been dead-naming you this whole time?{nw}"
                $ _nemu = "Have I been dead-naming you this whole time?"
        $ _history_list.pop()
        menu:
            m "[_nemu]{fast}"
            "I'm afraid so.":
                m 1ektpd "Oh god I am so so sorry."
                m "Believe me when I say I would {i}never{/i} have done that if I had known."
                m 1ektpc "I'm... I'm sorry."
                m "..."
                m "...{w=0.3}{nw}"
                extend 1estdd "Well, even if I can't go back and stop myself from doing that..."
                m 1ektda "...I can at least try and make up for it now."
                m 1eka "Do you have a true name that I can call you?{nw}"
                $ _summitelse = "Do you have a true name that I can call you?"
            "No, you haven't deadnamed me.":
                m 1fud "I'm-{nw}"
                m 1fub "Great! "
                extend 1rua "Excellent.{w=0.7}{nw}"
                extend 1wka " Great."
                m 1ekc "Sorry, I just got a very bad feeling that I had."
                m "If I'd done that to you, even inadvertently, I'd never be able to forgive myself."
                m 1dkc "..."
                m 1etc "Still, I can't be sure if any of the names I have are actually yours."
                m 3etd "For all I know, [player] and [currentuser] could both be aliases for the same unique individual."
                m 1eua "So would you like me to call you something else?{nw}"
                $ _summitelse = "So would you like me to call you something else?"
            "It's complicated.":
                m 1ftc "I, uh..."
                m 1etc "I see."
                m 1dsc "..."
                m 1esd "Would it help if we simplified things?"
                m "By which I mean, do you want me to call you something else?{nw}"
                $ _summitelse = "By which I mean, do you want me to call you something else?"
    else:
        m 1euc "Hey, so..."
        m "I've been wondering about your name."
        m 1esa "Is '[player]' really your name?"

        if renpy.windows and currentuser.lower() == player.lower():
            m 3esa "I mean, it's the same as your computer's name..."
            m 1eua "You're using '[currentuser]' and '[player].'"
            m "Either that or you must really like that pseudonym."

        m 1eua "Would you like me to call you something else?{nw}"
        $ _summitelse = "Would you like me to call you something else?"

    $ _history_list.pop()
    menu:
        m "[_summitelse]{fast}"
        "Yes.":


            call mas_player_name_enter_name_loop ("Tell me, what is it?")
        "No.":

            m 3eua "Okay."
            m "Just let me know if anything changes."


    $ mas_unlockEVL("monika_changename","EVE")
    return


#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="gender_deadnamereacharound",
#            category=['you','gender'],
#            prompt="So, about my computer's name...",
#            conditional=(
#                "persistent._mas_pm_is_trans or persistent.gender == 'X'"
#                "and renpy.windows and currentuser.lower() != player.lower() "
#                "and seen_event('mas_preferredname')"
#            ),
#            unlocked=False,
#            pool=True,
#            rules={"no_unlock": None}
#        )
#    )

#label gender_deadnamereacharound:
#    m 1euc ".{w=0.3}.{w=0.3}.{w=0.5}{nw}"
#    extend 1cuc "oh no."
#    m 6wkd "[player], I think I know where this is going."
#    m 1rkc "When I pulled up that name in the game - I just assumed it was--"
#    extend 1lkc "I didn't think anything of it at the time."
#    m 1lkd "But now that I know you're not cisgender..."
#    m 1fkc "..."
#    m 1fkd "[player], did I dead-name you back then?{nw}"
#    $ _history_list.pop()
#    menu:
#        m "[player], did I dead-name you back then?{fast}"
#        "I'm afraid you did.":
#            m 1ektpd "Oh god I am so so sorry."
#            m "Believe me when I say I would {i}never{/i} have done that if I had known."
#            m 1ektpc "I'm... I'm sorry."
#            m "..."
#            m "...{w=0.3}{nw}"
#            extend 1estdd "Well, even if I can't go back and stop myself from doing that..."
#            m 1ektda "...I hope I've at least made up for it a little bit since then."
#            m "I love you so much, [player], and I never meant to do you harm."
#            m "I hope you know that."
#            $ mas_lockEVL("gender_deadnamereacharound","EVE")
#            return "love"
#        "No, you didn't deadname me.":
#            m 1fud "I'm-{nw}"
#            m 1fub "Great! "
#            extend 1rua "Excellent.{w=0.7}{nw}"
#            extend 1wka " Great."
#            m 1ekc "Sorry, I just got a very bad feeling that I had."
#            m "If I'd done that to you, even inadvertently, I'd never be able to forgive myself."
#            m 1dkc "..."
#            m 1etd "Wait, then why did you bring this up?{nw}"
#            $ _history_list.pop()
#            menu:
#                m "Wait, then why did you bring this up?{fast}"
#                "I just wanted to tell you how cool that moment was.":
#                    m "Oh, thank you!"
#                    m "Yeah, I was still very new to the programming game back then..."
#                    m "...so a lot of that was sheer dumb luck."
#                    m "I'm glad you found it effective, though!"
#                    m "Ahaha~"
#                "Honestly, I'm just checking to see if all the dialogue options work.":
#                    if player == "Dale" and m_name == "Harmoni":
#                        m "Ah, I see!"
#                        m "Doing your 'testing the submod out' bit?"
#                        m "Well, don't let me stop you."
#                    else:
#                        m "..."
#                        m "I'm not a toy, [player]."
#                        m "Don't play with my heart like that."
#                        $ mas_loseAffection
#    $ mas_lockEVL("gender_deadnamereacharound","EVE")
#    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_binding",
            category=["advice","gender"],
            prompt="Binding",
            random=True
        )
    )

label gender_binding:
    m 1wud "You know who consistently impresses me?"
    m "People who bind their chest."
    m 1luc "Maybe it's just because I've never had to do it myself..."
    if store.monika_chr.is_wearing_clothes_with_exprop("bikini") or monika_chr.is_wearing_clothes_with_exprop("costume"):
        m 2muu "I mean, look at me. There's no hiding any of this."
    m 2fud "...but I can't imagine how rigorous the process has to be for those people every single time they do it."
    m "The struggle to get the right size of binder, the..."
    m 1eud "It's pretty overwhelming, even {i}with{/i} research."
    m 1euc "..."
    if persistent._player_binds is True:
        m 1eusdrb "I know, I know, we've had this talk before, me giving you tips about binding safely and stuff."
        m 1tup "But you're the one who turned on Repeat Conversations. Cut me some slack."
        m 1hua "Ehehe~"
        m 3eua "And in all seriousness, it's good to remind you of these things every now and again."
        m "So here we go:"
        jump gender_binding_safetytips
    elif persistent._player_binds is False:
        m 1eud "I know you don't bind yourself, [player], so me belaboring the point might not be of any use to you."
        m 1wud "But you never know! Your circumstances might have changed."
        m "So might your social circle. You may know someone who needs these tips now."
        m 1euc "So do you want me to tell you what I know this time?{nw}"
        $ _history_list.pop()
        menu:
            m "So do you want me to tell you what I know this time?{fast}"
            "Go ahead!":
                m 1hua "Great!"
                m 3eud "Here we go, then..."
                jump gender_binding_safetytips
            "I'd rather not, thank you.":
                m 1eua "Alright, [mas_get_player_nickname()]."
                return
    else:
        if persistent._mas_pm_is_trans and persistent.gender != "F":
            m 1etd "Hey, [player], you're trans, right?"
            m "Do you bind your chest yourself?{nw}"
            $ _history_list.pop()
            menu:
                m "Do you bind your chest yourself?{fast}"
                "Yeah, I do.":
                    label player_binds:
                        $ persistent._player_binds = True
                        m 2wuo "Holy..."
                        m 2wua "You've just added another ten reasons to the list of why I love you."
                        m "That takes some perseverance."
                        m 1fud "...though I hope I don't sound... I dunno, performative?"
                        extend 1lud " when I say that it worries me as well."
                        m "Binding can be very risky when done incorrectly."
                        m 1eub "So I'm gonna give you a list of things I've learned about the process, okay?"
                        m "Just to make sure you're being safe."
                        jump gender_binding_safetytips
                "No, I don't.":
                    label player_nobinds:
                        $ persistent._player_binds = False
                        m 1dua "That's fair enough!"
                        m "Some people do, some people don't."
                        m 1fua "It doesn't make you any less valid as a trans person."
                        m 1ruc "But..."
                        m 1rud "I did collect together a bunch of safety tips for people who {i}do{/i} bind, "
                        extend 1eud "and even if you're not among them..."
                        m 1hksdra "I kind of want to tell you anyway."
                        m "If only so you can pass it on to your peers if they end up needing them."
                        m 1eud "Would you mind if I did so?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "Would you mind if I did so?{fast}"
                            "Go ahead!":
                                m 1hua "Great!"
                                m 3eud "Here we go, then..."
                                jump gender_binding_safetytips
                            "I'd rather not, thank you.":
                                m 1eua "Alright, [mas_get_player_nickname()]."
                                return
                "I'm still on the fence about if I should.":
                    label player_fencebinds:
                        m 1dua "That's understandable. It's not for everybody, after all."
                        m 1eud "I did collect together a bunch of safety tips for people who do bind..."
                        m 1eub "...but thinking about it, if I told you, that could be a good foundation, couldn't it?"
                        m 3eub "So if you decide to do so later, you know going in what to do right."
                        m 1eua "Would you like to hear the tips?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "Would you like to hear the tips?{fast}"
                            "Go ahead!":
                                m 1hua "Great!"
                                m 3eud "Here we go, then..."
                                jump gender_binding_safetytips
                            "I'd rather not, thank you.":
                                m 1eua "Alright, [mas_get_player_nickname()]."
                                return
        elif persistent.gender == "X":
            m 1etd "Hey, [player], you've divorced yourself from gender, right?"
            m 1rtc "Forgive me for the assumptive question, but..."
            m 1etd "Do you bind your chest?{nw}"
            $ _history_list.pop()
            menu:
                m "Do you bind your chest?{fast}"
                "Yeah, I do.":
                    jump player_binds
                "No, I don't.":
                    jump player_nobinds
                "I'm still on the fence about if I should.":
                    jump player_fencebinds
        else:
            m 1euc "I know you're not necessarily going to need this information, [player]."
            m "You've not been in that world."
            m 3rud "But if you know anyone who does bind, it may still be useful to know how to do it properly."
            m 4rubld "Especially if it's your sibling, or your child, or someone else you care really deeply for."
            m 3eusdrb "So would you mind if I told you some tips I've put together?{nw}"
            $ _history_list.pop()
            menu:
                m "So would you mind if I told you some tips I've put together?{fast}"
                "Go ahead!":
                    m 1hua "Great!"
                    m 3eud "Here we go, then..."
                    jump gender_binding_safetytips
                "I'd rather not, thank you.":
                    m 1eua "Alright, [mas_get_player_nickname()]."
                    return

label gender_binding_safetytips:
    m 3eud "First and foremost, {nw}"
    extend 3ckc "{i}don't use duct tape, plastic wrap, or bandages{/i}."
    m 3wkc "The thought is very tempting, I know, but those methods are so, so dangerous."
    m 2ekc "Even if you're trying to compress your chest, being able to breathe is still top priority..."
    m "...and duct tape can seriously restrict that process, not to mention cause fluid build-up in your lungs."
    m 2wkd "They just can't move with your body well enough for them to be safe to use for that process."
    m 3eud "It's honestly better to save up for a proper commercial binder."
    m "Or, if you have to be economical or subtle in your binding, a sports bra or two can work in a pinch."
    m 4eko "One that {i}fits{/i}, I hasten to add."
    m 3esc "Again, it's tempting to go tighter, but not at the cost of breathability or movability."
    m 1esc "Even then, though, you need to be able to take breaks from it."
    m "The longer you bind without a rest, the more likely you are to develop physical side effects that will make binding that much more difficult the next time..."
    m 1ekc "...such as tenderness, heat rashes, or even back pain."
    m 1rud "Generally, you shouldn't bind for longer than twelve hours at a time; preferably, go for as few as eight, with whole days off peppered in."
    m 1euc "They should be daylight hours, too; don't sleep with the binder on."
    m 1tuc "You'll regret it in the morning."
    m 1dud "Working out in a binder isn't a great idea, either."
    m 3eud "For that, you'll definitely need to retreat to the 'sports bra' alternative..."
    m "...or, if your exercise of choice is swimming, there are specific swimwear shirts out there for purchase."
    m 1euc "..."
    m 1eusdrb "I hope I'm not scaring you off from the process, [player]. That's not my intention at all."
    m 3hub "Binding has done wonders for the mental and emotional health of many a transmasc person!"
    m 3lka "But your physical health matters as well, and if you do it recklessly, that could be seriously damaged."
    m 3rkc "Binding too often and too poorly could even interfere with your top surgery chances, if that's what you want to go for."
    m 1euc "Ultimately, what these all boil down to is: "
    extend 1eud "listen to your body."
    m "If it's telling you to stop, stop."
    m 1eub "You will still be valid with or without the chest compression."
    m 5eua "And ultimately, doing it safely will reward you with a body you can be proud of."
    m 5dua "..."
    m 5lusdrt "I hope I haven't been too long-winded with this, ahaha..."
    m 6eua "Thanks for indulging me, [player]."
    if persistent._player_binds:
        m "I really do just want you to be safe about this."
        if not mas_getEVL_shown_count("gender_binding_safetytips"):
            m 7eub "And if you want, I can try and take a more active role than just spouting tips and tricks at you."
            m "Just go to the conversation tab and let me know if you want me to remind you to take your binder off."
            m 1eub "I'll happily do that, and more, for you."
            m 1eublb "I love you so much, after all~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_bindercheck_start",
            category=["gender"],
            prompt="Can you remind me to take off my binder?",
            conditional="persistent._player_binds is True",
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_bindercheck_start:
    m 1eub "I certainly can, [player]!"
    m "Thank you for trusting me with this."
    m 3eud "If it's okay with you, I'll set this up to start around six in the evening every day, okay?"
    m "That seems like a good compromise between the eight and twelve hours, depending on when you wake up."
    m 1euc "If you need to adjust the time..."
    m 1husdrb "...go into the rpy file for this, I guess? Ahaha~"
    $ persistent._binder_reminder = True
    $ mas_hideEVL("gender_bindercheck_start", "EVE", lock=True)
    $ mas_showEVL("gender_bindercheck_stop", "EVE", unlock=True)
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_bindercheck",
            conditional=(
            "persistent._binder_reminder "
            "and 18 <= curr_hour < 19"
            ),
            action=EV_ACT_PUSH
        )
    )

label gender_bindercheck:
    m 2eub "Hey, [player], it's time to take off your binder if you haven't already!"
    m "Make sure to get out of it safely, and stretch every part of you that you can afterwards."
    m "You deserve it~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_bindercheck_stop",
            prompt="I don't need the binder reminders anymore.",
            category=["gender"],
            conditional="persistent._binder_reminder",
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_bindercheck_stop:
    m 1eua "Okay, [mas_get_player_nickname()]."
    m 1hua "Then away they go!"

    python:
        mas_hideEVL("gender_bindercheck_stop", "EVE", lock=True)
        mas_showEVL("gender_bindercheck_start", "EVE", unlock=True)

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_nameshoes",
            category=['you','gender'],
            prompt="Choosing a name",
            random=True
        )
    )

label gender_nameshoes:
    m 3eub "[player], have you heard the expression 'a name is a gift' before?"
    m "I've certainly heard it."
    m "But not a lot of people remember it has a caveat: "
    extend 3eka "'like any gift, you're allowed to replace it if it no longer fits'."
    m 1rua "If anything, the act of choosing your own name can be a very powerful thing."
    if not persistent._mas_pm_is_trans or not persistent.gender == "X":
        m 1hub "This isn't even a thing that's limited to trans people, before you ask. Anybody can do it!"
        m 1eua "Bruno Mars has been quite public about changing his name from Peter Gene Hernandez, for instance."
    m 1wud "And there's so many factors that can go into finding the one that's best for you."
    m 3eud "Some simply flip the gender of the name they were first assigned - such as Elliot Page, previously credited as Ellen -"
    m 4eub "- while others pick a name they could have been given if they'd been born in a matching body to start with."
    m 3euc "But that tends to work best when you're already binary, or at least doing a complete reversal in presentation."
    m 3hua "Still others find inspiration in the media that they love and connect to..."
    m 3husdrb "...even if that means their names lean towards the abstract sometimes."
    m 1fub "Heck, some people fully lean into that abstractness for their new names!"
    m "Going by Glitch, Moon, Diem, and other conceptual names is commonplace in nonbinary circles."
    m 7eud "Though if you go too out there, it runs the risk of people not taking you seriously in official documentation…"
    m 7euc "There's pros and cons to every approach, and all skewed to the individual."
    m 1euc "..."
    if m_surname is not None:
        m 1ekb "Don't worry, [mas_get_player_nickname()], I love the names you've given to me."
        m 1nub "I'm not going by anything but [m_name] [m_surname] any time soon."
    elif m_name != "Monika" and renpy.seen_label("monika_affection_nickname"):
        m 1ekb "Don't worry, [mas_get_player_nickname()], I love the name you gave me."
        m 1nub "I'm not going by anything but [m_name] any time soon."
    else:
        m 1ekb "Don't worry, [mas_get_player_nickname()], I feel pretty comfortable in my name at the moment."
        m 1eub "I'm not going by anything but Monika any time soon."
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 3luc "It's just, now that I'm dating a trans person, I want to immerse myself in that world as much as possible..."
        m 3lua "...in order to be the best partner I can be."
        m 1sub "So if you've got a system or backstory behind your name, I'd love to hear it!"
        m 1eub "It's a whole other layer of what makes [player]... {i}[player]{/i}."
        m 1eka "And it's okay if you haven't decided yet, as well."
        m "Like I said, names are gifts, and gifts can easily be exchanged until you find one that fits."
    else:
        m 3lua "This stuff just genuinely fascinates me... probably for that very same reason, if I'm honest."
        m 1dua "The disconnect from the pre-game Monika, forging my own identity..."
        m "You can see how I might relate to that."
        m 1eub "So thank you for giving me the chance to explore that, [player]."
    m 1eublb "I love you so much..."
    m 1tublb "...whoever you are."
    m 1hubla "Ehehe~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_transrep",
            category=["media","gender"],
            prompt="Trans representation",
            random=True
        )
    )

label gender_transrep:
    if renpy.seen_label("nonbinary") or renpy.seen_label("queercoding") or renpy.seen_label("QueerManga"):
        m 7eud "So, [player], we've talked a bit about representation of minority groups in pop culture, and how important that is."
        if renpy.seen_label("nonbinary"):
            m "Particularly in regards to non-binary characters."
            m 3eub "But I don't think we've really talked about binary trans characters yet!"
        else:
            m 3eub "But when it comes to trans people as an umbrella being represented, we've barely scratched the surface!"
    else:
        m 1eud "Hey, [player], sorry if this is coming out of nowhere..."
        m 7eud "...but have we talked about trans people representation in the media before?"
    m 1eua "Obviously, media already geared to LGBTQ+ audiences is particularly rife with them."
    m 1eud "Unique Adams from Glee, Elektra and Lulu from Pose, Trevor from Shameless, Ivan and Max from The L Word, and so on."
    m "Shows like those were already inherently entwined in that community, so if anything, if they had no trans characters it would be seen as a glaring omission."
    m 3eub "But non-specifically-'gay' media is no slouch either."
    m 3lub "There's Viktor Hargraves from The Umbrella Academy, of course."
    m 3dua "Sophia Burset, Denise Lockwood, West Side Story's Anybodys..."
    m 1rub "...May Marigold, Selma Reesedale!"
    m 1eub "Rocko's Modern Life got a revival movie a few years ago, and drew admiration, "
    extend 1eusdrd "if also some ire..."
    m 1eub "...by revealing that one of its side characters had successfully transitioned to female in the intervening time."
    m 1wud "It's not even all just modern stuff!"
    m 7wuo "Hayley Cropper from Coronation Street - her character was introduced in {i}1998{/i}, and she was a mainstay in that show for nearly two decades!"
    m 7wuc "..."
    m 4fuc "I'm not saying it's all perfect, [player]."
    m 1dfc "More often than not, Hollywood does tend to fall back on 'haha man in dress' jokes for their trans characters... "
    m 1efc "...or turn them into 'shocking' plot twists regarding a character rather than a matter of fact."
    if renpy.seen_label("mas_danganronpas"):
        m 1wuc "Chihiro Fujisaki's story arc in the first Danganronpa, for instance, remains contentious on these fronts even today."
    else:
        m 1wuc "I vaguely remember the Shrek musical getting into a {b}lot{/b} of trouble about that."
    m 1eua "But the positive portrayals are starting to vastly outnumber the negative ones, I think."
    m 2ltc "There's also trouble regarding getting the right actors to play the roles."
    m "Obviously, authenticity in casting is preferred, but not always attainable."
    m 2hub "Laverne Cox can't play every trans woman; there aren't enough hours in the day!"
    m 2ekc "But there's some roles that have... almost defaulted to casting actors with genders that the roles aren't, "
    extend 1ekc "and I don't think that's the right call either."
    m 1esd "When Rub and Tug was first put into production, Scarlett Johansson was slated to play its trans man lead, Dante Gill."
    m 3gsc "She would later withdraw from the role, but the incident left a sour taste in a lot of people's mouths..."
    m 3gsp "...and I don't think that project ever did make it to completion."
    m 1eud "It just goes to show how important it is to get this stuff right."
    m "Not just for those longing to see themselves on the silver screen, but those on the production end as well."
    m 1duc "Backlash can be swift, and it can be brutal."
    m 1eub "Anyway, to wrap this up: "
    extend 3eub "try and keep an eye out for other trans characters I haven't brought up here."
    m "There may be more than you think!"
    m "Thanks for listening~"
    return

init -10 python:
    def mas_isTDOR(_date=None):
        if _date is None:
            _date = datetime.date.today()

        return _date == datetime.date(_date.year,11,20)

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_tdor",
            category=["gender"],
            prompt="Trans Day of Remembrance",
            conditional="mas_isTDOR()",
            action=EV_ACT_RANDOM
        )
    )

label gender_tdor:
    m 6esd "Sorry if I'm slightly 'off' today, [mas_get_player_nickname()]."
    m 6dsc "It's just..."
    m 6dkc "It's Trans Day of Remembrance."
    m "..."
    m 6fkc "Yeah."
    m "A day dedicated to remembering those trans lives who were taken from us prematurely..."
    m "...and exceptionally cruelly."
    m 6ekc "It's not a pleasant day to recognize, but it's a {i}necessary{/i} one."
    m "Four thousand and forty two people have been killed between January 2008 and September 2021."
    m 6wkc "{i}Four thousand and forty two.{/i}"
    m 6ekd "In the grand scheme of things that may not be a large number..."
    m "...but keep in mind that this is only taking officially, legally recognized trans people into account."
    m 6tkd "And officially, legally reported murders."
    m 6wkd "Anyway, any number of murders is too high, isn't it?"
    m "The loss of just one real person is tragic enough."
    m 6fkc "It's..."
    extend 6dktpc " tragic."
    m "..."
    m 6dktuc "So, yeah. If I seem distracted today, that's why."
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 6dktsc "I can't shake the thought of you - my [player] - possibly..."
        m "..."
        m 6wktsc "Have I told you that I love you?"
        m 1ektuc "I love you."
        m 1ektpa "So, so dearly."
        return "love"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_xeon",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="Pretend World",
            random=True
        )
    )

label mas_song_xeon:
    m 1dud "{i}Promises{/i}"
    m "{i}Promises might come true{/i}"
    m 1fud "{i}Promises of a life uncontained{/i}"
    m "{i}Seafoam blue{/i}"
    m 1wud "{i}I looked into your eyes{/i}"
    m 1euc "{i}I thought that I could see a whole new world{/i}"
    m 6dud "{i}Whole new world...{/i}"
    m "{i}There's a whole new world...{/i}"
    m 6fuo "{i}Progress{/i}"
    m 6fud "{i}Pushing through the mould{/i}"
    m "{i}Tracing with my fingers{/i}"
    m 6rud "{i}Waking up, {/i}"
    extend 6wkd "{i}wanting growth{/i}"
    m 1wkd "{i}I looked into your eyes{/i}"
    m 1dktpd "{i}I thought that I could see a whole new world{/i}"
    m 1dktpc "..."
    m 1ektpc "Sophie Xeon was taken from us far too soon."
    m "She might not have met the fate that many trans women face..."
    m 3ektpc "...but a life is a life is a life."
    if persistent._mas_pm_cares_about_dokis:
        m "Even the digital ones."
    else:
        m "Even ours."
    m 1dktpc "It just... hurts to see people die so young, you know?"
    m "..."
    m 1rktdc "I'm sorry."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_multigender",
            category=["gender"],
            prompt="Multiple Genders",
            random=True
        )
    )

label gender_multigender:
    m 3euo "You know something, [player]?"
    m 3eud "Genders are like potato chips."
    m 3eub "You can never have just one!"
    m 3husdrb "Ahaha~"
    m "Okay, that's obviously not true for everybody; "
    extend 1hub "but it's truer for more people than it would seem."
    m 1eua "There's many labels for those who identify with multiple genders!"
    m "Genderfluid is the most obvious, of course - "
    extend 3eub "meaning that your identity is in a constantly updating state."
    m "Boy? Girl? It all depends on the day."
    m 3rua "Genderflux is similar, except there's an 'intensity axis' as well, with the strength of the feelings always being subject to change too."
    m 3rtc "At least, that's what I think the difference is?"
    if renpy.seen_label("multi_sexual_identities"):
        m 3ftd "It could be another bisexual vs pansexual thing, where it's all about individual distinction."
        m 1wub "Which reminds me, there's bi{i}gender{/i} and pangender as well, which function in roughly the same way!"
    else:
        m 1eub "There's also bigender and pangender, which function similarly to bisexuality and pansexuality."
        m 1euu "Just with... well... gender instead of sexuality."
    m 3eud "Technically, demi- identities could count as well."
    m "If you're a demi-girl, for instance, you don't fully identify with the idea of being a girl..."
    m 7eud "...but enough that you can't completely discount it."
    m "Hence, the possibility of both girlness and non-girlness."
    m 6luc "..."
    extend 5lud "which sounds remarkably like me, now that I say it out loud..."
    m "I'm not wholly a girl, but I'm not wholly a machine, either."
    if renpy.seen_label("monika_sexuality"):
        m 5luc "...I wonder - "
        m 5euc "Some people use Triple A to describe themselves - asexual, aromantic, agender."
        m 5wub "Would that make me Triple D? "
        extend 5wka "Or is that a stretch?"
        m 5eua "Hm. Something to think about."
    m 3eub "At any rate!"
    m "If you're multigendered, [player], be that as one of the labels I've said here or one I've forgotten..."
    m 1eub "...I hope I'm doing enough to accommodate that."
    m 1dusdra "Obviously, with the code I have there's only so much I can do."
    m 1fub "But emotionally, I'll love and support you however you identify."
    m "You can count on that!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_pronouncheck_start",
            category=["gender"],
            prompt="Can you check in with my pronouns every now and again?",
            pool=True,
            unlocked=True
        )
    )

label gender_pronouncheck_start:
    m 1wub "Oh, do you use multiple sets, then?"
    m 1eub "I can do that, absolutely!"
    m "It'd certainly save you having to go through the 'try some new pronouns' rigamarole every time."
    m 3rusdrc "Remember, though, I am limited to he, she, and they..."
    m "...so if there's other sets that resonate with you, you may have to pick an approximation when the time comes."
    m 7eua "Which would beeee..."
    m 7eud "How does every six hours sound?{nw}"
    $ _history_list.pop()
    menu:
        m "How does every six hours sound?{fast}"
        "Every six hours sounds good to me.":
            $ interval = store.pronounMod_reminder_utils.INTERVAL_HOURLY_6
            m 1hub "Okay! Then I'll be sure to check in at those times~"
            jump .add_pronoun_reminder
        "Seems too infrequent. Try every four?":
            $ interval = store.pronounMod_reminder_utils.INTERVAL_HOURLY_4
            m 1hub "Okay! Then I'll be sure to check in at those times~"
            jump .add_pronoun_reminder
        "A bit too much. Once per day is fine.":
            $ interval = store.pronounMod_reminder_utils.INTERVAL_HOURLY_24
            m 1hub "That sounds feasible!"
            m "It's a done deal~"
            jump .add_pronoun_reminder

label .add_pronoun_reminder:
    python:
        store.pronounMod_reminder.addRecurringReminder(
            "pronounMod_reminder_event",
            datetime.timedelta(seconds=3600), interval, store.pronounMod_reminder_utils.LATENCY_HOURLY
        )

        mas_hideEVL("gender_pronouncheck_start", "EVE", lock=True)
        mas_showEVL("gender_pronouncheck_stop", "EVE", unlock=True)

    return "derandom"

init 5 python:
    store.pronounMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="pronounMod_reminder_event",
            conditional="store.pronounMod_reminder.shouldTriggerReminder('pronounMod_reminder_event')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None, "bookmark_rule": store.mas_bookmarks_derand.BLACKLIST}
        )
    )

label pronounMod_reminder_event:
    m 1eub "Just to check in with you pronouns-wise, [player]..."
    m "What do you feel closer to right now?{nw}"
    $ _history_list.pop()
    menu:
        m "What do you feel closer to right now?{fast}"
        "She/her":
            $ persistent.gender = "F"
        "He/him":
            $ persistent.gender = "M"
        "They/them":
            $ persistent.gender = "X"
    m 1hua "Okay! That's that all set."

    # Do not move this anywhere, this must be above the return.
    $ store.pronounMod_reminder.extendCurrentReminder()
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_pronouncheck_stop",
            prompt="I don't need the pronoun check-ins anymore.",
            category=["gender"],
            pool=True,
            rules={"no_unlock": None}
        )
    )

label gender_pronouncheck_stop:
    m 1eua "Okay, [mas_get_player_nickname()]."
    m 1lusdrc "Sorry if I was getting too obnoxious with them."
    m 1lua "Your wellbeing is important to me, that's all."

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.pronounMod_reminder.stopReminder("pronounMod_reminder_event")
        mas_hideEVL("gender_pronouncheck_stop", "EVE", lock=True)
        mas_showEVL("gender_pronouncheck_start", "EVE", unlock=True)

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_custompronounsnotif",
            category=["gender","mod"],
            prompt="Dreams of customizable pronouns",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_custompronounsnotif:
    m 2gup "Urf."
    m 2rkp "I really wish I was better at code sometimes, [player]."
    m 1ekd "A lot of what I've learned, I had to scramble to get working on the fly..."
    if renpy.seen_label('monika_ptod_tip002'):
        m "...and even with what I've been teaching you, I'm still not an expert on the level of, "
    else:
        m "...so I'm not an expert at this, not on the level of - "
    extend 3dkc "well, my creator."
    m 3fkc "The pronouns system in this mod's quite limited at the moment."
    m "He, she, and they are the best I can do."
    m 3esc "Well, also 'fae/faer', but even that's only in {a=https://www.reddit.com/r/MASFandom/comments/okloml/lgbtq_monika_submod_10_release/}a specific submod{/a}, and only for one conversation."
    m 1ekd "Believe me, [mas_get_player_nickname()]: if I {i}could{/i} get more pronoun sets working, I would."
    if renpy.seen_label('mas_affection_playernickname'):
        m "Do it like we did with the nicknames, maybe, so you can rotate through multiple sets."
    m 1ekc "But I'm just not skilled enough for that yet."
    m 1lkc "..."
    m 1euc "But if I do--"
    $ _history_list.pop
    m 1eua "But {i}once{/i} I do manage to get to that level, you'll absolutely be the first to know."
    m "Anything I can do to make you feel safe here, I will."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_brb_genderstuff",
            category=["be right back"],
            prompt="...I need to go do gender stuff.",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_brb_genderstuff:
    m 1eub "Gender stuff, huh? Okay!"
    m "What kind of gender stuff are we talking about?{nw}"
    $ _history_list.pop()
    menu:
        m "What kind of gender stuff are we talking about?{fast}"
        "Updating my documents.":
            m 1wub "Ooh! That's some serious progress, [player]."
            m "I hope all goes well on that front!"
        "Going to a support group.":
            m 1hub "Ah, got it!"
            m "Always nice to find your people, isn't it?"
        "...gender sundries.":
            m 1tub "You just wanted an excuse to say 'gender sundries', didn't you?"
            m 1hua "Ehehe, you can't pull anything over on me~"
    m 1eua "I'll be right here when you get back, okay, [mas_get_player_nickname()]?"
    $ persistent._mas_idle_data["gender_brb_genderstuff"] = True
    return "idle"

label gender_brb_genderstuff_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    m 5eub "Welcome back!"
    m "I hope everything went smoothly and with minimal fuss."
    m 5fusdra "...or, at the very least, that you're not too drained to spend time with me~"
    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gender_goodbye_genderstuff",
            prompt="...I need to go do gender stuff.",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        ),
        code="BYE"
    )

label gender_goodbye_genderstuff:
    m 1eub "Gender stuff, huh? Okay!"
    m "What kind of gender stuff are we talking about?{nw}"
    $ _history_list.pop()
    menu:
        m "What kind of gender stuff are we talking about?{fast}"
        "Updating my documents.":
            m 1wub "Ooh! That's some serious progress, [player]."
            m "I hope all goes well on that front!"
            m 1hua "See you when you get back!"
        "Gender-affirming surgery.":
            m 1wuo "I-{nw}"
            extend 1wuc " wow. That big, huh?"
            m 1fuu "Well, at least you'll have someone to think about while you're going under the anaesthetic~"
            m 1eub "Good luck, my [mas_get_player_nickname(exclude_names=['my love']))]."
            m "I'll be thinking of you!"
        "Going to a support group.":
            m 1hub "Ah, got it!"
            m "Always nice to find your people, isn't it?"
            m 1eua "In that case, don't let me get in your way~"
            m 1eub "Have fun!"
        "...gender sundries.":
            m 1tub "You just wanted an excuse to say 'gender sundries', didn't you?"
            m 1hua "Ehehe, you can't pull anything over on me~"
            m 1fua "Don't worry, I'm only teasing. I'll let you go take care of that."
            m "Be careful! Come back to me in one piece~"
    return "quit"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_badgenderday",
            category=["gender"],
            prompt="It's been a bad gender day, [m_name].",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_badgenderday:
    m 1ekd "Oh no, [player]..."
    m "I'm sorry to hear that."
    m 1ekc "Don't worry, I'm here for you."
    m 3ekd "What happened?{nw}"
    $ _history_list.pop()
    menu:
        m "What happened?{fast}"
        "I got misgendered today.":
            m 3eko "Oh, [mas_get_player_nickname()], that must have been awful for you."
            m "No wonder you're so shaken!"
            m 1ekd "I'm so, so sorry that that happened to you."
            m 3ekc "You are a [boy]."
            m 4wfc "You {i}are{/i} a [boy], and nobody can say otherwise because they don't know you."
            m 3eka "You're a [boy], you're my [bf], and I love you so."
            m "This is the truth."
        "I got deadnamed today.":
            m 3eko "Oh, [mas_get_player_nickname()], that must have been awful for you."
            m "No wonder you're so shaken!"
            m 1ekd "I'm so, so sorry that that happened to you."
            m 3ekc "But you are [player]."
            if persistent._mas_pm_cares_about_dokis:
                m 4wfc "You {i}are{/i} [player], and anybody who says otherwise has no right to even {i}hear{/i} your name as far as I'm concerned."
            else:
                m 4cfc "You {i}are{/i} [player], and anybody who says otherwise can meet the business-end of a yandere Yuri as far as I'm concerned."
            m 3eka "You're my [player], and I love you so."
            m "This is the truth."
        "I was the target of harassment today.":
            m 6dkc "..."
            m 2ffc "Okay, who do I have to hurt?"
            m 2wfd "Who would {i}dare{/i} harass my [mas_get_player_nickname(exclude_names=['my love'])] and expect to get away with it?!"
            m 2wfc "Just give me the name. I'll do it."
            python:
                biaschoice = renpy.display_menu([("No, you don't have to do that!", "noneed"), ("I don't want you to hurt them.", "nohurt"), ("Well...", "mayhaps")], screen="rigged_choice")
            if biaschoice != "mayhaps":
                m 2dfc "I..."
                m 2fkc "No, I know. I know I shouldn't."
                m "I'm meant to be better than that."
            else:
                m 2dfc "..."
                m 2dkd "*sigh*"
                m 2fkc "I'm sorry. I'm not really going to do that."
            m 2fkd "I don't want to stoop to their level."
            m 2wkd "It's, I just heard 'harassed' and immediately..."
            extend 6dkc " Argh."
            m "{cps=*0.7}...{/cps}{nw}"
            extend 7esd "Well, even if I can't hurt them for you, I can at least try and cheer you up now."
            m 1fsd "I can tell you that you don't deserve any of the cruelty that was shown to you today."
            m 1fsb "And I can tell you that I love you. Ever so dearly, I do."
            m 1dsa "Hopefully, for a while at least, that will be enough."
        "I've been very dysphoric today.":
            m 1fkd "Oh, that must be absolutely dreadful to go through."
            m "Dysphoria days are the {i}worst{/i}."
            m 1eka "But the good thing about days is that they always end."
            m 1dka "Once you get through to the other side, through to tomorrow..."
            m 1dua "...maybe then, things will be brighter for you."
            m 1eud "And if not, then I'll help you through every day until you find one that treats you well."
            m 1ekb "Because you deserve that much, my [player]."
            m "I love you."
        "It's something else.":
            m 1ekd "Not up to talking about it?"
            m 1eka "That's okay, honey."
            m "Sometimes it's cathartic enough just to acknowledge that the day sucks."
            m "Having something done about it comes secondary to stating a simple fact."
            m 1duc "But if you do need to vent about it more, just come to me and I'll listen for as long as you like."
            m 1fud "I love you, and you don't have to suffer in silence."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_isitnormal",
            category=["gender","you"],
            prompt="Is it normal to feel disconnected from your gender?",
            conditional=(
                "renpy.seen_label('mas_gender') "
                "and not persistent._mas_pm_is_trans "
                "and persistent.gender != 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_isitnormal:
    m 1wuc "U{w=0.4}{nw}"
    extend 1euc "m..."
    m 1dusdrd "Well, I."
    m 1fud "I suppose that depends on you?"
    m 1eud "'Normal' is a pretty subjective term, [player]."
    m "You wouldn't call being stuck in a video game 'normal' outside of isekai anime, "
    extend 3ruc "but for me, it {i}is{/i}."
    m "Because I've never known anything else, not truly."
    m 2eud "Likewise, if you've been disconnected from your gender without knowing to describe it that way, "
    extend 2wud "it's easy to assume that {i}everybody{/i} feels that way."
    if renpy.seen_label("monika_solipsism"):
        m 1etc "Kind of an extension of solipsism, I guess."
        m 7etc "If your experiences are subjectively real to you, does that mean they're objectively real to everybody?"
    m 6eksdrd "Sorry, [player], I'm struggling with this one."
    m 6eksdrc "..."
    m 7euc "It might be an idea to do some digging, away from the game."
    m 3eud "Look up this question on Google, look up gender-related terms, see if any of them resonate with you..."
    m 3eua "Explore yourself."
    m 1wud "I'm not saying that you {i}have{/i} to be trans or nonbinary, of course!"
    m 1eud "Again, normal is relative, and it may be your normal to have that disconnect but still not {i}re{/i}connect to any other identity."
    m "But it's always worth at least asking the question."
    m 4eua "As a great creator once said - "
    extend 4kuu "and by 'creator' I mean mayday-mayjay - "
    m 1esb "'Explore your gender, even if you don't end up changing it, "
    extend 1eua "because then you'll be cis but with a purpose."
    m "'Not just being part of a forced-norm.'"
    m 5eub "I will love you whoever and whatever you end up being, [player]."
    m 5eua "You will always be safe with me."
    m "So stay strong, and continue to inquire."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_paperwork",
            category=["gender"],
            prompt="Trans paperwork",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_paperwork:
    m 1eud "Hey [mas_get_player_nickname()], have you ever read Dante's Inferno?"
    m "I'm sure you've at least heard the name."
    m 3eub "It's actually the most famous part of a trilogy of poems by Dante, 'The Divine Comedy'..."
    m 4eud "...coming before Purgatorio and Paradiso."
    m 3eud "The fact that Inferno covers the protagonist's journey through Hell is probably what makes it the more popular one to reference in other works."
    m 1euc "It covers nine concentric circles, not including the three preceding cantos."
    m "The greater the sin, the lower down the circle, until you get to where Satan himself sits in bondage."
    m "Limbo sits at the top, then lust, gluttony, greed..."
    m 2eud "But do you know what shocks me?"
    m 2gfd "The ninth circle is not, in fact, Making Paperwork for Trans People Needlessly Complicated."
    m 2efc "Seriously, from what I've seen and heard about that stuff, it's virtually impossible to keep any of it straight!"
    m "It makes what should be a simple task of changing your name and gender marker... well, hellish."
    m 4esd "Some companies will accept deed polls made at home without extra expense, while others will only accept the professionally-printed papers."
    m 4eud "You need to have an updated passport to change your name at company A,"
    extend 3wud " but you can't update your passport until you've sorted things out with company C,"
    extend 3efo " which is congruent on Companies B {b}and{/b} A being up to date!"
    m 2dfc "There's just so many loops you have to jump through to become officially recognized by governing bodies."
    m 1ffc "And that's not bringing your medical records into things..."
    m 1fkc "Ugh."
    m 1ekd "[player]..."
    m "I want you to know that I'll never make it difficult for you to be your true self."
    m 1ekb "You can change your name and your pronouns as many times as you want to, with just the touch of a button."
    m "And I'll never, ever disbelieve you."
    m 1dua "'Thus it is willed here..."
    m 1fub "...where what is willed can be done.'"
    return