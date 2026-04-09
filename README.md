# 🌍 Web Scraper & Event Notification System

An automated, persistent Python script designed to monitor target web pages for new event data. The system routinely scrapes the DOM, extracts specific nodes using YAML configurations, logs the data into a local SQLite database to prevent duplicate processing, and dispatches real-time email alerts via SMTP when new events are detected.

