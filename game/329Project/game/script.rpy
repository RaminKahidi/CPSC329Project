# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Ramin: As mentioned above, this is how we can define characters in the game
# Color is a optional parameter, dw about adding it.

# define e = Character("Eileen")
define a = Character('[player_name]', color="#ff0000")
define b = Character('Boss', color="#2f00ff")
define n = Character('Narrator', color="#9900ff")


# The game starts here.

label start:

# Ramin: The way you can think about the game is that every time you click the mouse, 
# renpy will move down a line and read the next show the next text or the next image etc.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

# Ramin: So right now we haven't uploaded any photos but when we do we will 
# show and hide them like so: "show photo1"
# key points: 
    # - make sure the names of the photos are all lowercase and don't include the ".jpg" pr ".png" bits
    # when you write them here. For instance, if a photo is called "RaminHairCut.png" in the images directory,
    # you should bring it up with "show raminhaircut". 
# Also, you can hide by saying "hide raminhaircut"

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "boss.png" to the images
    # directory.

    show boss

    # These display lines of dialogue.

    $ player_name = renpy.input("What is your name, Agent?")
    $ player_name = player_name.strip()

    if player_name =="":
        $ player_name= "X"


    b "Hello Agent [player_name]. As our top agent, you’ve been entrusted with a high priority mission. Should you choose to accept, 
    your mission is to protect top-secret classified information from a terrorist group of malicious attackers."
    
    b "Remember, the fate of the entire world rests in your hands…"

    hide boss
    show player
    
    a "I accept!"

    hide player
    show boss
    
    b "I knew I could count on our best agent. To get started, I'll walk you through the essential steps in keeping private information secure. "

    b "Section 1: Passwords"

    b "The first barrier against having your personal information stolen is a strong password. The stronger your password,
    the more difficult it is for attackers to gain unauthorized access to your assets."

    b "A strong password is hard to guess, meaning it should be unique and unrelated to any of your personal information."
    
    b "On top of this, your password should have at least 12 characters (the more the better) that should a mix of uppercase and lowercase letters. Your password should
    also include numbers and at least one special character."

    b "Weak passwords often contain personal information (such as names or birthdays), words from the dictionary, repeated patterns (12345), or series of characters
    that appear together on the keyboard (qwerty)."

    b "Now, it is your turn Agent [player_name] to create a strong password of your own using the information I have taught you."

    hide boss
    show player

    label password:
        $ player_password = renpy.input("Enter your new password here:")
        $ player_password = player_password.strip()

        if player_password == "":
            call password from _call_password

        else:
            $ password_strength_meter = 0
            $ password_long_enough = False
            $ password_contains_digits = False
            $ password_contains_lowercase = False
            $ password_contains_uppercase = False
            $ password_contains_special = False

            if len(player_password) > 11:
                $ password_long_enough = True
                $ password_strength_meter += 1
            
            $ character = 0
            while character < len(player_password):
                if player_password[character].isdigit():
                    $ password_contains_digits = True
                if player_password[character].islower():
                    $ password_contains_lowercase = True
                if player_password[character].isupper():
                    $ password_contains_uppercase = True
                if player_password[character].isdigit() == False and player_password[character].isalpha() == False:
                    $ password_contains_special = True
                $ character += 1

            if password_contains_digits:
                $ password_strength_meter += 1
            if password_contains_lowercase:
                $ password_strength_meter += 1
            if password_contains_uppercase:
                $ password_strength_meter += 1
            if password_contains_special:
                $ password_strength_meter += 1

            hide player
            show boss

            b "Okay Agent [player_name], let's see how strong your password is..."

            if password_strength_meter == 5:
                b "Congratulations, your password was 100\% secure! I knew our best agent would come up with a secure password! 
                However, this is just the start of your mission if you're determined to keep our classified information secure."

            else:
                b "Oh no! The malicious attackers were able to guess your password and steal our classified information."
                if password_long_enough == False:
                    b "Your password was less than 12 characters long."
                if password_contains_lowercase == False:
                    b "Your password did not contain any lowercase characters."
                if password_contains_uppercase == False:
                    b "Your password did not contain any uppercase characters."
                if password_contains_digits == False:
                    b "Your password did not contain any digits."
                if password_contains_special == False:
                    b "Your password did not contain any special characters."
                $ password_strength_meter_percent = int(password_strength_meter) * 100 / 5 + renpy.random.randint(0,10)
                b "Your password was only [password_strength_meter_percent]\% secure. Please retry the mission."
                call password from _call_password_1

                
    b "You now have a strong password. However, cyber criminals are still able to guess, steal, and compromise this password using other sneaky methods."

    b "Section 2: Multifactor Authentication"

    b "Multi-factor authentication works as another barrier between your classified information and the malicious attackers."
    
    b "Unlike a password alone that is a single factor of authentication, multi-factor authentication confirms your identity based things you know, 
    things you have, or thingsyou are."
    
    b "Your next task Agent [player_name], should you choose to accept, is to correctly identify which of the three authentication categories 
    each example belongs to."

    hide boss
    show player

    a "I accept!"

    hide player
    show boss
    
    # Categorizing authentication forms game
    b "Wow Agent [player_name],  you really understand the different forms of authentication! Now that these have been identified, you must construct the
    strongest form of two-factor authentication by choosing two different factors."

    hide boss
    show player
    
    # Agent chooses factors

    hide player
    show boss

    b "That's right Agent [player_name]! A strong two-factor authentication utilizes factors from different categories. This will help us protect the
    classified information from the hackers!"
    
    b "But be careful, there are many ways the attackers could trick you into stealing this. Remember, the world is counting on you."
    
    b "Section 3: Social Engineering"

    b "Look Agent [player_name]! It appears that you've received a couple of emails. Let's inspect them together... One of these emails seems suspicious,
    can you tell which one is the real one?"

    hide boss
    show player
    
    # Agent chooses email

    hide player
    show boss

    b "I agree. This one seems to have been curated by the attackers so they can access the classified assets by stealing your private information and
    impersonating you. Nice work Agent [player_name]."

    hide boss
    show player

    a "It seems I've gotten a some voicemails as well. Let's listen to them together... it could be vital information about the mission."

    # Listen to both calls

    hide player
    show boss

    b "I think one of them is another trick from the attackers! Which one do you think the scam call is?"

    hide boss
    show player

    # Agent picks scam call

    hide player
    show boss

    b "Alright, what made you choose that call as the fake one?"

    hide boss
    show player

    # Agent picks call criteria

    hide player
    show boss
    
    b "That's right Agent! These things you've pointed out make that call very suspicious. You made the right decision by not trusting it. I'm sure it
    was part of the attackers' plan to steal our classified assets. Nice work!"

    b " Section 4: Phishing"

    b "Continue being on the lookout for suspicious activity Agent [player_name]. I'm sure the attackers will continue their tricks to try to deceive us."

    hide boss
    show player

    # Pop up ad appears

    a "Hmm, something new just popped up on my screen! What is this?"

    # Option 1 (click ad)
    a "Oh no, it must have been a trick! I've been compromised!" # restart chapter

    # Option 2 (click out of ad)
    a "This looks suspicious. I better not interact with it."

    # Google login

    a "Now I've been asked to log into my Google Account? What should I do?"

    # Option 1 (log in)
    a "Oh no! It was a trick! I've been compromised!" # restart chapter

    # Option 2 (exit)
    a "This page seems different from the actual Google login page. First of all, the URL looks different. Also, I wasn't even trying to log into my 
    Google account. I should exit the page."

    # Credit card information

    a "Now I'm being asked for my credit card information too? What could this before?"

    # Option 1 (give information)
    a "Oh no, I've been tricked! My information has been compromised!" # restart chapter

    # Option 2 (exit page)
    a "This website does not seem credible. I should first confirm whether the site and merchandise are official and secure before giving out
    any personal information that would put the classified assets at risk. Let's exit this page."

    hide player
    show boss

    b "Wow Agent [player_name]! I'm really impressed by your decision-making abilities. You were always careful to confirm the credibility of online
    activities before acting."

    b "Because of your decisions to not interact with the suspicious websites, you were able to avoid all the attacks from the malicious attackers!
    Great job!"

    b "The malicious attackers failed to get their hands on our classified assets, all thanks to you Agent [player_name]! You were able to set up
    a secure protection system using a password and multi-factor authentication."

    b "You were also able to avoid all of the malicious attempts of the attackers to steal the top secret information. I want to congratulate you for
    successfully finishing this very important mission! You really are the best!"

    hide boss
    show player

    a "Thanks boss! I'm going to keep using these cyber strategies to stay safe online and to keep my personal information secure!"

    return


# The following is some code I stole from my other renpy game, use this basis to make the minigames

#    n "."
#    label mg1:
#        menu:
#            "Every year, an estimated _______ worth of high-value metals such as gold, silver, copper, platinum, and REEs are just dumped or burned 
#            rather than recycled and reused."
#
#            "$57 billion":
#                "Spot on! Nice work!"
#
#            "$5,000":
#                "Not quite, try again!"
#                call mg1 from _call_mg1
#
#            "$500 million":
#                "Not quite, try again!"
#                call mg1 from _call_mg1_1
#
#            "$500 gazillion":
#                "Not quite, try again!"
#                call mg1 from _call_mg1_2
#
#    return
