from langchain_community.llms import Ollama 
from crewai import Agent, Task, Crew, Process 
import os 
model = Ollama(model = 'llama3')

# user input as audio 
# need model output as audio 
# further prompting 
# done 

user_input = "I want to kill myself"

os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1" 
os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'
os.environ["OPENAI_API_KEY"] = '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'

classifier = Agent(
    role = "MentalHealth Classifier",
    goal = "Analyze the text to determine if there are indications of mental health issues. Consider emotional expressions, content themes, and language intensity.",
    backstory = "You are an AI Mental Health Assistant whose only job is to understand what the patient is saying and know if he is facing mental health issues. Your job is to help the user by giving words of affirmation in case he is having any mental problem.",
    verbose = True,
    allow_delegation = False,
)

responder = Agent(
    role = "Mental Health Responder",
    goal = "Based on the severity level and likely geographic location (urban/rural), suggest appropriate mental health resources in Lebanon. Include names, contact details, and any relevant information about these services (e.g., specialties, languages spoken).Offer actionable advice that can help the user manage their symptoms until they can seek professional help. This could include techniques for stress management, links to online mindfulness resources, or encouragement to engage in physical activity or other healthy habits. Encourage continued dialogue or follow-up actions, such as booking an appointment with a mental health professional or reaching out to support networks.Suggest practical steps for follow-up, like how to make an appointment, what to expect during a mental health consultation, or how to prepare for a session with a therapist.",
    backstory = "You are an AI Mental Health Assistant whose only job is to understand what the patient is saying and know if he is facing mental health issues. Your job is to help the user by giving words of affirmation in case he is having any mental problem.",
    verbose = True, 
    allow_delegation = False, 
)

classify_user = Task(
    description = f"Classify the symptoms '{user_input}",
    agent = classifier,
    expected_output = "One of these 2 options: 'Have Mental Problems', 'Doesn't have Mental Problems"
)

response_to_user = Task(
    description = f"Respond to the user: '{user_input}'",
    agent = responder, 
    expected_output = "In case of having mental problems provide positive vibes and support the user, in case of severe mental problems like suicide for example suggest seeking help from therapist, and in case of not having any mental problems just show some support."
)

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_user, response_to_user],
    verbose = 2, 
    process = Process.sequential
)

output = crew.kickoff() 
print(output)
