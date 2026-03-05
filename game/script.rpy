define kyle = Character("Kyle", color="#b4befe")
define josh = Character("Josh", color="#89b4fa")
define sebastian = Character("Sebastian")
define niko = Character("Niko", color="#94e2d5")
define mrfraud = Character("Mr Fraud (Niko)", color="#f38ba8")
define tristian = Character("Tristian")

define sixseven = Character("Tattoo 67 Kid", color="#f38ba8")
define tom = Character("Tom (Tattoo 67 Kid)", color="#a6e3a1")

image kyle:
 "images/kyle.jpg"
 zoom 0.5

image josh:
  "images/josh.png"
  zoom 9

image tristain:
  "images/tristian.png"
  zoom 0.5

image mrfraud:
  "images/mrfraud.png"
  zoom 8

image niko:
  "images/niko.png"

label start:
    scene room

    show kyle

    kyle "Welcome to Campfire Auckland!"

    hide kyle

    sebastian "I like blinding people with obnoxious lights!"

    show niko
    niko "Please remember the Hack Club CoC applies"

    menu:
      niko "Have you read the CoC?"
      "Yes":
        jump yes
      "No":
        hide niko
        jump angerniko

label back:
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



label sixseven:
  sixseven "SIX SEVEN SIX SEVEN SIX SEVEN"
  return

label yay:
 tom "YESSS SIX SEVENNN!! I DREW 67 ON MY ARMS 67 TIMES AND HAD TOO MUCH SODAAAA"
 jump continue

label continue:
  show tristian
  tristian "*sings* NEVER GONNA GIVE YOU UP"
  hide tristian
  jump goodending

label goodending:
  show josh
  josh "WOW! You survived the hyper 67 kid and Campfire Auckland!"
  hide josh

  show kyle
  kyle "Good job! I have a microphone and I'm not afraid to use it (SEBASTIAN TURN OFF OVERFLOW)"
  return

label angerniko:
  show mrfraud
  mrfraud "RAHHHH READ THE COC OR ELSE I'LL HACKATIME BAN YOU"
  mrfraud "SAY GOODBYE TO YOUR CHARGING PORT!!!"
  hide mrfraud
  return

label yes:
  niko "I'd expect no less."
  hide niko
  jump back
