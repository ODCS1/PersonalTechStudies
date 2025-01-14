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

    static instance: FullList = new FullList();

    private constructor(
        private _list: ListItem[] = []
    ){}
    
    get list():ListItem[] {
        return this._list;
    }

    load(): void {
        const storedList: string | null = localStorage.getItem("myList");


        if (typeof storedList !== "string") return;

        const parsedList: { _id: string, _item: string, _checked: boolean }[] = JSON.parse(storedList);

        parsedList.forEach(itemObj => {
            const newListItem = new ListItem(itemObj._id, itemObj._item, itemObj._checked);
            FullList.instance.addItem(newListItem);
        });
        
    }

    save(): void {
        localStorage.setItem("myList", JSON.stringify(this._list));
    }

    clearList(): void {
        this._list = [];
        this.save();
    }

    addItem(itemObj: ListItem): void {
        this._list.push(itemObj);
        this.save();
    }

    removeItem(id: string): void {
        let found:boolean = false;

        for(let i = 0; i < this._list.length; i++){

            if (found) { this._list[i-1] = this.list[i]; }

            if (this._list[i].id === id) { found = true; }
        }
        this._list.pop();

        // OR
        // this._list = this._list.filter(item => item.id !== id);

        this.save();
    }

    existsItemName(newName: string): boolean {
        for (let i = 0; i < this._list.length; i++) {
            let currName:string = this._list[i].item;
            if (currName === newName) {
                return true;
            }
        }

        return false;
    }
}
