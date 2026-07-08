from pydantic import BaseModel


class ServiceSubcategoryResponse(BaseModel):
    id: int
    name_en: str
    name_hi: str
    name_mr: str


class ServiceCategoryResponse(BaseModel):
    id: int
    name_en: str
    name_hi: str
    name_mr: str
    is_active: bool
    subcategories: list[ServiceSubcategoryResponse]


class ServiceCategoryListResponse(BaseModel):
    categories: list[ServiceCategoryResponse]