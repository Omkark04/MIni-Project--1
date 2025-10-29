import Navbar from "../components/Navabar";
import Rform from "../components/Rform";
import "../styles/home.css";

function Home () {
    return (
        <div className="home">
            <Navbar/>
            <div className="padding"></div>
            <div className="dashboard">
                <Rform/>
            </div>
        </div>
    )
}

export default Home;