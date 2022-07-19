export default class Currency {
    constructor(code, name) {
        if(typeof(code) != "string" || typeof(name) != "string") {
            TypeError("need to be a string")
        }
        this._code = code
        this._name = name
    }
    displayFullCurrency() {
        return `${this._name} (${this._code})`
    }
}