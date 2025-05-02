#!/usr/bin/env python3
"""
Pagination hypermedia résistante aux suppressions
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Classe Serveur pour paginer une base de données de prénoms populaires.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Dataset mis en cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexé par position de tri, commençant à 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10
            ) -> Dict[str, Any]:
        """
        Renvoie un dictionnaire avec les données de pagination résistante
        aux suppressions.

        Args:
            index: L'index de début actuel de la page de retour
            page_size: La taille de page actuelle

        Returns:
            Dictionnaire contenant les paires clé-valeur suivantes:
                - index: l'index de début actuel de la page de retour
                - next_index: le prochain index à interroger
                - page_size: la taille de page actuelle
                - data: la page actuelle du dataset
        """
        indexed_dataset = self.indexed_dataset()
        dataset_size = len(indexed_dataset)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < dataset_size

        data = []
        current_idx = index
        count = 0

        while count < page_size and current_idx < dataset_size:
            if current_idx in indexed_dataset:
                data.append(indexed_dataset[current_idx])
                count += 1
            current_idx += 1

        next_idx = current_idx

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_idx
        }
