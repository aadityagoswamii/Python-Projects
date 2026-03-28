def create_name(first,middle,last):
    first = first.capitalize()
    last = last.capitalize()
    middle = middle.capitalize()
    return (first + " " + middle + " " + last)

full_name = create_name("aaditya" , "sandip" , "goswami")
print(full_name)