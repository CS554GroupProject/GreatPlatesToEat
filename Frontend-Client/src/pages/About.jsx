import React from 'react';

const About = () => {
  return (
    <div className="d-flex flex-column mt-5 mx-5 shadow-lg w-75 mx-auto">
      <h1 className="text-center my-3 mx-auto">About Us</h1>
      <div className="text-center font-weight-bold bg-white shadow-lg mx-5">
        <p className="my-3">Soft Eng frontend for great plates to eat!</p>
        <div className="mx-auto">
          <p className="mx-3 text-black">Nathan Moes: moes@pdx.edu</p>
          <p className="mx-3 text-black">Nicholas Scalzone</p>
          <p className="mx-3 text-black">Alex Novitchkov-Burbank</p>
          <p className="mx-3 text-black">Jawaher Alsaiari</p>
        </div>
      </div>
    </div>
  );
};

export default About;
