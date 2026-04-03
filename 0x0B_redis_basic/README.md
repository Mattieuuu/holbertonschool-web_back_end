# 0x0B. Redis Basic

This directory contains exercises for learning how to use Redis with Python.

## Files

- `exercise.py`: defines a `Cache` class using `redis.Redis`.

## Requirements

- Python 3.9+
- Redis server running locally
- `redis` Python package

## Quick Start

1. Start Redis:

	```bash
	service redis-server start
	```

2. Install dependency:

	```bash
	pip3 install redis
	```

3. Run your script that uses `Cache`:

	```python
	from exercise import Cache

	cache = Cache()
	key = cache.store(b"hello")
	print(key)
	```
