# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("You")
define n = Character("Narrator")
define c = Character("Colin")
define r = Character("Rory")
define why = Character("You ruined thanksgiving")


# The game starts here.

label start:
  
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene outside house
    n "Chapter 2: It's Fall"
    n "1995: Texas, US"
    stop music fadeout 1.0
    play music [  "audio/s1.ogg","audio/s2.ogg"  ]  fadein 1.0 fadeout 1.0
    n "You finally finished traveling to your grandmas house for thanksgiving. "
    scene inside house
    n "You walk inside your grandma's house, you see grandma cooking food and everone else watching tv."
    n "You and you family plays borad games and card games"
    play music [ "audio/s3.ogg" ] fadein 1.0
    n "Colin won every card and borad game like normal, Rory acuses him of cheating"
    c "No I did't!"
    r "You can't win every single game we played, unless you CHEATED!"
    n "Colin and Rory contiune arguing for hours, everyone just wants them to stop."
    n "The food has finished cooking."
    play music [ "audio/s4.ogg" ] fadein 1.0
    scene night 
    n "It's getting late so you sleep in one of the guests bedroom."
    n "You hear rory and colin talking."
    c "Let's go to the pizzarea down the road"
    r "But is't that closed?"
    c "Let's just go anyways"
    n "They walk outside"
    n "What should you do"
    play music [ "audio/s5.ogg" ] fadein 1.0 
menu:
     "Follow??"

     "Follow":
         "You decide to follow."

     "Don't Follow":
         

         "Ÿ̴̮́̉͋̍̆̀̈́̓̚͠ǫ̸̨̨̨̫̼͇̹̪̪̲͓͚͍̗͕͉̅́̈́͆͒͒̏̽̉͒̈́̅̑͌̓̃̍̀͗̂̕͜͝u̷͙̱͎̜̘͕͌͊͑͛̀̂̽͘͝ͅ ̷̡̧̳͑͆ḍ̴̢̺̟̹̻͚͙̥̳̖͓̼̤̭͓̮̠̺̹̋͗̉̈̌͋̽̆̉̌͑̃͊̑͐̄̿́̄̿͊̕ͅę̸͓͖̪͎̼͎̫̬̦͕̣͑̈̉͐̓̔̏̔̉̇͐͂́̀̌͗͊͊́̊̀͐̃̔̀̚͝͝ͅc̵̢̧̰̖͎̥̟̅́̇͑̈́̒̏̔̓̽̇͠ͅì̷̢̧̨͈̳̺̲͔͕̙̼̜̯̱͙̤̪͖̩͔̥̘̺́͂̈́̊̈́̂̿̍̏̈̐̈́̓̀͋͌̑̊͆̌̕͘͝ͅd̸͎̤͕̪̋̍̍͋̋̈́̓̏̎͊͂̑̈́̿̆̿̎̃͆̆̔̀͊̎͑͘͘͘͜͝ę̵̡͖̭̰̠̣̱̲͓̯̙̬̉̈́̈́͘͝ ̷̧͕̜̦̬̠͕̥̀̌́̚ͅt̸̨̛̥̙̺̰̤̹̣̻̘͕͕̳̙͍̙̯̯̪̺͕̪̏͂̉̓͒́̒̅̐͗̓̎͒̏́̾͘͘͘̚̕̚͠o̸̠̺̒̾̌̌́̎̊̕ ̸̨̹͓̠̱̼̭̱͚̫̝̬̦̭̮̀́̀̊̊͒̏͗̀̆͛̇̄̀̐͊͒̓̃̒̈́̈́́͆̄̕͘̕͜͝f̸̢̨̛̟̯̣̣͎͔͔̦͍͎̲̱̰͋́͆̈́́̅̍́̈́̑̓̈́̈̑̑͑̔̓ǒ̷̱͍̮̈̊̍̈́̎̑̋̃̐̎͗͐̅͐͒̓̉͂͂͛͌̍̉̿̌̚͝͝l̷̗̉̔̉̑̽͘͠l̴̨̥̣̩̹̩̰̗͚̮͔͎͖̤͍̈̋̽̌̈́͒̈́̅̓͋̿̓̚͘͝ǫ̵̠̦̪̣̫̱̞͍͎͖͔̞̘̹̹̠̗̯͉͓̱̤̐͊̋̎̄̉̏̋̊̉̊͝w̵̲͙̫̆̈͑͐̑̓͛̾́̈̇͊̆͑̊͋̂̕"

     

label after_menu:
 n "You trail after them making sure not to be seen, your also to far away to hear what there saying"
 n  "They walk into the basemnet of the pizzarea. You hear screams form the basement."
 play music [ "audio/s7.ogg" ] fadein 1.0
menu:
     "Enter the basement?"

     "Enter":
         jump end

     "Don't Enter":
      return

label end:
scene basement
n "You walk in and you see Rory's body on the floor dead, Colin  has a bloddy knife in his hand. Colin is smiling."
n "The end"