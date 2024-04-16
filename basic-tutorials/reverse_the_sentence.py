
def reverse_the_sentence(sentence):
    split_array = sentence.split()
    reversed_sentence = ""
    for i in range(len(split_array)-1,-1,-1):
        reversed_sentence += split_array[i]
        if i != -1-(len(split_array)-1):
            reversed_sentence += " "
    return reversed_sentence


if __name__ == "__main__":
    sentence = "i live in a house"
    reversed_sentence = reverse_the_sentence(sentence)
    print(reversed_sentence)