# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ksr = Character("Dr. Kasser")
define mcq = Character("Macaque")
define yn = Character("yn")
define house = Character("Dr.House MD")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene bg room: 
 zoom 2
"choose character"

menu:
 "Macaque":
  jump macaquestart
  label macaquestart:
  $ menu_flag = True
  show dr_kasser:
   zoom 1.5 xoffset 1920/2/1.5
  ksr "good morning class"
  ksr "i graded your exams"
  ksr "call macaque the united kingdom in 2021 the way he got 0 points"
  ksr "light up the room!!"
  ksr "great now that song is stuck in my head"
  ksr "detention!!!"
  hide dr_kasser
  with dissolve
  show macaque scoff:
   zoom 2 xoffset 1920/2/2
  mcq "looks at y/n, scoffs and walks away"
 

 "Dr. House MD":   
  jump housestart
  label housestart:
  $ menu_flag = True

  show dr_kasser:
   zoom 1.5 xoffset 1920/2/1.5
  ksr "good morning class"
  ksr "i graded your exams"
  ksr "and although we have someone with a phd in this room"
  ksr "the class average was still a 20 percent"
  ksr "sigh."
  ksr "dismissed"
  hide dr_kasser
  with dissolve
  show dr_house:
   zoom 2 xoffset 1920/2/2
  house "what a shit show."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

ksr "test1"

    # This ends the game.

return
