# Own Cat Tool

This is a custom implementation of the `cat` command in Python. It supports numbering all output lines and numbering non-blank output lines.

## Requirements

- Python 3

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/username/OwnCatTool.git
    ```

    Replace `username` with your GitHub username.

2. Navigate to the project directory:

    ```bash
    cd OwnCatTool
    ```

3. Run the script:

    ```bash
    python3 own_cat_py.py [options] [file...]
    ```

    Replace `[options]` with any of the following options:

    - `-n`: Number all output lines
    - `-b`: Number non-blank output lines

    Replace `[file...]` with the path to one or more files. If no file is specified, the script will read from standard input.

    For example, to number all lines in `file.txt`, you would run:

    ```bash
    python3 own_cat_py.py -n file.txt
    ```

    To read from standard input, you would run:

    ```bash
    echo "Hello, world!" | python3 own_cat_py.py -n
    ```

