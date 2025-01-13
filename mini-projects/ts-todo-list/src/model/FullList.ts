import ListItem from "./ListItem";

interface List {
    list: ListItem[];
    load(): void;
    save(): void;
    clearList(): void;
    addItem(itemObj: ListItem): void;
    removeItem(id: string): void;
}

export default class FullList implements List {

    constructor(
        private _list: ListItem[] = []
    ){}
    
    get list():ListItem[] {
        return this._list;
    }

    load(): void {
        
    }

    save(): void {
        
    }

    clearList(): void {
        this._list = [];
    }

    addItem(itemObj: ListItem): void {
        this._list.push(itemObj);
    }

    removeItem(id: string): void {
        let found:boolean = false;

        for(let i = 0; i < this._list.length; i++){

            if (found) { this._list[i-1] = this.list[i]; }

            if (this._list[i].id === id) { found = true; }
        }
    }
}
