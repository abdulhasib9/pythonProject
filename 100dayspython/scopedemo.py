enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# def mainfunction():
#    def main2():
#     print("inner main function")
    
# mainfunction.main2()

