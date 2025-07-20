# Streamlit Llama Blog Generator

An AI-powered blog writer built on LLaMA 2 and CTransformers, with caching & streaming capabilities. This application allows users to generate blog posts on any topic using a local LLaMA 2 model.

## Features

- **Local AI Model**: Uses LLaMA 2 7B Chat model locally via CTransformers
- **Streamlit Interface**: Clean and intuitive web interface
- **Streaming Generation**: Real-time token streaming for better user experience
- **Multiple Writing Styles**: Generate content for different audiences:
  - Researchers
  - Data Scientists
  - Data Engineers
  - General Audience
- **Customizable Length**: Specify the number of words for your blog post
- **Caching**: Model is cached to avoid reloading on each request

## Prerequisites

- Python 3.9+
- LLaMA 2 7B Chat model file (`llama-2-7b-chat.ggmlv3.q8_0.bin`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Revanthinfosec/stream-llama-blog.git
cd stream-llama-blog
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the LLaMA 2 model:
   - Download `llama-2-7b-chat.ggmlv3.q8_0.bin` from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)
   - Place it in the project root directory

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your blog topic, specify the number of words, and select your target audience

4. Click "Generate" to create your blog post

## Configuration

The model configuration can be adjusted in `app.py`:

```python
config = {
    "max_new_tokens": 256,  # Maximum tokens to generate
    "temperature": 0.01,    # Creativity level (0.0 = deterministic, 1.0 = random)
    "threads": 4           # Number of CPU threads to use
}
```

## Model Path

Update the `MODEL_PATH` variable in `app.py` to point to your model file location:

```python
MODEL_PATH = "path/to/your/llama-2-7b-chat.ggmlv3.q8_0.bin"
```

## Dependencies

- `streamlit`: Web interface framework
- `ctransformers`: Efficient inference for LLaMA models
- `langchain`: LLM framework and utilities
- `langchain-community`: Community-maintained LangChain components
- `sentence-transformers`: Text embedding models
- `fastapi`: API framework (if needed for future extensions)
- `python-box`: Enhanced dictionary access
- `watchdog`: File system monitoring
- `ipykernel`: Jupyter kernel support

## Project Structure

```
stream-llama-blog/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore           # Git ignore rules
└── llama-2-7b-chat.ggmlv3.q8_0.bin  # Model file (not tracked in git)
```

## Performance Tips

- **Hardware**: The model requires significant RAM (8GB+ recommended)
- **Threading**: Adjust the `threads` parameter based on your CPU cores
- **Temperature**: Lower values (0.01-0.1) produce more focused content
- **Token Limit**: Increase `max_new_tokens` for longer blog posts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [Meta AI](https://ai.meta.com/) for LLaMA 2
- [TheBloke](https://huggingface.co/TheBloke) for the GGML model conversion
- [CTransformers](https://github.com/marella/ctransformers) for efficient inference
- [Streamlit](https://streamlit.io/) for the web interface framework

## Support

For issues and questions, please open an issue on the GitHub repository.
