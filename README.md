# debate_team
Code, samples, and a working app for creating and using a debate team of AI agents with with Agent AutoBuild.

Meant mainly as an example of what can be done with multiple agents and of how it is to create badly-needed teachingl tools with AI.

## overview

[Autobuild](https://microsoft.github.io/autogen/blog/2023/11/26/Agent-AutoBuild/) is part of autogen from Microsoft. It partly automates the task of a creating a group of agents to coloborate on a task. It is low-code but not no-code.

builddebateteam.py in this repository builds a team of four debating agents, a moderator, and a judge to debate any proposition given to them. The agents are created as a JSON file, debateteam.json, which is then input to the user-facing debate application.

The depository is set up so that an application can be uploaded to the Streamlit cloud. That has been done and the application is [here](https://debateteam.streamlit.app/). The .gitignore and requirements.txt are specific to streamlit cloud.

debatemanager.py is incorporated in the streamlit app but also be run as standalone Python with a console-based interface to test debating and debate topics.

ststreamer.py is a helper module for the streamer app which reditects console output and streams it to the streamlit user while a long-running app (like a debate) is writing to console. It is usable independent of the rest of this code but is not on PyPi. 

## usage

### as a streamlit app:
Click the URL https://debateteam.streamlit.app/. You will need an OPENAI api key in the paid tier. The free api key will not work because the agents use GPT4.

### as a basis for deploying your own Streamlit app.
1. clone the repository.
2. make any changes you want to make.
3. be sure to update .gitignore and requirements.txt as needed.
4. deploy from Streamlit (you need an acount, of course).

### to make a modified debate team
1. download builddebateteamm.py and SAMPLE.env into your favorite IDE.
2. modify SAMPLE.env by addind your own paid OPENAI api key where indicated. The free api key will not work because the agents and agentbuilder use GPT4.
3. save as .env.
4. pip install autogen[autobuild]
5. change the text of building_task in builddebateteam tyo whatever you want.
6. run.
7. you will be prompted for an optional test debate topic and a name for the saved debate team.
8. if you use your debate team with either debatemanager or a Streamlit app, be sure to specifiy the name and location of your debate team json file in debatemanager __main___ or streamlit_app.py as appropriate. If you uploaded the json file containing your debate team speciifcation to your own repository or somewhere else, you can give the url ratther than a file address.

### to capture console output from a Python function and stream it to streamlit
1. download ststreamer.py (it's not on PyPi).
2. import ststreamer into the code that your're writing
3. write a function like this and use it to call your function.
 ~~~Python
    # Function to capture the console output
    def capture_console_output(func, *args, **kwargs):
      f = ststreamer.ObservableStringIO()
      with redirect_stdout(f):
        func(*args, **kwargs)
    output = f.getvalue()
    return output
 ~~~
## ideas for enhancement
Let one or more of the debaters be humans

Empower the debaters to do research

Empower the judge to fact-check

Implement with an open source LLM

## privacy
No code here explititly collects any information of any kind. However, some usage stastics are available from both github and Streamlit.

## disclaimer
This all comes with no warranty of any kind nor any promise to fix problems or maintain compatabity with the code it uses. However, bug reports, issues, and enhancement pull requests are welcome.




