import axios from 'axios';

const addressOfTheBackendServer =
  'http://localhost:8000/post_to_gpt/get_recipe/';

/**
 * Send a request for the backend data saved
 * @returns {Promise<any>} - The response from the server.
 */
export async function getFromChatGPT() {
  const url = `${addressOfTheBackendServer}`;

  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error('There was a problem with the request:', error.message);
    throw error;
  }
}
