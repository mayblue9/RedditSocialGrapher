import xml.etree.ElementTree as ET
import json
import sys

"""This script converts a SVG file into a JSON file for data assignment using d3. 
This script should be replaced with a more holistic one that integrates original data that is lost during the svg conversion, such as post content or upvotes."""

filename = sys.argv[1];

jsonrep = dict()
edges = list()
nodes = list()
arrows = list()
labels = list()

tree = ET.parse(filename)
root = tree.getroot()

svgattribs = root.attrib
width  = svgattribs["width"]
height = svgattribs["height"]
viewbox = svgattribs["viewBox"]

for child in root:
    for element in child:
        elementID = child.attrib["id"]
        attribs = element.attrib
        attribs["name"] = attribs["class"]
        if elementID == "nodes":
            nodes.append(attribs)
        elif elementID == "edges":
            edges.append(attribs)
        elif elementID == "arrows":
            arrows.append(attribs)
        elif elementID == "node-labels":
            attribs["text"] = element.text
            labels.append(attribs)
            
            
jsonrep["nodes"] = nodes
jsonrep["edges"] = edges
jsonrep["arrows"] = arrows
jsonrep["labels"] = labels

jsonrep["width"] = width
jsonrep["height"] = height
jsonrep["viewBox"] = viewbox

file = open(filename[:-4] + ".json", "w")
file.write(json.dumps(jsonrep, sort_keys=True, indent=4, separators=(',', ': ')))
