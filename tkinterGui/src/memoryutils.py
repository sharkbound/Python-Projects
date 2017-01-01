import sys
import memory_profiler


def printmemory():
    print(f"Current Memory Usage: {str(memory_profiler.memory_usage()).replace('[', '').replace(']', '')}MB")


def getmemory():
    return float(str(memory_profiler.memory_usage()).replace('[', '').replace(']', ''))
