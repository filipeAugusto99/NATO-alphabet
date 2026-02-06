# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas

data_letters = pandas.read_csv("nato_phonetic_alphabet.csv")

data_frame_letters = pandas.DataFrame(data_letters)

dict_letters = {row.letter:row.code for (index, row) in data_frame_letters.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Enter a word: ").upper()

nato_words = [dict_letters[word] for word in input_word]

# nato_words = []
# for word in input_word:
#     nato_words.append(dict_letters[word])



print(nato_words)