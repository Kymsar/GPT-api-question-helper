# GPT API question helper

### What does it do?

It's a simple python code that calls the OpenAI completions API with a question and then writes the parameters it used (model, system_prompt, user_prompt and the response it got from GPT) to a markdown file. The md filename is the date and time the question was made. The MD files are sligtly formatted to make the output more readable.

### How to customize it?

Just go to `parameters.py` and change the parameters to you liking. If you need info on what the parameters do, got to the [OpenAI api reference for chat completions](https://platform.openai.com/docs/api-reference/chat)

### What do I need to run it?

You need an OpenAI API key. To get an api key go and register on OpenAI APIs [here](https://platform.openai.com/signup).

### Configuring your api key

Once you have that, export your key as an environment variable. On mac or linux you can do so from the terminal with:

    export OPENAI_API_KEY=""

### To launch

1. Run `sh create-env.sh`
2. Run `source scripts/.gpt-venv/bin/activate`
3. Get your `OPENAI_API_KEY` as an environment variable. I explained how to so [here](#configuring-your-api-key)
4. Run `python3 main.py` and enjoy!