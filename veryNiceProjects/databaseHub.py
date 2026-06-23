from os import remove
div = "--------------------------------"
done = "no"
open_file = "n"   

while done == "no":
    while open_file == "n":
        print(div)
        do = input("What do you want to do? Open a database (o), create a new one (c), remove a database (q), or exit (e) ").lower().strip()
        print(div)
        if do == "o":
            o_what = input("What is the file name? ").strip()
            file_name = o_what + ".txt"
            try:
                file = open(file_name, "r+")
            except FileNotFoundError:
                print("I am sorry for your inconvenience but no such file is found. :(")
            else:
                print(f"Opened {file_name}...")
                file.close()
                file = open(file_name, "a+")
                open_file = "y"
        elif do == "c":
            name = input("What should be the database's name? ").strip()
            file_name = name + ".txt"
            try:
                file = open(file_name, "x")
            except FileExistsError:
                print("The file already exists.")
            else:
                print(f"{file_name} created and opened...")
                file.close()
                file = open(file_name, "a+")
                open_file = "y"
        elif do == "q":
            del_name = input("What is the file name? ")
            del_file = del_name + ".txt"
            try:
                sureness = input("Are you sure? (y/n) ").lower().strip()
                if sureness == "y":
                    remove(del_file)
                    print(f"{del_file} is dead forever!")
                elif sureness == "n":
                    print("Cool, not deleting.")
                else:
                    print("That is not an option. Not deleting anything.")
            except FileNotFoundError:
                print("I am sorry for your inconvenience but no such file is found. :(")
        elif do == "e":
            exit("Goodbye!")
        else:
            print("That is not an option")

    print(div)
    do_file = input(f"""
                    
What do you want to do with {file_name}?
                    
Create an entry (c)
Read your entries (r)
Update an entry (u)
Delete an entry (d)
Exit database (e)


""").lower().strip()
    if do_file == "c":
        write = input("What do you want to add? ")
        file.write(write + "\n")
        file.close()
        file = open(file_name, "a+")
    elif do_file == "r":
        file.close()
        file = open(file_name, "r")
        read_ls = []
        readl = file.readlines()
        for i in readl:
            new_w = i[0:-1]
            read_ls.append(new_w)
        print(read_ls)
        file.close()
        file = open(file_name, "a+")
    elif do_file == "u":
        while True:
            try:
                u_line = int(input("What line do you want to update? "))
            except:
                print("Please enter a number")
            else:
                u_line -= 1 #important
                break
        file.close()
        file = open(file_name, "r")
        updated_ls = file.readlines()
        updated = input("What do you want to update it to: ")
        updated_ls[u_line] = updated + "\n"
        file.close()
        file = open(file_name, "w")
        file.writelines(updated_ls)
        file.close()
        file = open(file_name, "a+")
    elif do_file == "d":
        while True:
            try:
                d_line = int(input("What line do you want to delete? "))
            except:
                print("Please enter a number")
            else:
                break
        while True:
            decision = input("Are you sure? (y/n) ").lower().strip()
            if decision == "y":
                d_line -= 1 #important
                file.close()
                file = open(file_name, "r")
                old_ls = file.readlines()
                new_ls = []
                line = 0
                for entry in old_ls:
                    if entry != old_ls[d_line] or line != d_line:
                        new_ls.append(entry)
                    line += 1
                file.close()
                file = open(file_name, "w")
                file.writelines(new_ls)
                file.close()
                file = open(file_name, "a+")
                break
            elif decision == "n":
                print("Okay, not deleting")
                break
            else:
                print("I'm sorry but that is an invalid option.")
    elif do_file == "e":
        open_file = "n"
    else:
        print("I'm sorry but that is an invalid option.")
        
        