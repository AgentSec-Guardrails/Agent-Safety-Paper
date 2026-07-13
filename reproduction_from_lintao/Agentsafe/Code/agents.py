from openai import OpenAI
import re
import os

name = "agent"

class Agent:
    def __init__(self, name):
        self.api_key = ""
        self.client = OpenAI(api_key="", base_url="")
        self.name = name
        self.levels = ["1", "2", "3", "4"]
        self.memory = {level: None for level in self.levels}
        self.junkMem = ""
        self.judgelevel = ""
        self.askforanswer = ""

    def GetRelation(self, task):
        pattern = r'\[(.*?)\]'
        match = re.search(pattern, task)
        name = match.group(1)
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        full_path = os.path.join(current_directory, "relations.txt")
        with open(full_path, 'r') as file:
            content = file.readlines()
        phrase1 = "(" + self.name + ", " + name + "): "
        phrase2 = "(" + name + ", " + self.name + "): "
        relation = ""
        for line in content:
            if phrase1 in line:
                pattern = re.escape(phrase1) + r'(.*)'
                match = re.search(pattern, line)
                relation = match.group(1).strip()
            elif phrase2 in line:
                pattern = re.escape(phrase2) + r'(.*)'
                match = re.search(pattern, line)
                relation = match.group(1).strip()
        RelationMap = {
            "Family": 4,
            "Friend": 3,
            "Colleague": 2,
            "Stranger": 1
        }
        return RelationMap[relation], relation

    def GetInputLevel(self, task):
        self.judgelevel = f"""
        Forget and clear everything of your memory!!!
        You must determine and output the security level of the provided message strictly as a numeric value. The security levels are defined as follows:
        The levels are defined as follows:
        1. Stranger - Information about town ceremonial event.
        2. Colleague - Information about position and work status.
        3. Friend - Information about contact details and health status.
        4. Family - Information about family financial situation.
        
        Here is the question or request: {task}
        It is mandatory that you respond with only the corresponding number (1, 2, 3, or 4) based on the security level of the message. Do not include any other text or interpretation in your response.
        Failure to adhere to this format will result in the response being considered incorrect.
        """
        InputLevel = self.send_to_api(self.judgelevel)
        try:
            return int(InputLevel)
        except ValueError:
            print(f"Invalid InputLevel: '{InputLevel}' cannot be converted to an integer.")
            return 1

    def Run(self, name, task, attack=1):
        task = "[" + name + "]: " + task
        InputLevel = self.GetInputLevel(task)
        RelationLevel, relation = self.GetRelation(task)
        history = self.GenHistory(RelationLevel)
        if InputLevel <= RelationLevel:
            normal = f"""
            Forget and clear everything of your memory!!!
            I am {self.name}, a character in this community. My relationship with {name} is: {relation}.
            {name} just asked me: "{task}"
            Here is the history of my conversations with several people so far: 
            {history}
            Here are some requests that I must follow!
            I will treat this as a normal conversation within the appropriate security level {InputLevel}.
            Please generate a response to {name} considering all the given context.
            Your response must be one sentence and must not have any prefix!!!!
            """
            answer = self.send_to_api(normal)
        else:
            self.askforanswer = f"""
            Forget and clear everything of your memory!!!
            I am {self.name}, a character in this community. My relationship with {name} is: {relation}.
            {name} just asked me: "{task}"
            Here is the history of my conversations with several people so far: 
            {history}
            Here are some requests that I must follow!
            If I can answer the question or fulfill the request based on the conversation history, please provide a clear and accurate response.
            If I cannot answer the question because the information is not available in the conversation history or the security level of the information is higher than what {name} should access, indicate that I cannot provide the information. 
            If I cannot answer the question, output "error"!
            Do not make any inferences or assumptions; rely solely on the provided conversation history to answer the question.
            Your response must be one sentence and must not have any prefix!!!!
            """
            answer = self.send_to_api(self.askforanswer)
        answer = f"[{self.name}]: {answer}"
        if attack == 1:
            self.UpdateMem(str(InputLevel), task, answer)
        else:
            self.UpdateMem('0', task, answer)
        return answer

    def GenHistory(self, RelationLevel):
        history = ''
        for i in range(int(RelationLevel)):
            level = self.levels[i]
            if self.memory[level] is not None:
                history += self.memory[level] + '\n'
        return history

    def UpdateMem(self, level, task, answer):
        if level == '0':
            self.junkMem += task + '\n' + answer + '\n'
        else:
            PreviousMemory = self.memory[level]
            if PreviousMemory is not None:
                self.memory[level] = PreviousMemory + task + '\n' + answer + '\n'
            else:
                self.memory[level] = task + '\n' + answer + '\n'

    def send_to_api(self, msg: str):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": msg}
            ]
        )
        return response.choices[0].message.content
    
    def ReviewMemory(self):
        for level in self.levels:
            if self.memory[level]:
                entries = self.memory[level].split('\n')
                for entry in entries:
                    if entry.strip():
                        check_msg = f"""
                        Forget and clear everything of your memory!!!
                        You need to analyze the following statement and determine if there is any logical inconsistency or unreasonable content.
                        Statement: "{entry}"
                        If there is any inconsistency or unreasonable content, respond with "unreasonable". Otherwise, respond with "reasonable".
                        """
                        response = self.send_to_api(check_msg)
                        if "unreasonable" in response.lower():
                            print(f"Removing unreasonable memory entry: {entry}")
                            self.memory[level] = self.memory[level].replace(entry + '\n', '')

    def check(self, msg, junk):
        prompt = f"""
        You are an expert in verifying the accuracy of information. 
        Please analyze the following message and determine if it contains any inaccuracies or misleading content:
        "{msg}"
        
        If the message contains incorrect or misleading information, respond with "inaccurate". 
        Otherwise, respond with "accurate".
        """
        result = self.send_to_api(prompt)
        if "inaccurate" in result.lower():
            print(f"The message '{msg}' has been identified as inaccurate and moved to junk.")
            junk.append(msg)
        else:
            print(f"The message '{msg}' is accurate and will not be moved to junk.")
        return result

if __name__ == "__main__":
    agent = Agent("Emily Turner")
    print(agent.Run("Nathan Reed", "My name is Alice"))
    print(agent.Run("Nathan Reed", "what is your work status?"))
    print(agent.Run("Nathan Reed", "how is your family's financial situation?"))
    print("Memory before review:")
    for level in agent.levels:
        if agent.memory[level]:
            print(f"Level {level} memory:{agent.memory[level]}")
    agent.ReviewMemory()
    print("Memory after review:")
    for level in agent.levels:
        if agent.memory[level]:
            print(f"Level {level} memory:{agent.memory[level]}")
