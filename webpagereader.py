from llama_index.core import VectorStoreIndex
from llama_index.readers.web import SimpleWebPageReader
from dotenv import load_dotenv
import os

load_dotenv()


def main(url: str)-> None:
    document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.search("What is the capital of France?")
    print(response)


if __name__ == "__main__":
    main("https://en.wikipedia.org/wiki/Paris")
