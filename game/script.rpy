# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kyle = Character("Kyle", color="#b4befe")
define josh = Character("Josh")
define niko = Character("Niko")

define sixseven = Character("Six Seven Kid", color="#f38ba8")
define tom = Character("Tom (Six Seven Kid)", color="#a6e3a1")

image kyle:
 "images/kyle.jpg"
 zoom 0.5

image josh:
  "images/josh.png"
  zoom 9

# The game starts here.


label start:
    scene room

    show kyle

    kyle "Welcome to Campfire Auckland!"

    hide kyle

    niko "Please remember the Hack Club CoC applies"

    "A few hours later..."

    show josh

    josh "Campfire Dinner Date???"

    hide josh

    show kyle

    kyle "AT SHROUD AT SHROUD"

    hide kyle

    menu:
      sixseven "What's 100 - 33?"
      "Oh no... 67.":
        jump sixseven
      "SIX SEVENNNN":
        jump yay
      "NOPE":
        jump sixseven



label sixseven:
  sixseven "SIX SEVEN SIX SEVEN SIX SEVEN"
  return

label yay:
 tom "YESSS SIX SEVENNN!! I DREW 67 ON MY ARMS 67 TIMES AND HAD TOO MUCH SODAAAA"
 jump goodending

label goodending:
  josh "WOW! You survived the hyper 67 kid and Campfire Auckland!"

  show kyle
  kyle "Good job! I have a microphone and I'm not afraid to use it (SEBASTION TURN OFF OVERFLOW)"
  return
