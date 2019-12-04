def con():
  binary = input()
  if binary == '0':
      exit();
  else:
      temp = int(binary, 2)
      w=hex(temp)[2::]
      print(w)
con()
