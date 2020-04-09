## Short Name

Improve Watson Discovery Results using API based Relevancy Training

## Short Description

Improvise Watson Discovery Results by additional training with providing feedback with what default results are relevant and what are not.

## Author
Muralidhar Chavan (https://developer.ibm.com/profiles/muralidhar.chavan/)

## Code
https://github.com/IBM/improve-discovery-results-using-api-based-relevancy-training

## Video
NA

## Summary

Developers use the IBM Watson Discovery service to rapidly add a cognitive, search, and content analytics engine to applications. With that engine, they can identify patterns, trends, and insights from unstructured data that drive better decision making. Sometimes, you want to improvise the search results by providing additional training details. Relevance training is one such feature in Watson Discovery which provides additional training for more accurate search results. This code patterns shows how Relevancy training APIs can be used to Improvise search results in Watson Discovery.

## Description

Developers use the IBM Watson Discovery service to rapidly add a cognitive, search, and content analytics engine to applications. With that engine, they can identify patterns, trends, and insights from unstructured data that drive better decision making. With Watson Discovery, you can *ingest* (convert, enrich, clean, and normalize), store, and query data to extract actionable insights. In order to search and query, you need content that is injected and persisted in collections. You can learn more about developing applications with Watson Discovery by studying the [Cognitive discovery reference architecture](https://www.ibm.com/cloud/architecture/architectures/cognitiveDiscoveryDomain).

Relevancy Training is a powerful capability in Watson Discovery Service that can improve search accuracy if the right approach is taken. You can train Discovery to improve the relevance of query results for your particular organisation or subject area. When you provide a Discovery instance with *training data*, the service uses machine-learning Watson techniques to find signals in your content and questions. The service then reorders query results to display the most relevant results at the top. As you add more training data, the service instance becomes more accurate and sophisticated in the ordering of results it returns.

Relevancy training is optional; if the results of your queries meet your needs, no further training is necessary. For an overview of building use cases for training, see the blog post [How to get the most out of Relevancy Training](https://developer.ibm.com/dwblog/2017/get-relevancy-training/).

Relevancy training in Watson Discovery can be done in two ways as follows:

- Using Tooling. See [Improving result relevance with the tooling](https://cloud.ibm.com/docs/discovery?topic=discovery-improving-result-relevance-with-the-tooling) for more details.
- Using APIs. Watson Discovery provides APIs for performing Relevance Training.

If your Watson Discovery instance has fairly large number of questions for which relevance training needs to be done, then the tooling method might take much longer compared to the programattic (using APIs) way. Also, for using APIs, one need not be online connected to Discovery instance via browser.

This Code Pattern shows, with an example, how relevancy training can be achieved using APIs.


## Flow

<img src="./images/architecture.png" alt="Architecture" /> 

1. Client application sends natural language query for each of the queries that needs relevance training.
2. Watson Discovery return passages for each of the natural language query made.
3. The client application saves queries and corresponding passages in a TSV file, on local machine.
4. User assigns relevancy scores to documents and saves the file.
5. Application accesses file with updated relevancy scores.
6. Client application invokes APIs to update Discovery collection training using updated relevancy scores.
7. Client queries again to get improved results.


## Included components

* [Discovery service](https://cloud.ibm.com/docs/discovery?topic=discovery-getting-started): IBM Watson Discovery makes it possible to rapidly build cognitive, cloud-based exploration applications that unlock actionable insights hidden in unstructured data — including your own proprietary data, as well as public and third-party data.



## Featured technologies

* [Python](https://www.python.org/): Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

## Links

- [How to get the most out of Relevancy Training](https://developer.ibm.com/dwblog/2017/get-relevancy-training/)
- [Improving result relevance with the API](https://cloud.ibm.com/docs/discovery?topic=discovery-improving-result-relevance-with-the-api)

- [Watson Discovery](https://www.ibm.com/in-en/cloud/watson-discovery)