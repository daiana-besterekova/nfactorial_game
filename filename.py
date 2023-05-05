import pandas as pd 
# read the text file containing names
# IMPORTANT: Change the directory of the file below
data = pd.read_csv('/Users/daianabesterekova/Downloads/names.txt', sep=',')

def create_bigram(word):
    '''Returns a list of bigrams for a given word, including start and end symbols.
    
    Parameters:
    word (str): the word to create bigrams for
    
    Returns:
    list: a list of bigrams as strings
    '''
    
    # add start and end symbols to the word
    word = '^' + word + '$'
    
    # initialize a list to store the bigrams
    bigrams = []
    
    # iterate over the word and create bigrams
    for i in range(len(word)-1):
        bigram = word[i:i+2]
        bigrams.append(bigram)
    
    return bigrams

def create_all_bigrams(dataset):
    """
    Given a dataset containing names, this function creates all the bigrams of each name in the dataset.
    
    Args:
    - dataset: a pandas DataFrame containing a column named 'name' with the names to extract bigrams from.
    
    Returns:
    - a list containing all the bigrams from all the names in the dataset.
    """
    all_bigrams = []
    for i in range(len(dataset['name '])):
        all_bigrams = all_bigrams + create_bigram(dataset['name '][i])
    return all_bigrams

result = create_all_bigrams(data)


def create_dictionary(arr):
    """
    Takes a list of strings and returns a dictionary where the keys are unique bigrams and the values are their counts.
    
    Parameters:
    arr (list): A list of strings representing bigrams
    
    Returns:
    dictionary (dict): A dictionary where the keys are unique bigrams and the values are their counts
    """
    # Create an empty dictionary to store the bigrams and their counts
    dictionary = {}
    
    # Iterate over each element (bigram) in the input list
    for elem in arr:
        if elem not in dictionary:  # Check if the bigram is not already in the dictionary
            dictionary[elem] = 1   # If not, add it to the dictionary with a count of 1
        else:
            dictionary[elem] += 1  # If the bigram is already in the dictionary, increment its count
    
    # Return the resulting dictionary
    return dictionary

dictionary = create_dictionary(result)

def calculate_bigram_probabilities(dictionary):
    """
    Calculates the probability of each bigram in the given dictionary.

    Args:
        dictionary (dict): A dictionary with bigram keys and frequency count values.

    Returns:
        dict: A dictionary with bigram keys and their corresponding probabilities.
    """
    # count the total number of bigrams in the dictionary
    total_count = sum(dictionary.values())  
    
    # iterate over each bigram in the dictionary
    for bigram, count in dictionary.items():  
        
        # calculate the probability of the current bigram
        probability = count / total_count  
        
        # update the value of the current bigram key in the dictionary with its probability
        dictionary[bigram] = probability  
    return dictionary

import random

dictionary = calculate_bigram_probabilities(dictionary)

# create a list of keys from the dictionary that start with "^"
keys_starting_with_caret = [key for key in dictionary.keys() if key.startswith('^')]

# enter an integer value as input 
length = int(input('Enter desired name length for your baby: '))


import random
from prettytable import PrettyTable

def generate_name(dictionary, length):
    """
    Generate a name based on a given bigram dictionary and length.
    
    Args:
    - dictionary (dict): A dictionary of bigrams and their probabilities
    - length (int): The desired length of the name to be generated
    
    Returns:
    - A string containing the generated name
    """
    # Get list of bigrams that start with caret (^)
    keys_starting_with_caret = [key for key in dictionary.keys() if key.startswith('^')]
    # Get list of probabilities for bigrams starting with caret
    probs_starting_with_caret = [dictionary[key] for key in keys_starting_with_caret]
    # Choose a starting bigram at random based on the probabilities
    start = random.choices(keys_starting_with_caret, probs_starting_with_caret)[0]
    print(start)
    done = False 

    while done == False:
        table = PrettyTable()
        table.field_names = ["Key", "Value"]
        # Get dictionary of all bigrams starting with the last character of the current bigram
        nextt = {k: v for k, v in dictionary.items() if k[0] == start[-1]}
        # Sort the dictionary by probability in descending order
        sorted_items = sorted(nextt.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_items:
            # Add each bigram and its probability to the prettytable
            table.add_row([item[0], item[1]])
            # Choose the next bigram based on the most probable option
            next_key = sorted_items[0][0][-1]
        if next_key[-1] == '$' and len(start) < (length + 1):
            # If the last character of the next bigram is '$' and the desired length has not been reached yet,
            # choose the second most probable option for the next bigram to add to the name
            next_key = sorted_items[1][0][-1]
            start += next_key
        else: 
            start += next_key 
        if len(start) > length + 1: 
            done = True 
        print(table)
        print(start)
        

generate_name(dictionary, length)
