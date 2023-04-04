#!/usr/bin/env python3
""" Asyn Generator"""

import asyncio
from typying import Generator
import random


async def async_generator() -> Generator[float, None, None]:
	"""Using the random module. The coroutine will loop 10 times,
	each time asynchronously wait 1 second, then yield a random number.
	number between 0 and 10."""
	for i in range(10):
		await asyncio.sleep(1)
		yield random.uniform(0, 10)
