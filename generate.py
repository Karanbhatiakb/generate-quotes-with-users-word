from quote import quote

word = input("Please enter your word to generate quote: ")
print("Your Keyword : ",word)

res = quote(word,limit=1)
for i in range(len(res)):
    print("\nQuote Generated: ",res[i]['quote'])
