from collections import deque

def findItinerary(tickets):

    graph = {}

    for ticket in sorted(tickets):
        if ticket[0] in graph:
            graph[ticket[0]].append(ticket[1])
        else:
            graph[ticket[0]] = deque([ticket[1]])

    stack, answer = ["JFK"], []
    
    while stack:

        top = stack[-1]

        if top in graph and len(graph[top]) > 0:
            stack.append(graph[top].popleft())
        else:
            answer.append(stack.pop())

    return answer[::-1]