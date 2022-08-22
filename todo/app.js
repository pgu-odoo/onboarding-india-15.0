const { Component, useState, xml, mount } = owl;

(function () {
    console.log("hello owl", owl.__info__.version);
})();


// Owl Components
class Root extends Component {
  static template = xml`<div>todo app</div>`;
}

mount(Root, document.body);

class Counter extends Component {
  static template = xml`
    <button t-on-click="increment">
      Click Me! [<t t-esc="state.value"/>]
    </button><br/>
    <button t-on-click="decrement">
      Click Me decrement! [<t t-esc="state.de_value"/>]
    </button>`;

  state = useState({ value: 0, de_value: 100 });

  increment() {
    this.state.value++;
  }
  decrement() {
    this.state.de_value--;
  }
}

mount(Counter, document.body);