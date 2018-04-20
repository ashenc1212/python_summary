This file briefly summarize what is covered in the code.

logging: 
- basic logging:
    - logging.debug/info/warning/error/critical
        - %-style string formatting
    - logging.basicConfig(filename = '', level = logging.xxx, format = 'xxx'), should go before others
        - when the function in another package called logging.xxx, it is just like calling in the current script
- use loggers
    - config with json files. load into a dictionary. logging.config.dictConfig()
    - loggers, formaters, handlers


decorator:
- not much to say about it. A decorator get a function as input and output another function.
    - commonly used cases: @classmethod, @synchronized(lock), some functions in click package like @click.command, @click.argument.

context manager:
- "with" statement
    - call "__enter__" before context, call "__exit__" after context, use return value in "as"
- can define a new context manager using @contextmanager. (from contextlib import contextmanager, no need to write __enter__ or __exit__)


