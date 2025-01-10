import time

# Creating a large list of strings
words = ["word"] * 1000000


import time

# def generate_words(n):
#     for i in range(n):
#         yield "word"

# start_time = time.time()
# sentence_join = "".join(generate_words(1000000000))
# end_time = time.time()
# print(f"Using generator and join() took {end_time - start_time:.4f} seconds.")

# # Using +
# start_time = time.time()
# sentence_plus = ""
# for word in words:
#     sentence_plus += word
# end_time = time.time()
# print(f"Using + took {end_time - start_time:.4f} seconds.")

# Using join()
# start_time = time.time()
# sentence_join = "".join(words)
# end_time = time.time()
# print(f"Using join() took {end_time - start_time:.4f} seconds.")



import time
import numpy as np

# Number of repetitions
n = 10000

# Word to repeat
word = "word"

# Using NumPy
start_time = time.time()
# Create a NumPy array with the word repeated
arr = np.full(n, word, dtype='<U4')  # '<U4' for 4-character Unicode strings
# Concatenate using join
sentence = ''.join(arr)
end_time = time.time()
print(f"Using NumPy and join() took {end_time - start_time:.4f} seconds.")

sentence = "Python is awesome"
print(sentence.split())

tes= ['ewew', "ffs"]
print(tes[0:2])
