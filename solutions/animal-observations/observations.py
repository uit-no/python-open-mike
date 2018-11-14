#!/usr/bin/env python3
from collections import Counter


def distinct_species(observations):
    return {biome: set(species) for biome, species in observations.items()}


def get_species(observations):
    species = []
    for s in observations.values():
        species.extend(s)
    return species


def count_specie(observations, specie):
    species = get_species(observations)
    return species.count(specie)


def in_all_biomes(observations):
    species = set(get_species(observations))
    for s in observations.values():
        species.intersection_update(s)
    return species


def only_in_biome(observations, biome):
    biome_species = set(observations[biome])
    for key, species in observations.items():
        if key == biome:
            continue
        biome_species.difference_update(species)
    return biome_species


def most_common(observations):
    species = get_species(observations)
    return Counter(species).most_common(1)


if __name__ == "__main__":
    observations = {
        'forest': ['cow', 'cow', 'sheep', 'sheep', 'pig', 'sheep'],
        'plains': ['horse', 'horse', 'sheep', 'horse'],
        'jungle': ['ocelot', 'parrot', 'sheep', 'parrot'],
    }
    print("Distinct species", distinct_species(observations))
    specie = "sheep"
    print("{} occured: {} times in observations"
          .format(specie, count_specie(observations, specie)))
    print("{} is in all biomes.".format(in_all_biomes(observations)))
    for biome in observations:
        print("{} Are only in biome: {}."
              .format(only_in_biome(observations, biome), biome))
    print(most_common(observations),
          "is the most common specie in the observations")
    name = "parrot"
    biome = "jungle"
    print("{} only in {}: {}".format(name, biome,
                                     name in only_in_biome(observations, biome)))
