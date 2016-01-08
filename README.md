# Markdown2Python (md2py)

md2py parses and converts markdown into a usable Python object. This allows you
to navigate a markdown file as a document structure.

## Usage

Markdown2Python offers only one function `md2py`, which generates a Python
object from markdown text. This object embeds the markdown file's document
structure in object form.

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

With md2py, we can easily navigate this markdown file using a Python
"table of contents".

```
>>> obj = md2py(markdown)
>>> obj.h1.string
'Chikin Tales'
>>> obj.h1.h2
Chapter 1 : Chikin Fly
>>> list(obj.h1.h2.h3s)
['Waddling']
>>> list(obj.h1.h2s)[1] == obj.h1[1]
True
>>> obj.h1[1]
Chapter 2 : Chikin Scream
>>> list(obj.h1[1].h3s)
['Plopping', 'I Scream']
```

Akin to a navigation bar, the md2py object allows you to expand a markdown
file one level at a time.

## Installation

Install via pip.

```
pip install md2py
```

## Additional Notes

- Behind the scenes, the md2py uses `BeautifulSoup`. All md2py objects have a
`source` attribute containing a BeautifulSoup object.
