from test_framework import generic_test

def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError("Empty string is not a valid path")
        
    DELIMETER = '/'
    PARENT_DIR = '..'
    path_names = []

    if path[0] == '/':
        path_names.append('/')

    tokens = [token for token in path.split(DELIMETER) if token not in ['', '.']]

    for token in tokens:
        if token == PARENT_DIR:
            if not path_names or path_names[-1] == PARENT_DIR:
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                else:
                    path_names.pop()
        else:
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith("//"):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
