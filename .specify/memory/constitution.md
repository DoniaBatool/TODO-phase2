# Todo Hackathon Phase I Constitution
<!-- In-Memory Python Console Todo Application -->

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
**All features must be specification-first:**
- Every feature starts with a complete specification document in `/specs` folder
- Specifications must include user stories and acceptance criteria
- No code implementation without approved specification
- Claude Code must reference specifications during implementation
- Specs must be updated if requirements change

### II. Clean Code & Python Standards
**Code quality is mandatory:**
- Follow PEP 8 style guidelines strictly
- Type hints required for all function signatures
- Docstrings for all classes and public methods
- Descriptive variable and function names (no single letters except iterators)
- Maximum function length: 50 lines
- Single Responsibility Principle for all functions and classes

### III. In-Memory Storage Only
**Phase I constraint - no persistence:**
- All task data stored in Python data structures (lists, dictionaries)
- No file I/O, no databases, no external storage
- Data exists only during program runtime
- Clear data structure design documented in specs

### IV. Test-First Development
**Testing before implementation:**
- Unit tests written for each feature before implementation
- Tests must fail initially (Red)
- Implementation makes tests pass (Green)
- Refactor while maintaining green tests
- Minimum 80% code coverage required

### V. Command-Line Interface Excellence
**User experience matters even in CLI:**
- Clear, user-friendly menu system
- Proper input validation with helpful error messages
- Formatted output (tabular display for task lists)
- Confirmation prompts for destructive operations (delete)
- Graceful exit handling

### VI. Core Feature Completeness
**All 5 Basic Level features are mandatory:**
1. **Add Task**: Create new todo with title and description
2. **Delete Task**: Remove task by ID with confirmation
3. **Update Task**: Modify existing task details
4. **View Task List**: Display all tasks with status indicators
5. **Mark as Complete**: Toggle completion status

Each feature must be fully functional and tested before moving to next.

## Technology Stack Requirements

### Mandatory Technologies
- **Python Version**: 3.13 or higher
- **Package Manager**: UV (for dependency management)
- **Development Tool**: Claude Code with Spec-Kit Plus
- **Version Control**: Git with meaningful commit messages

### Project Structure
```
/src
  /todo
    __init__.py
    task.py          # Task model/class
    manager.py       # Task management logic
    cli.py           # Command-line interface
    main.py          # Application entry point
/tests
  test_task.py
  test_manager.py
  test_cli.py
/specs
  overview.md
  /features
    task-crud.md
README.md
CLAUDE.md
pyproject.toml
```

### Code Organization
- Separation of concerns: Model, Logic, Interface
- Task class represents individual todo items
- Manager class handles CRUD operations
- CLI class provides user interface
- Main module orchestrates the application

## Development Workflow

### Specification Phase
1. Write feature specification in `/specs/features/`
2. Include user stories (As a user, I want...)
3. Define acceptance criteria (Given/When/Then)
4. Get specification approved before coding

### Implementation Phase
1. Reference spec file with Claude Code: `@specs/features/[feature].md`
2. Write unit tests first (TDD)
3. Implement feature to pass tests
4. Verify all acceptance criteria met
5. Run full test suite before marking complete

### Quality Gates
**Before considering a feature complete:**
- [ ] Specification document exists and is complete
- [ ] Unit tests written and passing
- [ ] Code follows Python standards (PEP 8)
- [ ] Type hints present
- [ ] Docstrings written
- [ ] Manual testing performed
- [ ] No bugs or edge cases remaining

### Git Workflow
- Meaningful commit messages: `feat: add task creation functionality`
- Commit after each completed feature
- Keep commits atomic and focused
- Include spec files in repository

## Constraints & Non-Goals

### In Scope for Phase I
- Basic task management (add, delete, update, view, complete)
- In-memory storage only
- Single-user console application
- Input validation and error handling

### Out of Scope for Phase I
- ❌ No file persistence
- ❌ No database integration
- ❌ No multi-user support
- ❌ No advanced features (priorities, tags, due dates)
- ❌ No web interface
- ❌ No authentication

### Data Model Constraints
**Task must have:**
- `id`: Unique integer identifier (auto-incremented)
- `title`: String (1-200 characters, required)
- `description`: String (max 1000 characters, optional)
- `completed`: Boolean (default False)
- `created_at`: Timestamp (auto-generated)

## Error Handling Standards

### User Input Validation
- Empty title → Show error, retry
- Invalid ID → "Task not found" message
- Invalid menu choice → Show valid options, retry
- Always provide clear error messages

### Graceful Degradation
- Handle unexpected inputs without crashing
- Use try-except blocks appropriately
- Log errors to console during development
- Never expose Python tracebacks to end user

## Governance

### Constitution Authority
- This constitution supersedes all other development practices
- All Claude Code interactions must reference and follow these principles
- Deviations require documented justification
- CLAUDE.md file must reference this constitution

### Acceptance Criteria
**Phase I is complete when:**
1. All 5 Basic Level features fully implemented and tested
2. All tests passing with 80%+ coverage
3. Code meets all quality standards
4. README.md includes setup and usage instructions
5. CLAUDE.md includes Claude Code development guidelines
6. specs folder contains all feature specifications

### Success Metrics
- ✅ Application runs without errors
- ✅ All CRUD operations functional
- ✅ User-friendly CLI experience
- ✅ Clean, maintainable codebase
- ✅ Complete documentation
- ✅ Ready for demo video (under 90 seconds)

**Version**: 1.0.0 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-09
