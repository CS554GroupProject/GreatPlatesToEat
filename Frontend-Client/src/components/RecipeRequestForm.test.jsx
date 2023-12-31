import { fireEvent, render } from '@testing-library/react';
import RecipeRequestForm from './RecipeRequestForm';

describe('RecipeRequestForm', () => {
  it('calls onSubmit prop function when the form is submitted', () => {
    const handleSubmit = jest.fn();
    const { getByPlaceholderText, getByText, getByLabelText } = render(
      <RecipeRequestForm onSubmit={handleSubmit} response="Some response" />
    );

    fireEvent.change(getByPlaceholderText('Enter username'), {
      target: { value: 'Jawaher Alsaiari' },
    });

    fireEvent.change(getByPlaceholderText('Enter query'), {
      target: { value: 'chicken noodle soup' },
    });

    fireEvent.change(getByLabelText('Select number of recipes to receive'), {
      target: { value: '3' },
    });

    fireEvent.click(getByText('Submit'));

    expect(handleSubmit).toHaveBeenCalled();
  });

  it('displays the response prop', () => {
    const { getByText } = render(
      <RecipeRequestForm
        onSubmit={() => {}}
        response="Grandmas chicken noodle soup"
      />
    );

    expect(
      getByText('Response: Grandmas chicken noodle soup')
    ).toBeInTheDocument();
  });
});
