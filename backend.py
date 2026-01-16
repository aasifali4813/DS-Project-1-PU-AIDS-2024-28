import numpy as np
import scipy.stats as s
import pickle
import config
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Query
from typing import Annotated

def determine_placement_posterior_probability(input_features):

    input_features = np.array(input_features)
    input_features = input_features.reshape(1,input_features.shape[0])
    eig_vectors = np.load("eigen_vectors.npy")
    new_input_features = np.matmul(input_features,eig_vectors)

    placement_equals_1_likelihood = 1.0
    placement_equals_0_likelihood = 1.0

    with open("likelihood_distribution_params.pkl","rb") as file_handle:
        likelihood_distribution_params = pickle.load(file_handle)

    for input_feat, input_feat_value in zip(config.INPUT_FEATURE_NAMES, new_input_features):
        mu_0, sigma_0 = likelihood_distribution_params[0][input_feat]
        mu_1, sigma_1 = likelihood_distribution_params[1][input_feat]
        
        p_input_feature_on_0_placement = s.norm.pdf(input_feat_value,mu_0,sigma_0)
        p_input_feature_on_1_placement = s.norm.pdf(input_feat_value,mu_1,sigma_1)

        placement_equals_0_likelihood = placement_equals_0_likelihood * p_input_feature_on_0_placement
        placement_equals_1_likelihood = placement_equals_1_likelihood * p_input_feature_on_1_placement

    placement_equals_0_posterior = placement_equals_0_likelihood * (1-config.PLACEMENT_EQUALS_1_PRIOR)
    placement_equals_1_posterior = placement_equals_1_likelihood * config.PLACEMENT_EQUALS_1_PRIOR

    if placement_equals_1_posterior[0] > placement_equals_0_posterior[0]:
        return {"result":"Given your inputs, most likely you are going to get placed and the probability of you getting placed is roughly {}".format(placement_equals_1_posterior[0])}
    else:
        return {"result":"Given your inputs, most likely you are not going to get placed and the probability of you getting placed is roughly {}".format(placement_equals_1_posterior[0])}
    

app = FastAPI()


class InputFeatureVector(BaseModel):

    iq:Annotated[int, Query(ge=40,le=160)]
    previous_semester_result:Annotated[float, Query(ge=0,le=10)]
    cgpa:Annotated[float, Query(ge=0,le=10)]
    communication_skills:Annotated[int, Query(ge=0,le=10)]
    projects_completed:Annotated[int, Query(ge=0,le=10)]

@app.get("/")
def home_page():

    return "This web App predicts the Probability of a Student being Placed based on five factors"
    
    
@app.post("/compute-probability")
def compute_probability(input_features:InputFeatureVector):
    input_feature_values_list = list()
    for input_feature_name, input_feature_value in InputFeatureVector.model_fields.items():
        input_feature_values_list.append(getattr(input_features,input_feature_name))
    response = determine_placement_posterior_probability(input_feature_values_list)
    return response
