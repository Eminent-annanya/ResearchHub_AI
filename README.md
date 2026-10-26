# 📚 ResearchHub AI

### Your AI-powered research and learning companion

**ResearchHub AI** is a Python-based research assistant that helps learners, students, researchers, and developers discover useful learning resources, explore technical topics, and turn search results into actionable learning plans.

Instead of searching across multiple platforms manually, ResearchHub AI brings web search, book discovery, YouTube tutorials, research papers, and AI-generated insights together in one Streamlit application.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Tavily](https://img.shields.io/badge/Search-Tavily-6554C0)](https://tavily.com/)
[![Groq](https://img.shields.io/badge/AI-Groq-orange)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ✨ Features

### 🔎 1. Web Resource Search

Search the web for educational materials, technical documentation, tutorials, and other useful resources using the Tavily Search API.

- Search for a topic using a simple interface.
- View result titles, descriptions, and source links.
- Explore resources relevant to your learning goals.

### 📚 2. Book Discovery

Discover books related to your chosen subject using the Open Library Search API.

- Book titles and author information.
- Publication years when available.
- Book cover images when available.
- Access-status information, including publicly readable and borrowable resources where reported.

> Access labels are indicative. Always check the source for actual availability, download rights, and licensing.

### ▶️ 3. YouTube Tutorial Search

Find video-based learning resources for technical and academic subjects.

- Search for tutorials and lectures.
- Open relevant YouTube videos directly.
- Use video resources alongside books and research papers.

Video discovery currently uses web search rather than the official YouTube Data API, so results and metadata may vary.

### 📄 4. Research Paper Discovery

Search arXiv for scholarly papers and technical research.

- Paper titles and authors.
- Publication dates when available.
- Abstracts for understanding research before reading.
- Links to paper pages and PDF files when provided.

arXiv coverage is limited to the research available in its repository and is not a complete index of all academic publications.

### 🤖 5. AI Research Assistant

Use a Groq-hosted language model to turn a topic and retrieved search results into useful explanations and plans.

**Topic Brief**
- Understand the topic's meaning and importance.
- Learn core concepts.
- Explore simple examples.

**How to Use These Resources**
- Organize learning materials into a sensible sequence.
- Identify what to study from different resources.
- Build a practical learning roadmap.

**Future & Opportunities**
- Explore applications and emerging trends.
- Identify relevant skills and potential career paths.
- Distinguish established information from predictions.

AI-generated insights should be independently verified, particularly for statistics, career-demand claims, and technical decisions.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| Tavily Search API | Web search and resource discovery |
| Groq API | AI-generated reports |
| Open Library API | Book metadata and cover discovery |
| arXiv API | Scientific paper discovery |
| Requests | HTTP requests to external APIs |
| python-dotenv | Local environment-variable management |

---

## 🏗️ Project Structure

```text
ResearchHub-AI/
│
├── app.py                 # Main Streamlit application
├── config.py              # API client configuration
├── search_service.py      # General web search
├── ai_service.py          # AI report generation
├── book_service.py        # Book discovery
├── youtube_service.py     # YouTube tutorial search
├── paper_service.py       # Research paper discovery
├── requirements.txt       # Python dependencies
├── .gitignore             # Excluded files and secrets
├── .env                   # Local API keys (not committed)
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to run ResearchHub AI on your local machine.

### Prerequisites

- Python 3.10 or later.
- Git.
- A Tavily API key.
- A Groq API key.

Book discovery and arXiv search use public APIs and do not require additional API keys for the current implementation.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ResearchHub-AI.git
cd ResearchHub-AI
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```dotenv
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

Obtain your keys from:

- [Tavily](https://app.tavily.com/)
- [Groq Console](https://console.groq.com/)

Replace the placeholder values with your own API keys.

**Security:** Never publish your `.env` file, commit API keys, or share them in screenshots. The repository's `.gitignore` should exclude `.env`.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open that address in your browser.

---

## 📖 How to Use

1. Launch ResearchHub AI.
2. Enter a topic, such as `Python for Data Science`, `PCB Design using KiCad`, or `Metamaterial Absorbers`.
3. Select the desired resource category.
4. Click **Search** to retrieve relevant resources.
5. Explore the returned titles, descriptions, links, and available metadata.
6. Use the AI Research Assistant to generate a topic brief, a learning roadmap, or future-and-opportunities insights.

### Example research topics

| Topic | Suggested category |
|---|---|
| Python for Data Science | Books & PDFs |
| PCB Design using KiCad | YouTube tutorials |
| Metamaterial Absorbers | Research papers |
| Embedded Systems | All resources |

---

## 🔐 API Usage and Limitations

- Tavily and Groq API access is subject to the providers' current quotas, rate limits, and terms.
- Free-tier availability and limits may change.
- A working API key does not necessarily imply unlimited free usage.
- Search results can include pages that mention a resource without providing the full resource itself.
- Book availability labels are based on metadata returned by Open Library.
- arXiv is a specialized research repository and does not cover every publication.
- AI-generated content can contain errors and should be checked against primary sources.
- The current implementation does not guarantee measured keyword demand or search-volume statistics.

---

## 🗺️ Roadmap

Planned improvements for future versions:

- [ ] Unified resource library for books, videos, and papers.
- [ ] Save and organize resources locally.
- [ ] Advanced filtering and sorting.
- [ ] Improved verification of free and open-access resources.
- [ ] More scholarly search sources.
- [ ] Resource relevance and quality scoring.
- [ ] Learning plans tailored to a user's goals and skill level.
- [ ] Evidence-backed analysis of industry trends and demand.
- [ ] Deployment as a publicly accessible web application.

These items are planned improvements, not features currently guaranteed by the application.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork this repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application locally.
5. Submit a pull request describing your changes.

For larger changes, consider opening an issue first to discuss the proposed improvement.

---

## 🛡️ Security

Please do not commit API keys, passwords, or other sensitive information.

If a secret is accidentally published, revoke or rotate it immediately. Removing the secret from a later commit does not erase it from the repository's history.

---

## 📄 License

This project is intended to be released under the MIT License. Add a `LICENSE` file containing the official MIT License text and your copyright details before treating the repository as MIT-licensed.

---

## 👨‍💻 Author

**YOUR NAME**

- GitHub: [[@Eminent-Annanya](https://github.com/Eminent-annanya)]

---

*ResearchHub AI — Search smarter. Learn systematically. Explore what comes next.*﻿# ResearchHub_AI
