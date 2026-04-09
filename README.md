# 🌍 Web Scraper & Event Notification System

An automated, persistent Python script designed to monitor target web pages for new event data. The system routinely scrapes the DOM, extracts specific nodes using YAML configurations, logs the data into a local SQLite database to prevent duplicate processing, and dispatches real-time email alerts via SMTP when new events are detected.

## 🧠 Engineering Architecture
* **Data Acquisition:** Utilizes the `requests` library with spoofed User-Agent headers to bypass basic automated traffic filters.
* **Extraction Engine:** Implements `selectorlib` mapped to an `extract.yaml` blueprint to cleanly parse unstructured HTML into structured data.
* **Persistent Storage (Model):** Integrates Python's built-in `sqlite3` to maintain a historical ledger of processed events, ensuring notifications are only dispatched for mathematically unique records.
* **Notification Dispatcher:** Establishes a secure `SMTP_SSL` connection to transmit encrypted alerts to a designated email address.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** `requests`, `selectorlib`, `smtplib`, `ssl`, `sqlite3`, `time`


