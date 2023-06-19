from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
import os, environ
from rest_framework.parsers import JSONParser
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI

# --Set OPENAI key --
env = environ.Env()
environ.Env.read_env()


@api_view(['POST'])
@parser_classes([JSONParser])
def hello_world(request, format=None):
    question= request.data['question']
    message =answer(question)
    print(message)
    return Response({"message": message})

def answer(q):
    os.environ["OPENAI_API_KEY"] = env('OPENAI_API_KEY')
    df = pd.read_csv('../../task2/data/Result.csv')
    del df['Brand']
    del df['link']
    print(df.head(n=2))
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
    question_user = q
    answer_ai = agent.run(question_user)
    return answer_ai