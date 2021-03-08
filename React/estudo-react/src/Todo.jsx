import React, {Component} from 'react'

function Todo() {
    function eraseTodo(e) {
        console.log("Delete ToDo");
    }

	return (
		<div className="todo-main">
			<h1>To-Do</h1>
            <h3>2021-02-09 19:35</h3>
			<button className="button-todo" onClick={eraseTodo}>X</button>
		</div>	
	);
}

export default Todo;
