# AI-Based Code Explainer

This code explainer using the Google Gemini API to provide explanations for any code snippets that is provided. It uses the **Gemini 2.0 Flash** model.

This web-app uses Flask as a development server. Do not use this for production deployment.

**app.py**
Contains the main logic including the API endpoints. Use it to send code snippets to the model and receive explanations.

**'templates' folder**
Contains index.html: the html code for the front-end page.

**'static' folder**
Contains style.css to style the webpage and script.js to provide basic functionality.

## How to run it yourself:

### Step 1: Create project directory:
Run the following commands in your terminal:
```mkdir code-explainer
cd code-explainer
```

### Step 2: Create Virtual Environment:
```
 python3 -m venv venv  # Creates a 'venv' directory
# Activate it:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```
You should see (venv) at the begnning of your terminal prompt.

### Step 3: Install Libraries:
Create a file named requirements.txt with the following contents:
```
Flask
google-generativeai
python-dotenv
```
And then install them:
```
pip install -r requirements.txt
```
### Step 4: Add your API key:
You can get your Gemini API key by signing in to Google AI Studio and clicking on the 'Get API Key' button on the left. 
Now, create a file named '.env' (the leading dot is important0. Then, add your API key like this:

```GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

### Step 5: Create .gitignore File (optional):
You can do this if you intend to upload this project to github or use git in your system.  Create a file named .gitignore to prevent accidentally committing your secret key or virtual environment:
```
venv/
__pycache__/
*.pyc
.env
```
### Step 6: Create Subdirectories:
Create these subdirectories to contain the frontend files:
```
mkdir templates
mkdir static
```
### Step 7: Download and Run:
1. Download app.py into the main code-explainer directory.
2. Download index.html into the 'templates' folder.
3. Download style.css and script.js files into the 'static' folder.
4. Navigate to the main folder (code-explainer) and run the command:
```
flask run
```
5. You will see an https:// url. copy that and paste in your browser.
6. Finished! You can now use this app for yourself!
