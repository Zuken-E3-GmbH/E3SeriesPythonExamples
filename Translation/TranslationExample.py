import os
import e3series.tools as e3tools

# This example shows the usage of the e3series.tools.Translation module
# This tool can be used to use translations in your script based on a *.lng file created 
# with the Zuken E3.TranslationManager

path = os.path.dirname(__file__)                            # Determine the path of the script file
translationFile = os.path.join(path, "LanguageTest.lng")    # Create the full path of the translation file
translator = e3tools.Translation(translationFile, e3tools.Language.GERMAN)  # Create the translator instance. 
                                                            # The language is optional, if not given it will be determined by your E3.series installation
print(f"The translator translates to: {translator.GetUsedLanguage()}")  # Print which language the translator will translate to.
                                                            # The result should be Language.GERMAN in this example.
print(translator.Get("I am a Python script."))              # Print out a sinple translated text
print(translator.Get("I am a formatted string: '{0}', '{1}', '{2}'").format("first", "second", "third"))   # Print a formatted translated text
