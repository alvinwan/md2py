from md2py import md2py, Markdownpy

chikin = open('tests/samples/chikin.md').read()
iscream = open('tests/samples/iscream.md').read()

##############
# MAIN TESTS #
##############

def test_basic_prop():
    """tests that custom __getattr__ works"""
    obj = md2py(chikin)
    assert str(obj) == ''
    assert isinstance(obj.h1, Markdownpy)

def test_get_tags():
    """tests that tags are printed correctly"""
    obj = md2py(chikin)

    assert len(list(obj.h1s)) == 1
    assert str(obj.h1) == repr(obj.h1) == obj.h1.string == 'Chikin Tales'

def test_top_level():
    """tests parse for the top level of a markdown string"""
    obj = md2py(chikin)

    assert obj.h1.string == 'Chikin Tales'
    assert len(list(obj.h2s)) == 0
    assert len(list(obj.h3s)) == 0
    assert obj.depth == 1

def test_top_level2():
    """tests parse for top level of markdown string with only h2s"""
    obj = md2py(iscream)

    assert obj.h1 is None
    assert obj.h2.string == 'I Scream'
    assert len(list(obj.h2s)) == 2
    assert obj.depth == 2

def test_indexing():
    """test indices and """
    obj = md2py(chikin)

    assert list(obj.h1.h2s)[1] == obj.h1[1]
    assert obj.h1[1] == 'Chapter 2 : Chikin Scream'

def test_branches_limit():
    """Tests that branches include only headings of higher depth"""
    obj = md2py(chikin)

    assert obj.h1.h2 == 'Chapter 1 : Chikin Fly'
    assert list(obj.h1.h2.h3s) == ['Waddling']
    assert list(obj.h1[1].h3s) == ['Plopping', 'I Scream']
