def even_number_of_evens(numbers):
    """
    Should rase a Typeerror if a list is not passed into the function
    error message: "A list was not passed into the function"
    if the numbers is empty return False
    if the number of even numbers is odd, return False
    if the number of even numbers is 0, return False
    if the numbers of even numbers is even, return True
    """  
    # if isinstance(numbers, list):
    #     if numbers == []:
    #         return False
    #     else:
    #         evens = 0
            
    #         """
    #         The for loop is checking to see if the numbers 
    #         passed into the function is divisible by 2. And
    #         if so the add 1 to the evens variable 
    #         """
    #         for n % 2 == 0:
    #             evens += 1

    #         if evens:
    #             # As this will be 0 it will always return True.
    #             # Despite the outcome intended to be False
    #             return evens % 2 == 0 
    #         else:
    #             return False
    # else: 
    #     raise TypeError("A list was not passed into the function")

     """
     REFACTORING THE CODE
     """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")

    


"""
When python runs a file it renames the file to main. And will 
only run that file. Meaning that the code below prevents the 
other file running the code block. To run the code, this file 
needs to be called __main__. Running this in the console will
allow this code to run
""" 

if __name__ == '__main__':     
    print(even_number_of_evens(5))
