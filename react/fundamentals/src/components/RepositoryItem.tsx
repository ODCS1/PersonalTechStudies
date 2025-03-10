type RepositoryItemProps = {
  repository: {
    name: string;
    description: string;
    html_url: string;
  };
}

const RepositoryItem = (props: RepositoryItemProps) => {
  return (
    <li>
        <strong>{props.repository.name}</strong>
        <p>{props.repository.description}</p>
        <a rel="external" href={props.repository.html_url}>
            Acess
        </a>
    </li>
  );
};

export default RepositoryItem;
