# PyLogger

A dynamic logger for Python3.6+. Supports logging in text or JSON format. 
Can output logs to console, a file, and/or a Database. 

The Database plugin supports any database engine that follows the 
[Python DB API 2.0](https://www.python.org/dev/peps/pep-0249/ "Python Software Foundation"). 

## Usage
To create a simple logger write:
```python
logger = PyLogger()
```
This will output only to the console and log any priority in text format.
```text
Log: "Test", Log type: verbose
```

A more dynamic logger would be:
```python
from pylogger import PyLogger, formats, transporters, Levels
logger = PyLogger(
            input_formats=[
                formats.Timestamp,
                formats.FileCaller,
                formats.ClassCaller,
                formats.FunctionCaller
            ],
            transporters=[
                transporters.FileTransporter('error.log', Levels.ERROR),
                transporters.Console()
            ],
            json=True,
            level=Levels.INFO
        )
```

This will log any event with higher priority than `Levels.INFO` to the Console and `Levels.ERROR` to `error.log`, 
generate a json formatted output to *console* and *file* `error.log` (if ERROR or higher priority),
and add the timestamp, function caller, class caller and file caller.
```json
{"log": "Test", "timestamp": "Sat Nov 24 22:40:21 2018", "File caller": "console-test.py", "Class caller": "MyClass", "Function caller": "my_func", "Log type": "error"}
```

## Documentation
These are the default argument
```python 
    logger = PyLogger(self, input_formats: Format or List[Format]=None,
                 transporters: List[Transporter]=Console(),
                 json: bool=False, level: Levels=Levels.VERBOSE, name: str=None)
```

### Transporters

---
A transporter is the vehicle responsible for delivering the log to the console, 
file, or Database. 


Generic arguments for a Transporter
-   level: Levels **default: `None`**
-   name: str **default: `None`**
-   trans_id: str **default: `None`**

Transporters can have a log level independent of the one specified in the 
creation of the PyLogger.

```python
from pylogger import PyLogger, transporters, Levels
logger = PyLogger(
    transporters=[
        # 1
        transporters.FileTransporter(filename='everything.log'),
        # 2
        transporters.FileTransporter(filename='logs.log', level=Levels.WARN),
        # 3
        transporters.FileTransporter(filename='info.log', level=Levels.INFO, same_level=True),
         # 4
        transporters.Console(level=Levels.INFO)
    ],
    json=True,
    level=Levels.VERBOSE
    )
```
1. Logs to 'everything.log' when log priority is higher than or equal to `VERBOSE(1)`. `logger.verbose('Message')`
2. Logs to 'logs.log' only when the log priority is higher than or equal to `WARN(4)`
3. Logs to 'info.log' only when the log priority is equal to `INFO(3)`
4. Logs to 'Console' when log priority is higher than or equal to `INFO(3)` 

Transporters can be assigned an unique ID in which you can later use to 
log only to that Transporter.

```python
logger = PyLogger(
    transporters=[
        transporters.FileTransporter(
            filename='error.log', 
            level=Levels.ERROR, 
            same_level=True,
            trans_id='file1'
        ),
        transporters.Console(
                level=Levels.INFO, 
                trans_id='console1'
        )
    ]
)

# functionality extends across all of the log methods

# log to console1 transporter
logger.info(message='My message', trans_id='console1')

# log to file1 transporter
logger.error(message='My message', trans_id='file1')
```

Examples:
```python
# will log to Console only the log requests of priority WARN(4)
c_tranporter = Console(level=Levels.WARN, same_level=True)

# will log to a file by a log request of priority higher than or equal to DEBUG(3)
file_tranporter = FileTransporter('file.log', Levels.DEBUG, same_level=False)
```

You can create a `Transporter` of your own by extending the `Transporter` class.

#### Console
Outputs the log to the console

#### File
Outputs log to a designated file

#### Database
Outputs logs to a database

Works with the most common python modules for connecting 
to database engines as long as they comply with the
[Python DB API 2.0](https://www.python.org/dev/peps/pep-0249/ "Python Software Foundation") standards.

The `DbSchema` object is used to specify the the log and type of log of each column:

The `columns` argument can be a `Dict[str, Format]` or `List[ColumnMeta]`
```python
from pylogger.protocols.db import DbSchema, ColumnMeta
from pylogger import formats

schema_object: DbSchema = DbSchema(
    table='Log',
    log_column='log',
    log_type_column='type',
    # dict of string with Format
    columns={
        # DB Column Name: Type
        'time': formats.Timestamp,
        'class': formats.ClassCaller,
        'line': formats.FileLine,
        'file': formats.FileCaller
    } 
    # or list of ColumnMeta
    # columns=[
    #    ColumnMeta('time', formats.Timestamp),
    #    ColumnMeta('class', formats.ClassCaller),
    #    ...
    # ] 
)
```

The database transporter needs the DB engine`Connection` object and `DbSchema` object in order to work.

```python
from pylogger.transporters import DbTransporter
from pylogger import PyLogger, formats
import dbmodule

connection = dbmodule.connect(host='localhost', database='MyDatabase', user='me', password='123456')

logger = PyLogger(
        input_formats=[
            formats.FileLine,
            formats.FileCaller,
            formats.Timestamp,
            formats.ClassCaller
        ],
        transporters=DbTransporter(connection, schema_object),
        # does not affect output of DbTransporter
        json=True
    )
    
logger.verbose('My Log')
```
Assuming that:
- table: Log
- log_column: log
- log_type_column: type
- Format Columns: time, class, line, file
 


The logger will insert in DB:
```text
        time         |  class   | line |   log    |    file    |  type   
---------------------+----------+------+----------+------------+---------
 2018-11-24 22:09:57 | MyClass  | 66   |  My Log  | db-test.py | verbose
```

### Formats

---
You can create a `Format` of your own by extending the `Format` class.
#### Timestamp
Adds a timestamp to the log

#### Callers
  - FileCaller: Adds the file from which the logger was called
  - ClassCaller:  Adds the class from which the logger was called
  - FunctionCaller: Adds the function from which the logger was called
  
#### FileLine
Says in which line the log was requested

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
