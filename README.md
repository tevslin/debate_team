# debate_team
Code and samples for creating and using a debate team of AI agents with with Agent AutoBuild.

## overview

[Autobuild](https://microsoft.github.io/autogen/blog/2023/11/26/Agent-AutoBuild/) is part of autogen from Microsoft. It partly automates the task of a creating a group of agents to coloborate on a task. It is low-code but not no-code.

builddebateteam.py in this repository builds a team of four debating agents, a moderator, and a judge to debate any proposition given to them. The agents are created as a JSON file, debateteam.json, which is then input to the user-facing debate application.

The depository is set up so that an application can be uploaded to the Streamlit cloud. That has been done and the application is [here](https://debateteam.streamlit.app/). The .gitignore and requirements.txt are specific to streamlit cloud.

debatemanager.py is incorporated in the streamlit app but also be run as standalone Python with a console-based interface to test debating and debate topics.

ststreamer is a helper module for the streamer app which reditects console output and streams it to the streamlit user while a long-running app (like a debate) is writing to console. It is usable independent of the rest of this code but is not on PyPi. 



