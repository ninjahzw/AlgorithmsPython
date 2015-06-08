import re
a = """
    NOTE! this operation will override the existing Metrics in Production!
    ^Hello \nWorld
"""

print(re.sub('\n\s*\^', ' ', a.strip()))
