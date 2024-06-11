import Main from "./components/Screen1/Main/Main"
import { BrowserRouter } from "react-router-dom";
import { Routes, Route } from "react-router-dom";
import Main2 from "./components/Screen2/Main2";
import { useEffect } from 'react';

function App() {
  useEffect(() => {
    const body = document.querySelector('body');
    body.scrollRestoration = 'auto';
  }, []);
  return (
    <>
      <BrowserRouter>
        <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/LabInfo" element={<Main2 />} />
          </Routes>
      </BrowserRouter>
    </>
  
  )
}

export default App
