from random import choices


def fruit():
    fruits = ["apple", "cherry", "strawberry"]
    return choices(fruits)[0]

def meal(ingrediant):
   my_fruit = fruit()
   if my_fruit == "cherry":
      print(f"Your meal is fruit salad with {ingrediant} and {my_fruit}")
   else:
      print(f"Your meal is fruit salad with {ingrediant}")
# var = 1
# var = var
