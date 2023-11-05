# Conversational SQL: The next step towards database accessibility with LLMs
This project demonstrates a method to give a large language model (LLM) access to an SQL database using a proxy. For this demonstration, we have utilized the OpenAI Chat API as our backend.

## Configuration
1. Create a `.env` file in the `LLM` folder and insert your OpenAI API key in the following format: ```OPENAI_API_KEY="xyz"```


## Components
This project consists of three main components:

1. **Frontend**: Built with Plotly Dash, it serves as a user interface for querying the database.

2. **Database**: A sample database mimicking a social media platform with three tables: `users`, `posts`, and `comments`.

3. **LLM**: A Flask API that processes requests from the frontend and interacts with the OpenAI Chat backend to generate responses.

## Running the Project
To run the project, follow these steps:

1. Navigate to the root level of the repository.
2. Run the following command: ```docker-compose up```


After starting the Docker containers, the frontend will be accessible in your web browser at `localhost:8050`.

## Example Usage
1. Once the project is up and running, navigate to `localhost:8050` in your browser.
2. Enter a query, such as "Show me all comments from user 'bob456' on posts by 'alice123'", and observe how the LLM generates an SQL query to fetch the relevant data from the database and then provides a meaningful response.

## Known Issues and Future Work
While this approach is promising, there are some known issues and areas for future development:

1. The LLM sometimes provides incorrect queries and therefor wrong answers. Further work is needed to enhance the accuracy of responses.
2. The system currently requires manual input for the structure and content of the tables. Future versions should automatically read and comprehend this information.
3. Comprehensive testing across different databases and large-scale data warehouses is necessary to validate the system's effectiveness in diverse environments.


We welcome contributions and ideas to enhance this project!