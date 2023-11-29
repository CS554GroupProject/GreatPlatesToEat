const BASE_URL = 'https://localhost:8000/'; 

export const fetchUserItems = async (currentUser, recipeId) => {
  try {
    const response = await fetch(`${BASE_URL}/Backend-Server/myproject/apiapp/views.py/get_recipe`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user: currentUser,
        recipe_id: recipeId,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user items');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error(`Error fetching user items: ${error.message}`);
  }
};

