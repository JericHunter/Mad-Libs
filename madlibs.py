import random

def randomize(pos):
    random.shuffle(pos)


print("Enter 2 adjectives ")
adj = [input(),input()]
randomize(adj)

print("Enter a pronoun ")
pronoun = input()
randomize(pronoun)

print("Enter 4 verbs ")
verb = [input(),input(),input(),input()]
randomize(verb)

print("Enter 2 nouns ")
noun = [input(),input()]
randomize(noun)

def libs():
    print("I woke up really " + adj[0] + " into the night")
    print("I could barely see " + pronoun + " because the " + verb[0] + " was out")
    print(noun[1] + " was the only thing on my mind as I began " + verb[1] + " my way to the " + noun[0])
    print("I " + verb[2] + " very slowly trying to be " + adj[1])
    print("but mother woke me up and told me to " + verb[3] + " back to bed")


libs()
