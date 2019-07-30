---
layout: default
title: "2018-11-14: Lists, list comprehensions, dictionaries, sets, and tuples"
author: the organizers
status: past
---

## Exercises ([contributed solutions](https://github.com/uit-no/python-open-mike/tree/gh-pages/solutions/2))

1. Create a list `a` containing (floating point) numbers. Now create a new list `b` with each element of `a` squared.
2. Combine two lists `[a1, a2, ...]` and `[b1, b2, ...]` to a list of tuples: `[(a1, b1), (a2, b2), ...]`
3. Take some text (can be few paragraphs) from [Project Gutenberg](http://www.gutenberg.org) and find the 5 most
   frequent characters and 5 most frequent words. Ignore all punctuation and we recommend to lowercase the entire text.
4. Consider the following animal observations:

```python
observations = {
    'forest': ['cow', 'cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['horse', 'horse', 'sheep', 'horse'],
    'jungle': ['ocelot', 'parrot', 'sheep', 'parrot'],
}
```

Try to answer with code:
- How many distinct species were observed in each biome?
- How many sheep were observed in total?
- Are there any species that appear in all biomes?
- Which animals are only found in the jungle?
- Which is the most common animal of all?
- Are parrots found only in the jungle?
