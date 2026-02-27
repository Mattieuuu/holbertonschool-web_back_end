#!/usr/bin/env python3
"""
Mock test to demonstrate the main function output format
"""
import logging
from filtered_logger import get_logger

# Simulate what the main function does
logger = get_logger()

# Simulate a row from the database
row1_message = "name=Marlene Wood; email=hwestiii@att.net; phone=(473) 401-4253; ssn=261-72-6780; password=K5?BMNv; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;"

row2_message = "name=Belen Bailey; email=bcevc@yahoo.com; phone=(539) 233-4942; ssn=203-38-5395; password=^3EZ~TkX; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;"

print("Mock output showing how PII fields are filtered:\n")
logger.info(row1_message)
logger.info(row2_message)
