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

# def extract_statement(node, fd):
#     for _, snode in node.filter(javalang.tree.Statement):
#         if type(snode) != javalang.tree.Statement:
#             stype = snode.__class__.__name__
#             s = onto[stype]()
#             fd.body.append(s)
#
#
# def extract_parameter(node, fd):
#     for _ in node.parameters:
#         fp = onto['FormalParameter']()
#         fd.parameters.append(fp)
#
#
# def extract_function(node):
#     ftype = node.__class__.__name__
#     fd = onto[ftype]()
#     fd.jname = [node.name]
#     extract_parameter(node, fd)
#     extract_statement(node, fd)
#
#
# def extract_fields(fields, cd):
#     for f in fields.declarators:
#         fd = onto['FieldDeclaration']()
#         fd.jname = [f.name]
#         cd.body.append(fd)
#
#
# def extract_members(node, cd):
#     for m in node.body:
#         if type(m) in JAVA_FUNCTIONS:
#             cd.body.append(extract_function(m))
#         elif type(m) == javalang.tree.FieldDeclaration:
#             extract_fields(m, cd)
#
#
# def extract_class(tree):
#     for _,node in tree.filter(javalang.tree.ClassDeclaration):
#         cd = onto['ClassDeclaration']()
#         cd.jname = [node.name]
#         extract_members(node, cd)
#
#
# for file in os.listdir("../dir/android-chess/app/src/main/java/jwtc/chess"):
#     if file.endswith(".java"):
#         file_path = os.path.join("../dir/android-chess/app/src/main/java/jwtc/chess", file)
#         # file_path.append("../dir/android-chess/app/src/main/java/jwtc/chess/" + file)
#         print(file_path)
#         with open(file_path, 'r') as jfile:
#             extract_class(javalang.parse.parse(jfile.read()))
#


# for f in file_path:
#     class_name.append(f.split("/")[-1].replace(".java", ""))
# print(class_name)
#
# def extract_function(node):
#     function_type = node.__class__.__name__
#     fd = onto[function_type]()
#     fd.jname = [node.name]
#     for _, statement in node.filter(javalang.tree.Statement):
#         if type(statement) != javalang.tree.Statement:
#             typee = statement.__class__.__name__
#             s = onto[typee]()
#             fd.body.append(s)
#     for _ in node.parameters:
#         fp = onto['FormalParameter']()
#         fd.parameters.append(fp)
#
#
#
# def classdef(onto, nodes):
#     cd = onto["ClassDeclaration"]()
#     cd.jname = [nodes.name]
#     for node in nodes.body:
#     # the reason for inner class,
#     # for path, node in nodes:
#         if type(node) is javalang.tree.FieldDeclaration:
#             for v in node.declarators:
#                 fd = onto["FieldDeclaration"]()
#                 fd.jname = [v.name]
#                 cd.body.append(fd)
#
#         if type(node) is javalang.tree.MethodDeclaration or javalang.tree.ConstructorDeclaration:
#             cd.body.append(extract_function(node))
#
#
# def parsefile(onto, treee, nodes):
#     for path, node in treee.filter(javalang.tree.ClassDeclaration):
#         classdef(onto, node)
#
#
# def getast(each_file):
#     with open(each_file, "rt") as jfile:
#         return javalang.parse.parse(jfile.read())
#
#
# def getmethodname(onto, filepath):
#     for fff in filepath:
#         parsefile(onto, getast(fff), class_name)
#
#
# getmethodname(onto, file_path)
#
# onto.save("tree2.owl", format="rdfxml")
#


#
# JAVA_FUNCTIONS = [javalang.tree.MethodDeclaration, javalang.tree.ConstructorDeclaration]
# CHESS_PATH = '../dir/android-chess/app/src/main/java/jwtc/chess'
#
#
# # onto = owlready2.get_ontology('./out/tree.owl')
# onto.load()
#
#
# def extract_parameters(function_node, fd):
#     for _ in function_node.parameters:
#         fp = onto['FormalParameter']()
#         fd.parameters.append(fp)
#
#
# def extract_statements(function_node, fd):
#     for _, statement_node in function_node.filter(javalang.tree.Statement):
#         if type(statement_node) != javalang.tree.Statement:
#             statement_type = statement_node.__class__.__name__
#             s = onto[statement_type]()
#             fd.body.append(s)
#
#
# def extract_function(function_node):
#     function_type = function_node.__class__.__name__
#     fd = onto[function_type]()
#     fd.jname = [function_node.name]
#     extract_parameters(function_node, fd)
#     extract_statements(function_node, fd)
#     return fd
#
#
# def extract_fields(fields, cd):
#     for field in fields.declarators:
#         fd = onto['FieldDeclaration']()
#         fd.jname = [field.name]
#         cd.body.append(fd)
#
#
# def extract_members(class_node, cd):
#     for member in class_node.body:
#         if type(member) is javalang.tree.MethodDeclaration or javalang.tree.ConstructorDeclaration:
#         # if type(member) in JAVA_FUNCTIONS:
#             cd.body.append(extract_function(member))
#         elif type(member) == javalang.tree.FieldDeclaration:
#             extract_fields(member, cd)
#
#
# def extract_classes(ast):
#     for _, class_node in ast.filter(javalang.tree.ClassDeclaration):
#         cd = onto['ClassDeclaration']()
#         cd.jname = [class_node.name]
#         extract_members(class_node, cd)
#
#
# for file in os.listdir(CHESS_PATH):
#     if file.endswith('.java'):
#         path = os.path.join(CHESS_PATH, file)
#         with open(path, 'r') as javaFile:
#             extract_classes(javalang.parse.parse(javaFile.read()))
# # onto.save('./out/tree2.owl')
# onto.save("tree2.owl", format="rdfxml")
