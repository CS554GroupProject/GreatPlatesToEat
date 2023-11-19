import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context(s)/AuthContext';
import { useUserItems } from '../context(s)/RecipeStorageContext';
import RecipieCard from '../components/RecipieCard';

const SavedRecipesPage = () => {
  const { userItems, updateUserItems } = useUserItems();
  const { currentUser } = useAuth();
  console.log(userItems);

  return (
    <>
      {userItems !== null ? (
        userItems
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
          })
      ) : (
        <h1>
          No items for current user. Please login if you have stored some
          already
        </h1>
      )}
    </>
  );
};

export default SavedRecipesPage;
