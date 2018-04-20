from contextlib import contextmanager

@contextmanager
def tag(content):
    print("begin")
    yield content
    print("end")

with tag("hello world") as content:
    print(content)