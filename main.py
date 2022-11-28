from time import sleep

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You see a dog far away, he seems to be waiting for you. You can follow the dog (f) or walk along the ocean, you can walk to your right (r) or to your left(l).")
choosed_option = ""
choosed_option = input("What do you do? \n")
if choosed_option == "l" or choosed_option == "r":
  print("A huge wave hits the shore and drags you to your death. Game over.")
  exit()
elif choosed_option == "f":
  print("The dog patiently waits for you until you reach it. It has a collar and a name collar on it. Looks like his name is Jagger.")
else:
  print("You did nothing. A thick fog comes from the ocean and suffocates you to death. Game over.")
  exit()

print("Jagger makes you follow him until you reach an old house in the middle of the island. He seems to want to go inside the house. You can either knock the door (k), leave Jagger there and investigate on your own (l), or hide and wait in case someone arrives to or comes out of the mansion (w).")
choosed_option = input("What do you do?\n")
if choosed_option == "k":
  print("No sound comes out, the door slightly opens and Jagger storms inside. He starts barking.")
elif choosed_option == "l":
  print("Something big runs around the plants and grass, you barely have time to turn around before the creature eats you alive. Game over.")
  exit()
elif choosed_option == "w":
  print("You start hearing a high-pitched screech from afar which starts increasing in volume as the source apporaches your location. You blink and a smiling demon drags you to hell. Game over.")
else:
  print("You did nothing. A thick fog starts forming all around you and suffocates you to death. Game over.")

print("Looks like Jagger has found something and is calling you so you can see it.")
print("You look around the house, there are some stairs leading to where Jagger seems to be. You go up and find three closed doors and the barking seems to come out of all three doors at the same time... How did Jagger get inside if all doors are closed?\nOn each door is a picture. The leftmost door has a child around 12, smiling. The rightmost door has a landscape, looks like a lake. The door in the middle shows a picture of a huge castle.")
choosed_option = input("Which door do you go through? The left one (l), the one in the middle (m) or the right one (r)?")

if choosed_option == "l":
  print("You find an empty room. Jagger barks at a chest. You open it and it's a chest full of gold.")
elif choosed_option == "m":
  print("You enter a room full of dead, bloody, bodies. It's all dark and something is making chewing noises. Before you notice you're already bitten. You're eaten alive. Game over.")
  exit()
elif choosed_option == "r":
  print("You enter a room full of beds. Jagger is not here and the barking has stopped. You decide to rest for a minute in one of the beds. You close your eyes and immediatle a tall figure starts touching your chest, you start to see how your still beating heart comes out of your chest as the dark creature smirks at you. You've died. Game over.")
  exit()
else:
  print("You've done nothing. A thick fog comes from the ground floor and fills the whole place. You suffocate to death. Game over.")
  exit()

print("Seems like Jagger knew all along what you came looking for. The both of you come out and Jagger leads you back to the beach, where a little boat has appeared. You hop in but Jagger decides to stay. There's no way you can make him stay inside the boat.")
choosed_option = input("What do you do? You can leave Jagger there and go back home (l) or get off the boat and stay with him for a while (g).")
if choosed_option == "l":
  print("You leave the island. You're happy as you're full of gold and will be able to have almost anything you want. Some hours pass by and you fall asleep. Jagger shows up in your dream, you're leaving the island as he barks... You wake up skipping a heartbeat. There's a storm, lightning falls and after a few strikes to the ocean it finally strikes you. You survive the shock but you fall into the ocean. The chest of gold is lost, but you see the shore nearby. The storm stops and you start swimming towards the shore. With each stroke you give, the farther the shore seems. A little light starts shining and moving under you, beneath the still waves. It dances and reaches your feet. At first it tickles, but then a burning sensation starts eating away your flesh by melting it. The pain is unbearable. As your body slowly melts away you start getting closer to the shore. You make it barely alive, coughing and almost drowning, but only to bleed to death on the shore. Game over.")
  exit()
elif choosed_option == "g":
  print("A strong wave hits the boat when you get off it and washes it away along with the chest full of god. You scream of anger at first but then Jagger catches your attention. He's just sitting there, it looks even as it smiles at you. You sit by his side and start petting him. A sweet sensation fills your heart as you start to get sleepy. You lay on the sand and both Jagger and you fall asleep, you still petting him tender.")
  sleep(3)
  print("...")
  sleep(3)
  print("You wake up. You're 12 again and you're just meeting Jagger for the first time. But... it's been ten years since that... how can that be? However it may have occurred, happines floods your heart and tears come out of your eyes; such tears start fogging your vision until everything becomes still and you fall asleep again.")
  sleep(3)
  print("...")
  sleep(3)
  print("You wake up yet again, you're in your bedroom, sleeping alone in your bed. You stretch and wonder if everything was just a dream. It maybe was... it's dawn of the day you went out to Treasure Island... But something's different. You remember Jagger. You remember he's no longer here. But he remembers you as well. It's no lie you followed him when you were on the island. You start to question your sanity... when something shines on one corner of your room. You get up to see what shines so bright. It's the chest full of gold! Where did it come from?! You haven't even... Well... why should it matter anymore?")
  print("The end. :)")
else:
  print("You can't decide. You freeze. A thick fog comes from the ocean and suffocates you to death. Game over.")
  exit()
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

