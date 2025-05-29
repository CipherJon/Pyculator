# Advanced Calculator

A feature-rich command-line calculator with support for various mathematical operations, calculation history, and comprehensive error handling.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Advanced mathematical operations:
  - Power/exponentiation
  - Square root
  - Percentage calculations
  - Modulo operation
  - Absolute value
- Calculation history
- Clear screen functionality
- Comprehensive error handling:
  - Input validation
  - NaN detection and handling
  - Division by zero protection
  - Graceful handling of keyboard interrupts (Ctrl+C, Ctrl+D)
- Type hints and documentation
- Unit tests with pytest

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/calculator.git
cd calculator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the calculator:
```bash
python -m calculator.main
```

### Available Operations

1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Percentage
8. Modulo
9. Absolute Value

### Additional Commands

- `h`: Show calculation history
- `c`: Clear screen
- `q`: Quit calculator

### Error Handling

The calculator includes comprehensive error handling:
- Invalid numeric inputs are rejected with clear error messages
- NaN (Not a Number) values are detected and rejected
- Division by zero is prevented
- Keyboard interrupts (Ctrl+C, Ctrl+D) are handled gracefully
- All operations include proper input validation

## Development

### Running Tests

Run the test suite:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=calculator
```

### Code Style

The project follows PEP 8 style guidelines. You can check the code style using:
```bash
flake8 calculator tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
