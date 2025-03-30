import re

# --- Mapeamento de cores para Tailwind ---
tailwind_color_map = {
    '#FF0000': 'bg-red-500',
    '#00FF00': 'bg-green-500',
    '#0000FF': 'bg-blue-500',
    '#000000': 'text-black',
    '#FFFFFF': 'text-white',
}

# --- Mapeamento de cores para Bootstrap ---
bootstrap_color_map = {
    '#FF0000': 'bg-danger',
    '#00FF00': 'bg-success',
    '#0000FF': 'bg-primary',
    '#000000': 'text-dark',
    '#FFFFFF': 'text-light',
}

# --- Regras de conversão para Tailwind ---
tailwind_rules = {
    r'padding:\s*(\d+)px': lambda m: f'p-[{m.group(1)}px]',
    r'margin:\s*(\d+)px': lambda m: f'm-[{m.group(1)}px]',
    r'border:\s*1px solid (#[0-9A-Fa-f]{6})': lambda m: f'border border-[{m.group(1)}]',
    r'background-color:\s*(#[0-9A-Fa-f]{6})': lambda m: tailwind_color_map.get(m.group(1).upper(), f'bg-[{m.group(1)}]'),
    r'color:\s*(#[0-9A-Fa-f]{6})': lambda m: tailwind_color_map.get(m.group(1).upper(), f'text-[{m.group(1)}]'),
    r'border-color:\s*(#[0-9A-Fa-f]{6})': lambda m: f'border-[{m.group(1)}]',  # pode mapear se quiser
}

# --- Regras de conversão para Bootstrap ---
bootstrap_rules = {
    r'padding:\s*(\d+)px': lambda m: 'p-3',  # aproximação
    r'margin:\s*(\d+)px': lambda m: 'm-3',   # aproximação
    r'border:\s*1px solid (#[0-9A-Fa-f]{6})': lambda m: 'border border-success',  # simplificado
    r'background-color:\s*(#[0-9A-Fa-f]{6})': lambda m: bootstrap_color_map.get(m.group(1).upper(), 'bg-custom'),
    r'color:\s*(#[0-9A-Fa-f]{6})': lambda m: bootstrap_color_map.get(m.group(1).upper(), 'text-custom'),
    r'border-color:\s*(#[0-9A-Fa-f]{6})': lambda m: 'border-success',  # pode mapear se quiser
}


def convert_to_tailwind(css: str) -> str:
    classes = []

    for pattern, converter in tailwind_rules.items():
        match = re.search(pattern, css, re.IGNORECASE)
        if match:
            classes.append(converter(match))

    return f'<div class="{" ".join(classes)}"></div>' if classes else "Conversão não implementada."


def convert_to_bootstrap(css: str) -> str:
    classes = []

    for pattern, converter in bootstrap_rules.items():
        match = re.search(pattern, css, re.IGNORECASE)
        if match:
            classes.append(converter(match))

    return f'<div class="{" ".join(classes)}"></div>' if classes else "Conversão não implementada."
