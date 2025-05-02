#!/usr/bin/env python3
"""
Ce module fournit une fonction utilitaire pour calculer les index de début et de fin
pour la pagination basée sur un numéro de page et une taille de page.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retourne un tuple d'index de début et de fin pour une configuration de pagination donnée.

    Args:
        page (int): Le numéro de page actuel (indexé à partir de 1).
        page_size (int): Le nombre d'éléments par page.

    Returns:
        Tuple[int, int]: Un tuple contenant l'index de début et l'index de fin
                         pour les éléments de la page actuelle.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
