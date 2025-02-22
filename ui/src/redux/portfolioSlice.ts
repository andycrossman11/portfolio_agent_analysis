// portfolioSlice.ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface PortfolioState {
  positions: string[];
}

const initialState: PortfolioState = {
  positions: [],
};

const portfolioSlice = createSlice({
  name: 'portfolio',
  initialState,
  reducers: {
    addPosition: (state, action: PayloadAction<string>) => {
      state.positions.push(action.payload);
    },
    removePosition: (state, action: PayloadAction<string>) => {
      state.positions = state.positions.filter(position => position !== action.payload);
    },
    updatePosition: (state, action: PayloadAction<{ index: number; position: string }>) => {
      const { index, position } = action.payload;
      if (index >= 0 && index < state.positions.length) {
        state.positions[index] = position;
      }
    },
  },
});

export const { addPosition, removePosition, updatePosition } = portfolioSlice.actions;
export default portfolioSlice.reducer;