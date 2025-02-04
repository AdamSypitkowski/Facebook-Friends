#######################################################################################################################
#
#   Proj06 CSE 231
#       Intake a file with names of individuals
#           Intake file with 2 different types of friends for each person
#           Make a friends dictionary for each individual with 2 keys for the different friend groups
#           Preform different calculations with the nested dictionary:
#               Determining the maximum friends across platforms
#               Calculating the percent of individuals that do not share a friend between platforms
#               Printing an individuals friends on each platform
#               Calculating the percent of individuals that have more X friends compared to facebook
#               Determining friend triangles, a combination in which 3 people all are friends with each other
#                   Complete friend triangles for X friendships
#                   Complete friend triangles for facebook friendships
#                   Complete friend triangles for both X and facebook friendships combined
#           Continually prompt for more options, printing thank you at the end.
#
#######################################################################################################################

import csv
import sys


# def input( prompt=None ):
#     """
#         DO NOT MODIFY: Uncomment this function when submitting to Codio
#         or when using the run_file.py to test your code.
#         This function is needed for testing in Codio to echo the input to the output
#         Function to get user input from the standard input (stdin) with an optional prompt.
#         Args:
#             prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
#         Returns:
#             str: The user input received from stdin.
#     """
#
#     if prompt:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str


choices = '''
  Menu : 
     1: Max number of friends intersection between X and Facebook among all
     2: Percentage of people with no shared friends between X and Facebook
     3: Individual information
     4: Percentage of people with  more friends in X compared to Facebook
     5: The number of  triangle friendships in X
     6: The number of  triangle friendships on Facebook
     7: The number of  triangle friendships in X and Facebook together 
       Enter any other key(s) to exit

  '''

CHOICE_INPUT = "Input a choice ~:"

FILE_ERROR = "Error. File does not exist"
FILE_NAME = "\nEnter a names file ~:"
TWT_NAME = "\nEnter the X id file ~:"
FB_NAME = "\nEnter the facebook id file ~:"

ENTER_NAME = "Enter a person's name ~:"
INVALID_NAME = "Invalid name or does not exist"

THANK_YOU = "Thank you"


def open_file(file_str):
    '''
    check if the file is open-able, return a file pointer
    '''

    try:
        fp = open(file_str, 'r')
    except:
        print(FILE_ERROR)
    return fp


def make_dictionary(fp_csv, dictionary):
    '''
    makes a dictionary of all names in names file
    '''
    reader = csv.reader(fp_csv)
    name_lst = []

    # Goes through each name in csv file
    for line in reader:
        try:
            # If the name exists, add a 1 on the end of the string to make it unique
            test = dictionary[line[0]]
            dictionary[line[0] + '1'] = 0
            name_lst.append(line[0]+'1')
        except:
            # If new name, add to dictionary and name_lst
            dictionary[line[0]] = 0
            name_lst.append(line[0])
    return dictionary, name_lst


def make_friends(twt_fp, fb_fp, names_dct, names_lst):
    '''
    use the names_lst to determine which individual to add friends to
    split the line individuals to add to friend dictionary
    append friend dictionary to names dictionary
    '''

    for name in names_dct:
        friends = {}

        # Facebook reading individuals
        fb_line = fb_fp.readline()
        fb_lst = fb_line.strip().split(',')

        # Removes empty indexes
        for i in range(len(fb_lst)):
            if fb_lst[i] == "":
                del fb_lst[i]
        friends['fb'] = fb_lst

        # Twitter reading individuals
        twt_line = twt_fp.readline()
        twt_num_lst = twt_line.replace(',', ' ').strip().split()
        twt_lst = []

        # Gets the name at each index in the twitter list
        # Removes empty indexes
        for i in range(len(twt_num_lst)):
            twt_lst.append(names_lst[int(twt_num_lst[i])])
        friends['twt'] = twt_lst
        names_dct[name] = friends

    return names_dct


