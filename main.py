from thesaurus import Word
import time
import calendar

def main():
    words = ["apple"]
    endword = "banana"
    branchEndLength = [1]
    wordDict = {"1.":words[0]}
    wordDictFlipped = {words[0]:"1."}
    i = 0

    value = 1

    currentTime = time.time()

    for w in words:
        value = 1
        try:
            wObj = Word(w)
            synonyms = wObj.synonyms()
        except:
            synonyms = []
        for s in synonyms:
            if s not in words:
                words.append(s)
                wordDict[str(wordDictFlipped[w])+str(value)+"."] = s
                wordDictFlipped[s] = str(wordDictFlipped[w])+str(value)+"."
                value += 1
        if i >= branchEndLength[-1]:
            length = len(words)
            for j in branchEndLength:
                length -= j
            branchEndLength.append(length)
            print(branchEndLength)
            branchTime = time.time()-currentTime
            currentTime = time.time()
            print("Time elapsed for this branch: " + str(round(branchTime,2)) + " seconds")
            estimatedBranchTime = branchEndLength[-1]/branchEndLength[-2]*branchTime
            print("Estimated time until next branch: " + str(round(estimatedBranchTime,2)) + " seconds")

        if endword in words:
            print()
            key = wordDictFlipped[endword]
            for j in range(len(key)):

                if key[j] == ".":
                    print(wordDict[key[:j+1]])
            print(wordDictFlipped[endword])
            print(i)
            break
        i += 1
        # if i % 1000 == 0:
        #     cont = input("Break? (y/n)")
        #     if cont == "y":
        #         break
        # print(wordDictFlipped[w])
        # print(w)
        # print()



main()


#Results
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
