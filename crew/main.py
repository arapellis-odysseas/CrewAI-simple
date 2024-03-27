from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
load_dotenv()
from textwrap import dedent
from crewai import Crew, Agent,Task, Process
from crewai_tools import DirectoryReadTool, FileReadTool

# Set the local llm
my_llm = ChatOllama(model="crewAI2")

# Set the tools
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()

# Defining the post topic
post_topic = 'Electrical Automotive Engineering and Robotics'

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
  	role='Writer',
 	goal='Narrate compelling tech stories about {topic}',
  	backstory=dedent("""
    	With a flair for simplifying complex topics, you craft
    	engaging narratives that captivate and educate, bringing new
    	discoveries to light in an accessible manner."""),
    
	tools= [],
  	allow_delegation=False,
  	llm=my_llm,
    function_calling_llm=my_llm,
    max_iter=15,
    verbose=True,
    memory=True,
)

# Writing task with language model configuration
write_task = Task(
	description=dedent("""
		Compose an insightful article on {topic}.
		Focus on the latest trends and how it's impacting the industry.
		This article should be easy to understand, engaging, and positive.
        Make sure your article has appropriate structure, formatting and style.
        Make sure you include Titles, Subtitle, Headings, Lists, Images, etc. Whatever is necessary."""),
	expected_output='A 4 paragraph article on {topic} advancements formatted as markdown. Make sure to have a very nice formatting and style, with appropriate markdown syntax and elements (Bold, Italics, Headings, Ordered List, Unordered List, etc.).',
	agent=writer,
	async_execution=False,
    tools= [docs_tool, file_tool],
	output_file='./blog-posts/'+ post_topic + '_new_post.md'  # Example of output customization
)

# Forming the tech-focused crew with enhanced configurations
crew = Crew(
	agents=[writer],
	tasks=[write_task],
	process=Process.sequential,  # Optional: Sequential task execution is default
	verbose=2
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': post_topic})
print(result)