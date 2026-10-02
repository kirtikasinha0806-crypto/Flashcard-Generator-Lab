A simple Python project that uses the Hugging Face API to generate flashcards on any topic using an AI model.

## Technologies
- Python
- Hugging Face Hub
- Inference API
- python-dotenv

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install huggingface_hub python-dotenv
```

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token_here
```

## Run

```bash
python app.py
```

Enter a topic when prompted, and the program generates 5 flashcards containing questions and answers.

## Security

Never upload your actual `.env` file or Hugging Face token to GitHub.
