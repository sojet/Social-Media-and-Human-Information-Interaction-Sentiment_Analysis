# opening positive list
p = 'positive-words.txt'

positive = [] # create a list for positive words to compare

with open(p, encoding='unicode_escape') as fp1:
   line1 = fp1.readline()
   count1 = 1
   while line1:
       if count1 > 35 :
        positive.append(line1.strip())
    
       line1 = fp1.readline()
       count1 += 1

#print(positive) # for debugging

# opening negative list
f = 'negative-words.txt'

negative = [] # create a list for negative words to compare

with open(f, encoding='unicode_escape') as fp2:
   line2 = fp2.readline()
   count2 = 1
   while line2:
       if count2 > 35:
        negative.append(line2.strip())
       line2 = fp2.readline()
       count2 += 1

#print(negative) # for debugging

# reading comments from blogs

c = '1155125983.txt'
comments = []# create a list for commments to compare

with open(c, encoding='unicode_escape') as fp3:
    for line3 in fp3:
        for word in line3.split():
            comments.append(word.lower())
            
#print(comments) # for debugging
pcount = 0 # for counting sentiment score for positive
ncount = 0 # for counting sentiment score for negative

for i in range(len(comments)):
    for j in range(len(positive)): #counting the number of positive words
        if comments[i] == positive[j]:
            #print(comments[i])
            pcount += 1
    for k in range(len(negative)): #counting the number of negative words
        if comments[i] == negative[k]:
            #print(comments[i])
            ncount -= 1
            
print("Positive score: " + str(pcount))
print("Negative Score: " + str(ncount))
print("Number of words in comment: " + str(len(comments)))

score = (pcount + ncount) / len(comments)
print("Overall sentiment score: " + str(score))

