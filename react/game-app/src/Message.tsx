// tsx is used typescript to react components

// PascalCasing
function Message() {
    // JSX: JavaScript XML

    const name = 'Nambia';
    const m1 =
        <div id="message">
            <h1>Hello {name}!</h1>
        </div>
    
    const m2 =
        <div id="message">
            <h1>Hello World!</h1>
        </div>
    

    if (name) {
        return m1;
    }

    return m2;
}

export default Message;