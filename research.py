#research.py
import os
import cohere
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_cohere_client():
    api_key = os.getenv('COHERE_API_KEY')
    if not api_key:
        raise ValueError('COHERE_API_KEY not set in environment')
    return cohere.Client(api_key)

def generate_section(client, topic, requirements, section):
    prompts = {
        'introduction': f"""
        Write a professional introduction for a research report on the topic: '{topic}'.
        Requirements: {requirements}
        The introduction should set the context and importance of the topic.
        """,
        'history': f"""
        Provide a detailed history and background of '{topic}'.
        Requirements: {requirements}
        Use subheadings and bullet points where appropriate.
        """,
        'current_situation': f"""
        Describe the current situation regarding '{topic}'.
        Requirements: {requirements}
        Use subheadings and bullet points where appropriate.
        """,
        'current_impact': f"""
        Explain the current impact of '{topic}' on society, industry, or relevant fields.
        Requirements: {requirements}
        Use bullet points for key impacts.
        """,
        'advantages': f"""
        List and explain the main advantages of '{topic}'.
        Requirements: {requirements}
        Use bullet points.
        """,
        'disadvantages': f"""
        List and explain the main disadvantages or challenges of '{topic}'.
        Requirements: {requirements}
        Use bullet points.
        """,
        'important_notes': f"""
        Highlight the most important notes, warnings, or considerations about '{topic}'.
        Requirements: {requirements}
        Present as a highlighted section.
        """,
        'new_topics': f"""
        List and briefly describe new or emerging topics, trends, or technologies related to '{topic}'.
        Requirements: {requirements}
        Use bullet points.
        """,
        'summary': f"""
        Summarize the key points of the report on '{topic}'.
        Requirements: {requirements}
        Use bullet points or a short paragraph for each main section.
        """,
        'conclusion': f"""
        Write a strong conclusion for a research report on '{topic}'.
        Requirements: {requirements}
        Summarize the main points and suggest future directions or implications.
        """,
        'references': f"""
        Provide a list of at least 5 reputable references (websites, articles, books, or papers) used or recommended for further reading on '{topic}'.
        Format as a numbered list.
        """
    }
    prompt = prompts[section]
    response = client.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=800,
        temperature=0.7
    )
    return response.generations[0].text.strip()

def generate_research_content(topic, requirements):
    client = get_cohere_client()
    sections = {}
    for section in [
        'introduction', 'history', 'current_situation', 'current_impact',
        'advantages', 'disadvantages', 'important_notes', 'new_topics',
        'summary', 'conclusion', 'references']:
        sections[section] = generate_section(client, topic, requirements, section)
    # Parse references into a list
    references = []
    for line in sections['references'].split('\n'):
        if line.strip():
            references.append(line.strip())
    return {
        'topic': topic,
        'date': datetime.now().strftime('%B %d, %Y'),
        'introduction': sections['introduction'],
        'history': sections['history'],
        'current_situation': sections['current_situation'],
        'current_impact': sections['current_impact'],
        'advantages': sections['advantages'],
        'disadvantages': sections['disadvantages'],
        'important_notes': sections['important_notes'],
        'new_topics': sections['new_topics'],
        'summary': sections['summary'],
        'conclusion': sections['conclusion'],
        'references': references
    } 