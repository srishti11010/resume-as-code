import os
import weasyprint

def export_pdf(html_content: str, output_path: str):
    # Load CSS file contents
    css_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes', 'styles.css'))
    with open(css_path, 'r') as f:
        css = f.read()

    # Insert the CSS into the HTML inside <style> tag in the <head>
    if '</head>' in html_content:
        html_content = html_content.replace('</head>', f'<style>{css}</style></head>')
    else:
        # Fallback if no </head>
        html_content = f'<style>{css}</style>' + html_content

    weasyprint.HTML(string=html_content).write_pdf(target=output_path)
