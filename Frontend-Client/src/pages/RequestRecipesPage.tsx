import RecipeRequestForm from '../components/RecipeRequestForm';
import { postToChatGPT } from '../apis/postToChatGPT';
import React, { useState } from 'react';
import RecipeCard from '../components/RecipeCard';
import { useAuth } from '../context(s)/AuthContext';
import { useUserItems } from '../context(s)/RecipeStorageContext';
import { postToSaveRecipes } from '../apis/postToSaveRecipes';

interface Recipe {
  query: string;
  ingredientsList: [];
  restrictions: string;
  userName: string;
}

const RequestRecipesPage = (props: any) => {
  const { currentUser, login, logout } = useAuth();
  const { userItems, updateUserItems } = useUserItems();
  const [availableRecipes, setAvailableRecipes] = useState<Recipe[]>([]);
  const [numRecipes, setNumRecipes] = useState(1);
  const [query, setQuery] = useState('');
  const [restrictions, setRestrictions] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const onSaveRecipeCard = (
    name: string,
    desc: string,
    list: [string],
    key: number
  ) => {
    updateUserItems({
      userName: currentUser !== null ? currentUser : 'Default user',
      desc: name,
      list: list,
      key: key,
    });
    console.log(
      `Name: ${name} Desc: ${desc} IngList: ${list} Key: ${key} Created by: ${currentUser}`
    );
    setAvailableRecipes([]);
    // postToSaveRecipes({
    //   userName: currentUser !== null ? currentUser : 'Default user',
    //   desc: desc,
    //   list: list,
    //   key: key,
    // });
    // send some request to backend to save it
  };

  const onSubmitHandler = (event: any) => {
    event.preventDefault();
    setIsLoading(true);
    const responseDataForBackend = {
      query: query,
      numRequested: numRecipes,
      restrictions: restrictions !== '' ? restrictions : 'None',
      username: currentUser,
    };
    console.log(responseDataForBackend);
    postToChatGPT(JSON.stringify(responseDataForBackend))
      .then((data) => {
        setAvailableRecipes((prev) => {
          return [
            ...prev,
            {
              query: query + ' : ' + restrictions,
              ingredientsList: data.ingredients,
              restrictions: restrictions,
              userName: currentUser,
            },
          ];
        });
        console.log(data);
      })
      .catch((err) => console.log(err))
      .finally(() => {
        event.target.reset();
        setIsLoading(false);
      });
    setQuery('');
    setNumRecipes(1);
    setRestrictions('');
  };

  return (
    <div className="mb-5">
      <RecipeRequestForm
        onSubmit={onSubmitHandler}
        recipesCount={setNumRecipes}
        query={setQuery}
        restrictions={setRestrictions}
        disabled={currentUser === null}
      />
      {availableRecipes !== null
        ? availableRecipes
            .filter((item: { userName: string }) => {
              return item.userName === currentUser;
            })
            .map((item, index) => {
              return (
                <RecipeCard
                  Name={item.query}
                  desc={item.restrictions}
                  ingredientsList={item.ingredientsList}
                  key={Math.floor(Math.random() * 4000000)}
                  uniqueId={Math.floor(Math.random() * 4000000)}
                  onSave={onSaveRecipeCard}
                  onDelete={() => {}}
                  isDelete={false}
                />
              );
            })
        : null}
      {isLoading ? <div className="text-center">Loading...</div> : null}
    </div>
  );
};

export default RequestRecipesPage;

// https://kinsta.com/knowledgebase/objects-are-not-valid-as-a-react-child/#:~:text=Another%20common%20cause%20of%20the%20error%20is%20incorrect,the%20array%20to%20a%20valid%20React%20child%20element.
// https://rapidapi.com/blog/axios-react-api-tutorial/
// https://react.dev/learn/passing-props-to-a-component
// https://stackoverflow.com/questions/38412574/syntaxerror-json-parse-unexpected-character-at-line-1-column-2-of-the-json
