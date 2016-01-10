from md2py import md2py, TreeOfContents

chikin = open('tests/samples/chikin.md').read()
iscream = open('tests/samples/iscream.md').read()

tocs2strs = lambda tocs: list(map(str, tocs))

##############
# MAIN TESTS #
##############

def test_basic_prop():
    """tests that custom __getattr__ works"""
    toc = md2py(chikin)
    assert str(toc) == ''
    assert toc.depth == 1
    assert len(toc.branches) == 1
    assert isinstance(toc.h1, TreeOfContents)

def test_get_tags():
    """tests that tags are printed correctly"""
    toc = md2py(chikin)

    assert len(list(toc.h1s)) == 1
    assert str(toc.h1) == repr(toc.h1) == toc.h1.string == 'Chikin Tales'

def test_top_level():
    """tests parse for the top level of a markdown string"""
    toc = md2py(chikin)

    assert str(toc.h1) == 'Chikin Tales'
    assert len(list(toc.h2s)) == 0
    assert len(list(toc.h3s)) == 0
    assert toc.depth == 1

def test_top_level2():
    """tests parse for top level of markdown string with only h2s"""
    toc = md2py(iscream)

    assert toc.h1 is None
    assert str(toc.h2) == 'I Scream'
    assert len(list(toc.h2s)) == 2
    assert toc.depth == 2

def test_indexing():
    """test indices"""
    toc = md2py(chikin)

    assert list(toc.h1.h2s)[1] == toc.h1[1]
    assert str(toc.h1[1]) == 'Chapter 2 : Chikin Scream'

def test_branches_limit():
    """Tests that branches include only headings of higher depth"""
    toc = md2py(chikin)

    assert toc.h1.h2.string == 'Chapter 1 : Chikin Fly'
    assert list(map(str, toc.h1.h2.h3s)) == ['Waddling']
    assert list(map(str, toc.h1[1].h3s)) == ['Plopping', 'I Scream']
