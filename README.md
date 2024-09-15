# Business QA Chatbot

## Overview

The Business QA Chatbot project provides a conversational interface for business-related queries using a Streamlit application. It leverages advanced NLP and machine learning techniques to deliver accurate responses based on data extracted from PDF documents.

## Project Structure

- `streamlit_app/`: Contains the main Python files and Docker configuration for running the Streamlit app.
  - `Dockerfile`: Docker configuration for building and running the application.
  - `main.py`: The main Streamlit application script.
  - `requirements.txt`: Lists all the required Python packages for the application.
- `Business_QA_Chatbot.pynb`: Jupyter Notebook for interactive development and testing, recommended to use in Google Colab.
- `streamlit_run/data/`: Directory containing PDF files used to train the model.
- `vectorize_documentation.py`: Script to convert PDF data into a vector database using ChromaDB.

## Installation

### Manual Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/business-qa-chatbot.git
   cd business-qa-chatbot
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```
3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Rename Configuration Files**

    Rename `sample_config.json` to `config.json` and replace the placeholder `"YOUR_API_KEYS"` with your actual API key.

5. **Run the Streamlit App**

    Navigate to the `streamlit_app/` directory and start the Streamlit application:
    ```bash
    `streamlit run main.py`
    ```

## Docker Deployment
1. **Build the Docker Image**

    Navigate to the `streamlit_app/` folder where the `Dockerfile` is located. Build the Docker image using:
    
    ```bash
    docker build -t business-qa-chatbot .
    ```

2. **Run the Docker Container**

    After building the image, run the Docker container with:
    
    ```bash
    docker run -p 8080:8080 business-qa-chatbot
    ```

3. **Access the Application**

    Open your web browser and navigate to `http://localhost:8080` to access the Streamlit app.

## Docker Image Handling
### Pulling the Docker Image
To get the latest Docker image from Docker Hub, use:

```bash
docker pull gauravwankhede/business-qa-chatbot:latest
```
### Building the Docker Image Locally

1. **Navigate to the Directory Containing the Dockerfile**

```bash
cd path/to/streamlit_app
```
2. **Build the Docker Image**

```bash
docker build -t business-qa-chatbot .
```

### Running the Docker Container
1. **Run the Docker Container**

```bash
docker run -p 8080:8080 business-qa-chatbot
```

## PDF Data
All PDF files used for training the model are stored in the `streamlit_run/data/` folder. Ensure these files are correctly placed for the application to access.

## Vectorization
The `vectorize_documentation.py` file converts PDF data into a vector database using:

* `UnstructuredPDFLoader from langchain_community` for loading PDF documents.
* `RecursiveCharacterTextSplitter from langchain_text_splitters` for splitting text.
* `HuggingFaceEmbeddings from langchain_huggingface` for generating embeddings.
* `Chroma from langchain_chroma` for managing the vector database.

## Development
For interactive development and testing, use the `Business_QA_Chatbot.pynb` Jupyter Notebook. It is recommended to run this notebook in Google Colab.


## Contact
For any questions or feedback, please contact pgywww@gmail.com.