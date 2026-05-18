'''
PACKAGES  / DEBUGGING 
(1) python packages / core package 
(2) package manager / external package 
'''
from PIL import Image
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
t.circle(150)

turtle.done

print("=========")
my_life = open("material/message.txt", "r")
try:
    content = my_life.read()
    print("content:", content)
finally:
    my_life.close()

# WITH
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("done")

print("=== Package manager & External packages ===")
# Package manager for PYTHON: pip, pipenv
# Package manager for NODEJS: npm yarn

with Image.open("material/logo.jpg") as img_obj:
    resize = img_obj.resize((200, 200))
    resize.show()
    resize.save("material/result.jpg")
