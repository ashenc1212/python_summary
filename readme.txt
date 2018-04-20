logging: 
- logging.debug/info/warning/error/critical
- logging.basicConfig(filename = '', level = logging.xxx, format = 'xxx'), should go before others
- when the function in another package called logging.xxx, it is just like calling in the current script
- %-style string formatting
- use loggers, handlers, formatters
- config with json files. logging.config.dictConfig()
https://gist.github.com/pmav99/49c01313db33f3453b22


