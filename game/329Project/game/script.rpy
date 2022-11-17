# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Ramin: As mentioned above, this is how we can define characters in the game
# Color is a optional parameter, dw about adding it.

# define e = Character("Eileen")
define a = Character('[player_name]', color="#F7D762")
define b = Character('Boss', color="#1EC8F1")
define n = Character('Narrator', color="#1EC8F1")


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
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    $ player_name = renpy.input("What is your name, Agent?")
    $ player_name = player_name.strip()

    if player_name =="":
        $ player_name= "X"


    b "Hello Agent [player_name]. As our top agent, you’ve been entrusted with a high priority mission. Should you choose to accept, your mission is to protect top-secret classified information from a terrorist group of malicious attackers. The fate of the entire world rests in your hands…"

    b "Once you add a story, pictures, and music, you can release it to the world!"

    a "I accept!"
    a "Hello world."

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
