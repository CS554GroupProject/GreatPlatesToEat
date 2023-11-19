import React from 'react';

const RecipieRequestForm = (props) => {
  return (
    <>
      <div className="d-flex justify-content-center bg-dark mx-auto mt-5 rounded w-50 flex-column">
        <form
          onSubmit={(event) => {
            props.onSubmit(event);
          }}
          className="d-flex flex-column"
        >
          <h2 className="text-light pt-3 text-center">Recipe request form</h2>
          <div className="form-group">
            <label htmlFor="input1"></label>
            <textarea
              type="text"
              className="form-control w-75 mx-auto"
              id="input1"
              placeholder="Enter query"
              onChange={(event) => props.query(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="input2"></label>
            <textarea
              type="text"
              className="form-control w-75 mx-auto"
              id="input2"
              placeholder="Restrictions?"
              onChange={(event) => props.restrictions(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label
              className="text-light text-center w-50 ml-4 pl-4 mb-4"
              htmlFor="exampleFormControlSelect1"
            >
              Select number of recipes to receive
            </label>
            <select
              className="form-control w-75 mx-auto"
              id="exampleFormControlSelect1"
              onChange={(event) => props.recipesCount(event.target.value)}
            >
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </div>
          <button
            className="btn btn-primary mx-auto py-2 mb-3"
            type="submit"
            disabled={props.disabled}
          >
            Submit
          </button>
          <div>
            {props.disabled ? (
              <p className="text-center text-white">
                Please Login before submitting a request
              </p>
            ) : null}
          </div>
        </form>
      </div>
    </>
  );
};

export default RecipieRequestForm;
