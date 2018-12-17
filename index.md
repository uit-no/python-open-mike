---
layout: default
title: Python "open mike" events at UiT
---

## Format

Eventually it could be a platform where participants show something useful to
others. But it will take some time to warm up and until then each event will
have a theme and we will suggest exercises. Participants can prepare these
exercises but do not have to.  We go through the exercise and solutions
together but those who have solved the exercises can present alternative
solutions which we discuss together.

At each event we fix the dates for the next event and together we choose a
theme.


## What to expect

- Informal events.
- Interaction.
- Questions, answers, and discussions.


## What not to expect

Do not expect a semester-long course or lecture series
where you can sit back and somebody presents some slides. The goal is
to discuss, ask questions, and to demo. There are no slides, and there is no lecture.


## Exercises

You can email solutions to Radovan Bast (firstname.lastname@uit.no) who will
collect them and make them available (without names) so that you can
compare. It is OK to prepare all or prepare none.


## Next event

<ul>
  {% for post in site.posts %}
    {% if post.status != 'past' %}
      <li>
        <a href="{{ post.url | prepend:site.baseurl }}">{{ post.title }} ({{ post.time }}, room: {{ post.room }})</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>


## Past events

<ul>
  {% for post in site.posts %}
    {% if post.status == 'past' %}
      <li>
        <a href="{{ post.url | prepend:site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>


## Recommended reading

- [Real Python Tutorials](https://realpython.com)
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org)
- [Python 3 Module of the Week](https://pymotw.com/3/)


## Topics ideas for future events

- Context managers
- Functional programming
- `collections`
- File I/O
- `pygame`
- `pandas`
- `tkinter`
- `pytest`
- tic-tac-toe game
