from langchain_community.document_loaders import UnstructuredPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings()

loader = DirectoryLoader(
    path="data",
    glob="./*.pdf",
    loader_cls=UnstructuredPDFLoader
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=5000,  # Larger chunk size to accommodate long paragraphs
    chunk_overlap=1000,  # Adjust overlap to ensure some context between paragraphs
    separators=["\n\n", "\n"]  # Prioritize splitting by paragraph, then single newlines
)



text_chunks = text_splitter.split_documents(documents)

# Output the chunks or append them as needed
for i, chunk in enumerate(text_chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")

vectordb = Chroma.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    persist_directory="vector_db"
)

print("Documents Vectorized")