{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtsP3TM8Rt+A/7PDq2unT6",
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
        "<a href=\"https://colab.research.google.com/github/sucinursania/Praktikum_Search_Algorithms/blob/main/Latihan_DFS.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h8v-BXqGyhsl",
        "outputId": "9b2f9131-175b-41ad-d648-bc0269983d72"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Berikut adalah Penelusuran Depth First (dimulai dari node 2)\n",
            "2 0 1 3 "
          ]
        }
      ],
      "source": [
        "# pyhton3 program to print DFS traversal\n",
        "# from a given graph\n",
        "from collections import defaultdict\n",
        "\n",
        "# Kelas ini merepresentasikan sebuah graf yang diarahkan\n",
        "# menggunakan representasi daftar kejadian\n",
        "class Graph:\n",
        "\n",
        "  # Konstruktor\n",
        "    def __init__(self):\n",
        "        # Kamus default untuk menyimpan graf\n",
        "        self.graph = defaultdict(list)\n",
        "\n",
        "  # Fungsi untuk menambahkan tepi ke graf\n",
        "    def addEdge(self, u, v):\n",
        "        self.graph[u].append(v)\n",
        "\n",
        "  # Fungsi yang digunakan oleh DFS\n",
        "    def DFSUtil(self, v, visited):\n",
        "        # Tandai node saat ini sebagai sudah dikunjungi\n",
        "        # dan cetak\n",
        "        visited.add(v)\n",
        "        print(v, end=' ')\n",
        "\n",
        "        # Panggil rekursif untuk semua titik ujung\n",
        "        # yang berdekatan dengan titik ini\n",
        "        for neighbour in self.graph[v]:\n",
        "            if neighbour not in visited:\n",
        "                self.DFSUtil(neighbour, visited)\n",
        " # Fungsi untuk melakukan penelusuran DFS. Ini menggunakan\n",
        " # DFSUtil() rekursif\n",
        "    def DFS(self, v):\n",
        "\n",
        "        # Buat himpunan untuk menyimpan node yang sudah dikunjungi\n",
        "        visited = set()\n",
        "\n",
        "        # Panggil fungsi bantu rekursif\n",
        "        # untuk mencetak penelusuran DFS\n",
        "        self.DFSUtil(v, visited)\n",
        "\n",
        "# Kode pengguna\n",
        "if __name__ == \"__main__\":\n",
        "    g = Graph()\n",
        "    g.addEdge(0, 1)\n",
        "    g.addEdge(0, 2)\n",
        "    g.addEdge(1, 2)\n",
        "    g.addEdge(2, 0)\n",
        "    g.addEdge(2, 3)\n",
        "    g.addEdge(3, 3)\n",
        "\n",
        "    print(\"Berikut adalah Penelusuran Depth First (dimulai dari node 2)\")\n",
        "\n",
        "    # Panggilan fungsi\n",
        "    g.DFS(2)\n",
        "# kode ini disumbangkan oleh Neelam\n",
        "\n"
      ]
    }
  ]
}
