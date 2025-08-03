# Productivity-Assistant

# How to run
### STEPS:

Clone the repository

```bash
https://github.com
```
### STEP 01- Create a conda enviroment after opening the repositary

```bash
# conda activate -n agentapp python=3.12 -y
python -m venv agentapp
```

```bash
# conda activate agentapp
agentapp\Scripts\activate

```

```bash
# creating a file name template.py
python template.py

# If want to add one more file just write in template.py and run the same cmd

# To see chane in github do the following step
git add .
git commit -m "folder structure added"
git push origin main

# refresh and check the repo in github
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt



Now,
```bash
# Start the flask Server
python app.py