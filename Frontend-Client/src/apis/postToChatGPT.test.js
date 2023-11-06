import axios from 'axios';
import { postToChatGPT } from './postToChatGPT';

jest.mock('axios');

afterEach(() => {
  jest.clearAllMocks();
});

const addressOfTheBackendServer = 'http://localhost:8000/';

describe('postToChatGPT', () => {
  it('sends user data and receives a response', async () => {
    const userData = 'Some random Dummy data';
    const mockResponse = { data: 'Response from ChatGPT' };
    axios.post.mockResolvedValue(mockResponse);

    const response = await postToChatGPT(userData);

    expect(axios.post).toHaveBeenCalledWith(addressOfTheBackendServer, {
      Query: userData,
    });

    expect(response).toEqual(mockResponse.data);
  });
  it('throws an error when the request fails', async () => {
    const originalConsoleError = console.error;
    console.error = jest.fn();

    const userData = 'Some random Dummy data';
    const errorMessage = 'Network Error';
    const mockError = new Error(errorMessage);
    axios.post.mockRejectedValueOnce(mockError);

    await expect(postToChatGPT(userData)).rejects.toThrow(errorMessage);

    expect(axios.post).toHaveBeenCalledWith(addressOfTheBackendServer, {
      Query: userData,
    });

    console.error = originalConsoleError;
  });
});

// referenced materials:
// https://dev.to/endymion1818/how-to-test-javascript-api-calls-187k
