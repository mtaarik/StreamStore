# StreamStore: Kafka Learning Project 🛒

> [!NOTE]  
> **Project Status:** This is a **small-scale learning project** created to practice and understand the fundamentals of Apache Kafka. It simulates a basic order processing flow using Python.

---

## 📖 Overview
This project demonstrates a simple "Store" event-streaming pipeline. It uses Kafka's **KRaft mode** to handle message brokering without the need for Zookeeper.

### The Workflow:
1.  **Producer (`producer.py`)**: Generates a random order for an item (e.g., a phone) and sends it to the `orders` topic.
2.  **Kafka Broker**: Receives and stores the order events.
3.  **Tracker (`tracker.py`)**: Acts as a consumer that listens to the `orders` topic and prints incoming orders in real-time.



---

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Kafka Client:** `confluent-kafka`
* **Broker:** Confluent Kafka (Docker image `cp-kafka:7.8.3`)
* **Mode:** KRaft (Zookeeper-less)

---

## 🚦 Getting Started

### 1. Start the Kafka Infrastructure
Ensure Docker is running, then start the Kafka container:
```bash
docker-compose up -d
