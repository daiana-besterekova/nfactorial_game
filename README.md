# Language Bigram Game

## How to use? 

1. Ensure you have the necessary packages installed by running pip install pandas prettytable in your terminal.
2. Modify the directory path on line 4 to the location of your dataset file.
3. Run the code using python filename.py in your terminal.
4. Follow the prompt to enter the desired length of the name.
5. Wait for the program to generate and display the tables and bigrams.

## Limitations: 
The current implementation picks the bigram with the highest probability at each iteration, which may result in repeated bigrams dominating the generated name. To address this issue, it is suggested to randomize the selection of bigrams even after the first character is chosen, so that all bigrams have a chance of being selected. Another potential solution is to check if the selected substring (bigram) already exists in the generated name and choose the next bigram with the highest probability that does not lead to repetition.
