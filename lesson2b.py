import math
import random


#Lesson 2: Assignments: Nested If

#Task 1:Code Correction

place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")

#Task 2:Setting the Scene
    
place = input("Choose a place: forest or cave?")
    
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You tripped over a big rock, hit your head and passed out")

#Task 3:Default Path
        
place = input("Choose a place: forest or cave?")
    
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You tripped over a big rock, hit your head and passed out")
elif place != "forest" or "cave":
    pass
else:
    print("Try again later.")

#Quick Decisions:The Event Planner

#Task :The Code Correction

attendees = int(input("Enter number of attendees: "))

print("large hall") if attendees > 100 else print("conference room")

#Task 2:Venue Selection

if attendees < 100:
    print("add a large TV, microphone and subwoofer to conference room") if attendees > 50 else print("add only a microphone and one speaker to the conference room")
else:
    print("add 4 large speakers, 1 projector, a microphone, and a subwoofer to large hall") if attendees > 200 else print("add only a microphone, a prjector, 2 speakers, and a subwoofer to the large hall.")

#Task 3:Catering Choices

food_choice = input("Are the attendees vegetarians?  Enter yes or no: ")
print("I recommend Veggie Delight Caterers") if food_choice == "yes" else print("I recommend Gourmet Meals Caterers")

#Silent Failures:The Error Handler

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

print("Will correct error later.")

#Task 2:Division Calculator

x = input("Enter a number: ")

try:
    sum = 15 / x
except:
    pass
print("Will correct error later.")

#Task 3:File Reader

try:
    init_file = open("testfile.txt", "r")
except:
    pass
print("File not located. ")

#Nested Quick Decisions:The Shopping Assistant

#Task 1:Code Correction

weather = input("Enter the weather:sunny, rainy, or cold: ")

print("sunglasses") if weather == "sunny" else print("umbrella") if weather == "rainy" else print("sweater")

#Task 2:Clothing Recommendation

print("sunglasses and sundress") if weather == "sunny" else print("umbrella and jumpsuit") if weather == "rainy" else print("sweater and blue jeans")

#Task 3:Accessory Recommendation

print("Add a wide-brimmed hat") if weather == "sunny" else print("Add rain boots") if weather == "rainy" else print("add a knit hat and scarf set")

#The Silent Logger:System Monitor

#Task 1:Code Corrector

cpu_usage = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

#Task 2:System Check

memory_usage = random.randint(0, 100)

if memory_usage > 90:
    output_stmt = "Memory usage is HIGH, at {}%!"
    print(output_stmt.format(memory_usage))
elif memory_usage > 80 and memory_usage <= 90:
    pass

disk_space = random.randint(0, 100)

if disk_space > 90:
    output_stmt = "Disk space used is {}%!"
    print(output_stmt.format(disk_space))
elif disk_space > 80 and disk_space <= 90:
    pass

#Task 3:Alert System

print("Running system check in background.  Will alert of CPU, memory, or disk space is nearly full.")

cpu_usage = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage! Close some applications to prevent early shutdown!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

memory_usage = random.randint(0, 100)

if memory_usage > 90:
    output_stmt = "Memory usage is HIGH, at {}%!  Taking precautions now are recommended!"
    print(output_stmt.format(memory_usage))
elif memory_usage > 80 and memory_usage <= 90:
    pass

disk_space = random.randint(0, 100)

if disk_space > 90:
    output_stmt = "Disk space used is {}%! Recommend disk clean-up!"
    print(output_stmt.format(disk_space))
elif disk_space > 80 and disk_space <= 90:
    pass

#print("System check complete.")