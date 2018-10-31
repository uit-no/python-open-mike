observations = {
    'forest': ['cow', 'cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['horse', 'horse', 'sheep', 'horse'],
    'jungle': ['ocelot', 'parrot', 'sheep', 'parrot'],
}

species = {biome: set(observations[biome]) for biome in observations}


print('\nHow many distinct species were observed in each biome?')
for biome, animals in species.items():
    print(f'{biome}: {len(animals)} species')


print('\nHow many sheep were observed in total?')
count = 0
for animals in observations.values():
    count += animals.count('sheep')
print(count)


print('\nAre there any species that appear in all biomes?')
print(species['forest'].intersection(species['plains']).intersection(species['jungle']))


print('\nWhich animals are only found in the jungle?')
print(species['jungle'].difference(species['forest']).difference(species['plains']))


print('\nWhich is the most common animal of all?')
count = {}
for biome in observations:
    for animal in observations[biome]:
        if animal in count:
            count[animal] += 1
        else:
            count[animal] = 1
# Reverse dict:
for c, a in reversed(sorted((c, a) for (a, c) in count.items())):
    print(c, a)
    break


# another formulation using collections
from collections import Counter
print('\nWhich is the most common animal of all?')
all_animals = []
for biome in observations:
    for animal in observations[biome]:
        all_animals.append(animal)
c = Counter(all_animals)
print(c.most_common())


print('\nAre parrots found only in the jungle?')
for biome in species:
    if biome != 'jungle' and 'parrot' in observations[biome]:
        print('No')
        break
else:
    print('Yes')


# another formulation using set differences
print('\nAre parrots found only in the jungle?')
print('parrot' in species['jungle'].difference(species['forest']).difference(species['plains']))
