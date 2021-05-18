# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# C.Hast,18.5.2041,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
#objFile = None   # An object that represents a file
#dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
#strChoice = ""  # Captures the user option selection
# Holds user-inputted instructions in the form of an integer or boolean
intChoice = int()
booChoice = bool()
strTask = ""  # Captures the user task data
#strPriority = ""  # Captures the user priority data
#strStatus = ""  # Captures the status of an processing functions
# Returned by some functions to indicate a specific part of the function completed
booStatus = bool()

# Replacing the dictionaries with instances of a class.
# It never made sense to use dictionaries here, and my half-assed solution
# in the last assignment wasn't really any better. But the point there was
# to use dictionaries, so I did. I like this a lot better.

class Record:
    """Contain a single entry, i.e. task and corresponding priority"""
    
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Perform Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Read data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (boolean) whether the given file was successfully read
        """
        # Shifted the clearing of data elsewhere, to allow the method
        # to be called in cases where clearing is not desired.
#        list_of_rows.clear()  # clear current data
        try:
            file_in = open(file_name, "r")
            for line in file_in:
                task, priority = line.split(",")
                list_of_rows.append(Record(task.strip(), priority.strip()))
            file_in.close()
            return True
        except FileNotFoundError:
            print()
            print('{} cannot be opened. If it does not exist, this is not a problem.'.format(file_name))
            print('If it does exist, then something odd has happened and the data in it has not been read.')
            print('In that case, it is recommended that you quit and do not save.')
            return False

    # The following two methods have been removed to improve the code.
    # I get separation of concerns and whatnot, but it is more natural
    # to put these in single functions along with the IO methods. Anybody
    # editing the code later and wanting to find the funtion that takes
    # in and stores user-inputted data is going to look in the
    # section dealing with user-inputted data. Splitting adding and
    # removing into two methods each doesn't make things more readable,
    # if anything it makes things less readable.
    #
    # The Processor class has therefore been limited to fully behind-
    # the-scenes processing. Direct user interface with data is
    # all moved to one place in the IO class.

#    @staticmethod
#    def add_data_to_list(task, priority, list_of_rows):
#        # TODO: Add Code Here!
#        return list_of_rows, 'Success'

#    @staticmethod
#    def remove_data_from_list(task, list_of_rows):
#        # TODO: Add Code Here!
#        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, task_list):
        """Write the list of tasks and priorities to a .txt file"""
        file_out = open(file_name, 'w')
        for line in task_list:
            file_out.write(line.task + ',' + line.priority + '\n')
        file_out.close()

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current tasks
        2) Add a new task
        3) Remove an existing task
        4) Save data to file        
        5) Reload data from file
        6) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Get the menu choice from a user

        :return: integer
        """
        while True:
            try:
                choice = int(input("Which option would you like to perform? [1 to 6] - ").strip())
                break
            except ValueError:
                print('Please enter a number from 1 to 6')
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Show the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        if list_of_rows == []:
            print('There currently are no tasks.')
            print()
        else:
            print("******* The current tasks to do are: *******")
            for row in list_of_rows:
                print(row.task + " (" + row.priority + " priority)")
            print("*******************************************")
            print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Get a yes or no choice from the user

        :return: boolean
        """
        choice = input(message).strip().lower()
        while True:
            if choice == 'yes' or choice == 'y':
                return True
            elif choice == 'no' or choice == 'n':
                return False
            else:
                print('Please enter yes or no')
                choice = input('> ').strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority(task_list):
        """Add a single task/priority pair entered by the user to the list"""
        print('What task would you like to add?')
        tmp_task = input('> ').strip()
        for line in task_list:
            if tmp_task == line.task:
                print('That task is already on the list.')
                print('Its priority is {}.'.format(line.priority))
                print('Do you want to change the priority of {}?'.format(line.task))
                print('Enter "1" to change the priority, or "2" to return to main menu')
                while True:
                    try:
                        choice = int(input('> ').strip())
                        if choice == 1:
                            print('What should the new priority of {} be?'.format(line.task))
                            tmp_priority = input('> ').strip()
                            line.priority = tmp_priority
                            print('The priority of {} is now {}'.format(tmp_task, tmp_priority))
                            break
                        elif choice == 2:
                            break
                        else:
                            print('Please enter 1 or 2')
                    except ValueError:
                        print('Please enter 1 or 2')
                break
        else:
            print('What should the priority of {} be?'.format(tmp_task))
            tmp_priority = input('> ').strip()
            task_list.append(Record(tmp_task, tmp_priority))
            print('Added "{}" to the task list with priority "{}"'.format(tmp_task, tmp_priority))

    @staticmethod
    def input_task_to_remove(task_list):
        """Remove a single task/priroity pair from the list"""
        print('Which task would you like to remove?')
        tmp_task = input('> ').strip()
        
        for line in task_list:
            if tmp_task == line.task:
                task_list.remove(line)
                return True, tmp_task
        else:
            return False, tmp_task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
#    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    intChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if intChoice == 1:
        IO.print_current_Tasks_in_list(lstTable)
    
    if intChoice == 2:  # Add a new Task
        IO.input_new_task_and_priority(lstTable)
        IO.input_press_to_continue()
        continue  # to show the menu

    elif intChoice == 3:  # Remove an existing Task
        booStatus, strTask = IO.input_task_to_remove(lstTable)
        if booStatus:
            IO.input_press_to_continue('Successfully removed "{}" from the task list'.format(strTask))
        else:
            IO.input_press_to_continue('"{}" was not found on the task list'.format(strTask))
        continue  # to show the menu

    elif intChoice == 4:   # Save Data to File
        booChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if booChoice == True:
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue('Task list saved')
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    # To address something I said in a comment earlier: clearing the list within
    # the method doesn't make sense. You can do so here. But also, it would be useful
    # to add a way for the user to enter the file name. If that is done, then you
    # can add a choice to load additional data from a different file. In which case
    # you *don't* want to clear the list. Better to put the clearing within a portion
    # of code *only* called if you are specifically wiping your current data and reloading de novo.
    elif intChoice == 5:  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        booChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if booChoice == True:
            lstTable.clear()
            # Not a fan of how I did this...
            if Processor.read_data_from_file(strFileName, lstTable) == True:
                IO.input_press_to_continue('Task list reloaded from file')
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif intChoice == 6:  #  Exit Program
        print("Goodbye!")
        break   # and Exit
