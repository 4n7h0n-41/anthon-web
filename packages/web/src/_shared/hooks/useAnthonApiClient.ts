import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';

class HttpClient {
  private axiosInstance: AxiosInstance;

  constructor() {
    this.axiosInstance = axios.create({
      baseURL: 'http://localhost:8000',
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  get<T, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R> {
    return this.axiosInstance.get<T, R>(url, config);
  }

  post<T, B = NonNullable<unknown>, R = AxiosResponse<T>>(url: string, data?: B, config?: AxiosRequestConfig): Promise<R> {
    return this.axiosInstance.post<T, R>(url, data, config);
  }

  put<T, B = NonNullable<unknown>, R = AxiosResponse<T>>(url: string, data?: B, config?: AxiosRequestConfig): Promise<R> {
    return this.axiosInstance.put<T, R>(url, data, config);
  }

  delete<T, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R> {
    return this.axiosInstance.delete<T, R>(url, config);
  }
}

type CreateSalaryDto = {
  amount: number;
}

type CreateSalaryResponse = {
  salaries: Array<{
    id: string;
    amount: number;
  }>;
}

export const useAnthonApiClient = () => {
  const httpClient = new HttpClient();

  const createSalary = async (data: CreateSalaryDto): Promise<CreateSalaryResponse> => {
    return httpClient.post('/salaries', data);
  };

  return {
    createSalary,
  };
};
