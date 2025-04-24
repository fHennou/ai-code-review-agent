import requests
import yaml

class LLMClient:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        self.provider = config.get("provider", "openai")
        self.model = config.get("model", "gpt-3.5-turbo")
        self.api_key = config.get("api_key")

    def run(self, prompt, code_snippet):
        if self.provider == "openai":
            return self._call_openai(prompt, code_snippet)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def _call_openai(self, prompt, code_snippet):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": code_snippet}
            ]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
