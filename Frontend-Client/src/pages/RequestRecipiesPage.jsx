import RecipieRequestForm from "../components/RecipieRequestForm";
import { postToChatGPT } from "../apis/postToChatGPT";
import React, { useState } from "react";
import RecipieCard from "../components/RecipieCard";
import { useAuth } from "../context(s)/AuthContext";

const RequestRecipiesPage = (props) => {
  const { currentUser, login, logout } = useAuth();
  const [availableRecipes, setAvailableRecipes] = useState([]);
  const [numRecipes, setNumRecipes] = useState(1);
  const [query, setQuery] = useState("");
  const [restrictions, setRestrictions] = useState("");

  const onSaveRecipeCard = (event, name, desc, list, key) => {
    console.log(
      `Name: ${name} Desc: ${desc} IngList: ${list} Key: ${key} Created by: ${currentUser}`
    );
    // send some request to backend to save it
  };

  const onSubmitHandler = (event) => {
    event.preventDefault();
    setAvailableRecipes((prev) => {
      return [
        ...prev,
        { query: query, numRequested: numRecipes, restrictions: restrictions },
      ];
    });
    const responseDataForBackend = {
      query: query,
      numRequested: numRecipes,
      restrictions: restrictions !== "" ? restrictions : "None",
    };
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
        response={availableRecipes}
        recipesCount={setNumRecipes}
        query={setQuery}
        restrictions={setRestrictions}
        disabled={currentUser === null}
      />
      {availableRecipes !== null
        ? availableRecipes.map((item, index) => {
            return (
              <RecipieCard
                Name={item.query}
                desc={item.numRequested}
                ingredientsList={item.restrictions}
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
