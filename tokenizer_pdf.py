from langchain.vectorstores import Chroma

#Functionality: Chroma is a vector store, a data structure used for storing and managing vectors (typically embeddings) 
#in a way that allows efficient retrieval and similarity searches.

#Purpose: It's used to store and organize embeddings or vectors representing textual data in a manner that facilitates quick 
#search and retrieval based on similarity metrics.



from langchain.document_loaders import PyPDFLoader

#Functionality: PyPDFLoader is a module used for loading and extracting content from PDF files.
#Purpose: It allows the program to load PDF files and extract their textual content, making it accessible for further processing or analysis.

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

#Functionality: SentenceTransformerEmbeddings is a module used for generating sentence embeddings.

#Purpose: It's used to convert textual data (sentences, paragraphs, documents) into fixed-dimensional vectors (embeddings) 
#that capture semantic meanings and relationships between the text elements. These embeddings can then be used for various NLP tasks.


from langchain.text_splitter import RecursiveCharacterTextSplitter

#Functionality: RecursiveCharacterTextSplitter is a module used for splitting text into smaller chunks based on characters recursively.
#Purpose: It's employed to tokenize or break down larger chunks of text (documents, paragraphs) into smaller units, 
#often for further analysis or processing. This process is crucial for organizing and handling textual data efficiently.


# loader = PyPDFLoader("pdfs/economia.pdf")
# loader = PyPDFLoader("pdfs/astronomy.pdf")



content_list = []

# files = ["1. Que es la estrategia.pdf", "2. Recursos & Capacidades dinámicas.pdf", "2. Ventaja centrada en Recursos y Capacidades.pdf", "3. Estrategias_disruptivas_Cadena Valor.pdf", "Factors Críticos de Exito (FCE).pdf", "M1-T1.pdf", "M1-T2.pdf", "M1-T3.pdf", "Que es Estrategia.pdf"]

files = ["astronomy.pdf"]

for file in files:
    p = "pdfs/" + file
    loader = PyPDFLoader(p)
    content_list += loader.load_and_split()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 512,
    chunk_overlap  = 0,
    length_function = len,
    is_separator_regex = False,
)


toked = splitter.transform_documents(content_list)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(toked, embedding_function, persist_directory="./memory")

