from .md2py import TreeOfContents


def md2py(md, *args, **kwargs):
    """
    Converts markdown file Python object

    :param str md: markdown string
    :return: object
    """
    return TreeOfContents.fromMarkdown(md, *args, **kwargs)
