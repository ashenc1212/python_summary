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

Concurrency:
- threading: 
    - basic threading: class: Thread (target, arguments), method: start, join
    - Lock, RLock, (Bounded)Semaphore: acquire()/release() (can be used in "with")
    - condition variable (can be used in "with")
    - event: is_set(), set(), clear(), wait()
- multiprocessing
    - similar to threading API. Process(target= , argument = )
    - set_start_method() and get_context()
    - Queue() and Pipe() to share information. Queue has lock with itself. Pipe() can only have one user at each end. 
        - Attention: Queue internally uses a pipe with finite size. So Queue.put() may block
            - this means that using p.join() before the queue is empty may cause deadlock.
            - can use cancel_join_thread to prevent a thread from being automatically joined.
    - usually not use shared objects. Can be done using Manager() if needed.
    - Process Pools
- concurrent.futures
    - I think it's not useful. 
- queue 
    - queue.Queue implements synchronized queue structure. Can be used with threading.

typing:
- basic usage:
    - use : and -> to indicate type
    - type alias
    - new type
    - callable
- can use in comments

click:
- decorators (functions that return a decorator): click.command/argument/option/group/make_pass_decorator

unittest:
- assertions:
    - assertEqual, assertRaise
- setUp(), tearDown(), setUpClass(), tearDownClass()
- unittest.mock
    - use patch (as decorator or context manager) to create mock objects
