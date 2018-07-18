print("Congratulations! You're running Maddi's Task List Program.")



class Tasklist():
        def __init__(self, arrayOfTasks):
            self.arrayOfTasks = arrayOfTasks

def main():

    arrayOfTasks = ["learn", "practice", "teach"]

    userRequest = input("What would you like to do next?"
                    "1.List all tasks. "
                    "2.Add a task to the list. "
                    "3.Delete a task. "
                    "Type q to quit the program.")

    while userRequest != 'q':

        if userRequest == "1":
            print(arrayOfTasks)

        elif userRequest == "2":
            addedTask = input("Add a task")
            arrayOfTasks.append(addedTask)

        elif userRequest == "3":
            deleteTask = input("Delete a task")
            arrayOfTasks.remove(deleteTask)

        userRequest = input("What would you like to do next?"
                            "1.List all tasks. "
                            "2.Add a task to the list. "
                            "3.Delete a task. "
                            "Type q to quit the program.")




main()