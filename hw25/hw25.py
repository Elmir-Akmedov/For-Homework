"""
#- Map -
#A. Create a function that takes a list of numbers and uses the map() function to 
#double each number in the list.

user_list = input(">> ").split()
modified_list = list(map(lambda x: int(x) * 2, user_list))
print(modified_list)

#B. Write a function that takes a list of temperatures in Celsius and uses map() 
#to convert them to Fahrenheit using the appropriate conversion formula.

user_list = input(">> ").split()
modified_list = list(map(lambda x: (int(x) * 1.8 + 32, user_list))
print(modified_list)

#C. Implement a function that takes a list of numbers and uses the map() function to 
#calculate the square root of each number.

user_list = input(">> ").split()
def square_root(x):
    num = int(x) * 0.5
    return num
modified_list = list(map(square_root, user_list))
print(modified_list)
"""
#D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".

def greet_names(names):
    if len(names) == 1:
        return f"Hello {names[0]}"
    else:
        formatted_names = ", ".join(names[:-1])
        return f"Hello {formatted_names}, and {names[-1]}"
names_list = input(">> ").split()
greeting = greet_names(names_list)
print(greeting)

#E. Create a function that takes a list of numbers and uses the map() function to generate a 
#power series for each number, up to a specified exponent.
#F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
#of the same index from both lists.
#G. Create a function that takes a list of floats and uses the map() function to round each float 
#to a specified number of decimal places.
#H. Write a function that takes a list of prices and uses map() to apply a discount percentage to each price.
#I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
#a simple encryption algorithm.
#J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.
#K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.
#
#- Filter -
#A. Create a function that takes a list of numbers and uses the filter() function to 
#return a new list containing only the even numbers.
#B. Write a function that takes a list of numbers and uses the filter() function to 
#return a new list containing only the prime numbers.
#C. Implement a function that filters a list of strings to return a new tuple containing 
#only the words that are palindromes.
#D. Given a list of dictionaries representing employees and their salaries, use filter() 
#to create a new list of employees whose salary is above a specified threshold.
#E. Write a function that takes a list of file names and filters it to return a new list 
#containing only files with a specified file extension.
#F. Create a function that takes a dictionary of student names and their corresponding grades, 
#and uses filter() to return a new dictionary containing only students who passed (grades above 
#a certain threshold).
#G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
#filters it to return separate lists for each data type.
#H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
#of numbers based on the user-provided condition.
#I. Write a function that takes a list of strings and filters it to return a new list containing 
#only strings that contain a specific substring.
#J. Implement a function that takes a list of strings and filters it to return a new list containing 
#strings with a specified character appearing a certain number of times.
#K. Create a function that takes a list of integers and uses the filter() function to return a 
#new list containing only those numbers for which a specified mathematical function (e.g., square, 
#cube) yields a prime result.
#L. Write a function that takes a list of date objects and filters it to return a new list containing 
#dates within a specified range.
#M. Given a list of cities and their corresponding countries, use filter() to return a new list 
#containing cities from a specific country.
#N. Create a function that takes a list of product objects and uses the filter() function to return a 
#new list containing only available products.
#O. Implement a function that takes a list and uses filter() to return a new list containing only 
#the unique elements.
#P. Write a function that takes a list of words and filters it to return a new list containing only 
#anagrams of a specified word.
#Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
#specified range.
#R. Create a function that takes a list of strings and uses filter() to return a new list containing 
#only strings that match a specific regular expression.
#
#- Reversed -
#A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
#order of elements in the list.
#B. Create a function that takes a string and uses reversed() to reverse the characters in the string.
#C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.
#D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.
#E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.
#F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list.
#G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.
#H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.
#I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
#indices, while keeping the elements at even indices unchanged.
#J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.
#K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.
#L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
#separated by a specific delimiter.
#
#- Sorted -
#A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
#the numbers sorted in ascending order.
#B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
#the numbers sorted in descending order.
#C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
#with the strings sorted by their lengths.
#D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
#the tuples sorted based on their second element.
#E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
#with its items sorted by their values.
#F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
#with the strings sorted in a case-insensitive manner.
#G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
#with the objects sorted based on a specified attribute.
#H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
#with the dates sorted in chronological order.
#I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
#the lists sorted based on the sum of their elements.
#J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
#the integers sorted based on the number of factors they have.
#K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
#the strings sorted based on their last characters.
#L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
#with the dictionaries sorted based on their keys.
#M. Sort the following list of strings alphabetically by the second letter:
#string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]
#
#Quiz.
#1. What is the purpose of the filter() function in Python?
#    A) To remove elements from an iterable based on a given condition
#    B) To sort elements in an iterable
#    C) To modify elements in an iterable
#    D) To combine elements in an iterable
#
#2. Which of the following data types can the filter() function be applied to?
#    A) Lists
#    B) Strings
#    C) Tuples
#    D) All of the above
#
#3. What does the filter() function return?
#    A) A new iterable containing filtered elements
#    B) The original iterable with filtered elements
#    C) A list of filtered elements
#    D) A tuple of filtered elements
#
#4. Which parameter does the filter() function take?
#    A) A filter function
#    B) An iterable
#    C) Both A and B
#    D) Neither A nor B
#
#5. In the context of the filter() function, what does the filter function do?
#    A) Defines the condition for filtering elements
#    B) Specifies the data type of the iterable
#    C) Sorts the iterable elements
#    D) Combines the iterable elements
#
#6. Which of the following statements is true about the filter() function?
#    A) The filter function can only return True or False
#    B) The filter function can return any data type
#    C) The filter function must return a boolean
#    D) The filter function is not required
#
#7. What is the syntax for using the filter() function in Python?
#    A) filter(condition, iterable)
#    B) filter(iterable, condition)
#    C) filter(function, iterable)
#    D) filter(iterable, function)
#
#8. When using the filter() function, what happens if the filter function returns False for an element?
#    A) The element is removed from the iterable
#    B) The element is included in the iterable
#    C) An error is raised
#    D) None of the above
#
#9. Can the filter() function be used to filter elements based on multiple conditions?
#    A) Yes
#    B) No
#
#10. In Python 3, what does the filter() function return by default?
#    A) A filter object
#    B) A list of filtered elements
#    C) A tuple of filtered elements
#    D) A set of filtered elements
#
#11. What is the purpose of the map() function in Python?
#    A) To apply a given function to each item in an iterable
#    B) To filter elements from an iterable based on a given condition
#    C) To sort elements in an iterable
#    D) To combine elements in an iterable
#
#12. Which of the following is an iterable that can be passed to the map() function?
#    A) Lists
#    B) Strings
#    C) Tuples
#    D) All of the above
#
#13. What does the map() function return?
#    A) A new iterable containing transformed elements
#    B) The original iterable with transformed elements
#    C) A list of transformed elements
#    D) A tuple of transformed elements
#
#14. What parameters does the map() function take?
#    A) A mapping function and an iterable
#    B) A single iterable
#    C) A single mapping function
#    D) A mapping function, followed by one or more iterables
#
#15. In the context of the map() function, what does the mapping function do?
#    A) Defines the transformation to be applied to each element
#    B) Specifies the data type of the iterable
#    C) Sorts the iterable elements
#    D) Combines the iterable elements
#
#16. Which of the following is true about the map() function?
#    A) The mapping function can return any data type
#    B) The mapping function must return a boolean
#    C) The mapping function is not required
#    D) The mapping function must return an integer
#
#17. What is the syntax for using the map() function in Python?
#    A) map(mapping_function, iterable)
#    B) map(iterable, mapping_function)
#    C) map(function, iterable)
#    D) map(iterable, function)    
#
#18. When using the map() function, what happens if the mapping function returns None for an element?
#    A) The element is removed from the iterable
#    B) The element remains unchanged in the iterable
#    C) An error is raised
#    D) None of the above
#
#19. Can the map() function be used to transform elements from multiple iterables?
#    A) Yes
#    B) No
#
#20. In Python 3, what does the map() function return by default?
#    A) A map object
#    B) A list of transformed elements
#    C) A tuple of transformed elements
#    D) A set of transformed elements
#
#21. What is the purpose of the reversed() function in Python?
#    A) To reverse the order of elements in an iterable
#    B) To sort elements in an iterable
#    C) To remove elements from an iterable
#    D) To concatenate elements in an iterable
#
#22. Which of the following is an iterable that can be passed to the reversed() function?
#    A) Lists
#    B) Strings
#    C) Tuples
#    D) All of the above
#
#23. What does the reversed() function return?
#    A) A new iterable containing reversed elements
#    B) The original iterable with reversed elements
#    C) A list of reversed elements
#    D) A tuple of reversed elements
#
#24. What parameter does the reversed() function take?
#    A) An iterable
#    B) A single element
#    C) A number
#    D) A mapping function
#
#25. In the context of the reversed() function, what does "reversed elements" mean?
#    A) The elements are in the opposite order
#    B) The elements are sorted in ascending order
#    C) The elements are concatenated
#    D) The elements are multiplied
#
#26. Which of the following is true about the reversed() function?
#    A) The reversed elements are returned as a list
#    B) The reversed elements are returned as a tuple
#    C) The reversed elements are returned as an iterator
#    D) The reversed elements are returned as a set
#
#27. What is the syntax for using the reversed() function in Python?
#    A) reversed(iterable)
#    B) iterable.reversed()
#    C) reversed(function, iterable)
#    D) reversed(iterable, function)
#
#28. When using the reversed() function, can it be applied to strings?
#    A) Yes
#    B) No
#
#29. Can the reversed() function be used to reverse a dictionary?
#    A) Yes
#    B) No
#
#30. In Python 3, what does the reversed() function return by default?
#    A) A reversed object
#    B) A list of reversed elements
#    C) A tuple of reversed elements
#    D) A set of reversed elements
#
#31. What is the purpose of the sorted() function in Python?
#    A) To sort elements in an iterable and return a sorted list
#    B) To reverse the order of elements in an iterable
#    C) To remove elements from an iterable
#    D) To concatenate elements in an iterable
#
#32. Which of the following is an iterable that can be passed to the sorted() function?
#    A) Lists
#    B) Strings
#    C) Tuples
#    D) All of the above
#    
#33. What does the sorted() function return?
#    A) A new iterable containing sorted elements
#    B) The original iterable with sorted elements
#    C) A list of sorted elements
#    D) A tuple of sorted elements
#
#34. What parameters does the sorted() function take?
#    A) An iterable
#    B) A single element
#    C) A mapping function
#    D) A mapping function and an iterable
#
#35. In the context of the sorted() function, what does "sorted elements" mean?
#    A) The elements are arranged in ascending order
#    B) The elements are arranged in descending order
#    C) The elements are multiplied
#    D) The elements are concatenated
#
#36. Which of the following is true about the sorted() function?
#    A) The sorted elements are returned as a tuple
#    B) The sorted elements are returned as a set
#    C) The sorted elements are returned as an iterator
#    D) The sorted elements are returned as a list
#
#37. What is the syntax for using the sorted() function in Python?
#    A) sorted(iterable)
#    B) iterable.sorted()
#    C) sorted(function, iterable)
#    D) sorted(iterable, function)
#
#38. When using the sorted() function, can you specify a custom sorting order?
#    A) Yes, by providing a custom sorting function
#    B) No, the sorting order is always ascending
#    C) Yes, by providing a reverse parameter
#    D) No, the sorting order is always descending
#
#39. Can the sorted() function be used to sort a dictionary based on its keys or values?
#    A) Yes
#    B) No
#
#40. In Python 3, what does the sorted() function return by default?
#    A) A list of sorted elements
#    B) A sorted object
#    C) A tuple of sorted elements
#    D) A set of sorted elements
#"""