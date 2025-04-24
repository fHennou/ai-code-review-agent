# 🤖 AI Code Review Agent

Un assistant local (ou basé sur une API) capable d'analyser du code Python, de détecter les erreurs, d'améliorer la clarté, et de suggérer des corrections. Il agit comme un reviewer de code intelligent.

---

## 🎯 Objectif

Ce projet utilise des modèles d'IA (OpenAI, Claude, Ollama...) pour :
- Analyser automatiquement des fichiers Python
- Repérer les bugs, problèmes de style ou manque de clarté
- Suggérer des améliorations comme un reviewer humain
- Générer un rapport de revue clair en Markdown

---

## 📂 Structure du Projet

```bash
ai-code-review-agent/
├── agent/
│   ├── analyzer.py          # Logique d'analyse + prompts
│   └── llm_interface.py     # Intégration des modèles OpenAI/Ollama
├── cli.py                   # Interface en ligne de commande
├── config.yaml              # Clés API et configuration du modèle
├── examples/
│   ├── buggy_script.py
│   └── clean_script.py
├── prompts/
│   └── templates.yaml       # Styles de prompts (strict, mentor, test_focus)
├── reviews/
│   └── review_output.md     # Résultats des revues
├── requirements.txt         # Dépendances Python
├── README.md                # Ce fichier
└── .gitignore               # Fichiers à ignorer par Git
