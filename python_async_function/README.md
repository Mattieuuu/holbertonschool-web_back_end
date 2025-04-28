# Programmation Asynchrone en Python

## Table des matières
1. [Introduction](#introduction)
2. [Concepts Clés](#concepts-clés)
3. [Composants](#composants)
4. [Fonctionnement](#fonctionnement)
5. [Tâches du Projet](#tâches-du-projet)
6. [Bonnes Pratiques](#bonnes-pratiques)

## Introduction
La programmation asynchrone permet aux opérations de s'exécuter indépendamment du flux principal du programme. Au lieu d'une exécution séquentielle, elle offre une exécution concurrente des tâches.

### Comparaison des Modes d'Exécution
```
Exécution Séquentielle :
Tâche A -----> Tâche B -----> Tâche C -----> Fin

Exécution Asynchrone :
Tâche A ---->
Tâche B -------->
Tâche C -->
     Fin
```

## Concepts Clés
### Coroutines
Les coroutines sont des fonctions spéciales qui peuvent être interrompues et reprises.

```python
async def exemple_coroutine():
    await une_operation()
    return resultat
```

### Boucle d'Événements
```
┌───────────────────────┐
│ Boucle d'Événements   │
│  ┌────────────────┐   │
│  │ File d'Attente │   │
│  └────────────────┘   │
│          ↑↓          │
│  ┌────────────────┐   │
│  │   Coroutines   │   │
│  └────────────────┘   │
└───────────────────────┘
```

## Composants
1. **Coroutines**
   - Déclarées avec `async def`
   - Utilisent `await` pour les opérations asynchrones
   - Retournent des valeurs avec `return`

2. **Tasks**
   - Encapsulent les coroutines
   - Gérées par la boucle d'événements
   - Permettent le suivi et l'annulation

## Fonctionnement
```
Coroutine ──> Création de Tâche ──> File d'Attente ──> Exécution
                    ↑                      │
                    └──────────────────────┘
```

## Tâches du Projet

### Tâche 0: Syntaxe Async de Base
**Objectif**: Créer une coroutine pour délais aléatoires
```python
async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
```

### Tâche 1: Coroutines Multiples
**Flux de Processus**:
```
Création n Tâches ──> Planification ──> Collecte Résultats
        │                  │                   │
        v                  v                   v
  wait_random()    Exécution Parallèle   Tri Résultats
```

### Tâche 2: Mesure du Temps
**Processus**:
```
Temps Début ──> Exécution ──> Temps Fin ──> Calcul Moyenne
```

### Tâche 3: Création de Tâches
**Cycle de Vie**:
```
Coroutine ──> Création ──> Planifiée ──> En Cours ──> Terminée
```

### Tâche 4: Implémentation Avancée
**Structure**:
```
Création Tâches ──> Exécution Parallèle ──> Gestion Résultats
       │                    │                      │
       v                    v                      v
task_wait_random()   Boucle d'Événements    Délais Triés
```

## Bonnes Pratiques

### 1. Gestion des Erreurs
```python
try:
    await operation_async()
except Exception as e:
    gerer_erreur(e)
```

### 2. Gestion des Tâches
- Attendre toutes les tâches créées
- Utiliser `asyncio.gather()` pour les tâches multiples
- Gérer les annulations proprement

### 3. Optimisation
- Éviter de bloquer la boucle d'événements
- Utiliser `create_task()` pour la concurrence
- Implémenter une gestion d'erreurs robuste

## Avantages
1. **Performance**
   - Utilisation optimale des ressources
   - Réduction des temps d'attente

2. **Évolutivité**
   - Gestion efficace des opérations concurrentes
   - Optimisation des opérations I/O

3. **Efficacité**
   - Utilisation d'un seul thread
   - Empreinte mémoire optimisée