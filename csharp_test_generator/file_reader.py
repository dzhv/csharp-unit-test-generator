
def read(file_path: str) -> str:
    # TODO
    # check if file exists
    # check if file is not too large

    with open(file_path) as f:
        lines = f.readlines()

    return lines