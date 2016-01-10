# Markdown2Python (md2py)

md2py parses and converts markdown into a usable Python object. This allows you
to navigate a markdown file as a document structure.

## Usage

Markdown2Python offers only one function `md2py`, which generates a Python
object from markdown text. It additionally parses the markdwon file to
generate a "Tree of Contents," navigable Python object.

Take, for example, the following markdown file.

**chikin.md**

```
# Chikin Tales

## Chapter 1 : Chikin Fly

Chickens don't fly. They do only the following:

- waddle
- plop

### Waddling

## Chapter 2 : Chikin Scream

### Plopping

### I Scream
```

Akin to a navigation bar, the md2py object allows you to expand a markdown
file one level at a time.

```
>>> toc = md2py(markdown)
>>> toc.h1.string
'Chikin Tales'
>>> toc.h1.h2
Chapter 1 : Chikin Fly
>>> list(toc.h1.h2.h3s)
['Waddling']
>>> list(toc.h1.h2s)[1] == obj.h1[1]
True
>>> toc.h1[1]
Chapter 2 : Chikin Scream
>>> list(toc.h1[1].h3s)
['Plopping', 'I Scream']
```

## Installation

Install via pip.

```
pip install md2py
```

## Additional Notes

- Behind the scenes, the md2py uses `BeautifulSoup`. All md2py objects have a
`source` attribute containing a BeautifulSoup object.
