import React from 'react';
import Todo from './Todo';

function Header() {
    let ever_clicked = false;

    function showInput() {
        if (ever_clicked) {
            // return (
            //     <Todo />
            // );
            console.log("Ever clicked");
        } else {
            ever_clicked = true;
            // return (
            //     <input type="text"/>
            // );
            console.log("First click");
        }
    }

    return (
        <header className="header-page">
            <div className="title-header">
                <h1>TO-DOs App</h1>
            </div>
            <div className="add-todo">
                <button className="create-todo" onClick={showInput}>+</button>
            </div>
        </header>
    );
}

export default Header;