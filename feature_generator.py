#pip install pandas
#pip install numpy
#pip install -U google-generativeai
import pandas as pd
import os
import numpy as np
import google.generativeai as palm
import re
palm.configure(api_key='AIzaSyAedmPMHxXBrjTQFgOoypvQIYZLiz6L21k')





def cleaner(text):
    pattern = r'\d+\.\s+\*\*(\w+):\*\*'
    matches = re.findall(pattern, text)
    return matches

def generate_features(question,answer):


    output_list = []


    prompt = '''Discard all the previous instructions.
    Behave like you are an expert at feature-selection task and an expert at linguistics. Consider the following question :
    \n\n'''


    prompt += question

    prompt+='''Given that the answer to the question above is :\n\n'''

    prompt+=answer

    prompt = '''Generate exactly 10 features based on the quality and tone of the answer. For example:
    'We expect to deal and face with inflation' is a 'Defensive answer' whereas 'We are prepared to take advantage of the inflation'
    is an 'Aggressive answer'. In this case you would define an 'Aggression' variable with this answer and any more if needed.
    A few other examples could be: Clarity (vague vs clear) and Optimism (Optimistic vs Non-optimistic).
    Don't include any justification for the labels. Generate your answer in the following format:
    'Here are 10 features based on the quality and tone of an answer:\n\n1. **Aggression:** 
    The degree to which the answer is assertive or forceful.\n2. **Clarity:** The degree to which the answer is easy to understand.\n3. 
    **Confidence:** The degree to which the answer is expressed with certainty.\n4. **Defensiveness:** The degree to which the answer is 
    apologetic or evasive.\n5. **Optimism:** The degree to which the answer is hopeful or positive.\n6. **Passiveness:** The degree 
    to which the answer is meek or submissive.\n7. **Politeness:** The degree to which the answer is respectful or 
    considerate.\n8. **Relevance:** The degree to which the answer is related to the question.\n9. **Specificity:** The 
    degree to which the answer is detailed and precise.\n10. **Tone:** The overall emotional quality of the answer.\n\nThese 
    features can be used to assess the quality of an answer and to identify areas where the answer could be improved. For example, 
    if an answer is unclear, the writer could be asked to provide more detail or to rephrase the answer in a clearer way. 
    If an answer is defensive, the writer could be asked to be more assertive or to provide more evidence to support their claims.' '''

    res = palm.chat(messages = prompt)
    output_list.append(res.last)
    output_list = cleaner(output_list[0])
    return output_list