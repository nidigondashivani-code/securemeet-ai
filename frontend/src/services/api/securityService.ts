import { apiClient } from './client';
import { ApiResponse, SecurityPolicy } from '@/types';

export const securityApiService = {
  getPolicies: async (orgId: string): Promise<ApiResponse<SecurityPolicy[]>> => {
    const response = await apiClient.get<ApiResponse<SecurityPolicy[]>>('/security/policies', {
      params: { org_id: orgId },
    });
    return response.data;
  },
  createPolicy: async (policy: Partial<SecurityPolicy>): Promise<ApiResponse<SecurityPolicy>> => {
    const response = await apiClient.post<ApiResponse<SecurityPolicy>>('/security/policies', policy);
    return response.data;
  },
};
