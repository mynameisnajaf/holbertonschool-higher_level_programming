#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except (OSError, TypeError, AttributeError):
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        recon_dict = {}
        for child in root:
            text = child.text
            if text is None:
                value = None
            elif text.isdigit():
                value = int(text)
            else:
                try:
                    value = float(text)
                except ValueError:
                    if text.lower() == "true":
                        value = True
                    elif text.lower() == "false":
                        value = False
                    else:
                        value = text

            recon_dict[child.tag] = value

        return recon_dict
    except (OSError, ET.ParseError):
        return None
