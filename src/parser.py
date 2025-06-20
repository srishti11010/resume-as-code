import json
import yaml
import os
import mistune

def parse_resume_file(filepath: str):
    ext = os.path.splitext(filepath)[1].lower()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if ext in ['.yaml', '.yml']:
        return yaml.safe_load(content)
    elif ext == '.json':
        return json.loads(content)
    elif ext == '.md':
        return parse_markdown(content)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def parse_markdown(md_text: str):
    parser = mistune.create_markdown(renderer=mistune.AstRenderer())
    ast = parser(md_text)
    return markdown_ast_to_resume(ast)

def markdown_ast_to_resume(ast):
    # TODO: Implement Markdown AST traversal & conversion
    # For now, return raw AST or empty dict
    return {}
