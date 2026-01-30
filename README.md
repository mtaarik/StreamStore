# Kafka Crash Course: Taxi Simulation 🚖

> [!IMPORTANT]  
> **Learning Project:** This is a small-scale educational project designed to demonstrate the basics of Apache Kafka. It is not intended for production environments.

---

## 📖 Project Overview
This project simulates a real-time taxi service tracking system. It uses **Apache Kafka** to stream location data from "Drivers" (Producers) to "Customers" or "Service Apps" (Consumers).

### How it works:
1.  **Docker** spins up the Kafka infrastructure.
2.  **Producer (`driver.py`)**: Simulates a taxi driver sending location coordinates.
3.  **Consumer (`consumer.py`)**: Simulates a user or backend service receiving those coordinates in real-time.



---

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Library:** `confluent-kafka`
* **Infrastructure:** Docker & Docker Compose
* **Message Format:** JSON

---

## 🚦 Getting Started

### 1. Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* Python 3.10+ installed.

### 2. Setup the Kafka Broker
Navigate to the project folder and run:
```bash
docker-compose up -d
