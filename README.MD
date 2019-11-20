# directory sorter [![Build Status](https://travis-ci.org/ltblueberry/directory-sorter.svg?branch=master)](https://travis-ci.org/ltblueberry/directory-sorter)
It's a simple python script that take all files in specified directory and move them to created sub directories by file type.

# Make executable
```
chmod a+x directory_sorter.py
```

# Usage
```
./directory_sorter.py -d [directory]
```
or
```
./directory_sorter.py --directory [directory]
```

# Example
In **test** directory we have **4 files**: 2 txt, 1 png and 1 without extension.

After executing next command
```
./directory_sorter.py -d test
```

We have next output and result
```
1 files moved to /Users/user/Documents/github/directory-sorter/test/no_extension
1 files moved to /Users/user/Documents/github/directory-sorter/test/png
2 files moved to /Users/user/Documents/github/directory-sorter/test/txt
```

## License

**[MIT License](LICENSE)**

Copyright (c) 2019 [ltblueberry](https://github.com/ltblueberry)