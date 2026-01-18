Credit Risk Infrastructure Engine (Project Sentinel)
This repository demonstrates a production-grade infrastructure for credit risk modeling, provisioning, and stress testing, designed for a high-volume financial environment (RBC).
Key Features:
Data Engineering: Utilizes PySpark and SQL logic to process 5,000+ loan records, simulating big data scalability.
Regulatory Compliance: Implements IFRS9 Expected Credit Loss (ECL) calculations using PD/LGD/EAD frameworks.
Stress Testing (CCAR): Includes a "Severe Adverse" scenario engine to calculate capital buffers required during economic downturns.
DevOps & Infrastructure: Containerized with Docker and automated via GitHub Actions (CI/CD) to ensure model deployment stability.
Tech Stack:
Language: Python 3.9
Big Data: Apache Spark (PySpark)
DevOps: Docker, Git, GitHub Actions
Risk Domain: IFRS9, CCAR, Credit Risk Modeling
