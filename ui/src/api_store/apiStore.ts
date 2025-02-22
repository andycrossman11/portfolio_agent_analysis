import { ApiStoreInterface } from './apiStoreInterface';

export class ApiStoreImpl implements ApiStoreInterface {
  async getPositions(): Promise<string[]> {
    // Return dummy data for positions
    return Promise.resolve(['Position 1', 'Position 2', 'Position 3']);
  }

  async getPortfolioAnalysis(): Promise<string> {
    // Return dummy data for portfolio analysis
    return Promise.resolve('This is a dummy portfolio analysis.');
  }
}