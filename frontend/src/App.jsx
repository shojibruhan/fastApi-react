import "./App.css";
import Fruits from "./components/Fruits";
const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Fruit Management App</h1>
      </header>
      <main>
        <Fruits />
      </main>
    </div>
  );
};

export default App;
