picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for image in picture: # for each list in picture
  print("start list")
  for pixel in image: # for each number in each list
    if (pixel): # 1 == True
      print('*', end ="") #by default, python add \n on end=""
    else:
      print(' ', end ="") #if pixel == 0(False), print blank
  print('')#break link, same thing as "\n"