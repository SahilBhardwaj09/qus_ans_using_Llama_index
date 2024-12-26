from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv
import os
import sys

load_dotenv()


def main(url: str)-> None:
    document=SimpleDirectoryReader(url).load_data()
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.search("Tell me something about Generative AI")
    print(response)


if __name__ == "__main__":
    main(url=r"E:/Ineuron Gen AI/Youtube/Notes_Practical/02_Generative AI Complete History/GenAI_History.pdf")
