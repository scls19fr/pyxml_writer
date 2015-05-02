#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Create XML document like:

<person id='123'>
    <name>Julie</name>
</person>

"""


from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

def main():
    filename = 'person.xml'
    root = Element('person')
    tree = ElementTree(root)
    name = Element('name')
    root.append(name)
    name.text = 'Julie'
    root.set('id', '123')
    print etree.tostring(root)
    tree.write(open(filename, 'w'))

if __name__ == "__main__":
    main()
