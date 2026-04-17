# Queuing System in JS - Redis Setup Guide

This project uses Redis as the backend for queue-related exercises in JavaScript.
The steps below show how to install Redis 6.0.10, start it, verify that it works,
and prepare the project data file.

## Prerequisites

- Ubuntu or any Linux environment with build tools
- wget
- make
- gcc

If needed, install build tools first:

```bash
sudo apt update
sudo apt install -y build-essential wget
```

## 1) Download and extract Redis 6.0.10

```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
```

## 2) Build Redis

```bash
make
```

## 3) Start Redis

Run Redis in the background:

```bash
src/redis-server &
```

## 4) Verify Redis is running

```bash
src/redis-cli ping
```

Expected output:

```text
PONG
```

## 5) Quick key-value check

```bash
src/redis-cli set Holberton School
src/redis-cli get Holberton
```

Expected results:

- set command returns OK
- get command returns School

## 6) Stop Redis

Find the Redis process and stop it:

```bash
ps aux | grep redis-server
kill <REDIS_PID>
```

## 7) Project data file

After running Redis, copy the generated dump.rdb file to the root of this
project folder:

- queuing_system_in_js/dump.rdb

## Verification checklist

- Redis responds to ping with PONG
- The Holberton key stores and returns School
- dump.rdb exists in the project root

## Project files

- README.md: setup and usage instructions
- dump.rdb: Redis dump file used by the project

## Troubleshooting

- If redis-server is not found, install Redis or run it from the compiled source
	directory.
- If tests fail with ECONNREFUSED 127.0.0.1:6379, Redis is not running.
- If port 6379 is already in use, stop the existing Redis instance or update
	your local configuration.
