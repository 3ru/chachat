from diagrams import Cluster, Diagram
from diagrams.firebase.develop import Authentication as Auth
from  diagrams.firebase.develop import Storage as Storage
from  diagrams.firebase.develop import RealtimeDatabase as DB
from  diagrams.generic.os import Android as Android
from diagrams.generic.device import Mobile

graph_attr = {
    "fontsize": "20",
    "fontcolor":"black",
    "fontname": "helvetica"
}

node_attr = {
    "fontsize": "15",
    "fontname": "helvetica",
}

edge_attr={
    "color": "black"
}


with Diagram("Cloud Architecture", show=True, graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
    chachat = Android("App")

    with Cluster("Event"):
        chat_screen = Mobile("Chat Screen")

    with Cluster("Authenticate"):
        auth_group = [Auth("Authentication") - Storage("Storage") - DB("Database") ]

    chachat >> auth_group >> chat_screen
    chachat << auth_group << chat_screen
