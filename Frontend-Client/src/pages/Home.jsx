import React from 'react';
import recipeBook from '../staticAssets/recipeBook.jpg';

const Home = () => {
  return (
    <>
      <h1 className="text-center my-5">Home page</h1>
      <p className="text-center font-weight-bold bg-white mx-5 p-1">
        Welcome to Great plates to eat! Where you can request some recipes from
        chat GPT based on a simple prompt and have the ability to add in some
        restrictions
      </p>
      <img src={recipeBook} alt="Recipe book" className="img-fluid" />
    </>
  );
};

export default Home;
