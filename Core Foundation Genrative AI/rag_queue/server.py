from fastapi import FastAPI, Query
from .rq_client import queue
from .worker import process_query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "server is running..."}

@app.post('/chat')
def chat(
    query: str = Query(..., description="The chat query of user")
):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}

@app.get("/job_status")
def get_result(
    job_id: str = Query(..., description="Job ID")
):
    job = queue.fetch_job(job_id)
    if job is None:
        return {"error": "Job not found"}
    return {"status": job.get_status(), "result": job.result}
