import React from 'react';

const RecipeCard = (props: {
  ingredientsList: [];
  Name: string;
  desc: string;
  onSave: Function;
  onDelete: Function;
  key: number;
}) => {
  return (
    <div className="card mx-auto w-25 mt-3 d-flex flex-flow-row bg-white rounded border border-primary shadow-lg mb-3">
      <div className="card-body">
        <h5 className="card-title text-center">{props.Name}</h5>
        <p className="card-text text-center">{props.desc}</p>
        {props.ingredientsList.map((item: any) => {
          return (
            <p className="card-text text-center" key={item}>
              {item}
            </p>
          );
        })}
      </div>
      {props.onSave !== null ? (
        <button
          type="submit"
          className="btn btn-success mx-auto mb-3"
          onClick={(event) =>
            props.onSave(
              props.Name,
              props.desc,
              props.ingredientsList,
              props.key
            )
          }
        >
          Save
        </button>
      ) : null}
      {props.onDelete !== null ? (
        <button
          type="submit"
          className="btn btn-danger mx-auto mb-3"
          onClick={(event) => props.onDelete(props.key)}
        >
          Delete
        </button>
      ) : null}
    </div>
  );
};
export default RecipeCard;
