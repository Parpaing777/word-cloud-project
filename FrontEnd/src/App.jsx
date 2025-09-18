import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { NotFound } from "./pages/NotFound";

function App() {


  return (
    <>
      <BrowserRouter>
        <Routes>
          {/* Route for the main page */}
          <Route index element={<Home />} />
          {/* Catch-all route for 404 Not Found */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
