# AI Study Assistant

An AI-powered study assistant that combines Machine Learning and Generative AI to provide personalized study guidance based on a student's academic performance and weak topics.

## Features

- Predicts a student's final grade using Machine Learning.
- Uses Random Forest Regression for grade prediction.
- Allows students to enter their weak topics.
- Retrieves relevant study material from local `.txt` files.
- Uses Llama 3 through Ollama to generate personalized study guidance.
- Generates explanations and a 7-day study plan.
- Combines Machine Learning, LLMs and simple RAG.

## Project Architecture

Student Performance Data
        |
        v
Random Forest Model
        |
        v
Predicted Final Grade
        |
        v
Student enters weak topics
        |
        v
Relevant Notes Retrieval
        |
        v
Llama 3
        |
        v
Personalized Study Plan

## Machine Learning Component

The Machine Learning component uses student performance data to predict the student's final grade.

Features include:

- Study time
- Number of previous failures
- Absences
- First period grade (G1)
- Second period grade (G2)

The target variable is:

- G3 (final grade)

A Random Forest Regressor is used for prediction.


## Generative AI Component

Llama 3 is used as the Generative AI component.

The model receives:

- Predicted student grade
- Student's weak topics
- Relevant study notes

It then generates:

- Simple explanations
- Study priorities
- Personalized study recommendations
- A 7-day study plan


## RAG Component

The project uses a simple retrieval-based approach.
The student enters weak topics, for example:
Statistics, Machine Learning
The system searches the local notes directory and retrieves:
statistics.txt
machine_learning.txt
The retrieved content is then provided to Llama 3 as context.
This allows the LLM to generate answers based on the provided study material instead of relying only on its general knowledge.

## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd AI_STUDY_ASSISTANT