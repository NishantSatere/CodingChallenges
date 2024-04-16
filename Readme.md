To create an executable of your Python script, you can use a package like PyInstaller. However, to use it as a command like `ccat test.txt`, you need to add the executable to your system's PATH. Here's how you can do it:

1. First, install PyInstaller. You can do this with pip:

```bash
pip install pyinstaller
```

2. Then, use PyInstaller to create an executable from your script. The `--onefile` option creates a single executable file:

```bash
pyinstaller --onefile own_cat_py.py
```

This will create a `dist` directory in your current directory. Inside `dist`, you'll find your executable file, `own_cat_py`.

3. Rename the executable to `ccat`:

```bash
mv dist/own_cat_py dist/ccat
```

4. Now, you need to add the `dist` directory to your system's PATH. On a Unix-like system like macOS, you can do this by adding a line to your `.bashrc` or `.zshrc` file (depending on which shell you're using). The line should look like this, but replace `/path/to/dist` with the actual path to the `dist` directory:

```bash
export PATH="$PATH:/path/to/dist"
```

5. Finally, source your `.bashrc` or `.zshrc` file to apply the changes:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

Now, you should be able to use `ccat` as a command from anywhere in your system:

```bash
ccat test.txt
```

This will print the contents of `test.txt`.