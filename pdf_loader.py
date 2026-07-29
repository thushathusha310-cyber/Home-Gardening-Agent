from langchain_community.document_loaders import PyPDFLoader
import os


def load_pdfs():

    documents = []

    folder = "data"

    for file in os.listdir(folder):
        if file.endswith(".pdf"):

            pdf_path = os.path.join(folder, file)

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            documents.extend(docs)

            print(file, "loaded")

    return documents


if __name__ == "__main__":
    docs = load_pdfs()
    print("Total pages:", len(docs))