const { Component, useState, xml, mount, useRef, onMounted, reactive, useEnv } = owl;

(function () {
    console.log("hello owl", owl.__info__.version);
})();

class Counter extends Component {
  
  state = useState({ value: 0, de_value: 100 });
  
  increment() {
	this.state.value++;
  }
  decrement() {
	this.state.de_value--;
  }
}

// Local store
function useStore () {
	const env = useEnv();
	return useState(env.store);
}


// template can be used like this as well
Counter.template = xml /*xml*/`
	<button t-on-click="increment">
		Click Me! [<t t-esc="state.value"/>]
	</button><br/>
	<button t-on-click="decrement">
		Click Me decrement! [<t t-esc="state.de_value"/>]
	</button>`;

mount(Counter, document.body);



// Task Components (sub component)
class Task extends Component {
	static template = xml /* xml*/`
	<div class="task" t-att-class="props.task.isCompleted ? 'done': ''">
		<input type="checkbox" t-att-checked="props.task.isCompleted" t-on-click="toggleTask" />	
		<span><t t-esc="props.task.text" /></span>
		<span class="delete" t-on-click="deleteTask">🗑</span>
	</div>
	`;
	static props = ["task", "onDelete"];

	toggleTask () {
		this.props.task.isCompleted = !this.props.task.isCompleted;
	}

	deleteTask () {
		this.props.onDelete(this.props.task);
	}
}

class TaskList {
	nextId = 1;
	tasks = []

	// add new task
	addTask(text) {
		text = text.trim();
		if (text) {
			const task = {
				id: this.nextId++,
				text: text,
				isCompleted: false,
			};
			this.tasks.push(task)
		}
	}

	// toggle task, when isCompleted is true
	toggleTask(task) {
		task.isCompleted = !task.isCompleted;
	}

	// delete task
	deleteTask(task) {
		const index = this.tasks.findIndex( (t) => t.id === task.id );
		this.tasks.slice(index, 1);
	}
}


// ====================================

class Root extends Component {
	static template = xml /* xml */`
	<div class="todo-app">
		<input placeholder="Enter new Task" t-on-keyup="addTask" t-ref="add-input"/>
		<div class="task-list">
			<t t-foreach="tasks" t-as="task" t-key="task.id">
				<Task task="task" onDelete.bind="deleteTask"/>
			</t>
		</div>
	</div>
	`;
	static components = { Task };  // whenever we define a sub component, it needs to be added to the static components key of its parent
	
	nextId = 1;
	tasks = useState([]);

	addTask(e) {
		if (e.keyCode === 13) {
			const text = e.target.value.trim();
			e.target.value = "";
			if (text) {
				const newTask = {
					id: this.nextId++,
					text: text,
					isCompleted: false,
				};
				this.tasks.push(newTask);
			}
		}
	}

	// deleting task
	deleteTask (task) {
		const index = this.tasks.findIndex( t => t.id === task.id);
		this.tasks.splice(index, 1)
	}

	setup() {
		const inputRef = useRef("add-input");
		onMounted( () => inputRef.el.focus() );
	}
}

mount(Root, document.body, {dev: true});
