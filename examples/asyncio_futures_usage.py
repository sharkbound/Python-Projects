import asyncio
from asyncio import Future, TimeoutError
from typing import List, Callable, Tuple

wait_queue: List[Tuple[Future, Callable]] = []
queue = []


async def message_listener():
    while True:
        if queue:
            done = []
            item = queue.pop()
            for i, (future, predicate) in enumerate(wait_queue):
                if predicate(item):
                    future.set_result(item)
                    done.append(i)

            for i in reversed(done):
                del wait_queue[i]

        await asyncio.sleep(1)


async def delayed_append(delay, item):
    await asyncio.sleep(delay)
    queue.append(item)


def wait_until_message(predicate, timeout=30, default=None):
    future = asyncio.get_event_loop().create_future()
    wait_queue.append((future, predicate))

    async def _timeout_catcher():
        try:
            return await asyncio.wait_for(future, timeout)
        except TimeoutError:
            return default

    return _timeout_catcher()


async def main():
    asyncio.create_task(message_listener())
    asyncio.create_task(delayed_append(1, '2'))
    asyncio.create_task(delayed_append(1, '1'))
    asyncio.create_task(delayed_append(1, '1'))

    def check(x):
        if x != '1':
            raise ValueError("NO")
        return True

    for _ in range(3):
        value = await wait_until_message(check, timeout=3)
        print(value)


asyncio.run(main())
