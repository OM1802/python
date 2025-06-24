# ask user for their name
name=input("What is ur name? ")

name=name.strip().title()#remove whitespaces from string && capitalize users' name

#split name into first and last name
first, last= name.split(" ")

#say hello to the user
print(f"hello, {first}")
