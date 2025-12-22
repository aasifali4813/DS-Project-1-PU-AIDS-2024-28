from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

backend_app = FastAPI()

class predict_placement(BaseModel):

    iq:int[40,160]
    previous_sem_result:float[0,10]
    cgpa:float[0,10]
    communcation_skills:int[0,10]
    projects_completed:int[]

