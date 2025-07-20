# 📄 Resume as Code

Generate beautiful HTML and PDF resumes from structured YAML, JSON, or Markdown.  
Write your resume like code — keep it version-controlled, data-driven, and format-flexible.

---

## ✨ Features

- ✅ Input formats: YAML, JSON, or Markdown
- 🎨 Output formats: HTML & PDF
- 🧩 Jinja2 templating for custom themes
- 🛠 CLI-based workflow
- 💻 Built with Python & WeasyPrint

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/resume-as-code.git
cd resume-as-code
```

### 2. Install dependencies using [Poetry](https://python-poetry.org/)

```bash
poetry install
```

---

## 🛠 Prerequisites

### 🔧 System Libraries

**WeasyPrint** needs the following native libraries to generate PDFs.

#### macOS (using Homebrew)

```bash
brew install pango cairo gdk-pixbuf libffi
```

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install -y libpango-1.0-0 libcairo2 libgdk-pixbuf2.0-0 libffi-dev
```

#### Windows

- Install [GTK3 Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)
- Add the `bin/` folder from the install to your system `PATH`

---

## 🚀 Usage

### CLI

```bash
poetry run resume-as-code build <input-file> [--output-html file.html] [--output-pdf file.pdf]
```

### Example

```bash
poetry run resume-as-code build examples/example_resume.yaml --output-html output/my_resume.html --output-pdf output/my_resume.pdf
```

---

## 🧪 Testing

Run tests using:

```bash
poetry run pytest
```

---

## 📄 License

[MIT License](LICENSE)

---

## 🤝 Contributing

Pull requests welcome! If you have an idea for a new feature or a bug fix, open an issue or submit a PR.

---

## 🙌 Acknowledgements

- [WeasyPrint](https://weasyprint.org/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Click](https://click.palletsprojects.com/)
