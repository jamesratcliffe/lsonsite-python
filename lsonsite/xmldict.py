"""Provides a class that creates a dictionary from XML."""
import xmltodict
import collections
from xml.parsers.expat import ExpatError


class XMLDict(collections.OrderedDict):
    """Parse a string of XML to a dictionary. Prints as pretty XML."""
    def __init__(self, data):
        super(XMLDict, self).__init__()
        if isinstance(data, str):
            try:
                parsedxml = xmltodict.parse(data, xml_attribs=True)
            except ExpatError:
                pass
            else:
                self.update(parsedxml)
        elif isinstance(data, dict):
            self.update(data)

    def __str__(self):
        try:
            return xmltodict.unparse(self, pretty=True)
        except ValueError:
            return ""
