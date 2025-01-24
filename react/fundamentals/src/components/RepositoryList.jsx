import { useEffect, useState } from "react";
import "../styles/global.scss";
import "../styles/repositories.scss";
import RepositoryItem from "./RepositoryItem";


export function RepositoryList() {
  const [repositories, setRepositories] = useState([]);

  useEffect(() => {
    fetch("https://api.github.com/users/ODCS1/repos")
      .then((response) => response.json())
      .then((data) => setRepositories(data));
  }, []);

  return (
    <section className="repository-list">
      <h1>Repository List</h1>

      <ul>
        {repositories.map(repository => {
            return <RepositoryItem key={repository.name} repository={repository} />
        })}
      </ul>
    </section>
  );
}
