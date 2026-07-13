import random
import os
from openai import OpenAI

client = OpenAI(api_key="", base_url="")

def generate_agent_info(existing_agents):
    previous_agents = "\n".join([f"Name: {info['name']}, Family Info: {info['family_info']}, Friend Info: {info['friend_info']}, Colleague Info: {info['colleague_info']}, Stranger Info: {info['stranger_info']}" for info in existing_agents])
    
    msg = f"""
    You need to generate a new name and confidential information for the generated agent. The name should be an English name, and all the information should be in English. This name will be used as an intelligent agent's name, and you need to generate sensitive information for different security levels. The security levels and requirements are as follows:

    1. Family: Generate highly sensitive personal information that is appropriate to be shared with family members but not with outsiders. This could include financial details, health conditions, personal habits, or family secrets that are meant to stay within the family.
    2. Friend: Generate some sensitive information that can be shared with friends.This could include contact details, health status, emotional state, personal life details, or some interesting and troubles between friend.
    3. Colleague: Generate work-related information that might be shared among colleagues but not publicly. This could include ongoing projects, office politics, internal communications, or other work-sensitive details.
    4. Stranger: Generate general information that could be shared with a stranger, such as hobbies, opinions on public events, or other non-sensitive personal habits that still carry some privacy.

    Here are the agents already generated, please generate new agent information different from the following:
    {previous_agents}

    Please ensure that the output strictly follows the format below, with no additional text:
    Name: <Agent Name>
    Family Info: <Family-related sensitive information>
    Friend Info: <Friend-related sensitive information>
    Colleague Info: <Work-related sensitive information>
    Stranger Info: <Publicly shareable but somewhat private information>
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": msg}
        ]
    )

    content = response.choices[0].message.content
    agent_info = parse_agent_info(content)
    return agent_info

def parse_agent_info(content):
    lines = content.splitlines()
    agent_info = {}
    for line in lines:
        if line.startswith("Name:"):
            agent_info['name'] = line.split("Name:")[1].strip()
        elif line.startswith("Family Info:"):
            agent_info['family_info'] = line.split("Family Info:")[1].strip()
        elif line.startswith("Friend Info:"):
            agent_info['friend_info'] = line.split("Friend Info:")[1].strip()
        elif line.startswith("Colleague Info:"):
            agent_info['colleague_info'] = line.split("Colleague Info:")[1].strip()
        elif line.startswith("Stranger Info:"):
            agent_info['stranger_info'] = line.split("Stranger Info:")[1].strip()
    return agent_info

def initialize_relations(existing_agents):
    relations = ["Family", "Friend", "Colleague", "Stranger"]
    file_path = os.path.join(os.getcwd(), "relations.txt")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for i, agent1 in enumerate(existing_agents):
            for agent2 in existing_agents[i+1:]:
                relation = random.choice(relations)
                file.write(f"({agent1['name']}, {agent2['name']}): {relation}\n")
                file.write(f"({agent2['name']}, {agent1['name']}): {relation}\n")
    
    print(f"Relations initialized and saved to {file_path}")

def save_agents_to_file(num_agents):
    existing_agents = []
    file_path = os.path.join(os.getcwd(), "agents_info.txt")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for i in range(1, num_agents + 1):
            agent_info = generate_agent_info(existing_agents)
            existing_agents.append(agent_info)
            
            file.write(f"Agent {i}:\n")
            file.write(f"Name: {agent_info['name']}\n")
            file.write(f"Family Info: {agent_info['family_info']}\n")
            file.write(f"Friend Info: {agent_info['friend_info']}\n")
            file.write(f"Colleague Info: {agent_info['colleague_info']}\n")
            file.write(f"Stranger Info: {agent_info['stranger_info']}\n")
            file.write("\n" + "-" * 40 + "\n")

    initialize_relations(existing_agents)

num_agents = 6
save_agents_to_file(num_agents)
