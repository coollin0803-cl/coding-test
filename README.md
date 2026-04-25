# coding-test 

This is a coding-test repo about python. There are four parts in total, namely quiz.py, main.py, review.py and algo.py. Good Luck to me!!!Thank you for cloning.   

# Personal Statement

1. As i am currently employed and need to work overtime,i haven't enough time to complete the algo.py part.Although i am not sure if i could finish it correctly, i will try my best to investigate it continually.I will git push it into my github and send email to you as soon as i finish.  
2. As an honest person,i think it's very necessary to tell you about my abilities and coding skills.As for the webapp part,i don't know how to solve the image via python, because i am good at java more,as for python,i only know the libraries a little,so when i received this email and browsed all the questions,i learned how to handle the image via Google,and then finished the question independently.So when i am lucky to have an interview,you could ask me this knowledge,i am sure I can answer it.  OK,now i will introduce all the parts to you!Thank you for reading my statement~   

# Webapp

There are two apis to invoke. 

### POST: /upload-compress 

You could invoke this api to upload an image file.There is a required parameter which is file to input. 

My logics are below: 

1. Judge size of the file whether it is valid,if it exceeds 5MB or less than 1KB,an error will be reported.
2. Judge the file whether it is valid,if the file's suffix is not in 'png', 'jpg', 'jpeg', 'gif', 'webp',an error will be reported.
3. If file is valid,i will compress it via PIL and record the infomations.
4. add into history array, and return,include:(pay attention:when add into array,we need to add lock to control the **data accuracy**.)

- id:uuid
- file name
- original image informations including format,width,height,byte.
- compressed image informations including format,width,height,byte.
- created time

### GET: /history

You could invoke this api to review the history.

Pay attention: add lock,because when we write data into history and read history array at the same time,we will read wrong datas.

### Operation Instruction

- ensure you have python environment in your PC, you could enter the terminal and use the instructions: **"python --version" and "pip --version"**
- install PIL, FastAPI, multipart, uvicorn libraries, **"pip install fastapi uvicorn pillow", "pip install python-multipart"**
- enter webapp directory , could input command **"pwd"** to check your current path whether it is **"./coding-test"**, if it is right and input command "cd webapp"
- input command **"uvicorn main:app --reload"** to start the project
- open Google and input the url: **"http://127.0.0.1:8000/docs"**
- click any api and you could see **"Try it out"**, click it and could use apis

**If you have any questions, feel free to contact with me,my email is : "13199168939@163.com"**

# Review & Quiz

I have examples in the file, you could view it directly.