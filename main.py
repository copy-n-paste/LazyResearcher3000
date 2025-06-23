#main.py
import os
from research import generate_research_content
from pdf_generator import create_pdf
from dotenv import load_dotenv

def main():
    load_dotenv()
    topic = input('Enter the research topic: ')
    requirements = input('Enter any specific requirements (or leave blank): ')
    print('Generating research report...')
    report = generate_research_content(topic, requirements)
    output_path = f"{topic.replace(' ', '_')}_report.pdf"
    create_pdf(report, output_path)
    print(f'Report saved to {output_path}')

if __name__ == '__main__':
    main() 