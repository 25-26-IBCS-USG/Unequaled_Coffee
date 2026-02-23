from ZooLabAnimal import Animal
from ZooLabEnclosure import Enclosure
from ZooLabZoo import Zoo

def main():

    pb = Animal("Polar Bear", "While appearing white, polar bear fur is actually clear and hollow, while their skin is black to absorb sunlight!")
   
    af = Animal("Arctic Fox", "Arctic foxes use the same dens for generations—some are as old as 300 years.")

    n = Animal("Narwhal", "The narwhal's iconic long, spiraled 'horn' is actually a sensory tooth with roughly 10 million nerve endings!")

    w = Animal("Walrus", "In order to withstand the icy waters of the Arctic Ocean, the walrus has the ability to slow down its heartbeat.")

    bs = Animal("Bearded Seal", "The bearded seal is the largest species of seal in the Arctic, capable of reaching lengths of about 2.1-2.4 meters (7-8 feet) and weighing up to 360 kilograms (800 pounds).")

    m = Animal("Meerkat", "Active and social animals, meerkats live in groups that can include as many as 30 individuals, although the average pack size is around 10-15 individuals.")

    z = Animal("Zebra", "While zebras may look identical from a distance, each one has a distinct pattern of stripes, similar to human fingerprints.")

    r = Animal("Rhinoceros", "Rhino horns are not made of bone, but of keratin, the same material found in your hair and fingernails.")

    g = Animal("Giraffe", "Giraffes holds the title of being the world's tallest mammal, with even newborn giraffes surpassing the height of most humans.")

    c = Animal("Cheetah", "Cheetahs are fastest land animals in the world, capable of reaching 112km/h in just three seconds–faster than a sports car can accelerate!")

    l = Animal("Lion", "The roar of a lion is loud enough to be heard from as far as eight kilometers (five miles) away. Its roar reaches up to 114 decibels—louder than a chainsaw!")

    sm = Animal("Scarlet Macaw", "Most macaws are left-footed. This preferential bias is due to the right sides of their brains being more developed than the left, which is why they use their left feet to grasp, grab, and manipulate food while the right supports their bodies.")

    st = Animal("Sumatran Tiger", "Sumatran tigers have partially webbed paws that make them excellent swimmers!")

    sq = Animal ("Squirrel Monkey", "Squirrel monkeys are considered one of the most intelligent species of monkey, having the largest brain-to-body mass ratio of all primates.")

    mg = Animal ("Mountain Gorilla", "Humans share approximately 98% of their DNA with gorillas!")

    tf = Animal ("Red-Eyed Tree Frog", "The eggs of a red-eyed tree frog can differentiate between harmless vibrations such as rainfall and the vibrations of an approaching predator, such as a snake, and can hatch early if they feel threatened.")

    kf = Animal ("Kit Fox", "Despite being the smallest species of fox in North America, the kit fox is well known for its iconicly large ears—used to aid hearing and dissipate heat.")

    gm = Animal ("Gila Monster", "Although they are one of the few (highly) venomous lizards in the world, gila monster venom actually contains a compound that is used in diabetes medications.")

    bc = Animal ("Bactrian Camel", "Camels can drink over 30 gallons of water at once. They can survive six to seven months without water if they have food from which to get moisture.")

    ds = Animal ("Desert Bighorn Sheep", "The horns of a ram are called 'curls' and can weigh up to 30 pounds!")

    tr = Animal ("Tiger Rattlesnake", "The tiger rattlesnake is the most venomous of all rattlesnakes.")

    #ENCLOSURES

    Desert = Enclosure ("Desert", "The desert biome covers about one-fifth of the earth's surface. Deserts have a layer of soil that can either be sandy, gravelly or stony, depending on the type. Deserts get less than 25 centimeters (10 inches) of rainfall a year, and the creatures that live in deserts are adapted to this extremely dry climate.", [tr, ds, bc, gm, kf])
    Arctic = Enclosure ("Arctic", "For the majority of the year, the arctic is a cold, frozen landscape. This biome has a short growing season, followed by harsh conditions that have prompted the development of unique adaptations in the plants and animals in the region for survival.", [pb, af, n, w, bs])
    Grassland = Enclosure ("Grassland", "Grassland biomes are expansive, treeless ecosystems dominated by grasses and herbaceous plants, covering approximately 40% of Earth’s terrestrial surface. They are characterized by low to moderate precipitation, frequent fires, and grazing animals, making them crucial for biodiversity, carbon storage, and agriculture.", [m, z, r, g, c, l]) 
    Rainforest = Enclosure ("Tropical Forest", "Tropical forest biomes are hot, humid, and biodiversity-rich ecosystems located near the equator. They sport consistent 26-27°C temperatures, high annual rainfall, and dense, multi-layered vegetation. These forests hold half the world's species!", [sm, st, sq, mg, tf])

    print(Desert.getAnimals())

    #ZOO

    zoo = Zoo ("The Animal Kingdom", "$20 Adult Ticket, $14 Youth Ticket", "Open", [Desert, Arctic, Grassland, Rainforest])
    print(zoo)
        
if __name__ == "__main__":
    main()
