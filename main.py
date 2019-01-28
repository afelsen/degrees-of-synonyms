from thesaurus import Word
import time
import calendar

def main():

    ####EDIT starting and ending words####
    startword = "green"
    endword = "quick"
    ######################################

    words = [startword]

    #A list that represents the length of each level of the code
    branchEndLength = [1]

    #A dictionary that saves the branch values of each word.
        #For example if "dance" is the startword, it would have a value of 1. Corrupt is the fifteenth synonym, so it has a value of 1.15.
    wordDict = {"1.":words[0]}

    #A reversed version of the dictionary. This allows the program to use the word as the key
    wordDictFlipped = {words[0]:"1."}

    #How many iterations the main loops has been running
    i = 0

    currentTime = time.time()

    for w in words:
        value = 1

        #Find the synonyms of the word, if there are any
        try:
            wObj = Word(w)
            synonyms = wObj.synonyms()
        except:
            synonyms = []


        for s in synonyms:
            if s not in words:
                #Add each synonym to "words"
                words.append(s)

                #Add the word and its branch value to the dictionaries
                wordDict[str(wordDictFlipped[w])+str(value)+"."] = s
                wordDictFlipped[s] = str(wordDictFlipped[w])+str(value)+"."
                value += 1

        #If all of the words in a branch have been iterated through
        if i >= branchEndLength[-1]:
            length = len(words)
            for j in branchEndLength:
                length -= j
            branchEndLength.append(length)
            print(branchEndLength)

            #Print the time it took for a branch level and estimate the time the next branch will take
            branchTime = time.time()-currentTime
            currentTime = time.time()
            print("Time elapsed for this branch: " + str(round(branchTime,2)) + " seconds")
            estimatedBranchTime = branchEndLength[-1]/branchEndLength[-2]*branchTime
            print("Estimated time until next branch: " + str(round(estimatedBranchTime,2)) + " seconds")

        #Check if the endword has shown up (if it is connected by a synonym)
        if endword in words:
            print()
            #Check to see the branch value of the word
            key = wordDictFlipped[endword]

            #Print parent words of the endword (evil --> corrupt --> exploiting... --> good)
            for j in range(len(key)):
                if key[j] == ".":
                    print(wordDict[key[:j+1]])
            print(key)
            print(i)
            break
        i += 1
main()


#Some results
'''
apple
blue-green
royal
high
tremendous
amazing
1.1.6.10.5.1.
2132

evil
corrupt
exploiting
use
good
1.2.11.9.15.
1397

nick
cut
trim
dapper
swell
awesome
1.1.33.2.28.1.
5069

frozen
Siberian
bleak
burned
burnt
1.8.4.7.4.
1300

cry
howl
hoot
jeer
fleer
laugh
1.1.3.4.10.1.
1869

dance
frolic
fun
pleasant
soft
furry
1.15.3.4.19.5.
11825

stupid
ill-advised
brash
vivacious
jumping
1.5.6.17.1.
1802
'''
