# importing the module
import sys
import csv
import os
import math
import time


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, phoneBook, check):
        # print("Add func", phoneBook)
        # print("Check = ", check)
        dip = []
        for i in range(5):
            if i == 0:
                if check == 1:
                    dip.append(phoneBook[0])
                    # print("Name ", phoneBook[0])
                else:
                    dip.append(str(input("Enter name: ")))
            if i == 1:
                if check == 1:
                    dip.append(phoneBook[1])
                    # print("Number ", phoneBook[1])
                else:
                    dip.append(str(input("Enter number: ")))
            if i == 2:
                if check == 1:
                    dip.append(phoneBook[2])
                    # print("Email ", phoneBook[2])
                else:
                    dip.append(str(input("Enter e-mail address: ")))
            if i == 3:
                if check == 1:
                    dip.append(phoneBook[3])
                    # print("DOB ", phoneBook[3])
                else:
                    dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
            if i == 4:
                if check == 1:
                    dip.append(phoneBook[4])
                    # print("Category ", phoneBook[4])
                else:
                    dip.append(str(input("Enter category(Family/Friends/Work/Others): ")))

        if self.root is None:
            #self.root = Node(val)
            self.root = Node(dip[0])
            # print("root")
            if check != 1:
                phoneBook.append(dip)
            return phoneBook
        else:
            self._add(dip[0], self.root, dip, check)
            # print(self.root)
            return phoneBook

    def _add(self, val, node, dip, check):
        # print("Val", val)
        if val.lower() < str(node.v).lower():
            if node.l is not None:
                self._add(val, node.l, dip, check)
            else:
                node.l = Node(val)
                node.l.p = node
                if check != 1:
                    pb.append(dip)
                # print("Left ", pb)
                # print('add', val, 'parent is ', node.l.p.v)
        else:
            if node.r is not None:
                self._add(val, node.r, dip, check)
            else:
                node.r = Node(val)
                node.r.p = node
                if check != 1:
                    pb.append(dip)
                # print('add', val, 'parent is ', node.r.p.v)

    def find(self):
        name = str(input("Enter name that you want to search: ")).lower()
        if self.root is not None:
            time_start = time.time_ns()
            return self._find(name, self.root, time_start)
        else:
            return print("Invalid search criteria")

    def _find(self, val, node, time_start):
        if val < node.v and node.l is not None:
            return self._find(val, node.l, time_start)
        elif val > node.v and node.r is not None:
            return self._find(val, node.r, time_start)
        else:
            # print("val ", val)
            for i in range(len(pb)):
                if val == pb[i][0].lower():
                    # print("val2 ", val)
                    # print("PB ", pb[i][0].lower())
                    info = "Number: " + pb[i][1] + ", Email: " + pb[i][2] + ", DOB: " + pb[i][3] + ", Category: " + pb[i][4]
                    time_end = time.time_ns()
                    print("End", time_end)
                    print("Start ", time_start)
                    time_spent = time_end-time_start
                    return print(val + " -> " + info + "\n" + "Time Usage: ", time_spent)


    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v), ":")
            for i in range(len(pb)):
                if str(node.v) == pb[i][0]:
                    print("Number:", pb[i][1], ", Email:", pb[i][2], ", DOB:", pb[i][3], ", Category:", pb[i][4])
            self._printTree(node.r)


# this function will be the first to run as soon as the main function executes
def initial_phonebook():
    phone_book = []
    header = True
    #### To check wheter the contact book already existed or not
    if os.path.exists('ContactList_BST.csv'):
        # phone_book = pd.read_csv('ContactList.csv', header=None, index_col=0, squeeze=True).to_dict()
        with open('ContactList_BST.csv', 'r') as csvfile:
            csvReader = csv.reader(csvfile)
            next(csvReader)
            for row in csvReader:
                phone_book.append(row)
    # print(phone_book)
    return phone_book


def menu():
    # We created this simple menu function for
    # code reusability & also for an interactive console
    # Menu func will only execute when called
    print("********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Remove an existing contact")
    print("4. Delete all contacts")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    # Out of the provided 6 choices, user needs to enter any 1 choice among the 6
    # We return the entered choice to the calling function wiz main in our case
    choice = int(input("Please enter your choice: "))
    return choice


def remove_existing(pb):
    # This function is to remove a contact's details from existing phonebook
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    # We'll collect name of the contact and search if it exists in our phonebook

    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp.

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope

            print(pb.pop(i))
            # The pop function removes entry at index i

            print("This query has now been removed")
            # printing a confirmation message after removal.
            # This ensures that removal was successful.
            # After removal we will return the modified phonebook to the calling function
            # which is main in our program

            return pb
    if temp == 0:
        # Now if at all any case matches temp should've incremented but if otherwise,
        # temp will remain 0 and that means the query does not exist in this phonebook
        print("Sorry, you have entered an invalid query. Please recheck and try again later.")
        return pb


def delete_all(pb):
    # This function will simply delete all the entries in the phonebook pb
    # It will return an empty phonebook after clearing
    return pb.clear()


def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("********************************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


def writeCSV(pb):
    # header = set(i for b in map(dict.keys, pb.values()) for i in b)
    if not pb:
        if os.path.exists("ContactList_BST.csv"):
            os.remove("ContactList_BST.csv")
    else:
        header = ['Name', 'Phone', 'Email', 'DOB', 'Category']
        # with open("ContactList.csv", "w", newline="") as f:
        with open("ContactList_BST.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(pb)


# Main function code
print("....................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("....................................................................")
# This is solely meant for decoration purpose only.
# You're free to modify your interface as per your will to make it look interactive

ch = 1
tree = Tree()
pb = initial_phonebook()
# print("Existing contact in phonebook -> ", pb)
for i in range(len(pb)):
    # print(pb[i])
    tree.add(pb[i], 1)

while ch in (1, 2, 3, 4, 5, 6):
    ch = menu()
    if ch == 1:
        pb = tree.add(pb, 2)
    elif ch == 2:
        tree.find()
    elif ch == 3:
        pb = remove_existing(pb)
    elif ch == 4:
        pb = delete_all(pb)
    elif ch == 5:
        tree.printTree()
    elif ch == 6:
        writeCSV(pb)
        thanks()
    else:
        ch = menu()