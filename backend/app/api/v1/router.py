from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    users,
    organizations,
    roles,
    meetings,
    security,
    audit,
    notifications,
    ai,
    analytics,
    settings,
    health,
)

api_router = APIRouter()

# Include all module routers under /api/v1
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(organizations.router)
api_router.include_router(roles.router)
api_router.include_router(meetings.router)
api_router.include_router(security.router)
api_router.include_router(audit.router)
api_router.include_router(notifications.router)
api_router.include_router(ai.router)
api_router.include_router(analytics.router)
api_router.include_router(settings.router)
