import React, { createContext, useState, useEffect, useContext } from 'react';

export const UserItemsContext = createContext();

export const useUserItems = () => {
  return useContext(UserItemsContext);
};

export const UserItemsProvider = ({ children }) => {
  // State to hold the user-specific data
  // Initialize state from local storage if available
  const [userItems, setUserItems] = useState(() => {
    const localData = localStorage.getItem('userRecipes');
    return localData ? JSON.parse(localData) : [];
  });

  // Function to update the data
  const updateUserItems = (item) => {
    setUserItems((prevItems) => [...prevItems, item]);
  };

  // UseEffect to store data in local storage when userItems changes
  useEffect(() => {
    localStorage.setItem('userRecipes', JSON.stringify(userItems));
  }, [userItems]);

  return (
    <UserItemsContext.Provider value={{ userItems, updateUserItems }}>
      {children}
    </UserItemsContext.Provider>
  );
};
