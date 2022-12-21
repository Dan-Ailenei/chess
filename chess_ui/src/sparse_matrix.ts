export default class SparseMatrix {
    // Map to store the matrix elements
    private elements: Map<string, string>;
  
    // Number of rows and columns in the matrix
    private rows: number;
    private cols: number;
  
    constructor(rows: number, cols: number) {
      this.elements = new Map();
      this.rows = rows;
      this.cols = cols;
    }
  
    // Set the value of an element at the given row and column
    set(row: number, col: number, value: string) {
      if (row < 0 || row >= this.rows || col < 0 || col >= this.cols) {
        throw new Error("Invalid matrix index");
      }
      this.elements.set(`${row},${col}`, value);
    }
  
    // Get the value of an element at the given row and column
    get(row: number, col: number): string | null {
      if (row < 0 || row >= this.rows || col < 0 || col >= this.cols) {
        throw new Error("Invalid matrix index");
      }
      const value = this.elements.get(`${row},${col}`);
      return value !== undefined ? value : null;
    }
  }
  
  