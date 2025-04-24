import yaml
from agent.llm_interface import LLMClient

def load_prompt_template(mode):
    with open("prompts/templates.yaml", "r") as f:
        templates = yaml.safe_load(f)
    if mode not in templates:
        raise ValueError(f"Prompt mode '{mode}' not found.")
    return templates[mode]["description"]

def analyze_code(file_path, mode, provider):
    with open(file_path, "r") as f:
        code = f.read()

    prompt = load_prompt_template(mode)
    client = LLMClient()
    review = client.run(prompt, code)

    return review
