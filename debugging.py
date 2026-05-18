'''
PACKAGES  / DEBUGGING 
(1) python packages / core package 
(2) package manager / external package 
'''
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
