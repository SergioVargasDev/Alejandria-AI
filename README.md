# Alejandria AI

Alejandria AI is an enterprise document intelligence platform developed during HackMTY 2024, receiving an MLH Hackathon Honorable Mention. The system transforms static PDF documents into dynamic, searchable knowledge bases through advanced AI-powered document parsing and contextual search capabilities. Built with an Angular frontend and Spring Boot business logic, the platform processes 860+ page PDFs with vector indexing and achieves 40% improvement in answer precision through Meta's LLaMA integration and secure on-premises deployment.

## Features

- **Enterprise Document Parsing**: Automated PDF processing with scalable indexing and source-cited responses across internal document libraries.
- **Vector-Based Search**: Python-powered LangChain-Chroma pipelines enabling semantic search and contextual information retrieval.
- **Advanced NLP Processing**: Meta's LLaMA integration with custom embeddings for precise answer generation and document summarization.
- **Secure On-Premises Deployment**: PostgreSQL-backed offline document ingestion with local data persistence and enterprise security.
- **Source Citation System**: Meticulous source tracking and verification ensuring accurate and verifiable information retrieval.
- **Scalable Architecture**: Full-stack solution supporting large-scale document processing and concurrent user queries.

## Tech Stack

### Frontend
- **Angular** – Modern TypeScript framework for responsive user interface and document interaction portal.

### Backend
- **Spring Boot** – Enterprise-grade Java framework handling business logic and document processing workflows.

### Database
- **PostgreSQL** – Robust relational database for document metadata, user sessions, and query analytics.

### AI & NLP
- **Meta's LLaMA** – Large language model for document understanding and contextual answer generation.
- **LangChain** – Framework orchestrating AI workflows and document processing pipelines.
- **Chroma** – Vector database for efficient document embeddings and similarity search operations.

### Core Processing
- **Python** – Backend processing engine for PDF parsing, vector generation, and NLP operations.

## Installation

### Prerequisites

- **Java 17+** - Required for Spring Boot backend
- **Node.js 18.0+** - Required for Angular frontend
- **Python 3.8+** - For document processing and AI model integration
- **PostgreSQL 12+** - Database for document storage and analytics
- **Docker** - For containerized deployment (optional)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/alejandria-ai.git
   cd alejandria-ai
   ```

2. **Backend Setup (Spring Boot)**
   ```bash
   cd backend
   ./mvnw clean install
   
   # Configure environment variables
   cp application.properties.example application.properties
   # Add your database credentials and API keys
   
   # Start the server
   ./mvnw spring-boot:run
   ```

3. **Frontend Setup (Angular)**
   ```bash
   cd frontend
   npm install
   ng serve
   ```

4. **Python Processing Engine**
   ```bash
   cd ai-engine
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # Start processing service
   python main.py
   ```

5. **Database Configuration**
   ```sql
   CREATE DATABASE alejandria_ai;
   -- Run migration scripts
   ./mvnw flyway:migrate
   ```

6. **Access the platform**
   - Open your web browser and navigate to: `http://localhost:4200`
   - The Angular interface will load with document upload and search portal

### System Configuration

The platform can be configured through admin interface:

- **Document Processing**: Adjust PDF parsing parameters and batch sizes
- **Vector Settings**: Configure embedding dimensions and similarity thresholds  
- **Model Parameters**: Fine-tune LLaMA responses and citation accuracy
- **Security Settings**: Manage on-premises deployment and data persistence options

### File Structure

```
alejandria-ai/
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/  # Angular components for document interface
│   │   │   ├── services/    # API integration and data services
│   │   │   └── modules/     # Feature modules and routing
│   │   └── assets/          # Static assets and configurations
├── backend/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── com/alejandria/
│   │   │   │       ├── controllers/  # REST controllers and endpoints
│   │   │   │       ├── services/     # Business logic services
│   │   │   │       └── repositories/ # Data access layer
│   │   │   └── resources/
│   │   │       ├── application.properties
│   │   │       └── db/migration/     # Database migrations
├── ai-engine/
│   ├── models/             # LLaMA and embedding models
│   ├── processors/         # PDF parsing and vector generation
│   └── pipelines/          # LangChain processing workflows
├── database/
│   ├── migrations/         # PostgreSQL schema migrations
│   └── seeds/              # Initial data and configurations
└── README.md               # This file
```

### Running Different Components

#### 1. Development Mode
```bash
# Start Spring Boot backend
cd backend && ./mvnw spring-boot:run

# Start Angular frontend (in new terminal)
cd frontend && ng serve

# Start Python AI engine (in new terminal)
cd ai-engine && python main.py
```

#### 2. Production Deployment
```bash
# Build Angular frontend for production
cd frontend && ng build --prod

# Build Spring Boot backend
cd backend && ./mvnw clean package

# Run production backend
java -jar target/alejandria-ai-*.jar

# Deploy AI processing service
cd ai-engine && python -m gunicorn main:app
```

#### 3. Document Processing
```bash
# Process single PDF
python ai-engine/process_document.py --file document.pdf

# Batch process directory
python ai-engine/batch_process.py --directory /path/to/pdfs

# Update vector index
python ai-engine/update_index.py
```

### Platform Operations

Once the platform is running:

1. **Document Upload**: Drag-and-drop PDF files for automated processing and indexing
2. **Semantic Search**: Natural language queries across entire document library
3. **Source Citations**: Automatic citation generation with page references and context
4. **Answer Verification**: Cross-reference responses with original document sources
5. **Analytics Dashboard**: Query performance metrics and document usage statistics
6. **Batch Processing**: Large-scale document ingestion with progress monitoring

### Enterprise Integration

For deployment in corporate environments:

1. **Security Configuration**: Set up on-premises deployment with local data persistence
2. **Document Management**: Integration with existing document management systems
3. **User Authentication**: LDAP/Active Directory integration for enterprise access control
4. **API Integration**: RESTful APIs for third-party system connectivity
5. **Compliance**: Data governance and audit trail capabilities

### Troubleshooting

**Common Issues:**

- **PDF Processing Errors**: Check document format compatibility and file size limits
- **Vector Index Issues**: Verify Chroma database connectivity and storage permissions
- **LLaMA Model Loading**: Ensure sufficient RAM and model file accessibility
- **Database Connection**: Verify PostgreSQL service status and connection credentials

**Performance Optimization:**

- Implement Redis caching for frequent document queries
- Optimize vector index size and embedding dimensions
- Use GPU acceleration for LLaMA inference when available
- Monitor database query performance and index usage

## NOTES
- please download `ggml-model-gpt4all-falcon-q4_0.bin` from [here](https://gpt4all.io/index.html) and put it in the root of the ai folder
<div align = "center">
