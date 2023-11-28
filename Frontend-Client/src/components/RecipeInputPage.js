import React, { useState } from 'react';

const RecipeInputPage = ({ onSubmit }) => {
  const [recipeId, setRecipeId] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Check if the entered value is a valid integer
    const parsedRecipeId = parseInt(recipeId, 10);
    if (!isNaN(parsedRecipeId) && Number.isInteger(parsedRecipeId) && parsedRecipeId >= 0) {
      onSubmit(parsedRecipeId);
    } else {
      alert('Please enter a valid non-negative integer for Recipe ID.');
    }
  };

  return (
    <div className="recipe-input-page">
      <form onSubmit={handleSubmit}>
        <label>
          Recipe ID:
          <input
            type="text"
            value={recipeId}
            onChange={(e) => setRecipeId(e.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default RecipeInputPage;
