from fastapi import APIRouter
from app.models.css_request import CSSRequest
from app.services.converter import convert_to_tailwind, convert_to_bootstrap


router = APIRouter()

@router.post("/convert")
def convert_css(request: CSSRequest):
    if request.framework.lower() == "tailwind":
        return {"result": convert_to_tailwind(request.css)}
    elif request.framework.lower() == "bootstrap":
        return {"result": convert_to_bootstrap(request.css)}
    return {"result": "Framework não suportado."}