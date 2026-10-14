from typing import List
from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_audit_service
from app.schemas.audit import AuditLogResponse
from app.schemas.common import ApiResponse
from app.services.audit_service import AuditService

router = APIRouter(prefix="/audit", tags=["Audit Logs"])


@router.get("/logs", response_model=ApiResponse[List[AuditLogResponse]], status_code=status.HTTP_200_OK)
async def get_audit_logs(
    org_id: str = Query(..., description="Organization ID filter"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    audit_service: AuditService = Depends(get_audit_service),
) -> ApiResponse[List[AuditLogResponse]]:
    """Retrieves immutable SOC2 / ISO-27001 audit event logs for compliance inspection."""
    logs = await audit_service.get_org_audit_trail(org_id, skip=skip, limit=limit)
    return ApiResponse(data=[AuditLogResponse.model_validate(log) for log in logs])
