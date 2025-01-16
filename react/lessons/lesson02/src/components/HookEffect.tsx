import "../index.css";
import { useState, useEffect } from "react";

// Type for API Response
interface ApiResponse {
  data: string;
}

const HookEffect = () => {
  // STATE TO LOAD WITHOUT TYPE ANOTATION
  const [data, setData] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);


  // EXAMPLE 1: FETCHING DATA FROM AN API USING useEffect
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://api.example.com/data");
        const result: ApiResponse = await response.json();
        setData(result.data);
      } catch (error) {
        console.error("ERROR FETCHING DATA:", error);
        setData("ERROR FETCHING DATA FROM API (EXAMPLE)");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
    // EMPTY DEPENDENCY ARRAY ENSURES THIS EFFECT RUNS ONLY ONCE WHEN THE COMPONENT MOUNTS.
  }, []);


  // EXAMPLE 2: SUBSCRIBING TO AN EVENT (E.G., WINDOW RESIZE)
  useEffect(() => {
    const handleResize: EventListener = () => {
      console.log("Window resized!");
    };

    // ADD EVENT LISTENER
    window.addEventListener("resize", handleResize);

    
    // CLEANUP FUNCTION TO REMOVE THE EVENT LISTENER ON COMPONENT UNMOUNT
    return () => {
      window.removeEventListener("resize", handleResize);
    };

    // THIS EFFECT RUNS ONCE ON MOUNT AND CLEANS UP ON UNMOUNT.
  }, []);


  // EXAMPLE 3: COMPONENT mount/unmount (SIMILAR TO componentDidMount/componentWillUnmount)
  useEffect(() => {
    console.log("Component mounted");

    // CLEANUP FUNCTION (THIS IS CALLED WHEN THE COMPONENT UNMOUNTS)
    return () => {
      console.log("Component unmounted");
    };
  }, []);

  return (
    <div style={{
        marginBottom: "30px",
        borderBottom: "5px solid black",
        padding: "20px",
        textAlign: "center",
      }}>
      <h2>useEffect Hook Examples</h2>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <p>Data: {data}</p>
        </div>
      )}
    </div>
  );
};

export default HookEffect;
