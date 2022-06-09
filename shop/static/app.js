registry = {};

class Base{
	template = ""
	constructor(parent){
		this.parent = parent;
	}
	render(){
		var parser = new DOMParser();
		var tmpl = parser.parseFromString(this.template, "text/html").body.childNodes;
		this.parent.appendChild(tmpl[0])
	}
	

}