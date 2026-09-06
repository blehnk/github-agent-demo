# Project Architecture Overview

## Table of Contents
1. [High‑Level Overview](#high-level-overview)
2. [Main Components](#main-components)
3. [Data Flow](#data-flow)
4. [Deployment Diagram](#deployment-diagram)
5. [Technology Stack](#technology-stack)
6. [Extending the Architecture](#extending-the-architecture)

---

## High‑Level Overview
The project follows a **modular, layered architecture** that separates concerns between the **API layer**, **business logic**, **data access**, and **infrastructure**.  This enables independent development, testing, and scaling of each part while keeping the codebase maintainable.

```
+-------------------+      +-------------------+      +-------------------+
|   API (REST/GraphQL)  |  |   Business Logic   |  |   Data Access Layer |
+-------------------+      +-------------------+      +-------------------+
          |                         |                         |
          v                         v                         v
+---------------------------------------------------------------+
|                     Infrastructure Layer                     |
|  (Message broker, Cache, Auth, Monitoring, CI/CD, etc.)      |
+---------------------------------------------------------------+
```

## Main Components
| Component | Responsibility | Key Technologies |
|-----------|----------------|------------------|
| **API Layer** | Exposes HTTP/HTTPS endpoints, request validation, authentication/authorization. | FastAPI / Flask, OpenAPI, JWT |
| **Service Layer** (Business Logic) | Core domain rules, orchestrates calls to data layer, handles transactions. | Python services, Pydantic models |
| **Repository/Data Access Layer** | Abstracts persistence, provides CRUD operations, implements repository pattern. | SQLAlchemy / Prisma, PostgreSQL, Redis |
| **Message Broker** | Asynchronous processing, event‑driven communication between services. | RabbitMQ / Kafka |
| **Cache** | Reduces latency for frequently accessed data. | Redis |
| **Auth Service** | Centralized authentication, token issuance, user management. | Keycloak / Auth0 |
| **Monitoring & Logging** | Observability, tracing, alerting. | Prometheus, Grafana, Loki, OpenTelemetry |
| **CI/CD Pipeline** | Automated testing, linting, building Docker images, deployments. | GitHub Actions, Docker, Kubernetes |

## Data Flow
1. **Client Request** – A client sends an HTTP request to the API gateway.
2. **API Layer** – Validates request, authenticates the user, and forwards to the appropriate service.
3. **Service Layer** – Executes business rules, may call multiple repositories or publish events.
4. **Repository Layer** – Interacts with the database or cache to read/write data.
5. **Message Broker** – If the operation is asynchronous, the service publishes an event; workers consume the event and perform background tasks.
6. **Response** – The service returns a result to the API layer, which formats and sends the HTTP response back to the client.

```
Client → API → Service → Repository ↔ DB
                     ↘
                      ↘→ Message Broker → Worker(s)
```

## Deployment Diagram
The following diagram illustrates a typical production deployment using Docker and Kubernetes:

```
+-------------------+      +-------------------+      +-------------------+
|   Ingress (NGINX) | ---> |   API Pods (FastAPI) | ---> |   Service Pods |
+-------------------+      +-------------------+      +-------------------+
                                 |                     |
                                 v                     v
                         +-------------------+   +-------------------+
                         |   PostgreSQL DB   |   |   Redis Cache     |
                         +-------------------+   +-------------------+
                                 |
                                 v
                         +-------------------+
                         |   RabbitMQ / Kafka |
                         +-------------------+
```
*All components are containerised and orchestrated by Kubernetes.  Helm charts are provided in the `helm/` directory for easy installation.*

## Technology Stack
- **Language**: Python 3.11
- **Web Framework**: FastAPI
- **ORM**: SQLAlchemy (async)
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Message Queue**: RabbitMQ 3.9 (or Kafka 3.x)
- **Containerisation**: Docker
- **Orchestration**: Kubernetes (v1.27)
- **CI/CD**: GitHub Actions
- **Observability**: Prometheus, Grafana, Loki, OpenTelemetry

## Extending the Architecture
- **Add a new microservice**: Create a new folder under `services/`, implement its own API, service, and repository layers, and expose it via the ingress.
- **Introduce GraphQL**: Add a GraphQL gateway that forwards queries to existing REST services or directly to the service layer.
- **Server‑less functions**: Deploy lightweight tasks as AWS Lambda or Azure Functions and invoke them via the message broker.

---

*This document is a living artifact.  Please keep it up‑to‑date with any architectural changes.*
