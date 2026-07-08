from fastapi import APIRouter


router = APIRouter(prefix="/categories", tags=["Service Categories"])


SERVICE_CATEGORIES = [
    {
        "id": 1,
        "name_en": "AC Repair and Service",
        "name_hi": "एसी रिपेयर और सर्विस",
        "name_mr": "एसी दुरुस्ती आणि सर्विस",
        "is_active": True,
    },
    {
        "id": 2,
        "name_en": "Electrician",
        "name_hi": "इलेक्ट्रीशियन",
        "name_mr": "इलेक्ट्रिशियन",
        "is_active": True,
    },
    {
        "id": 3,
        "name_en": "Plumbing",
        "name_hi": "प्लंबर",
        "name_mr": "प्लंबर",
        "is_active": True,
    },
]


@router.get("")
def list_categories():
    return {
        "categories": SERVICE_CATEGORIES
    }