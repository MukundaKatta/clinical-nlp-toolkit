# Clinical Nlp Toolkit

NLP for clinical notes — entity extraction, coding, summarization

## Features

- Api
Deidentifier
Medication Extractor
Negation Detector
Ner
Pipeline
Temporal

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/clinical-nlp-toolkit.git
cd clinical-nlp-toolkit
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
clinical-nlp-toolkit/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
