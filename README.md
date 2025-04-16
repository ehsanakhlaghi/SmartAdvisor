# SmartAdvisor 🔒🤖  
**LLM-Based Security Recommendation Engine for Docker and Kubernetes Configurations**

SmartAdvisor is a research prototype that uses large language models (LLMs) to detect, analyze, and remediate misconfigurations in Dockerfiles and Kubernetes manifests. It leverages OpenAI's GPT-4 to provide contextual, human-readable security recommendations based on industry standards such as CIS Benchmarks, OWASP CSVS, and NIST SP 800-190.

---

## ✨ Features

- 🔍 LLM-powered misconfiguration detection
- 🛠 Context-aware remediation suggestions
- 📜 Natural language explanations
- 💡 Dual interface: CLI + Flask web app
- 📈 Evaluation-ready benchmarking dataset
- 📦 Dockerized and CI/CD ready

---

## 📂 Repository Structure

smartadvisor/ ├── app.py # Flask + CLI entry point ├── prompt_engine.py # Prompt generation logic ├── parser.py # Preprocessor and tokenizer ├── report_generator.py # HTML and JSON output generation ├── docker-compose.yml # Containerized local dev setup ├── static/ # Web assets ├── templates/ # HTML views └── data/ # Sample config files and annotations


---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.11+
- Docker (optional for containerized use)
- OpenAI API key

### 🧪 Installation

```bash
git clone https://github.com/ehsanakhlaghi/SmartAdvisor.git
cd SmartAdvisor
pip install -r requirements.txt

 **Run with GPT-4**

export OPENAI_API_KEY=your-key-here
python app.py --input sample.yaml

**Or launch the web UI:**

flask run

Benchmark Dataset

This repo includes a curated dataset of 530 real-world container configuration files, labeled with security annotations. Used for evaluating precision, recall, and remediation accuracy.





