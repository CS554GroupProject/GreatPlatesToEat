import axios from 'axios';

const addressOfTheBackendServer = 'http://localhost:8000/save_recipe/';

/**
 * Send a query to the backend ChatGPT API.
 *
 * @param {string} userData - The user's input data as a string.
 * @returns {Promise<any>} - The response from the server.
 */
export function postToSaveRecipes(userData) {
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

//  Expecting a JSON object. I just send to database as is.