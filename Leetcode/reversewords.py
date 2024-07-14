
def reversewords(s):
    nw = s.split()
    rw=""
    counter = len(nw) - 1
    while counter >= 0:
        rw += nw[counter]  # Add the word to the result string
        if counter > 0:
            rw += " "  # Add a space between words
        counter -= 1  # Move to the previous word
    return rw

print(reversewords("the sky is blue"))