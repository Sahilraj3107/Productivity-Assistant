Problem
Knowledge workers often struggle to retrieve actionable insights from scattered meeting notes, reminders, and documents efficiently.

Solution
This project implements a REST-based AI productivity assistant that combines Retrieval-Augmented Generation (RAG) with structured document ingestion to enable low-latency, context-aware querying over personal productivity data.

The system is designed as a backend-first AI service, emphasizing modularity, performance, and deployability.

Key Design Decisions & Trade-offs

Embedding Model Selection
Chose all-MiniLM-L6-v2 to balance semantic accuracy with low inference latency.

Vector Store
Used ChromaDB for fast local development and predictable query performance.

RAG over Fine-tuning
Enables real-time updates without retraining and reduces operational cost.

API-First Design
Allows easy integration with web or mobile frontends.

Core Features

RESTful API for querying notes, reminders, and events

Automated document ingestion and chunking

Semantic search using vector embeddings

Context-aware LLM responses

Sub-3s average response latency

Containerized deployment for portability

Deployment Architecture

Dockerized application

Container registry hosted on AWS ECR

Deployed on AWS EC2

CI/CD pipeline implemented using GitHub Actions for automated builds and deployments
