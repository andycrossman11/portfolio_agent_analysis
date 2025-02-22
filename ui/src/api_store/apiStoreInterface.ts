export interface ApiStoreInterface {
    getPositions(): Promise<string[]>;
    getPortfolioAnalysis(): Promise<string>;
  }