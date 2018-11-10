# PyLogger

A dynamic logger for Python3+. Supports logs in text or JSON format. 

## Usage
To create a simple logger write:
```python
logger = PyLogger()
```
This will output directly to the console and log any priority in text format.

A more modifiable logger would be
```python
from pylogger import PyLogger, formats, transporters, Levels
logger = PyLogger(
            input_formats=[
                formats.Timestamp,
                formats.FileCaller,
                formats.ClassCaller,
                formats.MethodCaller
            ],
            transporters=[
                transporters.FileTransporter('info.log'),
                transporters.Console()
            ],
            json=True,
            level=Levels.INFO
        )
```
This will log any event with higher priority than `Levels.INFO`, generate a json formatted output to console and log file `info.log`, and add the timestamp, function caller, class caller and file caller.

## Documentation

These are the default argument
```python 
    logger = PyLogger(input_formats=None, transporters=Console(), json=False, levels=Levels.INFO)
```

### Transporters

---
#### Console
Outputs the log to the console
#### File
Outputs log to a designated file


### Formats

---
#### Timestamp
Adds a timestamp to the log
#### Callers
  - FileCaller: Adds the file from which the logger was called
  - ClassCaller:  Adds the class from which the logger was called
  - FunctionCaller: Adds the function from which the logger was called

### Levels
The output works by priority. A logger will only output the logs with priorities above the one it was created.

| Log Level | Value |
| :---: | :---: |
| Verbose | 1 |
| Debug | 2 |
| Info | 3 |
| Warn | 4 |
| Error | 5 |

A logger created this with `Levels.WARN` will only log out events logged using `log.warn()` or `log.error()`
