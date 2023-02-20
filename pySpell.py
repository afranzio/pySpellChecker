# Basic Modules
import sys

# Language Library
import language_tool_python

lng_code = sys.argv[1]

# English - ('en-US')
# German - ('de-DE')
# Polish - ('nl')
# Dutch - ('pl-PL')

tool = language_tool_python.LanguageTool(lng_code)
 
text = sys.argv[2]
 
 
# get the matches
matches = tool.check(text)
 
if matches:
    print("Incorrect Spelling.")
    print("List of Suggestions", matches[0].replacements)
    print("Top Suggestion", matches[0].replacements[0])
else:
    print("It's a correct Spelling.")