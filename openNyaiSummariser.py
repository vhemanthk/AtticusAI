from opennyai import Pipeline
from opennyai.utils import Data
import urllib
import json


# Get court judgment texts on which to run the AI models
text1 = urllib.request.urlopen(
    'https://raw.githubusercontent.com/OpenNyAI/Opennyai/master/samples/sample_judgment1.txt').read().decode()
text2 = urllib.request.urlopen(
    'https://raw.githubusercontent.com/OpenNyAI/Opennyai/master/samples/sample_judgment2.txt').read().decode()

#texts_to_process = [text1, text2]
def openNyaiSummarise (inputText):
    if (inputText==""):
        return ""
    #texts_to_process = [inputText] # you can also load your text files directly into this    
    data = Data(inputText) # create Data object for data  preprocessing before running ML models    
    use_gpu = False # If you have access to GPU then set this to True else False

    # Choose which of the AI models you want to run from the 3 models 'NER', 'Rhetorical_Role','Summarizer'. E.g. If just Named Entity is of interest then just select 'NER'
    pipeline = Pipeline(components=['Summarizer'], use_gpu=use_gpu, verbose=True)
    results = pipeline(data)
    return results
