# Smart-SubMate Skeleton

This repository contains a minimal FastAPI implementation based on the PRD for **Smart-SubMate**, an AI chatbot for managing subscriptions.

## Features

- `POST /v1/chat` – stub chat endpoint with naive intent detection.
- `GET /v1/subscription/{user_id}` – returns sample subscription data.
- `POST /v1/feedback` – stores feedback in memory.

## Development

Install dependencies and run the API server:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```
