import os

def finder(files, queries):
    query_hash = {}
    for query in queries:
        query_hash[query] = True

    result = []
    for i in files:
        if os.path.basename(i) in query_hash:
            result.append(i)
            
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
