def LongestWord(sen):
    largest = ''
    for word in sen.split():
        if len(word) > len(largest):
            largest = word
    return largest

def test():
    print(LongestWord("Hello guys my name is Bot. I'm a bot created "
          + "by the amazing Junction team, and my job is to "
          +  "be your friend and bedazzle you!"))

if __name__ == '__main__':
    test()
    
