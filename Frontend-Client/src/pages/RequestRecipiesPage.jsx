import RecipieRequestForm from '../components/RecipieRequestForm';
import { postToChatGPT } from '../apis/postToChatGPT';
import React from 'react';

const RequestRecipiesPage = (props) => {
  let [response, setResponse] = React.useState('');

  const onSubmitHandler = (event) => {
    event.preventDefault();

    const form = event.target;
    const textareaValue = event.target.querySelector('#input1').value;
    console.log('Form submitted with value:', textareaValue);
    form.reset();
    postToChatGPT(JSON.stringify(textareaValue)).then((data) => setResponse(data));
  };

  return <RecipieRequestForm onSubmit={onSubmitHandler} response={response}/>;
};

export default RequestRecipiesPage;

// https://kinsta.com/knowledgebase/objects-are-not-valid-as-a-react-child/#:~:text=Another%20common%20cause%20of%20the%20error%20is%20incorrect,the%20array%20to%20a%20valid%20React%20child%20element.
// https://rapidapi.com/blog/axios-react-api-tutorial/
// https://react.dev/learn/passing-props-to-a-component
