import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context(s)/AuthContext';
import { useUserItems } from '../context(s)/RecipeStorageContext';
import RecipieCard from '../components/RecipieCard';

const SavedRecipesPage = () => {
  const { userItems, updateUserItems } = useUserItems();
  const { currentUser } = useAuth();
  console.log(userItems);

  const makeListOfSavedRecipes = () => {
    let recipes = [];
    recipes = userItems
      .filter((item) => {
        return item.userName === currentUser;
      })
      .map((item, index) => {
        return (
          <RecipieCard
            Name={item.userName}
            desc={item.desc}
            ingredientsList={item.list}
            key={index}
            indexOfCard={item.key}
            onSave={null}
          />
        );
      });
    if (recipes.length < 1) {
      return (
        <h1 className="text-center mt-5 bg-white rounded p-3 mx-5 shadow-lg">
          No items for current user. Please login if you have stored some
          already
        </h1>
      );
    } else {
      return recipes;
    }
  };

  return <>{makeListOfSavedRecipes()}</>;
};

export default SavedRecipesPage;
