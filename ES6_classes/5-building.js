export default class Building {
    constructor(sqft) {
      this._sqft = sqft;
  
      // Ensure that subclasses implement evacuationWarningMessage
      if (new.target !== Building && this.evacuationWarningMessage === undefined) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  
    // Getter for sqft
    get sqft() {
      return this._sqft;
    }
  }