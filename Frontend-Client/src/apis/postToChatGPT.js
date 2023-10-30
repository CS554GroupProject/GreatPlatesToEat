import axios from 'axios';

const addressOfTheBackendServer = 'http://localhost:8000/';

/**
 * Send a query to the backend ChatGPT API.
 *
 * @param {string} userData - The user's input data as a string.
 * @returns {Promise<any>} - The response from the server.
 */
export function postToChatGPT(userData) {
  const url = `${addressOfTheBackendServer}`;

  return axios
    .post(url, {
      Query: userData,
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      console.error('There was a problem with the request:', error.message);
      throw error;
    });
}

// Usage example:
// postToChatGPT('Hello ChatGPT!')
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.error('Error:', error.message);
//   });
