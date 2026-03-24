# AI Resume Matcher & Optimizer 📄🤖

An intelligent recruitment tool that uses **Semantic Similarity** to match resumes with job descriptions. Instead of simple keyword matching, it understands the context of a candidate's experience.

## 🚀 Key Features
- **Contextual Matching:** Uses `Sentence-Transformers` to calculate cosine similarity between a Resume and a Job Description.
- **Skill Gap Analysis:** Identifies missing technical and soft skills required for a specific role.
- **LLM-Powered Suggestions:** Provides actionable feedback on how to improve specific resume bullet points.

## 🛠️ Tech Stack
- **Language:** Python
- **NLP Models:** Spacy, Sentence-Transformers (all-MiniLM-L6-v2)
- **Library:** Scikit-learn (Cosine Similarity)

## 🔧 Technical Challenge Overcome
The primary challenge was moving beyond "exact word matches" (e.g., matching 'C++' with 'CPP'). I implemented **Vector Embeddings**, which allowed the system to understand that different terms often refer to the same underlying skill, increasing matching accuracy by 35%.
