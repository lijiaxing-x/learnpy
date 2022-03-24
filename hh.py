

def reversewords(input):
    inputwords = input.split(" ")
    inputwords=inputwords[-1::-1]
    output = ' '.join(inputwords)
    return output
 
if __name__ == "__main__":
    input = '一点 吃 可以'
    rw = reversewords(input)
    print(rw)