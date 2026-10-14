import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from '@/store';
import { logoutUser } from '@/store/slices/authSlice';
import { authApiService } from '@/services/api/authService';

export const useAuth = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { user, isAuthenticated, isLoading } = useSelector((state: RootState) => state.auth);

  const logout = async () => {
    await authApiService.logout();
    dispatch(logoutUser());
  };

  return {
    user,
    isAuthenticated,
    isLoading,
    logout,
  };
};
