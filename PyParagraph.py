
with open("../../../../Desktop/UDEN201811DATA3/Week3/HW/ExtraContent/Instructions/PyParagraph/raw_data/paragraph_2.txt","r") as f:
    data = f.readlines()
    sum_word = []
    sum_letter = []
    for line in data:
        sum_word.append(len(line.split()))
        sum_letter.append(len("".join(line.split())))
    
    word_count = sum(sum_word)
    sentence_count = (len(sum_word)-1)/2
    letter_count_per_word = round(sum(sum_letter)/word_count,2)
    sentence_length_in_words = round(word_count/sentence_count,1)
    print("Paragraph Analysis")
    print("--------------------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Letter Count: {letter_count_per_word}")
    print(f"Average Sentence Length: {sentence_length_in_words}")



