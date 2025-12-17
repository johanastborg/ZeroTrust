# LinkedIn Clone Project

A simplified LinkedIn clone built with Python on Google Cloud Platform.

## Architecture

- **Backend**: Python (FastAPI)
- **Database**: Google Cloud Bigtable (Scalable NoSQL)
- **Caching**: Google Cloud Memorystore (Redis)
- **Auth & Notifications**: Firebase
- **Mobile**: Android and iOS

## Structure

```
.
├── backend/                 # Python backend application
│   ├── app/                 # Application source code
│   │   ├── api/             # API Endpoints
│   │   ├── core/            # Configuration and Utilities
│   │   ├── models/          # Data models
│   │   └── services/        # Logic for Bigtable/Firebase/Redis
│   ├── tests/               # Unit and integration tests
│   └── requirements.txt     # Python dependencies
├── mobile/                  # Mobile client applications
│   ├── android/             # Android native project
│   └── ios/                 # iOS native project
└── docs/                    # Project documentation
```

## Getting Started

### Backend

1. Navigate to `backend/`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn app.main:app --reload`

### Mobile

Check the `mobile/README.md` for details.
