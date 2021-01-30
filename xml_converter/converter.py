# 3rd party imports
from xml.etree import ElementTree


def convert_xml_elem_to_dict(elem):

    _dict = {}
    children = list(elem)
    if children:
        # non-leaf node
        _dict[elem.tag] = []
        for child in children:
            _dict[elem.tag].append(convert_xml_elem_to_dict(child))
    else:
        # leaf node
        if elem.text is None:
            _dict[elem.tag] = ""
        else:
            _dict[elem.tag] = elem.text
    return _dict


def convert_xml_to_dict(xml):
    """
    Convert from XML string to dict

    Args:
        xml (str): XML string
    Returns:
        dict: JSON equivalent representation of the XML string
    """

    root = ElementTree.fromstring(xml)
    return convert_xml_elem_to_dict(root)
