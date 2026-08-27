print (""""
                      _____|\
                  _.--| SSt |:
                 <____|.----||
                        .---''---,
                         ;..__..'    _...
                       ,'/  ;|/..--''    \
                     ,'_/.-/':            :
                _..-'''/  /  |         _|/|
                    /-./_ ;       ;'   \
               ,   /   `:       //    `:`.
             ,'    /-._;   | :    : ::    ,.   .
           ,'     ::   /`-._| |    | || ' :  `.`.)
        _,'       |;._:: |  | |    | `|   :    `'
      ,'   `.     /   |`-:_ ; |    |  |  : \
      `--.   )   /|-._:    :          |    \
         /  /   :_|   ;`-._;   __..--';    : :
        /  (    ;|;-./_  _/.-:'o |   /     ' |
       /  , _/_/_./--''/_|:|___|_,'        |
      :  /   `'-'--'----'---------'          |
      | :     O ._O   O_. O ._O   O_.      ; ;
      : `.      //    //    //    //     ,' /
    ~~~`.______//____//____//____//_______,'~
              //    //~   //    //
       ~~   _//   _//   _// ~ _//     ~
     ~     / /   / /   / /   / /  ~      ~~
          ~~~   ~~~   ~~~   ~~~

""")
print("Welcome to Treasure Island.")
print("You wake up on a mysterious island with a treasure map in your hand. Somewhere on the island, a legendary treasure is hidden. Your mission is to find it!")
print("You arrive at a path with two directions.")
direction = input("Do you want to go LEFT or RIGHT? ")

if direction =="Left" or direction =="left" or direction =="LEFT" or direction =="lEFT" or direction =="LeFT" or direction =="LEft" or direction =="lEfT" or direction =="leFT" or direction =="lEft" or direction =="LeFt" or direction =="LEfT" or direction =="lEFt" or direction =="L" or direction =="l": 
    print("You walk down the left path and find a river. You see a boat and a bridge.")
    choice = input("Do you want to take the BOAT or CROSS the BRIDGE? ")
    if choice == "BOAT" or choice == "boat" or choice == "Boat":
        print("You sail across the river and find a cave. Inside, you see three doors: one RED, one BLUE, and one YELLOW.")
        door = input("Which door do you choose? RED, BLUE, or YELLOW? ")
        if door == "YELLOW" or door == "yellow" or door == "Yellow":
            print("""Congratulations! You found the treasure! You win!"
                      _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           .  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    """)
        elif door == "RED" or door == "red" or door == "Red":
            print("You enter the red door and fall into a pit of spikes. Game Over.")
        elif door == "BLUE" or door == "blue" or door == "Blue":
            print("You enter the blue door and are eaten by a giant monster. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You try to cross the bridge, but it collapses and you fall into the river. Game Over.")
