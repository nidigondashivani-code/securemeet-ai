from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.organization_repository import OrganizationRepository
from app.repositories.role_repository import RoleRepository
from app.repositories.meeting_repository import MeetingRepository
from app.repositories.security_repository import SecurityPolicyRepository
from app.repositories.audit_repository import AuditRepository
from app.repositories.notification_repository import NotificationRepository
from app.repositories.ai_repository import AISummaryRepository
from app.repositories.analytics_repository import AnalyticsRepository
from app.repositories.setting_repository import SettingRepository

from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.services.organization_service import OrganizationService
from app.services.role_service import RoleService
from app.services.meeting_service import MeetingService
from app.services.security_service import SecurityService
from app.services.audit_service import AuditService
from app.services.notification_service import NotificationService
from app.services.ai_service import AIService
from app.services.analytics_service import AnalyticsService
from app.services.setting_service import SettingService
from app.services.health_service import HealthService


# Repository Dependencies
def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_org_repository(db: AsyncSession = Depends(get_db)) -> OrganizationRepository:
    return OrganizationRepository(db)


def get_role_repository(db: AsyncSession = Depends(get_db)) -> RoleRepository:
    return RoleRepository(db)


def get_meeting_repository(db: AsyncSession = Depends(get_db)) -> MeetingRepository:
    return MeetingRepository(db)


def get_security_repository(db: AsyncSession = Depends(get_db)) -> SecurityPolicyRepository:
    return SecurityPolicyRepository(db)


def get_audit_repository(db: AsyncSession = Depends(get_db)) -> AuditRepository:
    return AuditRepository(db)


def get_notification_repository(db: AsyncSession = Depends(get_db)) -> NotificationRepository:
    return NotificationRepository(db)


def get_ai_repository(db: AsyncSession = Depends(get_db)) -> AISummaryRepository:
    return AISummaryRepository(db)


def get_analytics_repository(db: AsyncSession = Depends(get_db)) -> AnalyticsRepository:
    return AnalyticsRepository(db)


def get_setting_repository(db: AsyncSession = Depends(get_db)) -> SettingRepository:
    return SettingRepository(db)


# Service Dependencies (Injected into API Controllers)
def get_auth_service(user_repo: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repo)


def get_user_service(user_repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)


def get_org_service(org_repo: OrganizationRepository = Depends(get_org_repository)) -> OrganizationService:
    return OrganizationService(org_repo)


def get_role_service(role_repo: RoleRepository = Depends(get_role_repository)) -> RoleService:
    return RoleService(role_repo)


def get_meeting_service(meeting_repo: MeetingRepository = Depends(get_meeting_repository)) -> MeetingService:
    return MeetingService(meeting_repo)


def get_security_service(sec_repo: SecurityPolicyRepository = Depends(get_security_repository)) -> SecurityService:
    return SecurityService(sec_repo)


def get_audit_service(audit_repo: AuditRepository = Depends(get_audit_repository)) -> AuditService:
    return AuditService(audit_repo)


def get_notification_service(notif_repo: NotificationRepository = Depends(get_notification_repository)) -> NotificationService:
    return NotificationService(notif_repo)


def get_ai_service(ai_repo: AISummaryRepository = Depends(get_ai_repository)) -> AIService:
    return AIService(ai_repo)


def get_analytics_service(analytics_repo: AnalyticsRepository = Depends(get_analytics_repository)) -> AnalyticsService:
    return AnalyticsService(analytics_repo)


def get_setting_service(setting_repo: SettingRepository = Depends(get_setting_repository)) -> SettingService:
    return SettingService(setting_repo)


def get_health_service() -> HealthService:
    return HealthService()
