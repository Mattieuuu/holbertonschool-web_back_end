#!/usr/bin/env python3
"""
Pagination simple pour les données CSV
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Renvoie un tuple de taille deux contenant un index de début et un index de fin
    correspondant à la plage d'index à renvoyer dans une liste pour ces
    paramètres de pagination particuliers.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Classe Serveur pour paginer une base de données de prénoms populaires.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Dataset mis en cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Renvoie la page appropriée du dataset.

        Args:
            page: Numéro de page (indexé à partir de 1)
            page_size: Nombre d'éléments par page

        Returns:
            Liste des lignes pour la page demandée
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
    