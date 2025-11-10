# Project Overview

This project implements a Mood Based Recipe Recommendation System.

## Features Implemented:

- **SCRUM-194:** User Management
  - User registration, login with JWT authentication.
  - Password hashing and email uniqueness.

- **SCRUM-195:** Mood Input & Handling
  - Mood submission API with validation.
  - Backend storage of moods and linkage to users.

- **SCRUM-196:** Recipe Recommendation Engine
  - Rules-based engine mapping moods to recipe tags.
  - API to fetch recommended recipes by mood.

- **SCRUM-197:** Recipe Browsing & Viewing
  - Recipe listing and detailed view.
  - Pagination and search support.

- **SCRUM-198:** Backend API Services
  - RESTful APIs for users, moods, recipes, favorites.
  - JWT enforced security.

- **SCRUM-199:** Favorites & Recipe Saving
  - Add and retrieve user's favorite recipes.

- **SCRUM-200:** Social Sharing & Mood Journaling
  - Mood journal entries submission and retrieval.
  - Social sharing UI and backend services.

- **SCRUM-201:** Advanced Mood Detection (Sentiment Analysis)
  - Sentiment microservice integrated with mood inputs.

- **SCRUM-202:** Dietary Preference Filtering
  - User dietary preferences stored and used for filtering.

- **SCRUM-203:** AI-driven Personalized Meal Planning
  - AI/ML models for personalized meal plans.

- **SCRUM-204:** Social Features & Community
  - User posts, comments, likes, and forums.

- **SCRUM-205:** Security, Privacy & Compliance
  - HTTPS enforcement, OAuth2/JWT auth, GDPR compliance.

- **SCRUM-206:** Performance, Scalability & Reliability
  - Containerization, microservices, caching, auto-scaling.

- **SCRUM-207:** Testing, Logging & Monitoring
  - CI/CD integration, centralized logging, monitoring dashboards.

## Repository Structure

- `backend/` - API services and business logic modules
- `docs/` - Documentation files

All implemented features include unit and integration tests.

---
For detailed code and API usage, refer to each module's docstrings and code comments.
