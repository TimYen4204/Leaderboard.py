from tabulate import tabulate
from config import filepath

my_dict = {}

def add_score(name, score):
    # check if not exist
    if name not in my_dict:
        my_dict.update({name: score})

def update_score(name, score):
    # update if name in
    if name in my_dict:
        my_dict.update({name: score})
    else:
        print("Name not valid!")

def get_top(n):
    # sort items in dict
    my_dict.items().sorted()
    # return top: find max in key
    return max(my_dict, key=my_dict.get)

def save_to_file(filepath, my_dict):
    # open file path with "w" for writing
    with open(filepath, "w") as file:
        # for key value pairs in the dict, (in)file.write(key val pairs)
        for key, value in my_dict.items():
            file.write(f"{key}: {value}\n")


def load_from_file(filepath):
    # make new dict
    new_dict = {}
    with open(filepath, "r") as file:
        # for each line in file
        for line in file:
            # get key val pair
                # strip whitespace
                    # split at ": "
            key, value = line.strip().split(": ")
            # at key, insert val
            my_dict[key] = int(value)
        # write new dict n return
    return my_dict

def delete_score(name):
    if name in my_dict:
        del my_dict[name]
    else:
        print("User doesn't exist.")

def main():
    # gloabl access dict
    global my_dict
    
    while True:
        print(" -------------------------------------------------------------------------\n| Options: Add | Update | View (Top) | Show | Save | Load | Delete | Quit |")
        print(" -------------------------------------------------------------------------")
        choice = input("Enter your choise: ").strip().lower()
    
    # match set switch case
        match choice:
            case "add":
                try:
                    print("\n")
                    name = input("Input name: ")
                    score = int(input("Input score:"))
                    add_score(name, score)
                    print("\n")
                except:
                    print("\n")
                    print("Invalid input.")
                    print("\n")

            case "update":
                try:
                    print("\n")
                    name = input("Update name: ")
                    score = int(input("Update score: "))
                    update_score(name, score)
                    print("\n")
                except:
                    print("\n")
                    print("Invalid input.")
                    print("\n")

            case "view":
                print("\n")
                if my_dict:
                    n = int(input("Peek Top (How many?): "))
                    # sort array
                        #   lmba function:
                        #       sort by score (item[1] is the score in "name: score")
                        #       reverse the array (smallest to largest => largest to smallest)
                    sorted_scores = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
                    for name, score in sorted_scores[:n]:
                        print(f"{name}: {score}")
                    print("\n")
                
                else:
                    print("\n")
                    print("Leaderboard is empty.")
                    print("\n")
            
            case "show":
                print("\n")
                #   print "name: score" in the sorted array- reversed
                sorted_scores = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
                table = [(name, score) for name, score in sorted_scores]
                print(tabulate(table, headers=["Name", "Score"], tablefmt="fancy_grid"))
                print("\n")

            case "save":
                print("\n")
                save_to_file(filepath, my_dict)
                print("Saved")
                print("\n")
            
            case "load":
                print("\n")
                my_dict = load_from_file(filepath)
                print("Loaded")
                print("\n")
            
            case "delete":
                try:
                    print("\n")
                    name = input("Input name: ")
                    print("Are you sure? (y/n) ")
                    op = input("")
                    if op == 'y':
                        delete_score(name)

                except:
                    print("\n")
                    print("Invalid input.")
                    print("\n")

            case "quit":
                print("\n")
                leave = input("Are you sure you want to quit? (y/n) ")
                if leave.lower() == "y":
                    break
                print("\n")
            
            case _:
                print("\n")
                print("Invalid option.")
                print("\n")

if __name__ == "__main__":
    # light work, no reaction
    main()
    print("Program exited.")