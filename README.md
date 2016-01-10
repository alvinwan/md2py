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

Plopping involves three steps:

1. squawk
2. plop
3. repeat, unless ordered to squat

### I Scream
```

Akin to a navigation bar, the `TreeOfContents` object allows you to expand a
markdown file one level at a time. At the global level, we can access the title.

```
>>> toc = md2py(markdown)
>>> toc.h1
Chikin Tales
>>> str(toc.h1)
'Chikin Tales'
```

Notice that at this level, there are no `h2`s. We can only access one level
at we descend the tree.

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

In total, there are three `h3`s in this document. However, only one `h3` is
actually nested below the `h2` 'Chapter 1 : Chikin Fly'. `md2py` parses this
document correctly to bely this relationship.

```
>>> list(toc.h1.h2.h3s)
['Waddling']
```

The `TreeOfContents` class also has a few more conveniences defined. Among them
is support for indexing. Here are two uses for indices.

1. Accessing the `i`th element: Instead of `list(toc.<elem>)[i]`, simply use
`toc.<elem>s[i]`.
2. Accessing the `i`th child of an element: Instead of
`<elem>.branches[i]`, use `<elem>[i]`.

```
>>> list(toc.h1.h2s)[1] == toc.h1[1]
True
>>> toc.h1.branches[0] == toc.h1[0] == toc.h1.h2
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
