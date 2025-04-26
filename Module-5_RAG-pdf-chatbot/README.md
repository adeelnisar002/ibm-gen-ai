# Personal Data Assistant with Groq LLM

This project implements a PDF-based chatbot using Groq's LLM (Large Language Model) and LangChain. The chatbot can analyze PDF documents and answer questions about their content using state-of-the-art language models.

## Features

- PDF document analysis and processing
- Interactive Q&A based on document content
- Fast response times using Groq's high-performance LLMs
- Support for multiple document types
- Beautiful and intuitive web interface

## Screenshots

Here are some screenshots of the application in action:

![Screenshot 2025-04-27 024858](https://github.com/user-attachments/assets/a20cc3eb-b611-4f8c-ae54-d32fd6184034)

![image](https://github.com/user-attachments/assets/73bc9518-ef42-4bae-8a8b-7349bfffbb74)



## Technology Stack

- **LLM Provider**: Groq (using llama3-70b-8192 model)
- **Framework**: LangChain with langchain-groq integration
- **Embeddings**: HuggingFace Instructor Embeddings (sentence-transformers/all-MiniLM-L6-v2)
- **Vector Store**: Chroma
- **Web Framework**: Flask
- **Frontend**: HTML/CSS/JavaScript

## Prerequisites

- Python 3.10 or higher
- Groq API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Groq API key:
   - Create a `.env` file in the project root
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your-api-key-here
     ```

## Usage

1. Start the server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

3. Upload a PDF document and start asking questions!

## Configuration

The chatbot can be configured through the following parameters in `worker.py`:

- `temperature`: Controls response creativity (currently set to 0.3)
- `model_name`: The Groq model to use (currently using "llama3-70b-8192")
- `chunk_size`: Size of text chunks for processing (currently 1024)
- `chunk_overlap`: Overlap between chunks (currently 64)

## How It Works

1. **Document Processing**:
   - PDF documents are loaded and split into manageable chunks
   - Text chunks are converted into embeddings using HuggingFace's Instructor Embeddings
   - Embeddings are stored in a Chroma vector store

2. **Question Answering**:
   - User questions are processed through the Groq LLM
   - Relevant document sections are retrieved using MMR search
   - The LLM generates contextual responses based on the document content
