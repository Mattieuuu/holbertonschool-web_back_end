# Caching

This project implements various caching systems in Python, demonstrating different cache replacement algorithms.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## Caching Concepts

### What is a Caching System?
A caching system is a temporary storage layer that stores frequently accessed data in a fast-access location. It improves performance by reducing the time needed to access data from slower storage systems.

### Cache Replacement Algorithms

1. **FIFO (First In First Out)**: The first item added to the cache is the first to be removed when space is needed.

2. **LIFO (Last In First Out)**: The last item added to the cache is the first to be removed when space is needed.

3. **LRU (Least Recently Used)**: The item that hasn't been accessed for the longest time is removed when space is needed.

4. **MRU (Most Recently Used)**: The item that was most recently accessed is removed when space is needed.

5. **LFU (Least Frequently Used)**: The item that has been accessed the fewest times is removed when space is needed.

### Purpose and Limits
- **Purpose**: Improve application performance by storing frequently accessed data in fast memory
- **Limits**: 
  - Limited storage capacity
  - Memory overhead for tracking cache state
  - Cache invalidation complexity
  - Potential for cache misses

## Files

- `base_caching.py`: Base class defining the caching interface
- `0-basic_cache.py`: Basic cache with no limit
- `1-fifo_cache.py`: FIFO cache implementation
- `2-lifo_cache.py`: LIFO cache implementation
- `3-lru_cache.py`: LRU cache implementation
- `4-mru_cache.py`: MRU cache implementation

## Requirements

- Python 3.9
- All files are executable
- All files follow pycodestyle (version 2.5)
- All modules, classes, and functions have documentation
- All files start with `#!/usr/bin/env python3`

## Usage

Each cache implementation inherits from `BaseCaching` and provides `put()` and `get()` methods for storing and retrieving data respectively.

Example:
```python
from basic_cache import BasicCache

cache = BasicCache()
cache.put("key", "value")
print(cache.get("key"))  # Output: value
```