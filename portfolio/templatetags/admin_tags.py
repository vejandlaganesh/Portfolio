from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr):
    if hasattr(obj, attr):
        val = getattr(obj, attr)
        if val is None:
            return ""
        return val
    return ""

@register.filter
def replace_underscore(value):
    return value.replace("_", " ")

@register.filter
def split_csv(value):
    """'React, Node.js, Tailwind CSS' -> ['React', 'Node.js', 'Tailwind CSS'].

    Django's built-in `.split` in templates splits on whitespace, which broke
    multi-word technologies ("Tailwind CSS") and left trailing commas.
    """
    return [part.strip() for part in str(value or "").split(",") if part.strip()]

import re

@register.filter
def split_lines(value):
    """Splits a multiline string into non-empty lines, stripping existing bullets."""
    if not value: return []
    lines = []
    for line in str(value).splitlines():
        line = line.strip()
        if not line: continue
        # Strip leading bullets: •, -, *, or digits followed by dot/parenthesis
        line = re.sub(r'^[\u2022\-\*]\s*', '', line)
        line = re.sub(r'^\d+[\.\)]\s*', '', line)
        lines.append(line.strip())
    return lines

@register.filter
def split_blocks(value):
    """Splits text by double newlines into blocks."""
    if not value: return []
    blocks = [b.strip() for b in re.split(r'\n\s*\n', str(value)) if b.strip()]
    return blocks

@register.filter
def split_colon(value, index):
    """Splits a string by colon or newline and returns the specified index. Example for 'Title: text'"""
    if not value: return ""
    parts = re.split(r'[:\n]', str(value), maxsplit=1)
    try:
        return parts[int(index)].strip()
    except (IndexError, ValueError):
        return ""

@register.filter
def categorize_techs(value):
    techs = [part.strip() for part in str(value or "").split(",") if part.strip()]
    if not techs: return {}
    
    categories = {
        "Frontend": ["HTML", "CSS", "React", "React.js", "Tailwind CSS", "TailwindCSS", "JavaScript", "TypeScript", "Vite", "MERN Frontend", "Bootstrap"],
        "Backend": ["Python", "Django", "Node.js", "Express.js", "Java", "MERN Backend"],
        "Database": ["MySQL", "Firebase Firestore", "SQL", "MongoDB", "PostgreSQL", "SQLite"],
        "AI / GenAI": ["Generative AI", "Groq GenAI", "Gemini GenAI", "Groq API", "Image Generation", "LLMs", "Machine Learning", "OpenAI"],
        "Testing / Tools": ["Playwright", "ExcelJS", "POM", "Karate", "Git", "GitHub", "Docker", "AWS", "Figma"]
    }
    
    result = {}
    for tech in techs:
        placed = False
        for cat, list_t in categories.items():
            if any(t.lower() == tech.lower() for t in list_t):
                if cat not in result: result[cat] = []
                result[cat].append(tech)
                placed = True
                break
        if not placed:
            if "Other" not in result: result["Other"] = []
            result["Other"].append(tech)
            
    return list(result.items())
