// import { Component, useState, xml, mount, useRef, onMounted, reactive, useEnv } from "@odoo/owl";
const { Component, useState, xml, mount, useRef, onMounted, reactive, useEnv } = owl;  // Q1

(function () {
    console.log("hello owl", owl.__info__.version);
    console.log(owl);
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


// template can be used like this as well
Counter.template = xml /*xml*/`
    <button t-on-click="increment">
        Click Me! [<t t-esc="state.value"/>]
    </button><br/>
    <button t-on-click="decrement">
        Click Me decrement! [<t t-esc="state.de_value"/>]
    </button>`;

mount(Counter, document.body);

// Local store
function useStore () {
    const env = useEnv();
    console.log("useState(env.store): ", useState(env.store));
    return useState(env.store);
}


class TaskList {

    constructor(task) {
        this.tasks = this.tasks || [];
        console.log("this.tasks: ", this.tasks);
        const taskId = this.tasks.map((t) => t.id);
        this.nextId = taskId.length ? Math.max(...taskId) + 1 : 1;
    }

    // nextId = 1;
    // tasks = [];
    
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

// store task
function createTaskStore() {
    const saveTasks = () => localStorage.setItem("todoapp", JSON.stringify(taskStore.tasks));
    const initialTasks = JSON.parse(localStorage.getItem("todoapp") || "[]");
    const taskStore = reactive(new TaskList(initialTasks), saveTasks);
    saveTasks();
    console.log(taskStore);
    return taskStore;
}

// Task Components (sub component)
class Task extends Component {
    static template = xml /* xml*/`
    <div class="task" t-att-class="props.task.isCompleted ? 'done': ''">
        <input type="checkbox" t-att-checked="props.task.isCompleted"
               t-att-id="props.task.id"
               t-on-click="() => store.toggleTask(props.task)" />
        <label t-att-for="props.task.id"><t t-esc="props.task.text" /></label>
        <span class="delete" t-on-click="() => store.deleteTask(props.task)">🗑</span>
    </div>
    `;
    static props = ["task"];  // Q2

    setup() {
        this.store = useStore();
    }
}


// ====================================

class Root extends Component {
    static template = xml /* xml */`
    <div class="todo-app">
        <input placeholder="Enter new Task" t-on-keyup="addTask" t-ref="add-input"/>
        <div class="task-list">
            <t t-foreach="displayedTasks" t-as="task" t-key="task.id">
                <Task task="task" /> <!-- Q3 -->
            </t>
        </div>
        <div class="task-panel" t-if="store.tasks.length">
            <div class="task-counter">
                <t t-esc="displayedTasks.length"/>
                <t t-if="displayedTasks.length lt store.tasks.length"> /
                    <t t-esc="store.tasks.length"/>
                </t>
                task(s)
            </div>
            <div>
                <span t-foreach="['all', 'active', 'completed']" t-as="f" t-key="f"
                      t-att-class="{active: filter.value === f}"
                      t-on-click="() => this.setFilter(f)"
                      t-esc="f"/>
            </div>
        </div>
    </div>
    `;
    static components = { Task };  // whenever we define a sub component, it needs to be added to the static components key of its parent
    
    // nextId = 1;
    // tasks = useState([]);

    setup() {
        const inputRef = useRef("add-input");
        onMounted( () => inputRef.el.focus());
        this.store = useStore();
        this.filter = useState({ value: "all"});
    }

    addTask(e) {
        if (e.keyCode === 13) {
            this.store.addTask(e.target.value);
            e.target.value = ""
        }
    }

    get displayedTasks() {
        const tasks = this.store.tasks;
        switch (this.filter.value) {
            case "active": return tasks.filter(t => !t.isCompleted);
            case "completed": return tasks.filter(t => t.isCompleted)
            case "all": return tasks;
        }
    }

    setFilter(filter) {
        this.filter.value = filter;
    }
}

const env = {
    store: createTaskStore(),
};


mount(Root, document.body, {dev: true, env});
