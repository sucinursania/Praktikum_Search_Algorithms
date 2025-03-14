{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNeZCK/Fq4SVpSiJSPPyj0j",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sucinursania/Praktikum_Search_Algorithms/blob/main/Latihan_BFS.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "X0zRMbtLzCcG",
        "outputId": "38f312e4-5e7b-4320-f8b1-342aa2bcc865",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Following is Breadth First Traversal: \n",
            "0 1 2 3 "
          ]
        }
      ],
      "source": [
        "# BFS algorithm in Python\n",
        "\n",
        "import collections\n",
        "\n",
        "# BFS algorithm\n",
        "def bfs(graph, root):\n",
        "    visited, queue = set(), collections.deque([root])\n",
        "    visited.add(root)\n",
        "\n",
        "    while queue:\n",
        "        # Dequeue a vertex from queue\n",
        "        vertex = queue.popleft()\n",
        "        print(str(vertex) + \" \", end=\"\")\n",
        "\n",
        "        # If not visited, mark it as visited, and enqueue it\n",
        "        for neighbour in graph[vertex]:\n",
        "            if neighbour not in visited: # untuk node yang belum dikunjungi\n",
        "                visited.add(neighbour)\n",
        "                queue.append(neighbour)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}\n",
        "    print(\"Following is Breadth First Traversal: \")\n",
        "    bfs(graph, 0)\n"
      ]
    }
  ]
}
