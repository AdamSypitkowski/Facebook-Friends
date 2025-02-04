#######################################################################################################################
#
#   Proj06
#   Psuedocode
#
#   def function: open_file
#       '''
#       check if the file is open-able
#       '''
#
#       input: user string
#       try:
#       file pointer = open(input)
#       except:
#       print error message
#       return file pointer
#
#   def function: make_dictionary
#       '''
#       makes a dictionary of all names in names
#       '''
#
#       input (csv name file, name dictionary)
#       use the csv.reader(input)
#       for line in csv.reader:
#           combine each line (if necessary) to make full name
#           if name exists in dictionary:
#               continue
#           else:
#               append person to dictionary
#               append person to names_lst
#
#       return dictionary, names_lst
#
#   def function: facebook_friends
       '''
       use the names_lst to determine which individual to add friends to
       split the line individuals to add to friend dictionary
       append friend dictionary to names dictionary
       '''
#       input (file pointer fb_Friends, names dictionary, names_lst
#       i=0
#       for line in fp fb_Friends:
#           friend_lst = lst of individual names
#           friends['fb'] = friends_lst
#           dictionary[names_lst[i]] = friends['fb']
#           i += 1
#       return dictionary
#
#   def function: twt_friends
#       '''
#       Use names list to add names to the friends dictionary at each name in dictionary
#       '''
#       input(fp twt_Friends, names_dictionary, names_lst)
#
#       for line in twt_Friends:
#           function to get individual numbers
#
#           for i in range len names_lst:
#               if i = number:
#                   get name[i],
#                   append name[line] to dictionary of Friends['twt'] = name[i]
#
#       return names_dictionary
#
#   def function: friend_intersection
#       '''
#       checks if fb name matches twt name, adds 1. Prints the max
#       '''
#
#       input(names_dictionary)
#       max_friend = -1
#       for name in names_dictionary:
#           for i in range len(names_dictionary[name][fb]):
#               for j in range len(names_dictionary[name][twt]):
#                   if names_dictionary[name][fb][i] == names_dictionary[name][twt][j]:
#                       common_friend += 1
#           if common friend > max_friend:
#               assign common_friend to max_friend
#       print max_friend
#       return
#
#       def function: no_shared_friends
#           '''
#           determines number of names in dictionary that have no friends, returns %
#           '''
#           input(names_dictionary)
#           total_names = 0
#           common += 1
#           for name in names_dictionary:
#           total_names += 1
#               for i in range len(names_dictionary[name][fb]):
#                   for j in range len(names_dictionary[name][twt]):
#                       if names_dictionary[name][fb][i] == names_dictionary[name][twt][j]:
#                           name in common = True
#                   if name in common == True:
#                       common += 1
#                   name in common = False
#
#           uniqueness = (1 - (name in common / total_names)) * 100
#           return
#
#       def function: print_friends
#           '''
#           prompts for a name input and prints that persons friends
#           '''
#           input(names_dictionary)
#           name = False
#           while name == False:
#           user_string = prompt(input)
#               try:
#                   names_dictionary[user_string]
#                   name = True
#               except:
#                   print (invalid)
#
#           for i in range len (names_dictionary[user_string][twt]):
#               print names in twt list
#           for i in range len (names_dictionary[user_string][fb]):
#               print names in fb list
#           return
#
#
#       def function: more_twt_friends
#           '''
#           checks the length of the twt and fb list in friends, adds 1 if twt is >
#           returns a % of total
#           '''
#           input(names_dictionary)
#           total = 0
#           more twt = 0
#           for name in names_dictionary:
#               total += 1
#               if len of friends[twt] > len of friends[fb]:
#                   more twt += 1
#           print (more twt / total)
#           return
#
#       def function: twt_triangle_friendship
#           input(names_dictionary, names_lst)
#           for name in names_dictionary:
#               get twt_lst from name
#               for i in range len(twt_lst in dict):
#                   new_name = twt_lst[i]
#                   get twt_lst from new_name
#                   if twt_lst from new_name contains name:
#                       compare twt_lst from name and twt_lst from new_name for match
#                       if name matching name:
#                           get twt_lst from name_three
#                           check if name and new_name are in twt_lst name_three
#                           append name, new_name, name_three to tuple to store in triangle_friend_lst
#                           num of triangle friends += 1
#           return num of triangle friends
#
#
#       def function: fb_triangle_friendship
#           input(names_dictionary, names_lst)
#           for name in names_dictionary:
#               get fb_lst from name
#               for i in range len(fb_lst in dict):
#                   new_name = fb_lst[i]
#                   get fb_lst from new_name
#                   if fb_lst from new_name contains name:
#                       compare fb_lst from name and fb_lst from new_name for match
#                       if name matching name:
#                           get fb_lst from name_three
#                           check if name and new_name are in fb_lst name_three
#                           append name, new_name, name_three to tuple to store in triangle_friend_lst
#                           num of triangle friends += 1
#           return num of triangle friends
#
#       def function: combined_triangle_friendship
#           input(names_dictionary, names_lst)
#           for name in names_dictionary:
#               combined = combine twt_lst and fb_lst from name
#               for i in range len(combined):
#                   new_name = combined[i]
#                   get combined_lst from new_name
#                   if combined_lst from new_name contains name:
#                       compare combined_lst from name and combined_lst from new_name for match
#                       if name matching name:
#                           get combined_lst from name_three
#                           check if name and new_name are in combined_lst name_three
#                           append name, new_name, name_three to tuple to store in triangle_friend_lst
#                           num of triangle friends += 1
#           return num of triangle friends
#
#       def function: main
#           input()
#           names.csv_fp = open_file(names.csv)
#           dictionary, names_lst = make_dictionary(names_csv.fp)
#           fb_fp = open_file(facebook.txt)
#           twt_fp = open_file(twt.txt)
#           dictionary = fb_friends(dictionary, fb_fp, names_lst)
#           dictionary = twt_friends(dictionary, twt_fp, names_lst)
#
#           continue = True
#           while continue = True:
#               input number (1-7)
#               if number = 1:
#                   friend_intersection(dictionary)
#               elif number = 2:
#                   no_shared_friends(dictionary)
#               elif number = 3:
#                   input search_name
#                   print_friends(dictionary, search_name)
#               elif number = 4:
#                   more_twt_friends(dictionary)
#               elif number = 5:
#                   twt_triangle_friendship(dictionary, names_lst)
#               elif number = 6:
#                   fb_triangle_friendship(dictionary, names_lst)
#               elif number = 7:
#                   combined_triangle_friendship(dictionary, names_lst)
#               else:
#                   continue = False
#           print (Thank you)
#
#
#
#
#
#