# 🎓 Student Placement Prediction App


A machine learning web application that predicts the probability of a college student getting placed based on five key factors using a **Naive Bayes classifier**.

---

## 🌐 Live Demo

| Service | URL |
|---|---|
| 🖥️ Frontend (Streamlit) | https://placement-frontend-tu4p.onrender.com |
| ⚙️ Backend (FastAPI) | https://placement-backend-vwiy.onrender.com |
| 📄 API Docs | https://placement-backend-vwiy.onrender.com/docs |

---

## 📌 Features

- Predicts student placement probability using Naive Bayes
- REST API backend built with FastAPI
- Interactive frontend built with Streamlit
- Dockerized deployment (separate containers for backend & frontend)
- Deployed on Render (free tier)

---

## 🧠 Input Features

| Feature                      | Range      |
|------------------------------|------------|
| IQ                           | 40 – 160   |
| Previous Semester Result     | 0.0 – 10.0 |
| CGPA                         | 0.0 – 10.0 |
| Communication Skills         | 0 – 10     |
| Number of Projects Completed | 0 – 10     |

---

## 🗂️ Project Structure

```
DS-Project-1-PU-AIDS-2024-28/
├── backend.py                          # FastAPI backend
├── frontend.py                         # Streamlit frontend
├── config.py                           # Configuration (priors, column names)
├── __init__.py
├── ds-project-1.ipynb                  # Jupyter notebook (EDA + model training)
├── college_student_placement_dataset.csv  # Dataset
├── eigen_vectors.npy                   # PCA eigen vectors
├── likelihood_distribution_params.pkl  # Trained model parameters
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Original Dockerfile
├── Dockerfile.backend                  # Backend-only Dockerfile
├── Dockerfile.frontend                 # Frontend-only Dockerfile
├── start-backend-frontend.sh           # Script to run both services
└── .gitignore
```

---

## ⚙️ Tech Stack

| Layer                    | Technology                 |
|--------------------------|----------------------------|
| ML Model                 | Naive Bayes (from scratch) |
| Dimensionality Reduction | PCA (eigen vectors)        |
| Backend                  | FastAPI + Uvicorn          |
| Frontend                 | Streamlit                  |
| Containerization         | Docker                     |
| Deployment               | Render                     |
| Language                 | Python 3.12                |

---

## 🚀 Run Locally

### Prerequisites
- Python 3.12+
- Git

### Steps

**1. Clone the repository**
```bash
git clone -b sec-a https://github.com/aasifali4813/DS-Project-1-PU-AIDS-2024-28.git
cd DS-Project-1-PU-AIDS-2024-28
```

**2. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run Backend (Terminal 1)**
```bash
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```

**5. Run Frontend (Terminal 2)**
```bash
streamlit run frontend.py
```

**6. Open in browser**
- Frontend: http://localhost:8501
- Backend API Docs: http://localhost:8000/docs

---

## 🐳 Run with Docker

**Backend:**
```bash
docker build -f Dockerfile.backend -t placement-backend .
docker run -p 8000:8000 placement-backend
```

**Frontend:**
```bash
docker build -f Dockerfile.frontend -t placement-frontend .
docker run -p 10000:10000 placement-frontend
```

---

## 📡 API Reference

### GET `/`
Returns app description.

### POST `/compute-probability`
Computes placement probability.

**Request Body:**
```json
{
  "iq": 120,
  "previous_semester_result": 8.5,
  "cgpa": 8.0,
  "communication_skills": 8,
  "projects_completed": 5
}
```

**Response:**
```json
{
  "result": "Given your inputs, most likely you are going to get placed and the probability of you getting placed is roughly 0.99"
}
```

---

## ☁️ Deploy on Render

### Backend
| Field | Value |
|---|---|
| Runtime | Docker |
| Dockerfile Path | `./Dockerfile.backend` |
| Branch | `sec-a` |

### Frontend
| Field | Value |
|---|---|
| Runtime | Docker |
| Dockerfile Path | `./Dockerfile.frontend` |
| Branch | `sec-a` |

> ⚠️ **Note:** Free tier on Render spins down after 15 minutes of inactivity. First request may take 30–60 seconds.

---

## 📦 Dependencies

```
pandas
numpy
scipy
pydantic
uvicorn
fastapi
streamlit
```

---


