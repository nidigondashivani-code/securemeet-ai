from enum import Enum


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ORG_ADMIN = "org_admin"
    SECURITY_OFFICER = "security_officer"
    COMPLIANCE_AUDITOR = "compliance_auditor"
    MEMBER = "member"
    GUEST = "guest"


class MeetingPlatform(str, Enum):
    GOOGLE_MEET = "google_meet"
    ZOOM = "zoom"
    MS_TEAMS = "teams"


class SecurityRiskLevel(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class AuditActionType(str, Enum):
    AUTH_LOGIN = "auth.login"
    AUTH_LOGOUT = "auth.logout"
    MEETING_STARTED = "meeting.started"
    MEETING_TERMINATED = "meeting.terminated_by_policy"
    DATA_EXPORTED = "data.exported"
    POLICY_UPDATED = "security_policy.updated"
    MEMBER_INVITED = "org.member_invited"
