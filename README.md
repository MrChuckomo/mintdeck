# mintdeck


```bash
conda env create --prefix ./ops/pyenv/mintdeck_env --file ./environment.yml
conda env remove --prefix ./ops/pyenv/mintdeck_env

conda activate ./ops/pyenv/mintdeck_env
```


```bash
briefcase new
cd mintdeck
briefcase dev

# Package app for distribution
briefcase create
briefcase build
briefcase run
# Building installer
briefcase package --no-sign

# Update code of existing bundle
briefcase update
briefcase build
briefcase run
briefcase package --no-sign

# Update code and run in one command
briefcase run -u
# Update code and package in one command
briefcase package -u

# Update Python dependencies
briefcase update -d
briefcase build
briefcase run
```

https://toga.readthedocs.io/en/latest/
https://toga.readthedocs.io/en/latest/tutorial/tutorial-2.html
