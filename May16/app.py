import autogen

config_list = [
    {
        'model': 'gpt-3.5-turbo',
        'api_key': '#'
    }
]

llm_config = {
    'seed': 42,
    'config_list': config_list,
    'temperature': 0
}

assistant = autogen.AssistantAgent(
    name='assistant',
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name='user_proxy',
    human_input_mode='TERMINATE',
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get('content', '').rstrip().endswith('TERMINATE'),
    code_execution_config={'work_dir': 'web',
                           "use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been resolved at full satisfaction. Otherwise, reply CONTINUE, or the reason why task is not solved yet."""
)

task = """
Write a python code to output numbers 1 to 100, and then store the code in a file
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
Change the code in the file you just created to instead output numbers 1 to 200
"""

user_proxy.initiate_chat(
    assistant,
    message=task2
)