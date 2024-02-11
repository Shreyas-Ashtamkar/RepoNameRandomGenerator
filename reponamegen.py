from random import SystemRandom

#Word Bank
WORD = (
    ("spiritual","amused", "obscene", "willing", "smelly", "bright", "colossal", "abstracted", "understood", "whispering", "ignorant", "momentous", "black", "agonizing", "fluffy", "regular", "drunk", "harsh", "open", "closed", "entertaining", "jobless", "periodic", "filthy", "sick", "nebulous", "possible", "complex", "expensive", "fat", "psychotic", "descriptive", "safe", "past", "nasty", "curvy", "puny", "five", "obese", "windy", "dangerous", "lovely", "knowledgeable", "magical", "unique", "outrageous", "demonic", "unhealthy", "futuristic", "whole", "functional", "heavy", "damaging", "silent", "thirsty", "absurd", "tiny", "dusty", "chemical", "married", "plastic", "juicy", "gentle", "lethal", "general", "careful", "spiky", "super", "common", "poor", "unbiased", "exotic", "possessive", "hilarious", "fragile", "exciting", "deep", "helpful", "psychedelic", "calm", "flashy", "teeny-tiny", "fertile", "thankful", "fearless", "lonely", "adorable", "wet", "crowded", "unused", "tasteful", "unbreakable", "breakable", "youthful", "beautiful", "fast", "quick", "strong", "typed", "simple", "cuddly", "sunny"), 
    ("order", "butter", "ticket", "smoke", "birds", "rock", "wing", "fog", "sky", "water", "cream", "bikes", "shoes", "vegetable", "cow", "fork", "haircut", "waves", "dinosaurs", "blood", "servant", "structure", "party", "clown", "pen", "throat", "frogs", "earthquake", "card", "toothpaste", "spy", "worm", "activity", "truck", "potato", "office", "island", "bottle", "fairies", "maid", "needle", "squirrel", "cherry", "stone", "advertisement", "bells", "kittens", "deer", "hobbies", "river", "bubble", "soup", "cemetery", "coal", "crime", "sugar", "thunder", "grandfather", "ants", "steam", "aftermath", "hair", "respect", "wound", "ground", "door", "gold", "wish", "fire", "ring", "dogs", "theory", "watch", "machine", "soda", "star", "locket", "name", "berry", "castle", "reward", "pollution", "talk", "school", "reaction", "celery", "canvas", "car", "airplane", "pet", "cakes", "grass", "breath", "hand", "snake", "dolphin", "home", "directory", "bed", "desktop", "partner", "glass", "earth", "flower", "rose", "tree", "maze", "piano", "ball", "music", "food", "shower", "window", "umbrella", "fork", "plant", "towel")
)
JOIN = "-", ".", "_"

# True Random
randomGenerator = SystemRandom()

# Get Random Array Element
getRandElement = lambda arr: arr[randomGenerator.randint(0, len(arr)-1)]

print(getRandElement(JOIN).join((getRandElement(WORD[0]), getRandElement(WORD[1]))))
print()
