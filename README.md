# Alejandria AI

Alejandria AI is an enterprise document intelligence platform developed during HackMTY 2024, receiving an MLH Hackathon Honorable Mention. The system transforms static PDF documents into dynamic, searchable knowledge bases through advanced AI-powered document parsing and contextual search capabilities. Built with a Next.js frontend and Nest.js business logic, the platform processes 860+ page PDFs with vector indexing and achieves 40% improvement in answer precision through Meta's LLaMA integration and secure on-premises deployment.

## Features

- **Enterprise Document Parsing**: Automated PDF processing with scalable indexing and source-cited responses across internal document libraries.
- **Vector-Based Search**: Python-powered LangChain-Chroma pipelines enabling semantic search and contextual information retrieval.
- **Advanced NLP Processing**: Meta's LLaMA integration with custom embeddings for precise answer generation and document summarization.
- **Secure On-Premises Deployment**: PostgreSQL-backed offline document ingestion with local data persistence and enterprise security.
- **Source Citation System**: Meticulous source tracking and verification ensuring accurate and verifiable information retrieval.
- **Scalable Architecture**: Full-stack solution supporting large-scale document processing and concurrent user queries.

## Tech Stack

### Frontend
- **Next.js** – Modern React framework with SSR/SSG capabilities for responsive user interface and document interaction portal.

### Backend
- **Nest.js** – Enterprise-grade TypeScript framework handling business logic and document processing workflows.

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

- **Node.js 18.0+** - Required for Next.js frontend and Nest.js backend
- **npm or yarn** - Package manager for Node.js dependencies
- **Python 3.8+** - For document processing and AI model integration
- **PostgreSQL 12+** - Database for document storage and analytics
- **Docker** - For containerized deployment (optional)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/alejandria-ai.git
   cd alejandria-ai
   ```

2. **Backend Setup (Nest.js)**
   ```bash
   cd backend
   npm install
   
   # Configure environment variables
   cp .env.example .env
   # Add your database credentials and API keys
   
   # Start the server
   npm run start:dev
   ```

3. **Frontend Setup (Next.js)**
   ```bash
   cd frontend
   npm install
   npm run dev
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
   npm run migration:run
   ```

6. **Access the platform**
   - Open your web browser and navigate to: `http://localhost:3000`
   - The Next.js interface will load with document upload and search portal

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
│   │   ├── app/             # App Router directory (Next.js 13+)
│   │   │   ├── components/  # React components for document interface
│   │   │   ├── api/         # API routes and endpoints
│   │   │   └── (routes)/    # Page routes and layouts
│   │   ├── lib/             # Utility functions and configurations
│   │   └── styles/          # Global styles and Tailwind CSS
│   ├── public/              # Static assets
│   ├── next.config.js       # Next.js configuration
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── modules/         # Feature modules
│   │   │   ├── documents/   # Document processing modules
│   │   │   ├── search/      # Search and query modules
│   │   │   └── auth/        # Authentication modules
│   │   ├── common/          # Shared utilities and decorators
│   │   ├── database/        # Database configuration and entities
│   │   └── main.ts          # Application entry point
│   ├── migrations/          # TypeORM database migrations
│   ├── nest-cli.json        # Nest.js CLI configuration
│   └── package.json
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
# Start Nest.js backend
cd backend && npm run start:dev

# Start Next.js frontend (in new terminal)
cd frontend && npm run dev

# Start Python AI engine (in new terminal)
cd ai-engine && python main.py
```

#### 2. Production Deployment
```bash
# Build Next.js frontend for production
cd frontend && npm run build

# Build Nest.js backend
cd backend && npm run build

# Run production backend
cd backend && npm run start:prod

# Start production frontend
cd frontend && npm start

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

### Development Scripts

**Frontend (Next.js):**
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
npm run lint         # Run ESLint
npm run type-check   # TypeScript type checking
```

**Backend (Nest.js):**
```bash
npm run start:dev      # Start in development mode
npm run start:debug    # Start in debug mode
npm run build          # Build the application
npm run start:prod     # Start production server
npm run test           # Run unit tests
npm run test:e2e       # Run end-to-end tests
npm run migration:run  # Run database migrations
```

## NOTES
- Please download `ggml-model-gpt4all-falcon-q4_0.bin` from [here](https://gpt4all.io/index.html) and put it in the root of the ai folder
