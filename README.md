# Newsletter Generation with Gemini API

This project is about generating a 200-250-word newsletter from a topic through **Google GenAI**

## Workflow

genai package - outline - newsletter 1 - criticism *newsletter 2* - summary - saved in csv

## Steps to Run the Code

1. Cloning the repository:

git clone https://github.com/blackstag2k/Newsletter-Generation.git

2. Installing the Dependencies for the project:

* dependencies listed in the requirements.txt

pip install -r requirements.txt 

* If you want to execute the installed pip module instead of a script file, then use the command below in Command Window

pip -m install -r requirements.txt

### Example:

- python -m pip install pandas,
- python -m pip install google-generativeai

3. Add your API Key 

* Google AI API, Open AI API, etc. generated from any platform. Google Genai key is used here.

export GOOGLE_API_KEY="YOUR_KEY"

4. Run

python main.py

**Output**

Output CSV:
| Topic | Outline | Newsletter | Critique | Summary
|-------|--------|--------|--------|--------|
| Urban Tails and Trails Newsletter | Outline of the Newsletter | Newsletter Content | Critique of the Newsletter Content and Revision | Summary of 60 words for the Newsletter |

## Tools Used

- Google AI API (Gemini)
- Pandas
- Python 3.14

## Lessons to be Learned

- Using the Pandas DataFrame as a worksheet to save the particulars of the prompt.
- Executing the code through a virtual environment (.venv) like VS Code.
- Prompt chaining to execute multiple prompts and get the best results.


Documented during the Prompt Engineering Course for Prompt Chaining and Content Generation
