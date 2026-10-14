export interface ApiResponse<T = any> {
  success: boolean;
  message: string;
  data: T;
  error_code?: string;
  details?: Record<string, any>;
}

export interface PaginatedResponse<T = any> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

export interface User {
  id: string;
  email: string;
  full_name: string;
  is_active: boolean;
  is_verified: boolean;
  organization_id?: string;
  role_id?: string;
}

export interface Meeting {
  id: string;
  title: string;
  platform: 'google_meet' | 'zoom' | 'teams';
  external_meeting_id: string;
  host_id: string;
  organization_id: string;
  scheduled_start: string;
  scheduled_end: string;
  status: string;
  security_metadata: Record<string, any>;
}

export interface SecurityPolicy {
  id: string;
  organization_id: string;
  name: string;
  description?: string;
  is_active: boolean;
  rules: Record<string, any>;
}
