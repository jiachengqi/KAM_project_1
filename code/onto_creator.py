from owlready2 import *
import ast
import types

ontuple = ()

with open("../dir/tree.py", "r") as source:
    tree = ast.parse(source.read())

onto = get_ontology("http://test.org/tree.owl")



class Visitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
        if type(node) == ast.ClassDef:
            for a in node.bases:
                if a.id == "Node":
                    with onto:
                        types.new_class(node.name, (Thing,))
                else:
                    with onto:
                        types.new_class(node.name, (onto[a.id],))

        if type(node) == ast.Assign:
            for b in node.value.elts:
                if b.s != "body" and b.s != "parameters" and b.s != "name":
                    with onto:
                        types.new_class(b.s, (DataProperty,))
                if b.s == "name":
                    with onto:
                        types.new_class("jname", (DataProperty,))
                if b.s == "body" or b.s == "parameters":
                    with onto:
                        types.new_class(b.s,(ObjectProperty,))


visitor = Visitor()
visitor.visit(tree)
print(onto)
onto.save("tree.owl", format="rdfxml")
