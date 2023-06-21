
# Todo App



## Description
I've created this app with the help of pyhton while learning. I Implemeneted its backend with the help of **Python** and **Streamlit** module helped me to build a frontend with ease.

After building the project, I built a docker image with the help of **Dockerfile**.

I did not use any database to store the data rather just stored it into a text file as a beginner.
## Installation

Run with streamlit

```bash
  pip3 install requirements.txt
  streamlit run frontend.py
```
    
Run with Docker. Make sure docker is installed

Build Docker Image

```bash
  docker build todo-app:1.0 .
```
Run the Image
```bash
  docker run -d -p 8501:8501 todo-app:1.0
```

## Screenshot
![alt text](https://github.com/AkramExp/python-todo-app/blob/main/Screenshot.png?raw=true)
