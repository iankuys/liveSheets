# Live Sheets (WebSockets)

A minimalist collaborative spreadsheet-like app built with **WebSockets** for real-time updates. Users can edit shared cells, and all changes are instantly broadcast to connected clients.

## Tech Stack

- **Backend:** Python / Flask
- **Frontend:** HTML, CSS, JavaScript
- **Realtime Communication:** WebSockets with Socket.IO

## Features

- Live cell editing with real-time sync across all clients
- Lightweight frontend UI (basic table/grid layout)
- WebSocket-powered bidirectional communication
- Single shared sheet — simple, fast, no frill

## Getting Started

1. **Create venv**
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run app**
```
python main.py
```
