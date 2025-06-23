import pytest
from src.parser import parse_resume_file, parse_markdown

def test_parse_yaml(tmp_path):
    # Create a valid YAML file
    yaml_file = tmp_path / "resume.yaml"
    yaml_file.write_text("""
    basics:
      name: Jane Doe
      email: jane.doe@example.com
    """)
    
    # Parse the YAML file
    result = parse_resume_file(str(yaml_file))
    
    # Assert the parsed content is correct
    assert result["basics"]["name"] == "Jane Doe"
    assert result["basics"]["email"] == "jane.doe@example.com"

def test_parse_invalid_yaml(tmp_path):
    # Create an invalid YAML file
    yaml_file = tmp_path / "resume.yaml"
    yaml_file.write_text("invalid: [unclosed_bracket")
    
    # Assert that parsing raises a ValueError
    with pytest.raises(ValueError, match="Error parsing YAML file"):
        parse_resume_file(str(yaml_file))

def test_parse_json(tmp_path):
    # Create a valid JSON file
    json_file = tmp_path / "resume.json"
    json_file.write_text('{"basics": {"name": "Jane Doe", "email": "jane.doe@example.com"}}')
    
    # Parse the JSON file
    result = parse_resume_file(str(json_file))
    
    # Assert the parsed content is correct
    assert result["basics"]["name"] == "Jane Doe"
    assert result["basics"]["email"] == "jane.doe@example.com"

def test_parse_invalid_json(tmp_path):
    # Create an invalid JSON file
    json_file = tmp_path / "resume.json"
    json_file.write_text('{"basics": {"name": "Jane Doe", "email": "jane.doe@example.com"')
    
    # Assert that parsing raises a ValueError
    with pytest.raises(ValueError, match="Error parsing JSON file"):
        parse_resume_file(str(json_file))

def test_parse_markdown():
    # Create a valid Markdown string
    md_content = "# Jane Doe\n\n- Email: jane.doe@example.com"
    
    # Parse the Markdown content
    result = parse_markdown(md_content)
    
    # Assert the result is a dictionary (placeholder for actual Markdown parsing logic)
    assert isinstance(result, dict)

def test_parse_unsupported_file_format(tmp_path):
    # Create a file with an unsupported extension
    unsupported_file = tmp_path / "resume.txt"
    unsupported_file.write_text("This is not a valid resume format.")
    
    # Assert that parsing raises a ValueError
    with pytest.raises(ValueError, match="Unsupported file format"):
        parse_resume_file(str(unsupported_file))