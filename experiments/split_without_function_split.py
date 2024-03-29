print("Example 3: ")


sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
split_sentence = sentence.split("HELLO")
print(split_sentence)

#input: character string "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
#output: ['This', 'is', 'random', 'text', 'we', 'are', 'going', 'to', 'split', 'apart']

#1. Take n element of the string
#2. Move n element of the string to var. word_buffer
#3. Cmp word_buffer with "HELLO" and cmp "len(word_buffer)" <= 4 (we are counting from 0) 
#4 if "fasle" n+1 element of the string to "word_buffer" go to 3.
#5 else, if word_buffer == "HELLO", 
#   -set word_buffer empty, 
#   -slice_sentence = sentence[0:index], 
#   -sentence = sentence[index::], 
#   -n = 0
#   -go to 2.

index=0
word_buffer = new_sentence = ""

while index < len(sentence):
    
        if word_buffer != "HELLO" and len(word_buffer) <= 4:
            word_buffer = word_buffer + sentence[index]
            index += 1
        elif word_buffer == "HELLO":
            
            word_buffer = ""
            sentence_slice = sentence[0:index]
            new_sentence = new_sentence + sentence_slice[0:index - len("HELLO")] + " "
            sentence = sentence[index::]
            index = 0
             
        else:
             word_buffer = ""
             index -= 4
new_sentence = new_sentence + word_buffer        
print(new_sentence)    

