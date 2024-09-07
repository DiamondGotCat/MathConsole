# MathConsole
Python Interpreter for Mathematics

## Note
The software does not yet support indentation.
However, I think it can be used as an interpreter for mathematics.

## About Plugins
This software has the ability to add other software and make it available within the software in the form of plugins.
For example:
- [Tester](https://github.com/DiamondGotCat/Tester-for-MathConsole) - Test software for plugin system

## Usage
1. run command `mathconsole` to start MathConsole Interpreter
2. enter one line python code

## Unique specifications

### `that` - Use previous result
```
>>> 128 + 128
M: 256
>>> (that + that) / 4
M: 64
>>> that + 16
M: 80
```

## Install
1. Install [NIT](https://github.com/DiamondGotCat/NIT)
2. Install MathConsole using NIT
3. Add MathConsole to the path

### How to add MathConsole to the path

#### in Zsh

```
echo 'export PATH=$PATH:/usr/local/share/mathconsole/bin/' >> ~/.zshrc
source ~/.zshrc
```

#### in Bash

```
echo 'export PATH=$PATH:/usr/local/share/mathconsole/bin/' >> ~/.bashrc
source ~/.bashrc
```
