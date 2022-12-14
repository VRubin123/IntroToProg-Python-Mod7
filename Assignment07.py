# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate how pickling and structured
#               error handling work in Python programming
# ChangeLog (Who,When,What):
# VRubin,11.29.22,Created started script
#
# ---------------------------------------------------------------------------- #
#!/bin/bash

# Need to import the pickle function

import pickle

file_name_str = "SantasList"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name):
        file = open(file_name, "rb")
        list_of_rows = pickle.load(file)
        file.close()
        return list_of_rows

    @staticmethod
    def save_data_to_pickle_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :Dump: (list) of binary rows
        """

        file = open(file_name, "wb")
        pickle.dump(list_of_rows, file)
        file.close()
        return list_of_rows

    @staticmethod
    def add_name_to_list(name, status, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param name: (string) with name of child:
        :param status: (string) with naughty or nice status:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        # TODO: Add Code Here!
        row = {"Name": str(name).strip(), "Status": str(status).strip()}
        list_of_rows.append(row)
        return list_of_rows

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Name
        2) Save Data to File
        3) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_names_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current names are: *******")
        print(Processor.read_data_from_file(file_name_str))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_name_and_status():
        """  Gets name and status values to be added to the list

        :return: (string, string) with name and status
        """
        pass  # TODO: Add Code Here!
        try:
            name = input("Please input name:")
            status = input("Please assign status of person (Naughty or Nice):")
            if name.isdigit() == True:
                raise Exception("Do not use number for name")
                return name
            elif status.isdigit() == True:
                raise Exception("Do not use number for status")
                return status
            else:
                return name, status
        except Exception as e:
            print("There was a non-specific error!")
            print("Built=In Python error info:")
            print(e, e.__doc__, type(e), sep='\n')
        return name, status
# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from SantasList.
Processor.read_data_from_file(file_name=file_name_str) # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_names_in_list(list_of_rows = table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Name
        name, status = IO.input_new_name_and_status()
        table_lst = Processor.add_name_to_list(name=name, status=status, list_of_rows = table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Save Data to pickle File
        table_lst = Processor.save_data_to_pickle_file(file_name=file_name_str, list_of_rows = table_lst)
        print("Data Saved Santa! Way to go.")
        continue  # to show the menu

    elif choice_str == '3':  # Exit Program
        print("Toodles!")
        break  # by exiting loop