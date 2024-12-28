import asyncio
import time


def do_task(task):
    print(f"Doing {task}")
    time.sleep(1)
    print(f"Done with {task}")


def consecutive_execution():
    start = time.perf_counter()
    tasks = ["order parcel", "make coffee", "send email"]
    for task in tasks:
        do_task(task)
    end = time.perf_counter()
    print(f"Consecutive tasks finished in {end - start:.2f} seconds")


async def do_task_async(task):
    print(f"Doing {task}")
    await asyncio.sleep(1)
    print(f"Done with {task}")


async def async_execution():
    start = time.perf_counter()
    todo = ["order parcel", "make coffee", "send email"]
    tasks = [asyncio.create_task(do_task_async(task)) for task in todo]
    done, pending = await asyncio.wait(tasks, timeout=2)
    """
    done & pending can be used to handle tasks that are done and pending

    Also, you can use asyncio.gather() to run all tasks concurrently:
    coroutines = [do_task_async(task) for task in todo]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    
    Third method in Python 3.11+:
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(do_task_async(task)) for task in todo]
    """
    end = time.perf_counter()
    print(f"Async tasks finished in {end - start:.2f} seconds")


if __name__ == "__main__":
    print("Running consecutive_execution")
    consecutive_execution()
    print("---------------------------\nRunning async_execution")
    asyncio.run(async_execution())
