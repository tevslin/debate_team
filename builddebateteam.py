# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:31:00 2024

@author: tevslin

Uses AgentBukder in autogen to build a debate team.
Modify building_task below to change how the team is built.
"""

from dotenv import load_dotenv
import os
import json

load_dotenv()
llm="gpt-4-1106-preview"       
tdict={"model":llm,"api_key":os.getenv('OPENAI_API_KEY')}
os.environ['OAI_CONFIG_LIST']="["+json.dumps(tdict)+"]"
config_file_or_env = 'OAI_CONFIG_LIST'  # modify path
default_llm_config = {
    'temperature': 0
}
from autogen.agentchat.contrib.agent_builder import AgentBuilder

builder = AgentBuilder(config_file_or_env=config_file_or_env, builder_model='gpt-4-1106-preview', agent_model='gpt-4-1106-preview')

building_task=""""Conduct a debate between agents on a given proposition.
The proposition is given to the debaters by a debate moderator agent who is the chat manager.
The debaters speak in the order in which they are listed below after they have
been given the proposition by the moderator. Each debater speaks once
and only once.

The debaters are :
    1.affirmative constructive 
    2.negative contructive
    3.affirmative rebutalist
    4.negative rebutalist


The affirmative debaters must not rebut eachother
and the rebutalists must only rebut points actually made by their opponents and may not introduce
new arguments. Debaters may not terminate the session.
There is also a judge which gives each debater a score between 0 and 5 and gives a reason for the score and does terminate the session.
The judge must be created last.
The judge terminates the debate after passing judgment,
The agents created should all stream their output.""" #this line added 2/3/24

agent_list, agent_configs = builder.build(building_task, default_llm_config, coding=False)
import autogen

def start_task(execution_task: str, agent_list: list, llm_config: dict):
    config_list = autogen.config_list_from_json(config_file_or_env, filter_dict={"model": ["gpt-4-1106-preview"]})

    group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=15)
    manager = autogen.GroupChatManager(
        groupchat=group_chat, llm_config={"config_list": config_list, **llm_config}
    )
    agent_list[0].initiate_chat(manager, message=execution_task)

os.environ['AUTOGEN_USE_DOCKER']='False'
for agent in agent_list:
    print(agent.name)
proposition=input("enter proposition for test debate. Empty entry to skip test. ")
if len(proposition)>0:  #if test wanted, do it
    start_task(
        #execution_task="Debate the proposition that Vermont should devote available limited resources only to mitigating the effects of climate change rather than attempting to prevent it.",
        execution_task="Debate the proposition that Apple is better than Microsoft.",
        agent_list=agent_list,
        llm_config=default_llm_config
        )
file_name=input('enter name for debate team file. ".json" will be appended. Empty entry to skip save.')
if len(file_name)>0: #if save wanted
    saved_path = builder.save(file_name+'.json')
    