# A 'hello world' educational app

This is intended to be as simple as possible, while still being an authentic experience.
---

The first program that you write in any new notation (i.e. a language or a framework) is usually called a "Hello World" app, because all it does is display the text "Hello World". That might not sound impressive, but it means that your program is able to interpret code, execute, and provide some basic output from whatever it was doing. That's a lot!

That being said, this app is just a starter for whatever real applicaiton you have in mind. There is no database to install or keep up to date, it's not production-ready, and you only have to know two notations: Python and Flask.

This code is available under the MIT License. That means that you don't have to worry about copyright, but you also don't have any guarantees. See the license for full details. Flask is a simple web framework written in Python. Feel free to look it up, learn a bit, and apply your learning to a copy of this code!

Github (which is where this code is hosted) runs git. If you want to be able to undo mistakes or work with other programmers, it is a good idea to larn how to use git as well.

All of my programming assumes an Ubuntu operating system. If you plan on using much of my work, I recommend either getting a dedicated computer for your programming so that you can install Ubuntu on it, or dual-booting into Ubuntu. Unfortunately, it's extremely uncommon to program from a mobile device. You really do need a computer.

Once you figure out how to install Ubuntu, clone this repository, and install the python dependencies, you can run the server with the following:

```
cd backend
export FLASK_APP=main.py
flask run
```

Open a browser to the URL provided in the output, and you should see a simple "Hello World" message. Go to the path /activity/1 and you should see one of the hardcoded activities.

Congratulations! You're a programmer now! Whew! That was hard! Now, edit the code and get it to do whatever you want! There's plenty more to learn, but you are taking the first steps, and I hope you realize how that is a really big deal.
