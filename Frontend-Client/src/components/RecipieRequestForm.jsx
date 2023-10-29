import React from 'react';

const RecipieRequestForm = (props) => {
  return (
    <>
      <div className="d-flex justify-content-center bg-dark mx-auto mt-5 rounded w-50 flex-column">
        <form>
          <h2 className="text-light pt-3 text-center">Recipe request form</h2>
          <div className="form-group">
            <label htmlFor="input1"></label>
            <textarea
              type="text"
              className="form-control w-75 mx-auto"
              id="input1"
              placeholder="Enter query"
            />
          </div>
          <div className="form-group">
            <label
              className="text-light text-center w-50 ml-3"
              for="exampleFormControlSelect1"
            >
              Select number of recipes to receive
            </label>
            <select
              class="form-control w-75 mx-auto"
              id="exampleFormControlSelect1"
            >
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </div>
        </form>
        <button
          className="btn btn-primary w-25 mx-auto py-2 mb-3"
          type="submit"
          onSubmit={(event) => props.onSubmitHandler(event)}
        >
          Submit
        </button>
      </div>
    </>
  );
};

export default RecipieRequestForm;
