from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

app = FastAPI()

# Load vector DB
db = FAISS.load_local("vector_db", OpenAIEmbeddings())
retriever = db.as_retriever()

# Setup LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer(request: QuestionRequest):
    answer = qa_chain.run(request.question)
    
    # Stubbed: replace with real link-matching if needed
    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/example-link",
            "text": "Example relevant discussion."
        }
    ]
    
    return {
        "answer": answer,
        "links": links
    }
