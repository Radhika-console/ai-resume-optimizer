import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load a lightweight NLP model
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_match(resume_text, job_description):
    # Convert text to numerical vectors (Embeddings)
    embeddings = model.encode([resume_text, job_description])
    
    # Calculate Similarity Score
    score = cosine_similarity([embeddings[0]], [embeddings[1]])
    return round(score[0][0] * 100, 2)

if __name__ == "__main__":
    print(f"Match Score: {calculate_match('Python Developer with AI experience', 'Looking for an AI Engineer proficient in Python')}%")
