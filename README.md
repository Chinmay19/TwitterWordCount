# TwitterWordCount

## Objective:
Create a streaming application which gets tweets for a given twitter id and counts the occurences of the words in tweets

---
## Prerequisites:
1. Before we get into how to setup and run the application make sure that docker, docker-compose is installed on the system
2. Create an application on twitter developer account to be able to access the tweets via api
3. The api key, api secret, bearer token for twitter application is saved in .env file

---
## Steps to reproduce the application:
1. Create the virtual environment using `python -m venv ./venv_dir_name`
2. Activate the virtual environment as `source ./venv_dir_name/bin/activate`
3. Install the required packages using given _requirements.txt_ file. `pip install -r requirements.txt`
4. After packages are installed, run the docker-compose file to start the containers
5. In 3 separate terminal windowns run `get_tweets.py`, `consume.py`, `wordcount.py`

Output for the wordcount will be displayed on `wordcount.py` file's console

---
## Application flowchart
[Block Diagram](streaming_flow_chart.png)

---
## Next steps:
1. Push the results into a database, such that more applications based on this data can be realized
2. Configure apache nifi to work with twitter api v2, such that data can be loaded in a solid way.
3. Stream data from multiple users on multiple kafka topics