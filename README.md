# Markdown2Python (md2py)

md2py parses and converts markdown into a usable Python object. This allows you
to navigate a markdown file as a document structure.

## Usage

Markdown2Python offers only one function `md2py`, which generates a Python
object from markdown text. This object is a navigable, "Tree of Contents"
abstraction for the markdown file.

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

Plopping involves three steps:

1. squawk
2. plop
3. repeat, unless ordered to squat

### I Scream
```

Akin to a navigation bar, the `TreeOfContents` object allows you to expand a
markdown file one level at a time. Running `md2py` on the above markdown file
will generate a tree, abstracting the below structure.

```
          Chikin Tales
          /           \
    Chapter 1       Chapter 2
      /               /     \
  Waddling      Plopping    I Scream
```

At the global level, we can access the title.

```
>>> toc = md2py(markdown)
>>> toc.h1
Chikin Tales
>>> str(toc.h1)
'Chikin Tales'
```

Notice that at this level, there are no `h2`s.

```
>>> list(toc.h2s)
[]
```

The main `h1` has two `h2`s beneath it. We can access both.

```
>>> list(toc.h1.h2s)
[Chapter 1 : Chikin Fly, Chapter 2 : Chikin Scream]
>>> toc.h1.h2
Chapter 1 : Chikin Fly
```

In total, there are 3 `h3`s in this document. However, only 1 `h3` is
actually nested within 'Chapter 1 : Chikin Fly' (accessible via `toc.h1.h2`).
As a result, `toc.h1.h2.h3s` will only show one `h3`s.

```
>>> list(toc.h1.h2.h3s)
['Waddling']
```

The `TreeOfContents` class also has a few more conveniences defined. Among them
is support for indexing. To access the `i`th child of an `<element>` - instead of `<element>.branches[i]` - use `<element>[i]`.

See below for example usage.

```
>>> toc.h1.branches[0] == toc.h1[0] == toc.h1.h2
True
>>> list(toc.h1.h2s)[1] == toc.h1[1]
True
>>> toc.h1[1]
Chapter 2 : Chikin Scream
>>> list(toc.h1[1].h3s)
[Plopping, I Scream]
>>> list(map(str, toc.h1[1].h3s))
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
