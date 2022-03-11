#!/usr/bin/env python3
"""
asynico.Task modul
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return asynico.Task
    """
    delay_task = asyncio.create_task(wait_random(max_delay))
    return delay_task
