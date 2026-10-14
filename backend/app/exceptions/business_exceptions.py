from app.exceptions.base import NotFoundException, BadRequestException, ConflictException


class MeetingNotFoundException(NotFoundException):
    def __init__(self, meeting_id: str):
        super().__init__(message=f"Meeting with ID '{meeting_id}' not found", details={"meeting_id": meeting_id})


class OrgNotFoundException(NotFoundException):
    def __init__(self, org_id: str):
        super().__init__(message=f"Organization with ID '{org_id}' not found", details={"organization_id": org_id})


class SecurityPolicyViolationException(BadRequestException):
    def __init__(self, rule_name: str, reason: str):
        super().__init__(
            message=f"Security governance policy violation: {rule_name}",
            details={"rule": rule_name, "reason": reason}
        )


class IntegrationConnectionException(BadRequestException):
    def __init__(self, platform: str, reason: str):
        super().__init__(
            message=f"Failed to communicate with {platform} API: {reason}",
            details={"platform": platform, "reason": reason}
        )
