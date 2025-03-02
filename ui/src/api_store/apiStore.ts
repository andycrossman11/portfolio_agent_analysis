import axios from "axios";
import { Console } from "console";

const API_BASE_URL = "http://localhost:8000";

export interface StockPurchase {
  ticker: string;
  quantity: number;
  purchase_share_price: number;
  purchase_date: string;
}

export interface Position extends StockPurchase {
  id: string;
}

export interface Analysis {
  llm_summary: string;
  analysis_date: string
}

export const createEmptyPosition = (): Position => {
  const today = new Date();
  const formattedDate = `${today.getMonth() + 1}-${today.getDate()}-${today.getFullYear()}`;
  return {
    id: "",
    ticker: "",
    quantity: 0,
    purchase_share_price: 0,
    purchase_date: formattedDate,
  };
};

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
      console.log(JSON.stringify(data));
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
      console.log(updateData);
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

  static async getAllAnalysis(): Promise<Analysis[]> {
    try {
      const response = await axios.get(`${API_BASE_URL}/analysis`)
      return response.data
    } catch (error) {
      console.error("Error getting analysis:", error)
      throw error
    }
  }
}