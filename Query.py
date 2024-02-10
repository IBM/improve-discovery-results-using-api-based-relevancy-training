import json
import csv
import DiscoveryDetails as dt

output_file = open("./training_file.tsv", "w")
writer = csv.writer(output_file, delimiter="\t")
try:
    with open("./Questions.txt", encoding="Windows 1252") as questions:
        noOfQuestions = 0
        for line in questions:
            print("Question No = " + str(noOfQuestions + 1))
            question = line.replace("\n", "")
            print("Question = " + question)

            question = "%s" % (question)

            # run Discovery query to get results from untrained service
            result = dt.discovery.query(
                project_id=dt.project_id,
                query=question,
                count=5
            ).get_result()

            #print("Query Response = " + json.dumps(result))

            # create a row for each query and results
            result_list = [question]
            for resultDoc in result["results"]:
                id = resultDoc["document_id"]
                text = resultDoc["text"]
                if(len(text) > 1000):
                    text = text[:1000]
                # leave a space to enter a relevance label for each doc
                result_list.extend([id, text, ' '])

            # write the row to the file
            writer.writerow(result_list)
            noOfQuestions = noOfQuestions + 1
            print("==========================================================")
            print("")
    print("tsv file with questions and query results created")
    print("Number of questions processed = " + str(noOfQuestions))
    output_file.close()
except Exception as e:
    print("Exception occurred ####### ")
    print(e)
