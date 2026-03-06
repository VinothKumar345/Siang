# backend/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session

# Correct imports for backend structure
from backend.database.database import get_db
from backend.database.models import User

# Create router
router = APIRouter()


# Register user endpoint
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(
    full_name: str = Form(...),
    username: str = Form(...),
    email: str = Form(...),
    mobile_number: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    # Check if username or email already exists
    user_exists = db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists"
        )

    # Create new user
    new_user = User(
        full_name=full_name,
        username=username,
        email=email,
        mobile_number=mobile_number,
        hashed_password=password  # NOTE: Should hash password in production
    )

    # Save user to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Account created successfully! You can now log in."
    }