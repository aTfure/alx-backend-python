#!/usr/bin/env python3
"""
Alter wait_n to a new function task_wait_n. Nearly identical except the 
new function is being called."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values).
	List of delay are in ascending order"""
    delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
