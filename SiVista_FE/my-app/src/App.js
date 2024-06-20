import './App.css';
import LandingPage from './components/landing/LandingPage';
import LoginPage from './components/login/LoginPage';
import {Routes, Route} from 'react-router-dom'
function App() {
  return (
    <>
   <Routes>
    <Route path="/" element={<LoginPage/>}></Route>
    <Route path="/home" element={<LandingPage/>}></Route>
   </Routes>
    </>
  );
}

export default App;
