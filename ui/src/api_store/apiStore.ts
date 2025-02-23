import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export interface StockPurchase {
  ticker: string;
  quantity: number;
  total_purchase_price: number;
  purchase_date: string;
}

export interface Position extends StockPurchase {
  id: string;
}

export class APIStore {
  private constructor() {}

  static async fetchPositions(): Promise<Position[]> {
    try {
      const response = await axios.get<Position[]>(`${API_BASE_URL}/positions`);
      return response.data;
    } catch (error) {
      console.error("Error fetching positions:", error);
      throw error;
    }
  }

  static async createPosition(data: StockPurchase): Promise<Position> {
    try {
      const response = await axios.post<Position>(`${API_BASE_URL}/positions`, data);
      return response.data;
    } catch (error) {
      console.error("Error creating position:", error);
      throw error;
    }
  }

  static async updatePosition(data: Position): Promise<Position> {
    try {
      const { id, ...updateData } = data;
      await axios.put(`${API_BASE_URL}/positions/${id}`, updateData);
      return data;
    } catch (error) {
      console.error("Error updating position:", error);
      throw error;
    }
  }

  static async deletePosition(id: string): Promise<void> {
    try {
      await axios.delete(`${API_BASE_URL}/positions/${id}`);
    } catch (error) {
      console.error("Error deleting position:", error);
      throw error;
    }
  }
}