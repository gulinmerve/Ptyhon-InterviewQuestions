def shuffle(x,k):
    	deck = [i for i in range(1,k+1)]
	for i in range(x):
		x= randint(1,k)
		while True:
			y = randint(1,k)
			if y != x:
				break
		deck[x-2], deck[y-2] = deck[y-2], deck[x-2]
	return deck
print(shuffle(500,52))

def shuffle(cards, k):
    for i in range(k):
        pos = i + randint(0,k-i-1)
        cards[i], cards[pos] = cards[pos], cards[i]