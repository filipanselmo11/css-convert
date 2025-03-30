from pydantic import BaseModel

class CSSRequest(BaseModel):
    css: str
    framework: str # 'tailwind', 'bootstrap', 'bulma', etc.
    