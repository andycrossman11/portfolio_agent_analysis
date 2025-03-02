import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit';
import { Position, StockPurchase, Analysis, APIStore } from '../api_store/apiStore';

interface PortfolioState {
  isLoading: boolean;
  error: string | null;
  positions: Position[];
  editingIndex: number;
  swipeIndex: number;
  analyses: Analysis[];
}

const initialState: PortfolioState = {
  isLoading: false,
  error: null,
  positions: [],
  editingIndex: -1, 
  swipeIndex: -1,
  analyses: []
};

export const fetchPositions = createAsyncThunk('portfolio/fetchPositions', async () => {
    return await APIStore.fetchPositions();
});

export const createPosition = createAsyncThunk("positions/createPosition", async (data: StockPurchase) => {
  return await APIStore.createPosition(data);
});

export const updatePosition = createAsyncThunk("positions/updatePosition", async (data: Position) => {
  return await APIStore.updatePosition(data);
});

export const deletePosition = createAsyncThunk("positions/deletePosition", async (id: string) => {
  await APIStore.deletePosition(id);
  return id;
});

export const fetchAnalyses = createAsyncThunk('analysis/fetchAnalyses', async () => {
  return await APIStore.getAllAnalysis();
});

const portfolioSlice = createSlice({
  name: 'portfolio',
  initialState,
  reducers: {
    setEditingIndex: (state, action: PayloadAction<number>) => {
      state.editingIndex = action.payload;
    },
    setSwipeIndex: (state, action: PayloadAction<number>) => {
      state.swipeIndex = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder.addCase(fetchPositions.pending, (state) => {
      state.isLoading = true;
      state.error = null;
    });
    builder.addCase(fetchPositions.fulfilled, (state, action) => {
      state.isLoading = false;
      state.error = null;
      state.positions = action.payload;
    });
    builder.addCase(fetchPositions.rejected, (state, action) => {
      state.isLoading = false;
      state.error = action.error.message || 'An error occurred.';
    });
    builder.addCase(createPosition.fulfilled, (state, action: PayloadAction<Position>) => {
      state.positions.push(action.payload);
    })
    builder.addCase(updatePosition.fulfilled, (state, action) => {
      const index = state.positions.findIndex((p) => p.id === action.payload.id);
      if (index !== -1) {
        state.positions[index] = { ...state.positions[index], ...action.payload };
      }
    })
    builder.addCase(deletePosition.fulfilled, (state, action: PayloadAction<string>) => {
      state.positions = state.positions.filter((p) => p.id !== action.payload);
    })
    builder.addCase(fetchAnalyses.fulfilled, (state, action) => {
      state.isLoading = false;
      state.error = null;
      state.analyses = action.payload
    });
  }
});

export const { setEditingIndex, setSwipeIndex } = portfolioSlice.actions;

export default portfolioSlice.reducer;