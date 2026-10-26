
import streamlit as st

from config import get_tavily_client, get_ai_client
from search_service import search_resources
from ai_service import generate_report
from book_service import search_books
from youtube_service import search_youtube
from paper_service import search_papers

st.set_page_config(
    page_title="ResearchHub AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ResearchHub AI")
st.caption("Search the web. Understand topics. Discover opportunities.")

tavily = get_tavily_client()
ai = get_ai_client()

if "results" not in st.session_state:
    st.session_state.results = []

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "ai_report" not in st.session_state:
    st.session_state.ai_report = {}

query = st.text_input(
    "What do you want to learn or find?",
    placeholder="e.g. Python for data science"
)

resource_type = st.selectbox(
    "Choose resource type",
    [
        "All resources",
        "Books & PDFs",
        "YouTube tutorials",
        "Research papers"
    ]
)


if st.button("🔍 Search", type="primary") and query.strip():
    try:
        with st.spinner("Searching for resources..."):

            if resource_type == "Books & PDFs":
                st.session_state.results = search_books(
                    query.strip())
            elif resource_type == "YouTube tutorials":
                st.session_state.results = search_youtube(
                tavily, query.strip())
            elif resource_type == "Research papers":
                st.session_state.results = search_papers(
                query.strip())
            else:
                st.session_state.results = search_resources(
                    tavily, query, resource_type
                )

            st.session_state.topic = query.strip()
            st.session_state.ai_report = {}

    except Exception as error:
        st.error(f"Search failed: {error}")


if st.session_state.topic:
    left, right = st.columns([2.2, 1], gap="large")

    with left:
        st.subheader("🔎 Search Results")

        
        for item in st.session_state.results:
            if item.get("description") is not None and "access_status" not in item:
                st.markdown(f"### [{item['title']}]({item['url']})")
                st.write(item["description"])
                st.caption("YouTube search result")
                st.divider()  

            elif item.get("resource_type") == "paper":
                st.markdown(f"### [{item['title']}]({item['url']})")

                st.write(
                    "**Authors:** "
                    + (", ".join(item["authors"]) or "Not listed")
                )
                st.caption(f"Published: {item['published']}")

                with st.expander("Read abstract"):
                    st.write(item["abstract"])

                if item.get("pdf_url"):
                    st.markdown(f"[📄 Open PDF]({item['pdf_url']})")

                st.divider()

            elif "access_status" in item:
                if item.get("cover"):
                    st.image(item["cover"], width=110)

                st.markdown(f"### [{item['title']}]({item['url']})")

                st.write(
                    f"**Author:** {item.get('author') or 'Unknown'}"
                )
                st.write(f"**Year:** {item.get('year', 'Unknown')}")
                st.write(
                    f"**Access:** {item['access_status']}"
                )

                st.divider()

              

            else:
                st.markdown(
                    f"### [{item.get('title', 'Untitled')}]"
                    f"({item.get('url', '#')})"
                )
                st.write(item.get("content", ""))
                st.caption(item.get("url", ""))
                st.divider()
            

    with right:
        st.subheader("🤖 AI Research Assistant")
        st.caption(f"Current topic: {st.session_state.topic}")

        reports = {
            "brief": (
                "Topic Brief",
                "Explain the topic, core concepts, importance, "
                "and a simple example."
            ),
            "learning": (
                "How to Use These Resources",
                "Create a practical learning roadmap. "
                "Explain what to learn from each search result."
            ),
            "future": (
                "Future & Opportunities",
                "Explain applications, emerging trends, career "
                "opportunities, and required skills. Separate "
                "facts from predictions. Never invent statistics."
            )
        }

        for key, (label, task) in reports.items():
            if st.button(label, key=f"btn_{key}", use_container_width=True):
                if not ai:
                    st.error("Add GROQ_API_KEY to your .env file.")
                else:
                    try:
                        with st.spinner(f"Generating {label.lower()}..."):
                            answer = generate_report(
                                ai,
                                st.session_state.topic,
                                task,
                                st.session_state.results
                            )
                            st.session_state.ai_report[key] = (
                                label, answer
                            )
                    except Exception as error:
                        st.error(f"AI request failed: {error}")

        for key, (label, answer) in st.session_state.ai_report.items():
            with st.expander(label, expanded=True):
                st.markdown(answer)
