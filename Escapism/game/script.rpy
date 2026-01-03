# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Zuha character defined
define z = Character("Zuha", color="#6fa758")

#Noor character defined
define n = Character("Noor", color="#ddbf22")

#lg (little girl) character defined
define lg = Character("???", color="#b84756")


define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    z "Wow im alive!! Zuha Hassan in the flesh!"
    n "Uhh im here too yk..."
    lg "Im the girl from your dream silly!"
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
