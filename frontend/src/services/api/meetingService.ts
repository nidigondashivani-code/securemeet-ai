import { apiClient } from './client';
import { ApiResponse, Meeting } from '@/types';

export const meetingApiService = {
  getMeetings: async (orgId: string): Promise<ApiResponse<Meeting[]>> => {
    const response = await apiClient.get<ApiResponse<Meeting[]>>('/meetings', {
      params: { org_id: orgId },
    });
    return response.data;
  },
  scheduleMeeting: async (meeting: Partial<Meeting>): Promise<ApiResponse<Meeting>> => {
    const response = await apiClient.post<ApiResponse<Meeting>>('/meetings', meeting);
    return response.data;
  },
};
