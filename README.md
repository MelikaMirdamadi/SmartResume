# 📝 SmartResume - AI-Powered Resume Reviewer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

SmartResume is an intelligent resume analysis tool powered by AI that provides detailed feedback to help you improve your resume. Upload your resume in PDF or TXT format and get comprehensive insights on structure, content quality, skills presentation, and specific improvement suggestions.

## 🌟 Features

- **AI-Powered Analysis**: Uses Mistral LLM through Ollama for intelligent resume review
- **Multi-Format Support**: Accepts both PDF and TXT file formats
- **Job-Specific Feedback**: Optional job role input for targeted analysis
- **Comprehensive Review**: Analyzes structure, content, skills, and provides improvement suggestions
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- **Real-time Processing**: Fast analysis with loading indicators

## 🚀 Quick Start

### Prerequisites

Before running SmartResume, ensure you have:

1. **Python 3.8 or higher** installed
2. **Ollama** installed and running
3. **Mistral model** available in Ollama

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MelikaMirdamadi/SmartResume.git
   cd SmartResume
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and setup Ollama:**
   
   **For Windows:**
   - Download Ollama from [ollama.ai](https://ollama.ai/)
   - Install and run Ollama
   
   **For macOS/Linux:**
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

4. **Pull the Mistral model:**
   ```bash
   ollama pull mistral
   ```

5. **Verify Ollama setup:**
   ```bash
   ollama list
   ```
   You should see `mistral:latest` in the list.

### Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run main.py
   ```
   
   Or if `streamlit` command is not in PATH:
   ```bash
   python -m streamlit run main.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:8502
   ```

3. **Upload your resume** and get AI-powered feedback!

## 📖 How to Use

1. **Launch the application** using the commands above
2. **Upload your resume** in PDF or TXT format
3. **Enter job role** (optional) for targeted feedback
4. **Click "Analyze Resume"** button
5. **Review the AI feedback** and suggestions

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **AI Model**: Mistral (via Ollama)
- **PDF Processing**: PyPDF2
- **Language**: Python 3.8+

## 📋 Dependencies

All dependencies are listed in `requirements.txt`:

```
streamlit==1.49.1
PyPDF2==3.0.1
ollama==0.3.3
# ... and other required packages
```

## 🔧 Configuration

### Changing the AI Model

To use a different Ollama model, modify line 61 in `main.py`:

```python
response = chat(
    model='your-preferred-model',  # Change this to your model
    messages=[...],
)
```

Available models can be checked with:
```bash
ollama list
```

### Customizing the Analysis Prompt

You can modify the analysis criteria by editing the prompt in `main.py` (lines 42-55).

## 🐛 Troubleshooting

### Common Issues

1. **"Import 'streamlit' could not be resolved"**
   - Install requirements: `pip install -r requirements.txt`
   - Restart your IDE/editor

2. **"Ollama connection error"**
   - Ensure Ollama is running: `ollama serve`
   - Check if Mistral model is available: `ollama list`
   - Pull Mistral if missing: `ollama pull mistral`

3. **"Streamlit command not found"**
   - Use: `python -m streamlit run main.py`
   - Or add Python Scripts to PATH

4. **PDF processing errors**
   - Ensure the PDF is not password-protected
   - Try converting PDF to TXT format

### Performance Tips

- **Large files**: For large resume files, processing may take longer
- **Model performance**: Mistral provides good balance of speed and quality
- **Memory usage**: Close other applications if experiencing slow performance

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Enhancements

- [ ] Support for more file formats (DOCX, RTF)
- [ ] Multiple AI model options
- [ ] Resume scoring system
- [ ] Export analysis reports
- [ ] Batch processing capabilities
- [ ] Resume template suggestions
- [ ] Integration with job boards

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/MelikaMirdamadi/SmartResume/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

## 🏆 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Ollama](https://ollama.ai/) for local AI model deployment
- [Mistral AI](https://mistral.ai/) for the powerful language model
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing capabilities

---

⭐ **Star this repository** if you find it helpful!

**Made with ❤️ by [MelikaMirdamadi](https://github.com/MelikaMirdamadi)**
