import os 
import re
import inspect

def _get_parser_list(dirname):
    files=[f.replace(".py"," ") for f in os.listdir(dirname) if not f.startswith("__")]
    return files
    # will return files located in the weatherterm/parsers

def _import_parsers(parserfiles):
    m=re.compile(".+parser$")
    # + is will match one to finity . and $ show the end is parser 
    _modules=__import__("weatherterm.parsers",
                         globals(),
                         locals(),
                         parserfiles,
                         0)

    # the time is to import the module by the _import_parsers; first you need to import the weatherterm.parsers module and 
    # use the insepect package to check the parser classes
    # the inspect.getmembers function returns a list of tuples where the keys represent the property the module ans 
    _parsers =[(k,v) for k,v in inspect.getmembers(_modules) if inspect.ismodule(v) and m.match(k)]
    _classes=dict()
    for k,v in _parsers:
        _classes.update({k,v} for k,v in inspect.getmembers(v) if inspect.isclass(
            v) and m.match(k))
    return _classes
    #looping the items and return a dict

def load(dirname):
    parserfiles=_get_parser_list(dirname)
    return _import_parsers(parserfiles)