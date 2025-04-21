# GPT Translator

GPT Translator is a modern, web-based application that leverages OpenAI's language models to provide high-quality translations across multiple languages. Built with FastAPI and SQLite, it offers an intuitive interface for submitting text and receiving translations.

## Features

- **Multi-language Translation**: Translate text into multiple languages simultaneously
- **Background Processing**: Translations are processed asynchronously in the background
- **Persistent Storage**: All translation tasks and results are stored in a database
- **Clean UI**: Modern, responsive interface built with Bootstrap
- **RESTful API**: Well-structured API endpoints for programmatic access

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, JavaScript, Bootstrap 5
- **AI**: OpenAI GPT models for translation

## Installation

### Prerequisites

- Python 3.8+
- Poetry (optional, for dependency management)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gpt-translator.git
cd gpt-translator
```

2. Install dependencies:

```bash
# With Poetry
poetry install

# With pip
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./sql_app.db
```

## Usage

### Running the Application

1. Start the FastAPI server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the web interface at `http://localhost:8000/index`

### Using the Web Interface

1. Navigate to the main page
2. Enter the text you want to translate in the text area
3. Specify the target languages as a comma-separated list (e.g., "spanish, french, german")
4. Click "Translate"
5. You'll be redirected to a results page showing the status of your translation
6. Refresh the page to see updates if the translation is still in progress

### API Endpoints

- **GET `/index`**: Web interface for translation
- **POST `/translate`**: Submit a translation request
  - Request body: `{"text": "Hello world", "languages": ["spanish", "french"]}`
  - Returns: `{"task_id": 123}`
- **GET `/translate/{task_id}`**: Get the status and results of a translation task

## Project Structure

```
gpt-translator/
├── app/
│   ├── database/
│   │   ├── crud.py        # Database operations
│   │   ├── db.py          # Database connection
│   │   ├── models.py      # SQLAlchemy models
│   │   └── schemas.py     # Pydantic schemas
│   ├── templates/
│   │   ├── index.html     # Translation form
│   │   └── results.html   # Results display
│   ├── utils.py           # Utility functions
│   └── main.py            # FastAPI application
├── pyproject.toml         # Project dependencies
├── poetry.lock           # Locked dependencies
└── .env                  # Environment variables
```

## Development

### Adding Languages

The application supports any language that OpenAI's models can translate to. Simply include the language name in the comma-separated list.

### Database Migrations

The application uses SQLAlchemy's declarative base to create tables automatically. If you modify the models, the changes will be applied when you restart the application.

## Troubleshooting

### Common Issues

- **"ERR_BLOCKED_BY_CLIENT"**: This might be caused by ad blockers or browser extensions. Try disabling them or using a different browser.
- **422 Unprocessable Entity**: Ensure that your request format matches the expected schema.
- **Translations Not Appearing**: Check that your OpenAI API key is valid and has sufficient quota.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.