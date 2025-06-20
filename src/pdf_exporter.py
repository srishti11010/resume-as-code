import weasyprint

def export_pdf(html_content: str, output_path: str):
    weasyprint.HTML(string=html_content).write_pdf(target=output_path)
