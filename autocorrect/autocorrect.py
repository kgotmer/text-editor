# imports
import nltk
from nltk.metrics.distance  import edit_distance
from nltk.corpus import words


# necessary download
nltk.download('words')

# list of all correct words
correct_words = words.words()

# which ones are bad?
incorrect_words=['happpy', 'jyst', 'smaaaart']


# iterates through incorrect words and finds which spot in the word is wrong and displays the corrected words
for word in incorrect_words:
    temp = [(edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])