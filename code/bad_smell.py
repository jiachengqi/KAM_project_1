from owlready2 import *
import rdflib.plugins.sparql as sq

onto = get_ontology("file:///Users/jq/Desktop/bad_smell/code/tree2.owl").load()
graph = default_world.as_rdflib_graph()



# queries

# 1.1
q = sq.prepareQuery(
    """SELECT ?cn ?mn ?s (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    ?m tree:body ?s .
    ?s a/rdfs:subClassOf* tree:Statement .
    } GROUP BY ?m
    HAVING (COUNT(?s) >= 20)    """,
    initNs={"tree": "http://test.org/tree.owl#"}
)
sys.stdout = open("11.txt", "w")
for row in graph.query(q):
    print(row.cn, ":", row.mn, ":", int(row.tot))
sys.stdout.close()

# 1.2
q = sq.prepareQuery(
    """SELECT ?cn ?on ?s (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?o .
    ?o a tree:ConstructorDeclaration .
    ?o tree:jname ?on .
    ?o tree:body ?s .
    ?s a/rdfs:subClassOf* tree:Statement .
    } GROUP BY ?o""",
    initNs={"tree": "http://test.org/tree.owl#"}
)
print("Long constructor")
sys.stdout = open("12.txt", "w")
for row in graph.query(q):

    print(row.cn, ":", row.on, ":", int(row.tot))
sys.stdout.close()

# 2

q = sq.prepareQuery(
    """SELECT ?mn ?cn (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    } GROUP BY ?cn
    HAVING (COUNT(?m) >= 10)""",
    initNs={ "tree": "http://test.org/tree.owl#" }
)
# print("Large classess: ")
sys.stdout = open("2.txt", "w")

for row in graph.query(q):
    print(row.cn, ":", int(row.tot))
sys.stdout.close()


# 3.1
q = sq.prepareQuery(
    """SELECT ?cn ?mn ?s (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    ?m tree:body ?s .
    ?s a tree:SwitchStatement .
    } GROUP BY ?m
    HAVING (COUNT(?s) >= 1)    """,
    initNs={"tree": "http://test.org/tree.owl#"}
)
sys.stdout = open("31.txt", "w")
for row in graph.query(q):
    print(row.cn, ":", row.mn, ":", int(row.tot))
sys.stdout.close()


# 3.2
q = sq.prepareQuery(
    """SELECT ?cn ?on ?s (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?o .
    ?o a tree:ConstructorDeclaration .
    ?o tree:jname ?on .
    ?o tree:body ?s .
    ?s a tree:SwitchStatement .
    } GROUP BY ?o
    HAVING (COUNT(?s) >= 1)    """,
    initNs={"tree": "http://test.org/tree.owl#"}
)
sys.stdout = open("32.txt", "w")
for row in graph.query(q):

    print(row.cn, ":", row.on, ":", int(row.tot))
sys.stdout.close()





# 4.1
q = sq.prepareQuery(
    """SELECT ?cn ?mn ?s (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    ?m tree:parameters ?s .
    ?s a tree:FormalParameter .
    } GROUP BY ?m
    HAVING (COUNT(?s) >= 5)    """,
    initNs={"tree": "http://test.org/tree.owl#"}
)
sys.stdout = open("41.txt", "w")
for row in graph.query(q):
    print(row.cn, ":", row.mn, ":", int(row.tot))
sys.stdout.close()



# 4.2
q = sq.prepareQuery(
    """SELECT ?cn ?mn ?s (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:ConstructorDeclaration .
    ?m tree:jname ?mn .
    ?m tree:parameters ?s .
    ?s a tree:FormalParameter .
    } GROUP BY ?m
    HAVING (COUNT(?s) >= 5)    """,
    initNs={"tree": "http://test.org/tree.owl#"}
)
sys.stdout = open("42.txt", "w")
for row in graph.query(q):
    print(row.cn, ":", row.mn, ":", int(row.tot))
sys.stdout.close()


# 5
q = sq.prepareQuery(
    """SELECT ?mn ?cn (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    FILTER (regex(?mn, "get.*"))
    } GROUP BY ?cn""",
    initNs={ "tree": "http://test.org/tree.owl#" }
)
sys.stdout = open("5.txt", "w")

for row in graph.query(q):
    print(row.cn, ":", row.mn,":", int(row.tot))
sys.stdout.close()


q = sq.prepareQuery(
    """SELECT ?mn ?cn (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    FILTER (regex(?mn, "set.*"))
    } GROUP BY ?cn""",
    initNs={ "tree": "http://test.org/tree.owl#" }
)
sys.stdout = open("5.txt", "w")

for row in graph.query(q):
    print(row.cn, ":", row.mn,":", int(row.tot))
sys.stdout.close()


q = sq.prepareQuery(
    """SELECT ?mn ?cn (COUNT(*)AS ?tot) WHERE {
    ?c a tree:ClassDeclaration .
    ?c tree:jname ?cn .
    ?c tree:body ?m .
    ?m a tree:MethodDeclaration .
    ?m tree:jname ?mn .
    } GROUP BY ?cn""",
    initNs={ "tree": "http://test.org/tree.owl#" }
)
sys.stdout = open("5.txt", "w")

for row in graph.query(q):
    print(row.cn, ":", row.mn,":", int(row.tot))
sys.stdout.close()