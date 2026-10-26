
import requests
import xml.etree.ElementTree as ET

ARXIV_API = "https://export.arxiv.org/api/query"

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def search_papers(topic, max_results=8):
    params = {
        "search_query": f"all:{topic}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }

    response = requests.get(
        ARXIV_API,
        params=params,
        timeout=25,
        headers={"User-Agent": "ResearchHubAI/1.0"}
    )
    response.raise_for_status()

    root = ET.fromstring(response.text)
    papers = []

    for entry in root.findall(f"{ATOM}entry"):
        title = entry.findtext(f"{ATOM}title", "").strip()
        summary = entry.findtext(f"{ATOM}summary", "").strip()
        published = entry.findtext(f"{ATOM}published", "")[:10]

        authors = [
            author.findtext(f"{ATOM}name", "")
            for author in entry.findall(f"{ATOM}author")
        ]

        paper_url = entry.findtext(f"{ATOM}id", "").strip()

        pdf_url = None
        for link in entry.findall(f"{ATOM}link"):
            if link.attrib.get("title") == "pdf":
                pdf_url = link.attrib.get("href")
                break

        papers.append({
            "resource_type": "paper",
            "title": " ".join(title.split()),
            "authors": authors,
            "published": published,
            "abstract": " ".join(summary.split()),
            "url": paper_url,
            "pdf_url": pdf_url,
        })

    return papers
