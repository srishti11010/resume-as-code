import pytest
import os
from src.pdf_exporter import export_pdf

def test_export_pdf_creates_file(tmp_path):
    # Create temporary HTML content
    html_content = "<html><body><h1>Test Resume</h1></body></html>"
    output_pdf = tmp_path / "resume.pdf"
    
    # Export the PDF
    export_pdf(html_content, str(output_pdf))
    
    # Assert the PDF file was created
    assert os.path.exists(output_pdf)

def test_export_pdf_empty_html(tmp_path):
    # Create empty HTML content
    html_content = ""
    output_pdf = tmp_path / "resume.pdf"
    
    # Assert that exporting empty HTML raises an exception
    with pytest.raises(ValueError, match="HTML content is empty"):
        export_pdf(html_content, str(output_pdf))