import React from 'react';

const RecipeCard = (props) => {
  return (
    <div className="card mx-auto w-25 mt-3 d-flex flex-flow-row bg-white rounded border border-primary shadow-lg">
      <div className="card-body">
        <h5 className="card-title text-center">{props.Name}</h5>
        <p className="card-text text-center">{props.desc}</p>
        <p className="card-text text-center">{props.ingredientsList}</p>
      </div>
      {props.onSave !== null ? (
        <button
          type="submit"
          className="btn btn-success mx-auto mb-3"
          onClick={(event) =>
            props.onSave(
              event,
              props.Name,
              props.desc,
              props.ingredientsList,
              props.indexOfCard
            )
          }
        >
          Save
        </button>
      ) : null}
    </div>
  );
};
export default RecipeCard;