def friend_intersection(names_dct):
    '''
    checks if fb name matches twt name, adds 1. Prints the max number of friends
    '''
    most_friends = -1
    # Go through all names in dictionary
    for name in names_dct:
        common_friend = 0
        # Index all facebook friends
        for i in range(len(names_dct[name]['fb'])):
            # Index all twitter friends
            for j in range(len(names_dct[name]['twt'])):
                if names_dct[name]['fb'][i] == names_dct[name]['twt'][j]:
                    # when twitter friend == facebook friend
                    common_friend += 1
        if common_friend > most_friends:
            # Append if the number is greater
            most_friends = common_friend
    # Print statement
    print(f"The Max number intersection of friends between X and Facebook is: {most_friends:.0f}")
    return


def no_shared_friends(names_dct):
    '''
    determines number of names in dictionary that have no friends, returns % of that of the total
    '''
    total_people = 0
    unique_friends = 0

    # Go through dictionary
    for name in names_dct:
        total_people += 1
        shared_name = False
        for i in range(len(names_dct[name]['fb'])):
            for j in range(len(names_dct[name]['twt'])):
                if names_dct[name]['fb'][i] == names_dct[name]['twt'][j]:
                    # If the friend is the same, change value to true
                    shared_name = True
        if not shared_name:
            unique_friends += 1

    # Converts to percentage value
    percentage = (unique_friends / total_people) * 100
    print(f"{percentage:.0f}% of people have no friends in common on X and Facebook")
    return


def print_friends(friends):
    '''
    prompts for a name input and prints that persons friends. This happens for both the
    X and the facebook keys
    '''

    # Sorts alphabetically
    friends['twt'].sort()
    friends['fb'].sort()
    print("-" * 14 + "\nFriends in X\n" + "*" * 14)

    # Prints all twitter
    for i in range(len(friends['twt'])):
        print(friends['twt'][i])

    # Prints all facebook
    print("-" * 20 + "\nFriends in Facebook\n" + "*" * 20)
    for i in range(len(friends['fb'])):
        print(friends['fb'][i])
    return


def more_twt_friends(names_dct):
    '''
    checks the length of the twt and fb list in friends, adds 1 if twt is >
    returns a % of total
    '''

    total = len(names_dct)
    more_twt = 0
    for name in names_dct:
        # Compares the length of the lists at each key in the dictionary
        if len(names_dct[name]['twt']) > len(names_dct[name]['fb']):
            more_twt += 1

    # Converts to a percentage
    percentage = (more_twt / total) * 100
    print(f"{percentage:.0f}% of people have more friends in X compared to Facebook")


def triangle_friends_twt(names_dct):
    '''
    Takes the names in the twt key for each name in the main dictionary.
    That list of names is indexed to see if any of those names, have the original name
    as a twt friend. If that is true, it will compare the sets of the original name and
    the indexed name to determine if there is a match, the matching name is used as a key,
    and it is determined if original name and indexed name are in the twt friends.
    Then adds 1 to triangle. Triangle is returned.
    '''

    triangles = 0
    triangles_lst = []

    for name in names_dct:
        name_lst1 = names_dct[name]['twt']
        name_set1 = set(name_lst1)

        # Each twitter friend list
        for i in range(len(name_lst1)):
            name_set2 = set(names_dct[name_lst1[i]]['twt'])

            if name in name_set2:
                # Determines if there are any similar friends
                similarity = name_set1.intersection(name_set2)

                # Determines if that similar friend also has them as friends
                for item in similarity:
                    name_lst3 = names_dct[item]['twt']
                    if name in name_lst3 and name_lst1[i] in name_lst3:
                        test_triangle = [name, name_lst1[i], item]
                        test_triangle.sort()
                        # Tests if the triangle was already accounted for
                        if test_triangle not in triangles_lst:
                            triangles_lst.append(test_triangle)
                            triangles += 1

    return triangles


