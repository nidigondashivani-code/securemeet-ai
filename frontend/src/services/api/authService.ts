import { apiClient } from './client';
import { ApiResponse, User } from '@/types';

export interface LoginPayload {
  email: string;
  password: string;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  expires_in: number;
}

export const authApiService = {
  login: async (payload: LoginPayload): Promise<ApiResponse<AuthTokens>> => {
    const response = await apiClient.post<ApiResponse<AuthTokens>>('/auth/login', payload);
    return response.data;
  },
  getCurrentUser: async (): Promise<ApiResponse<User>> => {
    const response = await apiClient.get<ApiResponse<User>>('/users/me');
    return response.data;
  },
  logout: async (): Promise<void> => {
    localStorage.removeItem('securemeet_access_token');
    localStorage.removeItem('securemeet_refresh_token');
  },
};
