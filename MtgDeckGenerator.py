import numpy as np
import math

#defining cards, this would be different in your program
class Card:
    name: str

    def __init__(self, name:str):
        self.name = name

Mountain = Card(name="Mountain")
PlayWithFire = Card(name="PlayWithFire")
LightUpTheStage = Card(name="LightUpTheStage")
MonastarySwiftspear = Card(name="MonastarySwiftspear")
GhituLavaRunner = Card(name="GhituLavaRunner")
card4 = Card(name="card4")
card5 = Card(name="card5")
card6 = Card(name="card6")
card7 = Card(name="card7")
card8 = Card(name="card8")
card9 = Card(name="card9")
card10 = Card(name="card10")
card11 = Card(name="card11")
card12 = Card(name="card12")
card13 = Card(name="card13")
card14 = Card(name="card14")
card15 = Card(name="card15")

#list of creatures and noncreatures, in order of best to worst
nonCreaturesInOrder = [PlayWithFire, LightUpTheStage, card4, card5, card6, card7, card8, card9]
creaturesInOrder = [MonastarySwiftspear, GhituLavaRunner, card10, card11, card12, card13, card14, card15]

#function you care about
#giving function parameters type hints and default values is usually good practice, so that when you're calling your function you know what kind of value each parameter is expecting
#This is a pure function, it takes input and gives output with no side affects. Making functions pure when possible is usually good practice
def generateDeck(creatures: list[Card], nonCreatures: list[Card], land: Card, spellRatio: float = 2/3, creatureRatio: float = 0.5, deckSize: int = 60):
    #calculate number of creatures, noncreatures, and lands given a ratio of spells to lands and a ratio of creatures to non-creatures
    numSpell = math.floor(deckSize * spellRatio)
    numCreature = math.floor(numSpell * creatureRatio)
    numNonCreature = numSpell - numCreature
    numLand = deckSize-numSpell

    #preprocesses creature and noncreature lists so they contain 4 copies of each card. This makes the rest of the function cleaner
    creatureList = []
    for card in creatures:
        creatureList.extend([card, card, card, card])
    nonCreatureList = []
    for card in nonCreatures:
        nonCreatureList.extend([card, card, card, card])

    #adds cards to deck according to the calculated numbers of creatures, noncreatures, and lands
    deck = []
    for i in range(numCreature):
        deck.append(creatureList[i])
    for i in range(numNonCreature):
        deck.append(nonCreatureList[i])
    for i in range(numLand):
        deck.append(land)

    #outputs the final deck
    return deck

#runs generate deck function and prints the names of the cards in the deck. Because I set default values, I don't need to explicitly set ratios and deck sizes unless I want to
print([i.name for i in generateDeck(creaturesInOrder, nonCreaturesInOrder, Mountain)])

"""
An idea for how you might go about using this to automatically generate decks and gather data

ratios = np.linspace(0, 1, 100)
data = []
for rat in ratios:
    generateDeck(creaturesInOrder, nonCreaturesInOrder, Mountain, rat)
    for g in range(100):
        data.append(rungame(deck))"""
