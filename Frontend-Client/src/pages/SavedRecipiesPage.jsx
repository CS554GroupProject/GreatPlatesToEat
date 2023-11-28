import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context(s)/AuthContext';
import { useUserItems } from '../context(s)/RecipeStorageContext';
import RecipieCard from '../components/RecipieCard';
import { fetchUserItems } from '../apis/recipeapi';
import RecipeInputPage from './RecipeInputPage'; 

const SavedRecipesPage = () => {
  const { currentUser } = useAuth();
  const [userItems, setUserItems] = useState([]);
  const [recipeId, setRecipeId] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (recipeId) {
      const getUserItems = async () => {
        try {
          const items = await fetchUserItems(currentUser, recipeId);
          setUserItems(items);
        } catch (error) {
          console.error('Error fetching user items:', error);
        }
      };

      getUserItems();
    }
  }, [currentUser, recipeId]);

  const handleRecipeIdSubmit = (id) => {
    setRecipeId(id);
  };

  const makeListOfSavedRecipes = () => {
    if (userItems.length === 0) {
      return (
        <h1 className="text-center mt-5 bg-white rounded p-3 mx-5 shadow-lg">
          No items for the current user. Please login if you have stored some already.
        </h1>
      );
    }

    return userItems.map((item, index) => (
      <RecipeCard
        Name={item.userName}
        desc={item.desc}
        ingredientsList={item.list}
        key={index}
        indexOfCard={item.key}
        onSave={null}
      />
    ));
  };

  return (
    <>
      <RecipeInputPage onSubmit={handleRecipeIdSubmit} />
      {makeListOfSavedRecipes()}
    </>
  );
};


export default SavedRecipesPage;
