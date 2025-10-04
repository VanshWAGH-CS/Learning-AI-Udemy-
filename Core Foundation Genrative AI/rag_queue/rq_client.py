from redis import Redis
from rq import Queue

# Connect to Redis
redis_conn = Redis(
    host="localhost",
    port=6379  # must be int, not str
)

# Create a queue
queue = Queue(connection=redis_conn)

# Example: enqueue a function
def example_task(x, y):
    return x + y

# Enqueue the function with arguments
job = queue.enqueue(example_task, 5, 7)

print(f"Job enqueued: {job.id}")
