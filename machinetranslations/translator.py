from deep_translator import  GoogleTranslator
import detectlanguage

detectlanguage.configuration.api_key = "fc4026498edef3fec8c19d3767ea5d21"

def TranslateToEnglish(word):
    result = detectlanguage.detect(word)
    language =  result[0]['language']
    translated_word = GoogleTranslator(source=language, target='en').translate(word)
    if word==None:
        return "No input"
    else:
        return translated_word
    
def language_detect(word):
    result = detectlanguage.detect(word)
    language =  result[0]['language']
    return language
