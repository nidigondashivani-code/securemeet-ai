import { useQuery } from '@tanstack/react-query';
import { meetingApiService } from '@/services/api/meetingService';

export const useMeetings = (orgId: string) => {
  return useQuery({
    queryKey: ['meetings', orgId],
    queryFn: () => meetingApiService.getMeetings(orgId),
    enabled: Boolean(orgId),
    staleTime: 1000 * 60 * 2, // 2 minutes cache validity
  });
};
