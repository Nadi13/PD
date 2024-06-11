import Main from "./components/Screen1/Main/Main"
import { BrowserRouter } from "react-router-dom";
import { Routes, Route } from "react-router-dom";
import Main2 from "./components/Screen2/Main2";
import { ScrollRestoration } from "react-router-dom";
import ScrollToTop from './ScrollToBottom.tsx'
import Login from '../src/components/Avtorization/Avtorization.tsx'

function App() {
  return (
    <>
      <BrowserRouter>
        <ScrollToTop />
        <Routes>
            <Route path="/log" element={<Login />} />
            <Route path="/" element={<Main />} />
            <Route path="/LabInfo" element={<Main2 />} />
          </Routes>
      </BrowserRouter>
    </>
  
  )
}

export default App
