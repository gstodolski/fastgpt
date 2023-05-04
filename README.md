# Smalltalk
### A ChatGPT wrapper built for a Yale CS senior project.

#### Setting up the application
In order to use Smalltalk, you must first generate your **OpenAI API key**. To do so, [sign up or log in](https://platform.openai.com/signup) to your account. From there, click on your profile in the upper-right, select *View API Keys*, and copy or create your secret key.

Download the Smalltalk source code from this repository. Once downloaded, create a `.env` file in the `smalltalk` directory. Paste your API key into the `.env` file in this format: `OPENAI_API_KEY=*insert_your_key_here*`.

#### Using the application
To run Smalltalk, start a virtual environment by running `pipenv shell`. Then, simply type `python gui.py` to launch the application. From there, you will be able to use Smalltalk to generate AI-written messages based on templates you create.

The application is a prototype, meaning there may be minor bugs you encounter while using. Updates will be released in the near future to address these issues.
