#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#JSON schema
data_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Bucket List Keywords",
  "description": "A schema for defining main keywords and their associated details for a bucket list.",
  "type": "object",
  "properties": {
    "BucketList": {
      "type": "object",
      "description": "MainKeywords related to the bucket list",
      "properties": {
        "MainKeyword1": {
          "type": "object",
          "description": "Details related to MainKeyword1 for the bucket list",
          "properties": {
            "Value": { "type": "string", "description": "Main keyword1 to achieve bucket list" },
            "Details": {
              "type": "object",
              "properties": {
                "Detail1": { "type": "string", "description": "The first detail for MainKeyword1." },
                "Detail2": { "type": "string", "description": "The second detail for MainKeyword1." },
                "Detail3": { "type": "string", "description": "The third detail for MainKeyword1." },
                "Detail4": { "type": "string", "description": "The fourth detail for MainKeyword1." }
              },
              "required": ["Detail1", "Detail2", "Detail3", "Detail4"]
            }
          },
          "required": ["Value", "Details"]
        },
        "MainKeyword2": {
          "type": "object",
          "description": "Details related to MainKeyword2 for the bucket list",
          "properties": {
            "Value": { "type": "string", "description": "Main keyword2 to achieve bucket list" },
            "Details": {
              "type": "object",
              "properties": {
                "Detail1": { "type": "string", "description": "The first detail for MainKeyword2." },
                "Detail2": { "type": "string", "description": "The second detail for MainKeyword2." },
                "Detail3": { "type": "string", "description": "The third detail for MainKeyword2." },
                "Detail4": { "type": "string", "description": "The fourth detail for MainKeyword2." }
              },
              "required": ["Detail1", "Detail2", "Detail3", "Detail4"]
            }
          },
          "required": ["Value", "Details"]
        },
        "MainKeyword3": {
          "type": "object",
          "description": "Details related to MainKeyword3 for the bucket list",
          "properties": {
            "Value": { "type": "string", "description":"Main keyword3 to achieve bucket list"},
            "Details": {
              "type": "object",
              "properties": {
                "Detail1": { "type": "string", "description": "The first detail for MainKeyword3." },
                "Detail2": { "type": "string", "description": "The second detail for MainKeyword3." },
                "Detail3": { "type": "string", "description": "The third detail for MainKeyword3." },
                "Detail4": { "type": "string", "description": "The fourth detail for MainKeyword3." }
              },
              "required": ["Detail1", "Detail2", "Detail3", "Detail4"]
            }
          },
          "required": ["Value", "Details"]
        },
        "MainKeyword4": {
          "type": "object",
          "description": "Details related to MainKeyword4 for the bucket list",
          "properties": {
            "Value": { "type": "string", "description": "Main keyword4 to achieve bucket list" },
            "Details": {
              "type": "object",
              "properties": {
                "Detail1": { "type": "string", "description": "The first detail for MainKeyword4." },
                "Detail2": { "type": "string", "description": "The second detail for MainKeyword4." },
                "Detail3": { "type": "string", "description": "The third detail for MainKeyword4." },
                "Detail4": { "type": "string", "description": "The fourth detail for MainKeyword4." }
              },
              "required": ["Detail1", "Detail2", "Detail3", "Detail4"]
            }
          },
          "required": ["Value", "Details"]
        }
       
      }
    }
  }
}


#gpt api를 활용해서 JSON형태로 추출한것!

import openai
import json

# OpenAI API 키 설정
import openai
import json

# OpenAI API 키 설정
api_key = "open-api-key"
openai.api_key = api_key

# 사용자 입력 정보
age = "11"
job = "학생"
bucket_list = "유럽여행가기"

prompt = f"직업: {job}, 나이: {age}, 버킷리스트: {bucket_list}\n\n버킷리스트를 이루기 위해 필요한 메인 키워드 4개와 각각의 메인 키워드를 이루기 위한 세부 목표를 4개씩 json형태로 생성해줘"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {
            "role": "system",
            "content": "Provide realistic solutions so you can achieve people's dreams one step closer"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    # Implement a function call with JSON output schema
    functions=[
        {
            "name": "data_schema",
            "description": "Using the given age, gender, occupation, and bucket list information, create four main keywords for achieving a bucket list that fits the situation, and four detailed keywords according to each main keyword",
            "parameters": data_schema
        }
    ],  # Removed unnecessary outer brackets
    # Define the function which needs to be called when the output has received
    function_call={
        "name": "data_schema"
    },
    
    temperature =0.7,
    top_p=1.0 ,
    frequency_penalty = 0.0,
    presence_penalty= 0.0,
    max_tokens = 1000
)

# Extract the JSON schema from the response
# Extract the output schema from the response
output_schema = response["choices"][0]["message"]["function_call"]["arguments"]

# Print or do something with the output schema
print(output_schema)

