import React from "react";

const RepositoryItem = (props) => {
  return (
    <li>
        <strong>{props.repository?.name ?? "Default"}</strong>
        <p>{props.repository?.description ?? "Description"}</p>
        <a rel="external" href={props.repository?.html_url ?? "#"}>
            Acess
        </a>
    </li>
  );
};

export default RepositoryItem;
