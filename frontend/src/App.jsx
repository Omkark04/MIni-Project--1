import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import ProtectedRoute from "./components/ProtectedRoutes";
import JobListPage from "./components/JobList";
import ScrapePage from "./pages/ScrapePage";
import Rform from "./components/Rform";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/logout" element={<Navigate to="/login" />} />
        <Route path="*" element={<NotFound />} />
        <Route path="/jobs" element={<JobListPage />} />
        <Route path="/scrape" element={<ScrapePage />} />
        <Route path="/rform" element={<Rform />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;