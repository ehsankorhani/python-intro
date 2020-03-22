# Learning Python
Python learning journey

## Install Python (on Ubuntu 18.04)

**1**. Update package repository list

```bash
$ sudo apt update
```

**2**. Install Supporting Software

The software-properties-common package gives you better control over your package manager
```bash
$ sudo apt install software-properties-common
```

**3**. Add Deadsnakes PPA

Deadsnakes is a PPA with newer releases than the default Ubuntu repositories.

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

Refresh package list another time:

```bash
$ sudo apt update
```

**4**. Install Python 3.7

```bash
$ sudo apt install python3.7
```

Verify the Python version with:

```bash
python ––version
```

---

### References
* [Real Python](https://realpython.com/)
* [Python 3.8.2 documentation](https://docs.python.org/3.8/)
* [Python Practice Book](https://anandology.com/python-practice-book)
* [How To Install Python 3.7 On Ubuntu 18.04](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
