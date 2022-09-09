import "./App.css";
import Favorites from "./components/Favorites";
import Modal from "./components/Modal";
import Contacts from "./components/Contacts";
import Search from "./components/Search";

function App() {
  return (
    <main>
      <Favorites />
      <Modal />
      <Contacts />
      <Search />
    </main>
  );
}

export default App;
