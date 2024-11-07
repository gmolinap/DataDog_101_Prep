"""

Problem: Service Dependency Graph (Detecting Cycles in Microservices)
In a distributed system or microservices architecture, services often depend on each other. A service may call other services to complete its tasks, and these dependencies can be represented as a directed graph, where each node represents a service, and each directed edge represents a dependency from one service to another.

Task:
You are given a list of services and their dependencies. Each service is represented as a node, and a directed edge from A to B means that service A depends on service B. Your task is to:

Detect if there is a cycle in the graph (i.e., whether a service has a circular dependency).
If a cycle is detected, return True. If no cycle is detected, return False.
A cycle in the graph would indicate a problematic dependency because it could lead to deadlocks or unresolvable service calls in a distributed system. 

services = {
    'A': ['B'],  # Service A depends on B
    'B': ['C'],  # Service B depends on C
    'C': ['A']   # Service C depends on A (cycle: A -> B -> C -> A)
}

True  # There is a cycle in the graph.


"""