#pdf_generator.py
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import re

MARGIN = 1 * inch
SECTION_SPACING = 0.5 * inch

# Clean text: remove any stray symbols or invalid characters
INVALID_SYMBOLS = r'[\*#_`~\[\]<>|]'  # add more if needed
def clean_text(text):
    text = re.sub(INVALID_SYMBOLS, '', text)
    text = re.sub(r'\s+', ' ', text)  # collapse whitespace
    return text.strip()

def header_footer(canvas, doc, title):
    canvas.saveState()
    width, height = LETTER
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawString(MARGIN, height - 0.7 * inch, title)
    canvas.drawRightString(width - MARGIN, 0.7 * inch, f"Page {doc.page}")
    canvas.setFillColor(colors.black)
    canvas.restoreState()

def create_pdf(report, output_path):
    styles = getSampleStyleSheet()
    story = []
    title = report['topic']
    author = "Author: [Your Name]"  # Optionally make this dynamic
    org = "Organization: [Your Organization]"
    date = report['date']

    # Title Page
    story.append(Spacer(1, 2 * inch))
    style_title = ParagraphStyle('title', fontSize=28, alignment=TA_CENTER, spaceAfter=20, leading=32)
    story.append(Paragraph(clean_text(title), style_title))
    style_sub = ParagraphStyle('sub', fontSize=16, alignment=TA_CENTER, spaceAfter=10)
    story.append(Paragraph("Research Report", style_sub))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(f"<b>{clean_text(author)}</b>", style_sub))
    story.append(Paragraph(f"<b>{clean_text(org)}</b>", style_sub))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(f"<b>Date:</b> {clean_text(date)}", style_sub))
    story.append(PageBreak())

    # Table of Contents
    style_head = ParagraphStyle('head', fontSize=18, alignment=TA_LEFT, spaceAfter=10, leading=22)
    story.append(Paragraph("Index", style_head))
    toc_items = [
        "1. Introduction",
        "2. History",
        "3. Current Situation",
        "4. Current Impact",
        "5. Advantages",
        "6. Disadvantages",
        "7. Important Notes",
        "8. New/Emerging Topics",
        "9. Summary of Key Points",
        "10. Conclusion",
        "11. References"
    ]
    for item in toc_items:
        story.append(Paragraph(clean_text(item), styles['Normal']))
    story.append(PageBreak())

    # Section helper
    def add_section(title, content):
        story.append(Spacer(1, SECTION_SPACING))
        style_section = ParagraphStyle('section', fontSize=16, alignment=TA_LEFT, spaceAfter=10, leading=20)
        story.append(Paragraph(title, style_section))
        style_normal = ParagraphStyle('normal', fontSize=12, alignment=TA_LEFT, leading=16)
        for line in clean_text(content).split('. '):
            if line:
                story.append(Paragraph(line.strip(), style_normal))

    # Add all sections
    add_section("Introduction", report['introduction'])
    add_section("History", report['history'])
    add_section("Current Situation", report['current_situation'])
    add_section("Current Impact", report['current_impact'])
    add_section("Advantages", report['advantages'])
    add_section("Disadvantages", report['disadvantages'])
    add_section("Important Notes", report['important_notes'])
    add_section("New/Emerging Topics", report['new_topics'])
    add_section("Summary of Key Points", report['summary'])
    add_section("Conclusion", report['conclusion'])

    # References
    story.append(Spacer(1, SECTION_SPACING))
    style_section = ParagraphStyle('section', fontSize=16, alignment=TA_LEFT, spaceAfter=10, leading=20)
    story.append(Paragraph("References", style_section))
    ref_style = ParagraphStyle('ref', fontSize=10, leftIndent=20, leading=14)
    for ref in report['references']:
        story.append(Paragraph(clean_text(ref), ref_style))

    # Build PDF
    doc = SimpleDocTemplate(
        output_path,
        pagesize=LETTER,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )
    doc.build(story, onFirstPage=lambda c, d: header_footer(c, d, title), onLaterPages=lambda c, d: header_footer(c, d, title)) 