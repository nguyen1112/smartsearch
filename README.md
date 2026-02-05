# SmartSearch

**AI-Powered Local Document Intelligence Platform**

Search across 1400+ file formats using semantic AI search. Your data stays on your computer.

---

## Features

- 🔍 **Semantic Search** - Find documents by meaning, not just keywords
- 📄 **1400+ File Formats** - PDF, Word, Excel, images, code, CAD files, and more
- 👁️ **OCR Support** - Extract text from scanned documents and images
- ⚡ **Real-time Indexing** - Automatically index new files as they're added
- 🔒 **100% Local** - Your documents never leave your computer
- 🎨 **Modern Interface** - Clean, fast web UI with dark mode

---

## Installation

### Requirements

- Python 3.11 or higher
- Docker
- 10GB free disk space

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/nguyen1112/smartsearch.git
cd smartsearch/apps/smartsearch

# 2. Install SmartSearch
pip install -e .

# 3. Run SmartSearch
smartsearch
```

SmartSearch will open in your browser at `http://localhost:8274`

---

## Platform-Specific Setup

### Linux

```bash
# Install Docker
sudo apt-get update
sudo apt-get install docker.io

# Install SmartSearch
git clone https://github.com/nguyen1112/smartsearch.git
cd smartsearch/apps/smartsearch
pip install -e .
smartsearch
```

### macOS

```bash
# Install Docker Desktop from: https://www.docker.com/products/docker-desktop

# Install SmartSearch
git clone https://github.com/nguyen1112/smartsearch.git
cd smartsearch/apps/smartsearch
pip3 install -e .
smartsearch
```

### Windows

```powershell
# 1. Install Docker Desktop from: https://www.docker.com/products/docker-desktop
# 2. Install Python 3.11+ from: https://www.python.org/downloads/

# 3. Install SmartSearch (in PowerShell or WSL2)
git clone https://github.com/nguyen1112/smartsearch.git
cd smartsearch/apps/smartsearch
pip install -e .
smartsearch
```

---

## Usage

1. **Start SmartSearch**: Run `smartsearch` command
2. **Add Folders**: Click "Add Folder" button to index your documents
3. **Search**: Type in the search box - results update instantly
4. **Enable Auto-Index**: Turn on to automatically index new files

---

## How It Works

SmartSearch uses:
- **Typesense** - Fast search engine with vector search
- **Apache Tika** - Extract text from any file format
- **AI Embeddings** - Understand document meaning for semantic search
- **Docker** - Easy setup with containerized services

---

## Troubleshooting

### Docker containers won't start
```bash
docker ps  # Check if Docker is running
docker logs smartsearch-search-engine  # Check logs
```

### Port already in use
```bash
# Change the port
export SMARTSEARCH_PORT=8275
smartsearch
```

### Permission errors (Linux)
```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

## Supported File Formats

**Documents**: PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), Text, Markdown, RTF

**Images**: JPEG, PNG, GIF, TIFF, BMP (with OCR)

**Code**: Python, JavaScript, Java, C++, HTML, CSS, JSON, XML, YAML

**CAD**: AutoCAD (.dwg, .dxf), SolidWorks

**Archives**: ZIP, RAR, 7Z, TAR

**And 1400+ more formats!**

---

## Contact

**Nguyen T Nguyen**
- Email: nnguyen.t.nguyen@gmail.com
- GitHub: [@nguyen1112](https://github.com/nguyen1112)

---

## License & Credits

Apache 2.0 License - Copyright © 2026 Nguyen T Nguyen

Based on [File Brain](https://github.com/Hamza5/file-brain) by Hamza Abbad
