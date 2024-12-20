# Custom Logger Class

## Overview

This project provides a custom logger class designed to facilitate logging in Python applications. The logger supports logging to both the terminal and a log file, ensuring a comprehensive log of application events.

## Features

- Logging to both the console and a file.
- Configurable log level settings.
- Customizable log formatting.
- Prevents duplicate logs by checking existing handlers.

## Installation

No specific installation is required. Simply include the `logger.py` file in your project.

## Usage

Here is an example of how to use the custom logger class:

```python
from logger import Logger

# Create a logger instance
logger = Logger('application.log')

# Log messages of various severities
logger.info('This is an informational message.')
logger.error('This is an error message.')
logger.debug('This is a debug message.')
logger.critical('This is a critical message.')
