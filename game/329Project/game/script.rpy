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
    your mission is to protect top-secret classified information from a terrorist group of malicious attackers. Remember, the fate of 
    the entire world rests in your hands…"

    show player
    
    a "I accept!"

    show boss
    
    b "I knew I could count on our best agent. To get started, I'll walk you through the essential steps in keeping private information secure. "

    b "Section 1 - Passwords: The first barrier against having your personal information stolen is a strong password. The stronger your password,
    the more difficult it is for attackers to gain unauthorized access to your assets."

    b "A strong password is hard to guess, meaning it should be unique and unrelated to any of your personal information. On top of this, your 
    password should have at least 12 characters (the more the better) that should a mix of uppercase and lowercase letters. Your password should
    also include numbers and at least one special character."

    b "Weak passwords often contain personal information (such as names or birthdays), words from the dictionary, repeated patterns (12345), or series of characters
    that appear together on the keyboard (qwerty)."

    b "Now, it is your turn Agent [player_name] to create a strong password of your own using the information I have taught you."

    label password:
        $ player_password = renpy.input("Enter your new password here:")
        $ player_password = player_password.strip()

        $ strong_password = False

        #Add password strength code here
        if len(player_password) > 11:
            $ strong_password = True

        b "Okay Agent [player_name], let's see how strong your password is..."

        if strong_password == False:
            b "Oh no! The malicious attackers were able to guess your password and steal our classified information. Please retry the mission."
            call password from _call_password
        else:
            b "You did it! I knew our best agent would come up with a secure password! However, this is just the start of your mission if you're determined to keep our classified
            information secure. "


# The following is some code I stole from my other renpy game, use this basis to make the minigames
    n "."
    label mg1:
        menu:
            "Every year, an estimated _______ worth of high-value metals such as gold, silver, copper, platinum, and REEs are just dumped or burned rather than recycled and reused."

            "$57 billion":
                "Spot on! Nice work!"

            "$5,000":
                "Not quite, try again!"
                call mg1 from _call_mg1

            "$500 million":
                "Not quite, try again!"
                call mg1 from _call_mg1_1

            "$500 gazillion":
                "Not quite, try again!"
                call mg1 from _call_mg1_2





    return
