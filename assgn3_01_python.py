print("Question 1 :  To count the number of words in a string or characters . \n")

input_str = input("Enter a string : ")
str = input_str.lower()
word_list = [x.strip() for x in str.split()]

num_words ={}
if len(word_list)==1:
    print("Since word length is 1 so checking for the number of same  characters :")
    for ch in word_list[0]:
        if ch not in num_words:
            num_words[ch]=1
        else:
            num_words[ch]+=1
else:
    print("Since word length is greater than 1 so checking for the number of same words :")
    for words in word_list:
        if words not in num_words:
            num_words[words]=1
        else:
            num_words[words]+=1

for word in num_words:
    print("{:<13}:{:<10}".format(word,num_words[word]))
