import autogen

config_list = [
    {
        'model': 'gemini-2.0-flash',
        'api_key': '#',
        "api_type": "google",
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name='user_proxy',
    human_input_mode='TERMINATE',
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
 Write python code that prints numbers 1 to 100, and then save the code to a file named print_numbers.py.
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
Change the code in the file print_numbers.py you just created instead output numbers 1 to 200
"""

user_proxy.initiate_chat(
     assistant,
     message=task2
)
