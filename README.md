# PyLogger

A dynamic logger for Python3.5+. Supports logging in text or JSON format. 

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
                transporters.FileTransporter('info.log', Levels.ERROR),
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
    logger = PyLogger(self, input_formats: Format or List[Format]=None,
                 transporters: List[Transporter]=Console(),
                 json: bool=False, level: Levels=Levels.INFO, name: str=None)
```

### Transporters
---
A transporter is the vehicle responsible for delivering the log to the console or 
designated file. It can be assigned a level in which it is allowed to log. 
Also if needs to be the same or higher log level as the level requested by the API. 

Generic arguments for a Transporter
-   level: Levels **default: None**
-   name: str **default: None**


Examples:
```python
# will log to Console only the log requests of priority WARN(4)
c_tranporter = Console(level=Levels.WARN, same_level=True)

# will log to a file by a log request of priority higher than DEBUG(3)
file_tranporter = FileTransporter('file.log', Levels.DEBUG, same_level=False)
```

You can create a `Transporter` of your own by extending the `Transporter` class.

#### Console
Outputs the log to the console
#### File
Outputs log to a designated file


### Formats

---
You can create a `Format` of your own by extending the `Format` class.
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
