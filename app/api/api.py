from fastapi import APIRouter

from app.api.endpoints import (
    root,
    location,
    auth,
    user,
    income,
    expenditure,
    saving,
    plan,
    target,
    storage,
    device,
    dsaving,
    case,
    loan,
    debt,
    bank,
    dexpenditure,
    dexpend_form,
    financial_bucket,
)

api_router = APIRouter()

api_router.include_router(root.router, tags=["root"])
api_router.include_router(location.router, tags=["location"])
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(income.router, prefix="/income", tags=["income"])
api_router.include_router(
    expenditure.router, prefix="/expenditure", tags=["expenditure"]
)
api_router.include_router(
    dexpenditure.router, prefix="/dexpenditure", tags=["dexpenditure"]
)
api_router.include_router(saving.router, prefix="/saving", tags=["saving"])
api_router.include_router(target.router, prefix="/target", tags=["target"])
api_router.include_router(loan.router, prefix="/loan", tags=["loan"])
api_router.include_router(plan.router, prefix="/plan", tags=["plan"])
api_router.include_router(storage.router, prefix="/storage", tags=["storage"])
api_router.include_router(device.router, prefix="/device", tags=["device"])
api_router.include_router(dsaving.router, prefix="/dsaving", tags=["dsaving"])
api_router.include_router(case.router, prefix="/case", tags=["case"])
api_router.include_router(debt.router, prefix="/debt", tags=["debt"])
api_router.include_router(bank.router, prefix="/bank", tags=["bank"])
api_router.include_router(
    dexpend_form.router, prefix="/dexpend-form", tags=["dexpend-form"]
)
api_router.include_router(
    financial_bucket.router,
    prefix="/financial-bucket",
    tags=["Financial Bucket"],
)
