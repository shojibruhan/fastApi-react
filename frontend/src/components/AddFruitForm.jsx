import { useState } from "react";

const AddFruitForm = ({ addFruit }) => {
  const [fruitsName, setFruitsName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (fruitsName) {
      addFruit(fruitsName);
      setFruitsName("");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={fruitsName}
        onChange={(e) => {
          setFruitsName(e.target.value);
        }}
        placeholder="Enter Fruit Name"
      />
      <button type="submit">Add Fruit Name</button>
    </form>
  );
};

export default AddFruitForm;
