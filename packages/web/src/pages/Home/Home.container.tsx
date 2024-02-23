import { FC } from 'react';
import { useMutation } from '@tanstack/react-query';

import { HomeComponent } from './Home.component.tsx';
import { useAnthonApiClient } from '../../_shared';

export const HomeContainer: FC = () => {
  const anthonApiClient = useAnthonApiClient();

  const mutation = useMutation({
    mutationFn: anthonApiClient.createSalary,
    onSuccess: (data) => {
      // Invalidate and refetch
      console.log(data);

    },
  });


  return <HomeComponent />;
};
