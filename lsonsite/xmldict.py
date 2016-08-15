"""Provides a class that creates a dictionary from XML."""
import xmltodict
import collections
from xml.parsers.expat import ExpatError


class XMLDict(collections.OrderedDict):
    """Parse a string of XML to a dictionary. Prints as pretty XML."""
    def __init__(self, xml):
        try:
            parsedxml = xmltodict.parse(xml, xml_attribs=True)
        except ExpatError:
            pass
        else:
            self.update(parsedxml)

    def __str__(self):
        return xmltodict.unparse(self, pretty=True)
