import RecipieRequestForm from '../components/RecipieRequestForm';
import { postToChatGPT } from '../apis/postToChatGPT';
import React, { useState } from 'react';
import RecipieCard from '../components/RecipieCard';
import { useAuth } from '../context(s)/AuthContext';
import { useUserItems } from '../context(s)/RecipeStorageContext';

const RequestRecipiesPage = (props) => {
  const { currentUser, login, logout } = useAuth();
  const { userItems, updateUserItems } = useUserItems();
  const [availableRecipes, setAvailableRecipes] = useState([]);
  const [numRecipes, setNumRecipes] = useState(1);
  const [query, setQuery] = useState('');
  const [restrictions, setRestrictions] = useState('');

  const onSaveRecipeCard = (event, name, desc, list, key) => {
    updateUserItems({
      userName: currentUser !== null ? currentUser : 'Default user',
      desc: desc,
      list: list,
      key: key,
    });
    console.log(
      `Name: ${name} Desc: ${desc} IngList: ${list} Key: ${key} Created by: ${currentUser}`
    );
    // send some request to backend to save it
  };

  const onSubmitHandler = (event) => {
    event.preventDefault();
    const responseDataForBackend = {
      query: query,
      numRequested: numRecipes,
      restrictions: restrictions !== '' ? restrictions : 'None',
    };
    setAvailableRecipes((prev) => {
      return [
        ...prev,
        {
          query: query,
          numRequested: numRecipes,
          restrictions: restrictions,
          userName: currentUser,
        },
      ];
    });
    console.log(responseDataForBackend);
    postToChatGPT(JSON.stringify(responseDataForBackend))
      .then((data) => console.log(data))
      .catch((err) => console.log(err))
      .finally(() => {
        event.target.reset();
      });
  };

  return (
    <>
      <RecipieRequestForm
        onSubmit={onSubmitHandler}
        recipesCount={setNumRecipes}
        query={setQuery}
        restrictions={setRestrictions}
        disabled={currentUser === null}
      />
      {availableRecipes !== null
        ? availableRecipes
            .filter((item) => {
              return item.userName === currentUser;
            })
            .map((item, index) => {
              return (
                <RecipieCard
                  Name={item.query}
                  desc={item.restrictions}
                  ingredientsList={item.numRequested}
                  key={index}
                  indexOfCard={index}
                  onSave={onSaveRecipeCard}
                />
              );
            })
        : null}
    </>
  );
};

export default RequestRecipiesPage;

// https://kinsta.com/knowledgebase/objects-are-not-valid-as-a-react-child/#:~:text=Another%20common%20cause%20of%20the%20error%20is%20incorrect,the%20array%20to%20a%20valid%20React%20child%20element.
// https://rapidapi.com/blog/axios-react-api-tutorial/
// https://react.dev/learn/passing-props-to-a-component
// https://stackoverflow.com/questions/38412574/syntaxerror-json-parse-unexpected-character-at-line-1-column-2-of-the-json
