# Todo Console App - Phase I

A command-line todo list manager built with Python following **Spec-Driven Development** principles.

## 🎯 Project Overview

This is Phase I of the Todo Hackathon project, implementing a simple in-memory console application for managing daily tasks. The project follows Test-Driven Development (TDD) and clean code principles.

## ✨ Features

### Phase I - Basic Level Features
- ✅ **Add Task**: Create new todo items with title and description
- ✅ **View Tasks**: Display all tasks with status indicators
- ✅ **Update Task**: Modify existing task details
- ✅ **Mark Complete**: Toggle task completion status
- ✅ **Delete Task**: Remove tasks from the list

## 🛠️ Technology Stack

- **Language**: Python 3.13+
- **Package Manager**: UV
- **Development**: Claude Code + Spec-Kit Plus
- **Testing**: pytest with coverage
- **Storage**: In-memory (Python data structures)

## 📁 Project Structure

```
todo/
├── .specify/
│   └── memory/
│       └── constitution.md      # Project principles and standards
├── specs/
│   ├── README.md                # Specs guide
│   ├── overview.md              # Project overview
│   └── features/
│       └── add-task.md          # Feature specifications
├── src/
│   └── todo/
│       ├── __init__.py
│       ├── task.py              # Task model with validation
│       ├── manager.py           # Task CRUD operations
│       ├── cli.py               # Command-line interface
│       └── main.py              # Application entry point
├── tests/
│   ├── test_task.py             # Task model tests
│   ├── test_manager.py          # Manager tests
│   └── test_cli.py              # CLI tests
├── pyproject.toml               # Project configuration
├── CLAUDE.md                    # Claude Code instructions
└── README.md                    # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.13 or higher
- UV package manager (optional but recommended)
- WSL 2 (for Windows users)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd todo
```

2. **Install UV (if not already installed)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **Create virtual environment and install dependencies**
```bash
# Using UV
uv venv
source .venv/bin/activate  # On Windows WSL/Linux
# .venv\Scripts\activate   # On Windows CMD

uv pip install -e ".[dev]"
```

Or using standard Python:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 🎮 Usage

### Run the Application

```bash
# Using the installed command
todo

# Or run directly
python -m src.todo.main
```

### Main Menu
```
==================================================
           TODO LIST MANAGER
==================================================
1. Add Task
2. View All Tasks
3. Update Task
4. Mark Task Complete/Incomplete
5. Delete Task
6. Exit
==================================================
```

## 🧪 Testing

### Run All Tests
```bash
pytest
```

### Run Tests with Coverage
```bash
pytest --cov=src/todo --cov-report=html
```

### Run Specific Test File
```bash
pytest tests/test_task.py
pytest tests/test_manager.py
pytest tests/test_cli.py
```

### View Coverage Report
```bash
# Open coverage report in browser
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## 📊 Test Coverage Goal

**Target**: 80%+ code coverage

Current coverage includes:
- ✅ Task model validation
- ✅ Task manager CRUD operations
- ✅ Error handling scenarios
- ✅ Edge cases (empty input, max length, etc.)

## 🎯 Data Model

### Task Entity
```python
@dataclass
class Task:
    id: int              # Auto-incremented unique identifier
    title: str           # 1-200 characters, required
    description: str     # Max 1000 characters, optional
    completed: bool      # Default: False
    created_at: datetime # Auto-generated timestamp
```

## 🔧 Development Guidelines

### Code Standards
- Follow PEP 8 style guidelines
- Type hints required for all functions
- Docstrings for all classes and public methods
- Maximum function length: 50 lines
- Single Responsibility Principle

### Test-Driven Development
1. Write tests first (Red)
2. Implement feature (Green)
3. Refactor while keeping tests green
4. Maintain 80%+ coverage

### Git Workflow
```bash
git add .
git commit -m "feat: add task creation functionality"
git push
```

## 📝 Specification-Driven Development

All features are implemented following detailed specifications in the `specs/` directory:

1. Read specification: `specs/features/[feature].md`
2. Write tests based on spec test cases
3. Implement feature according to technical spec
4. Verify all acceptance criteria met

## ❌ Out of Scope (Phase I)

- ❌ File persistence
- ❌ Database integration
- ❌ Multi-user support
- ❌ Advanced features (priorities, tags, due dates)
- ❌ Web interface
- ❌ Authentication

## 🐛 Known Issues

None currently. Please report any bugs!

## 📚 Documentation

- **Constitution**: `.specify/memory/constitution.md` - Core principles
- **Specifications**: `specs/` - Feature specifications
- **Claude Instructions**: `CLAUDE.md` - Development guidelines
- **Hackathon Guide**: `Hackathon II - Todo Spec-Driven Development.md`

## 🎓 Learning Objectives

This project teaches:
- ✅ Spec-Driven Development with Claude Code
- ✅ Test-Driven Development (TDD)
- ✅ Clean code principles
- ✅ Python project structure
- ✅ Command-line interface design
- ✅ Input validation and error handling

## 🚀 Next Steps (Phase II)

- Full-stack web application with Next.js
- FastAPI backend
- PostgreSQL database (Neon)
- User authentication
- RESTful API

## 📄 License

This project is created for educational purposes as part of the Panaversity Hackathon II.

## 👤 Author

**Donia Batool**

---

**Phase**: I  
**Status**: In Development  
**Version**: 0.1.0  
**Last Updated**: December 9, 2025