def triangle_friends_fb(names_dct):
    '''
    Takes the names in the fb key for each name in the main dictionary.
    That list of names is indexed to see if any of those names, have the original name
    as a fb friend. If that is true, it will compare the sets of the original name and
    the indexed name to determine if there is a match, the matching name is used as a key,
    and it is determined if original name and indexed name are in the fb friends.
    Then adds 1 to triangle. Triangle is returned.
    '''
    triangles = 0
    triangles_lst = []
    for name in names_dct:
        name_lst1 = names_dct[name]['fb']
        name_set1 = set(name_lst1)

        for i in range(len(name_lst1)):
            name_set2 = set(names_dct[name_lst1[i]]['fb'])

            if name in name_set2:
                # Determines similar friends
                similarity = name_set1.intersection(name_set2)
                for item in similarity:
                    # Finds if that similar friend has the two as a friend
                    name_lst3 = names_dct[item]['fb']
                    if name in name_lst3 and name_lst1[i] in name_lst3:
                        test_triangle = [name, name_lst1[i], item]
                        test_triangle.sort()
                        # Tests if the triangle was already accounted for
                        if test_triangle not in triangles_lst:
                            triangles_lst.append(test_triangle)
                            triangles += 1

    return triangles


def triangle_friends_total(names_dct):
    '''
    Takes the names in the combined fb and twt keys for each name in the main dictionary.
    That list of names is indexed to see if any of those names, have the original name
    as a friend in twt or fb. If that is true, it will compare the sets of the original name and
    the indexed name to determine if there is a match, the matching name is used as a key,
    and it is determined if original name and indexed name are in the combined friends.
    Then adds 1 to triangle. Triangle is returned.
    '''
    triangles = 0
    triangles_lst = []
    for name in names_dct:
        # Makes a combined list of twitter and fb
        name_lst1 = names_dct[name]['twt']
        name_lst1 += names_dct[name]['fb']
        name_set1 = set(name_lst1)

        for i in range(len(name_lst1)):
            # Makes a combined list of twitter and fb
            name_lst2 = names_dct[name_lst1[i]]['twt']
            name_lst2 += names_dct[name_lst1[i]]['fb']

            # Creates set
            name_set2 = set(name_lst2)

            if name in name_set2:
                # Determines any similar name
                similarity = name_set1.intersection(name_set2)
                for item in similarity:
                    name_lst3 = names_dct[item]['twt']
                    name_lst3 += names_dct[item]['fb']
                    name_set3 = set(name_lst3)

                    if name in name_set3 and name_lst1[i] in name_set3:
                        test_triangle = [name, name_lst1[i], item]
                        test_triangle.sort()
                        # Tests if the triangle was already accounted for
                        if test_triangle not in triangles_lst:
                            triangles_lst.append(test_triangle)
                            triangles += 1
                            print(triangles)

    return triangles

def main():

    while True:
        file_str = input(FILE_NAME)

        try:
            fp = open_file(file_str)
            break
        except:
            continue

    names_dct = {}
    names_dct, name_lst = make_dictionary(fp, names_dct)
    fp.close()

    while True:
        file_str = input(TWT_NAME)

        try:
            twt_fp = open_file(file_str)
            break
        except:
            continue

    while True:
        file_str = input(FB_NAME)

        try:
            fb_fp = open_file(file_str)
            break
        except:
            continue

    names_dct = make_friends(twt_fp, fb_fp, names_dct, name_lst)
    while True:
        print(choices)
        user_input = input(CHOICE_INPUT)

        if user_input == '1':
            friend_intersection(names_dct)

        elif user_input == '2':
            no_shared_friends(names_dct)

        elif user_input == '3':
            while True:
                person_name = input(ENTER_NAME)
                try:
                    friends = names_dct[person_name]
                    break
                except:
                    print(INVALID_NAME)
            print_friends(friends)

        elif user_input == '4':
            more_twt_friends(names_dct)

        elif user_input == '5':
            triangles = triangle_friends_twt(names_dct)
            print(f"The number of triangle friendships in X is: {triangles:.0f}")

        elif user_input == '6':
            triangles = triangle_friends_fb(names_dct)
            print(f"The number of triangle friendships in Facebook is: {triangles:.0f}")

        elif user_input == '7':
            triangles = triangle_friends_total(names_dct)
            print(f"The number of triangle friendships in X merged with Facebook is:  {triangles:.0f}")

        else:
            break

    print(THANK_YOU)
    return


if __name__ == '__main__':
    main()