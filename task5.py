import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import time
import heapq
import random


class Node:
    def __init__(self, key, color="#78C858"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла


def build_tree_from_heap(heap):
    if not heap:
        return None

    def helper(index):
        if index >= len(heap):
            return None
        node = Node(heap[index])
        node.left = helper(2 * index + 1)
        node.right = helper(2 * index + 2)
        return node

    return helper(0)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = {}

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_nodes.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()



def hex_color_gradient(start_color, steps):
  
    # Конвертуємо HEX у RGB (0-1)
    start_rgb = np.array(mcolors.to_rgb(start_color))  
    
    # Створюємо градієнт, поступово змішуючи з білим (1,1,1)
    gradients = [start_rgb + (np.array([1, 1, 1]) - start_rgb) * (i / (steps - 1)) for i in range(steps)]
    
    # Конвертуємо назад у HEX-формат
    colors = [mcolors.to_hex(rgb) for rgb in gradients]

    return colors

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def bfs_traversal(tree_root):
    if not tree_root:
        return

    queue = [tree_root]
    visited_nodes = {}
    
    # Визначаємо кількість вузлів для правильного розрахунку градієнта
    total_nodes = count_nodes(tree_root)
    colors = hex_color_gradient("#003366", total_nodes)

    step = 0
    while queue:
        node = queue.pop(0)
        if step < total_nodes: 
            visited_nodes[node.id] = colors[step]
        draw_tree(tree_root, visited_nodes)
        time.sleep(0.8)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        step += 1


def dfs_traversal(tree_root):
    if not tree_root:
        return

    stack = [tree_root]
    visited_nodes = {}

    total_nodes = count_nodes(tree_root)  # Визначаємо кількість вузлів
    colors = hex_color_gradient("#003377", total_nodes)

    step = 0
    while stack:
        node = stack.pop()
        if step < total_nodes:  # Уникаємо виходу за межі масиву кольорів
            visited_nodes[node.id] = colors[step]
        draw_tree(tree_root, visited_nodes)
        time.sleep(0.8)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        step += 1




# Генеруємо купу
heap = [random.randint(1, 100) for _ in range(10)]
heapq.heapify(heap)

# Побудова дерева
root = build_tree_from_heap(heap)

# Візуалізація обходу BFS
print("Обхід у ширину (BFS):")
bfs_traversal(root)

# Візуалізація обходу DFS
print("Обхід у глибину (DFS):")
dfs_traversal(root)
