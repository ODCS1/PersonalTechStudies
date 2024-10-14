import { useState } from "react";

interface ListGroupProp {
  items: string[];
    heading: string;
    onSelectItem: (item: string) => void;
}

function ListGroup({ items, heading, onSelectItem }: ListGroupProp) {
  //   let items = ["São Paulo", "Tokyo", "Paris", "Roma"];

  // Hook
  const [selectedIndex, setSelectedIndex] = useState(-1);
  // VARIABLE (SelectedIndex)

  // Event Handler
  //   const handleClick = (event: MouseEvent) => console.log(event);

  const getMessage = () => {
    return items.length === 0 && <p>No item Found</p>;
  };

  //   items = [];

  return (
    <>
      <h1>{heading}</h1>

      {getMessage()}

      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={() => {
                setSelectedIndex(index);
                onSelectItem(item);
            }}
          >
            {item}
          </li>
        ))}
      </ul>

      <br />
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam velit
        totam maxime laborum officia exercitationem cum suscipit sequi possimus
        vel aut, sunt modi. Blanditiis ipsam, officia facilis nesciunt quo
        quisquam?
      </p>
    </>
  );
}

export default ListGroup;

// import { Fragment } from "react/jsx-runtime";

// function ListGroup() {
//     return (
//         <Fragment>
//             <h1>List</h1>
//             <ul className="list-group">
//                 <li className="list-group-item">An item</li>
//                 <li className="list-group-item">A second item</li>
//                 <li className="list-group-item">A third item</li>
//                 <li className="list-group-item">A fourth item</li>
//                 <li className="list-group-item">And a fifth one</li>
//             </ul>
//         </Fragment>
//     );
// }
