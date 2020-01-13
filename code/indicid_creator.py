import os
import javalang.tree
import owlready2

onto = owlready2.get_ontology("tree.owl").load()
file_repo = '../dir/android-chess/app/src/main/java/jwtc/chess'


def extract_field(field, cd):
    for f in field.declarators:
        fd = onto['FieldDeclaration']()
        fd.jname = [f.name]
        cd.body.append(fd)


def extract_statements(node, fd):
    for _ in node.parameters:
        fp = onto['FormalParameter']()
        fd.parameters.append(fp)


def extract_parameters(node, fd):
    for _, statement in node.filter(javalang.tree.Statement):
        if type(statement) != javalang.tree.Statement:
            s_type = statement.__class__.__name__
            s = onto[s_type]()
            fd.body.append(s)


def extract_function(node):
    f_type = node.__class__.__name__
    fd = onto[f_type]()
    fd.jname = [node.name]
    extract_parameters(node, fd)
    extract_statements(node, fd)
    return fd


def extract_member(node, cd):
    for member in node.body:
        if type(member) == javalang.tree.FieldDeclaration:
            extract_field(member, cd)
        elif type(member) in [javalang.tree.MethodDeclaration, javalang.tree.ConstructorDeclaration]:
            cd.body.append(extract_function(member))



def class_def(tree):
    for _, node in tree.filter(javalang.tree.ClassDeclaration):
        cd = onto['ClassDeclaration']()
        cd.jname = [node.name]
        extract_member(node, cd)


for file in os.listdir(file_repo):
    if file.endswith('.java'):
        file_path = os.path.join(file_repo, file)
        with open(file_path, 'rt') as jfile:
            class_def(javalang.parse.parse(jfile.read()))
onto.save("tree2.owl", format="rdfxml")
