import subprocess
import time

canvas = [
  "\r\n",
  "           .-------.\r\n",
  "          /.\:::::/.\\\r\n",
  "        .'.' |_O_| `.`.\r\n",
  "       =================\r\n",
  "         []. \"\"\"\"\" .[]\r\n",
  "            \[|||]/\r\n",
  "             \"---\"\r\n",              
  "\r\n",
  "\r\n",
  "\r\n",
  "     _______________________\r\n",
  "    /                       \\\r\n",
  "   /    ...............      \\\r\n",
  "  /    `:::::::::::::::`      \\\r\n",
  " /_____________________________\\\r\n",
  " |______________________________| \r\n",
  "\r\n",
  "\r\n"
]

canvas_landed = [
  "\r\n",
  "\r\n",
  "\r\n",
  "\r\n",
  "\r\n",
  "\r\n",
  "           .-------.\r\n",
  "          /.\:::::/.\\\r\n",
  "        .'.' |_O_| `.`.\r\n",
  "       =================\r\n",
  "     __/ []. \"\"\"\"\" .[] \____\r\n",
  "    / / / < \[|||]/ > \ \   \\\r\n",
  "   /  \ `    \"---\"    ' /    \\\r\n", 
  "  /    `:::::::::::::::'      \\\r\n", 
  " /_____________________________\\\r\n",
  " |_____________________________| \r\n",
  "\r\n",
  "\r\n"
]

top_position = 1

ship_height = 7
ship = canvas[top_position:ship_height + top_position]

travel = 8

_ = subprocess.call("clear", shell=True) # On Windows change `clever` to `cls`

print(*canvas)
input("Press enter to land")

for i in range(travel):
  if i == 0:
    continue

  time.sleep(0.5) # Wait for 500 milliseconds
  _ = subprocess.call("clear", shell=True) # On Windows change `clever` to `cls`

  scene = [
    "\r\n" for x in range(i)
  ]
  scene.extend(ship)
  scene.extend(canvas[i + ship_height:len(canvas) - 1])

  print(*scene)
  print("Landing in process!")

time.sleep(0.5) # Wait for 500 milliseconds
_ = subprocess.call("clear", shell=True) # On Windows change `clever` to `cls`

print(*canvas_landed)
print("We are landed! Dev is FUN!")
print()
