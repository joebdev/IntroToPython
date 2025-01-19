# 1. If you have a list named people, how can you determine the number of entries in that list?
# len(people) 

# 2. Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
stuff = ('hello', 'world', 'bye', 'now')
new_stuff = list(stuff)
new_stuff[2] = 'goodbye'
new_stuff = tuple(new_stuff)
print(new_stuff)

# 3. Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.
    # Differences - 
        # Lists use [], Sets use ()
        # Lists are mutable
    # Similarities
        # They're both collections
        # They're both heterogeneous (elements can be different types)

# 4. Why can we treat strings as sequences?
    # When accessing specific characters in strings, you are able to access them in the same way you would for
    # other sequences, str[0], str[1], etc. 

# 5. How do the set types differ from the sequence types?
    # Sets don't allow for unique values
    # Sets are unordered

# 6. Assume you have the following assignment:
    # Write some code that converts the value of pi to a string and assigns it to a variable named str_pi
pi = 3.141592
str_pi = str(pi)

# 7. Without running the following code, identify the numbers that are included in each of the following ranges:
range(7) # 0, 1, 2, 3, 4, 5, 6
range(1, 6) # 1, 2, 3, 4, 5
range(3, 15, 4) # 3, 7, 11
range(3, 8, -1) # this would be empty
range(8, 3, -1) # 8, 7, 6, 5, 4

# 8. How would you print all the numbers in the following range?
range(3, 17, 4)
print(list(range(3, 17, 4)))

# 9. Given the above code, answer the following questions and explain your answers:
    # Are the lists assigned to my_list and another_list equal? 
        # yes they are equal, they both contain the same values
    # Are the lists assigned to my_list and another_list the same object?
        # no, they are not the same object, they are both referring to different places in memory
    # Are the nested lists at index 3 of my_list and another_list equal?
        # yes, they both contain the same values
    # Are the nexted lists at index 3 of my_list and another_list the same object?
        # yes, it is a shallow copy, which doesn't create new nested lists

my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# 10. Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.
names = {'Chris', 'Claire', 'Karis', 'Karl', 'Max', 'Nick', 'Victor'}
print(names)

# They cannot be in guaranteed alphabetical order, because with sets, the order is random. 

# 11. Consider the data in the following table:
    # Name	Country
    # Alice	USA
    # Francois	Canada
    # Inti	Peru
    # Monika	Germany
    # Sanyu	Uganda
    # Yoshitaka	Japan
# You need to write some Python code to determine the country name associated with one of the list names. Your code should include the data structure(s) you need and at least one test case
# to ensure the code works. 

country_info = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan'
}

print(country_info['Alice'])
