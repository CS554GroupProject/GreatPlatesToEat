/* eslint-disable no-restricted-globals */
import React, { createContext, useState, useEffect, useContext } from 'react';

interface UserItemsContextType {
  userItems: any[]; // Adjust the type according to your data structure
  updateUserItems: (item: any) => void; // Adjust the type according to your needs
  deleteUserItem: (key: number) => void;
}

const defaultContextValue: UserItemsContextType = {
  userItems: [],
  updateUserItems: () => {},
  deleteUserItem: () => {},
};

interface UserItemsType {
  key: number;
  userName: string;
  desc: string;
  list: [];
}

export const UserItemsContext =
  createContext<UserItemsContextType>(defaultContextValue);

export const useUserItems = () => {
  return useContext(UserItemsContext);
};

type Props = {
  children: string | JSX.Element | JSX.Element[];
};

export const UserItemsProvider = ({ children }: Props) => {
  // Corrected to functional component syntax
  // State to hold the user-specific data
  // Initialize state from local storage if available
  const [userItems, setUserItems] = useState(() => {
    const localData = localStorage.getItem('userRecipes');
    return localData ? JSON.parse(localData) : [];
  });

  // Function to update the data
  const updateUserItems = (item: UserItemsType) => {
    setUserItems((prevItems: [UserItemsType]) => [...prevItems, item]);
  };

  // Function to delete an item by its key
  const deleteUserItem = (key: number) => {
    console.log('delete called');
    console.log('itemsWeGot: ', userItems);
    console.log('Key we are using to check for: ', key);
    setUserItems((prevItems: [UserItemsType]) =>
      prevItems.filter((item: UserItemsType) => item.key !== key)
    );
  };

  // UseEffect to store data in local storage when userItems changes
  useEffect(() => {
    localStorage.setItem('userRecipes', JSON.stringify(userItems));
  }, [userItems]);

  return (
    <UserItemsContext.Provider
      value={{ userItems, updateUserItems, deleteUserItem }}
    >
      {children}
    </UserItemsContext.Provider>
  );
};
