import click
from src.parser import parse_resume_file
from src.renderer import render_html
from src.pdf_exporter import export_pdf

@click.group()
def cli():
    pass

@cli.command()
@click.argument('input_file')
@click.option('--output-html', default='output.html')
def build(input_file, output_html):
    resume_data = parse_resume_file(input_file)
    html = render_html(resume_data)
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)
    click.echo(f'HTML resume saved to {output_html}')

@cli.command()
@click.argument('input_file')
@click.option('--output-pdf', default='output.pdf')
def export(input_file, output_pdf):
    resume_data = parse_resume_file(input_file)
    html = render_html(resume_data)
    export_pdf(html, output_pdf)
    click.echo(f'PDF resume saved to {output_pdf}')

if __name__ == '__main__':
    cli()
