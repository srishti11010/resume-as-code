import pytest
from click.testing import CliRunner
from src.cli import cli

@pytest.fixture
def runner():
    return CliRunner()

def create_temp_resume_file(tmp_path):
    """Helper function to create a temporary resume file with the required 'basics' key."""
    input_file = tmp_path / "resume.yaml"
    input_file.write_text("""
    basics:
      name: Jane Doe
      email: jane.doe@example.com
    """)
    return input_file

def test_build_command(runner, tmp_path):
    # Use the helper function to create the input file
    input_file = create_temp_resume_file(tmp_path)
    
    # Run the 'build' command
    result = runner.invoke(cli, ["build", str(input_file), "--output-html", "output.html"])
    
    # Assert the command ran successfully
    assert result.exit_code == 0
    assert "HTML resume saved to output.html" in result.output

def test_build_command_with_pdf(runner, tmp_path):
    # Use the helper function to create the input file
    input_file = create_temp_resume_file(tmp_path)
    
    # Run the 'build' command with PDF output
    result = runner.invoke(cli, ["build", str(input_file), "--output-html", "output.html", "--output-pdf", "output.pdf"])
    
    # Assert the command ran successfully
    assert result.exit_code == 0
    assert "HTML resume saved to output.html" in result.output
    assert "PDF resume saved to output.pdf" in result.output

def test_export_command(runner, tmp_path):
    # Use the helper function to create the input file
    input_file = create_temp_resume_file(tmp_path)
    
    # Run the 'export' command
    result = runner.invoke(cli, ["export", str(input_file), "--output-pdf", "output.pdf"])
    
    # Assert the command ran successfully
    assert result.exit_code == 0
    assert "PDF resume saved to output.pdf" in result.output

def test_missing_input_file(runner):
    # Run the 'build' command with a non-existent input file
    result = runner.invoke(cli, ["build", "non_existent_file.yaml", "--output-html", "output.html"])
    
    # Assert the command failed and an appropriate error message was displayed
    assert result.exit_code != 0
    assert "Error: Input file \'non_existent_file.yaml\' not found." in result.output

def test_invalid_file_format(runner, tmp_path):
    # Create a temporary input file with an unsupported extension
    input_file = tmp_path / "resume.txt"
    input_file.write_text("This is not a valid resume format.")
    
    # Run the 'build' command
    result = runner.invoke(cli, ["build", str(input_file), "--output-html", "output.html"])

    # Assert the command failed and an appropriate error message was displayed
    assert result.exit_code != 0
    assert "Error: Unsupported file format: .txt" in str(result)

