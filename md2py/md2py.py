from markdown import markdownFromFile, markdown
from bs4 import BeautifulSoup


class Markdownpy:
    """abstraction for markdown source"""

    source_type = BeautifulSoup
    valid_tags = ('a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
        'b', 'base', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button',
        'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'data',
        'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt',
        'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer', 'form',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr',
        'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'keygen', 'label',
        'legend', 'li', 'link', 'main', 'map', 'mark', 'menu', 'menuitem',
        'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup',
        'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q',
        'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small',
        'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'table',
        'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time',
        'title', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr')
    allowed_attrs = ('string', 'name')

    def __init__(self, source, depth=None):
        assert source is not None, 'NoneType source passed into Markdownpy'
        self.source = source
        self.depth = depth or self.parseTopDepth()
        self.branches = self.parseTopLevel()

    @staticmethod
    def getHeadingLevel(bs):
        """
        >>> bsify = lambda html: BeautifulSoup(html, 'html.parser')
        >>> bs = bsify('<h1>Hello</h1>').h1
        >>> Markdownpy.getHeadingLevel(bs)
        1
        >>> bs2 = bsify('<p>Hello</p>').p
        >>> Markdownpy.getHeadingLevel(bs2)

        >>> bs3 = bsify('<article>Hello</article>').article
        >>> Markdownpy.getHeadingLevel(bs3)

        """
        if not bs.name or len(bs.name) <= 1:
            return None
        n = bs.name[1]
        try:
            return int(n)
        except ValueError:
            return None

    def parseTopDepth(self):
        """parse highest heading in markdown

        >>> Markdownpy.fromHTML('<h2>haha</h2><h1>hoho</h1>').parseTopDepth()
        1
        >>> Markdownpy.fromHTML('<h3>haha</h3><h2>hoho</h2>').parseTopDepth()
        2
        """
        for i in range(1, 7):
            if getattr(self.source, 'h%d' % i):
                return i

    def parseTopLevel(self):
        """parse top level of markdown"""
        iterator, children = iter(self.source.children), []
        sameDepth = lambda child: self.getHeadingLevel(child) == self.depth
        for child in iterator:
            children.append(child)
            if sameDepth(child):
                break
        # for child in iterator:
        #     if sameDepth(child):
        #         children.append(child)
        #     else:
        #         parent = children[-1]
        #         parent.branches = getattr(parent, 'branches', [])
        #         parent.branches.append(child)
        children.extend(filter(sameDepth, iterator))
        return children

    def __getattr__(self, attr, *default):
        """Check source for attributes"""
        tag = attr[:-1]
        if attr in self.allowed_attrs:
            return getattr(self.source, attr, *default)
        if attr in self.valid_tags:
            try:
                return Markdownpy(next(filter(lambda t: t.name == attr, self.branches)))
            except StopIteration:
                return None
        if len(default):
            return default[0]
        if attr[-1] == 's' and tag in self.valid_tags:
            condition = lambda t:t.name == tag
            make = lambda child: Markdownpy(child, depth=self.depth+1)
            return map(make, filter(condition, self.branches))
        raise AttributeError("'Markdownpy' object has no attribute '%s'" % attr)

    def __repr__(self):
        """Display contents"""
        return str(self)

    def __str__(self):
        """Display contents"""
        return self.string or ''

    def __iter__(self):
        """Iterator over children"""
        return iter(self.branches)

    def __getitem__(self, i):
        return self.branches[i]

    @staticmethod
    def fromMarkdown(md, *args, **kwargs):
        """
        Creates abstraction using path to file

        :param str path: path to markdown file
        :return: Markdownpy object
        """
        return Markdownpy.fromHTML(markdown(md, *args, **kwargs))

    @staticmethod
    def fromHTML(html, *args, **kwargs):
        """
        Creates abstraction using HTML

        :param str html: HTML
        :return: Markdownpy object
        """
        return Markdownpy(BeautifulSoup(html, 'html.parser', *args, **kwargs))
