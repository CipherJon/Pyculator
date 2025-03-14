# Pyculator

A simple calculator application implemented in Python with extendable operations.

## Features

- Basic arithmetic operations (+, -, *, /)
- Interactive command-line interface
- Modular architecture for easy extension
- Unit test coverage

## Requirements

- Python 3.8+
- Dependencies:
  - setuptools==68.2.2

Development dependencies:
- pytest==8.0.0
- pytest-cov==4.1.0
- flake8==6.1.0

## Installation

### Using pip
```sh
pip install -r requirements.txt
```

### From source
```sh
python setup.py install
```

## Usage

### Command-line interface
```sh
python -m calculator.main
```
Example session:
```
Enter operation (+, -, *, /): +
Enter first number: 5
Enter second number: 3
Result: 8.0
```

### As a Python module
```python
from calculator.operations import add

result = add(10, 5)
print(result)  # 15.0
```

## Running Tests

```sh
# Run all tests with coverage
pytest --cov=calculator tests/

# View coverage report
pytest --cov-report term-missing
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure:
- All tests pass
- Code follows PEP8 guidelines (verified with flake8)
- New features include appropriate tests

## License
Distributed under the MIT License. See `LICENSE` for more information.
