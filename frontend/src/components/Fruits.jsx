import { useEffect, useState } from "react";
import api from "../api";
import AddFruitForm from "./AddFruitForm";

const Fruits = () => {
  const [fruits, setFruits] = useState([]);

  const fetchFruits = async () => {
    try {
      const response = await api.get("fruits");
      console.log(response.data);
      setFruits(response.data.fruits);
    } catch (err) {
      console.error("Error fetching data: ", err);
    }
  };

  const addFruit = async (fruitsName) => {
    try {
      await api.post("fruits", {
        name: fruitsName,
      });
      fetchFruits();
    } catch (err) {
      console.error("Error Posting fruits name: ", err);
    }
  };

  useEffect(() => {
    fetchFruits();
  }, []);

  return (
    <div>
      <h2>Fruits List</h2>
      <ul>
        {fruits.map((fruit, index) => {
          return <li key={index}>{fruit.name}</li>;
        })}
      </ul>
      <AddFruitForm addFruit={addFruit} />
    </div>
  );
};

export default Fruits;
