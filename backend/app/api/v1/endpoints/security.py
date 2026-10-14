from typing import List
from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_security_service
from app.schemas.common import ApiResponse
from app.schemas.security import SecurityPolicyCreate, SecurityPolicyResponse
from app.services.security_service import SecurityService

router = APIRouter(prefix="/security", tags=["Security Engine"])


@router.get("/policies", response_model=ApiResponse[List[SecurityPolicyResponse]], status_code=status.HTTP_200_OK)
async def list_policies(
    org_id: str = Query(..., description="Organization ID filter"),
    security_service: SecurityService = Depends(get_security_service),
) -> ApiResponse[List[SecurityPolicyResponse]]:
    """Lists enterprise DLP, participant restrictions, and meeting guardrail policies."""
    policies = await security_service.get_active_policies(org_id)
    return ApiResponse(data=[SecurityPolicyResponse.model_validate(p) for p in policies])


@router.post("/policies", response_model=ApiResponse[SecurityPolicyResponse], status_code=status.HTTP_201_CREATED)
async def create_policy(
    payload: SecurityPolicyCreate,
    security_service: SecurityService = Depends(get_security_service),
) -> ApiResponse[SecurityPolicyResponse]:
    """Configures a new meeting security rule set."""
    policy = await security_service.create(payload)
    return ApiResponse(message="Security policy active", data=SecurityPolicyResponse.model_validate(policy))
