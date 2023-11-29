import React, { useState } from 'react';

const RecipeSearchInput = ({ onSubmit }) => {
  const [recipeId, setRecipeId] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Check if the entered value is a valid integer
    const parsedRecipeId = parseInt(recipeId, 10);
    if (
      !isNaN(parsedRecipeId) &&
      Number.isInteger(parsedRecipeId) &&
      parsedRecipeId >= 0
    ) {
      onSubmit(parsedRecipeId);
    } else {
      alert('Please enter a valid non-negative integer for Recipe ID.');
    }
  };

  return (
    <div className="recipe-input-page d-flex justify-content-center align-items-center">
      <form onSubmit={handleSubmit} className="w-25">
        <div className="mb-3">
          <label htmlFor="recipeId" className="form-label">
            <b>Recipe ID:</b>
          </label>
          <input
            type="text"
            className="form-control"
            id="recipeId"
            value={recipeId}
            onChange={(e) => setRecipeId(e.target.value)}
          />
        </div>
        <div className="d-flex justify-content-center">
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
};

export default RecipeSearchInput;
