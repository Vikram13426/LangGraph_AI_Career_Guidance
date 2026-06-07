from langgraph.graph import StateGraph

from graph.state import CareerState

from graph.nodes.resume_parser_node import (
    resume_parser_node
)

from graph.nodes.memory_loader_node import (
    memory_loader_node
)

from graph.nodes.profile_node import (
    profile_node
)

from graph.nodes.planning_node import (
    planning_node
)

from graph.nodes.memory_saver_node import (
    memory_saver_node
)

from graph.nodes.resume_analysis_node import (
    resume_analysis_node
)

from graph.nodes.rag_node import (
    rag_node
)
# Create Graph Builder

graph_builder = StateGraph(
    CareerState
)

# ==========================
# REGISTER NODES
# ==========================

graph_builder.add_node(
    "resume_parser",
    resume_parser_node
)

graph_builder.add_node(
    "memory_loader",
    memory_loader_node
)

graph_builder.add_node(
    "profile_analysis",
    profile_node
)

graph_builder.add_node(
    "career_planning",
    planning_node
)

graph_builder.add_node(
    "memory_saver",
    memory_saver_node
)

graph_builder.add_node(

    "resume_analysis",

    resume_analysis_node

)

graph_builder.add_node(
    "rag_retriever",
    rag_node
)

# ==========================
# ENTRY POINT
# ==========================

graph_builder.set_entry_point(
    "resume_parser"
)


# ==========================
# EDGES
# ==========================

graph_builder.add_edge(
    "resume_parser",
    "memory_loader"
)

graph_builder.add_edge(
    "profile_analysis",
    "career_planning"
)

graph_builder.add_edge(
    "career_planning",
    "memory_saver"
)

graph_builder.add_edge(

    "resume_parser",

    "resume_analysis"

)
graph_builder.add_edge(

    "resume_analysis",

    "memory_loader"

)
graph_builder.add_edge(

    "memory_loader",

    "rag_retriever"

)
graph_builder.add_edge(

    "rag_retriever",

    "profile_analysis"

)

# ==========================
# FINISH POINT
# ==========================

graph_builder.set_finish_point(
    "memory_saver"
)


# ==========================
# COMPILE GRAPH
# ==========================

career_graph = (
    graph_builder.compile()
)