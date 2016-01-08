from .md2py import Markdownpy


def md2py(md, *args, **kwargs):
    """
    Converts markdown file Python object

    :param str md: markdown string
    :return: object
    """
    return Markdownpy.fromMarkdown(md, *args, **kwargs)
