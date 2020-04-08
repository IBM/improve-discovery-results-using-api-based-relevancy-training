import json
import csv
import requests
from requests.auth import HTTPBasicAuth
import DiscoveryDetails as dt
from ibm_cloud_sdk_core.api_exception import ApiException

def delete_and_add_example(query_id, document_id, relevance):
    deleteResult = dt.discovery.delete_training_example(dt.environment_id, dt.collection_id, query_id, document_id)
    print("Delete result = " + json.dumps(deleteResult.get_result()))
    add_example_result = dt.discovery.create_training_example(dt.environment_id, dt.collection_id, query_id, document_id=document_id, cross_reference=None, relevance=relevance)
    print("add_example_result = " + json.dumps(add_example_result.get_result()))
        


def create_training_example(query_id, document_id, relevance):
    print("---")
    print("document_id = " + str(document_id))
    print("relevance = " + str(relevance))
    try:
        create_result = dt.discovery.create_training_example(dt.environment_id, dt.collection_id, query_id, document_id=document_id, cross_reference=None, relevance=relevance)
        print("create_result = " + json.dumps(create_result))
    except ApiException as apiE:
        if( apiE.code == 409 ): #Example already exists. Delete it and add
            print("Example exists. Delete example and add example with new relevancy score")
            delete_and_add_example(query_id, document_id, relevance)

#function for posting to training data endpoint
def training_post(training_obj):
    nlQuery = training_obj["natural_language_query"]
    examples = training_obj["examples"]
    add_training_data_result = None
    try:
        add_training_data_result = dt.discovery.add_training_data(dt.environment_id, dt.collection_id, natural_language_query=nlQuery, filter=None, examples=examples)
    except ApiException as apiE:
        # Check if the query already exists
        try:
            if( apiE.code == 409 ): # Query already exists
                error = apiE.message
                partAfterQueryId = error.split("id ",1)[1]
                query_id = partAfterQueryId.split(" ",1)[0]
                print("Query already exists. Add examples")
                print("query_id = " + str(query_id))
                
                for example in training_obj["examples"]:
                    create_training_example(query_id, example["document_id"], example["relevance"])
            else:
                print("ApiException occurred in training_post when calling discovery.add_training_data api with error code = " + str(apiE.code))
                print(apiE)
                raise Exception(apiE)
        except Exception as e:
            print("Exception occurred in training_post when calling discovery.add_training_data api")
            print(e)
            raise Exception(e)

#open the training file and create new training data objects
with open("./training_file.tsv",'r') as training_doc:

    training_csv = csv.reader(training_doc, delimiter='\t')    
    
    #create a new object for each example 
    noOfQuestions = 0
    for row in training_csv:
        noOfExamples = int((len(row) - 1)/3)
        training_obj = {}
        training_obj["examples"] = []
        training_obj["natural_language_query"] = row[0]
        noOfQuestions = noOfQuestions + 1
        print("Question No. " + str(noOfQuestions))
        print("Question = " + training_obj["natural_language_query"])
        i = 1 
        for j in range(1, noOfExamples + 1):
            example_obj = {}
            if( row[i+2] and row[i+2].strip() == ""):
                row[i+2] = 0
            example_obj["relevance"] = row[i+2]
            example_obj["document_id"] = row[i]
            training_obj["examples"].append(example_obj)
            i = i + 3 

        training_post(training_obj)
        print("----------------")
    print("Number of questions = " + str(noOfQuestions))
    print("**************")
    print("************** RELEVANCY TRAINING COMPLETED **************")
    print("**************")

