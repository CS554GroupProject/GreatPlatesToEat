import RecipieRequestForm from '../components/RecipieRequestForm';
import { postToChatGPT } from '../apis/postToChatGPT';

const RequestRecipiesPage = (props) => {
  const onSubmitHandler = (event) => {
    event.preventDefault();

    const form = event.target;
    const textareaValue = event.target.querySelector('#input1').value;
    console.log('Form submitted with value:', textareaValue);
    form.reset();
    postToChatGPT(JSON.stringify(textareaValue));
  };

  return <RecipieRequestForm onSubmit={onSubmitHandler} />;
};

export default RequestRecipiesPage;
