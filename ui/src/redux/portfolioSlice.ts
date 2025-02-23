import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit';
import { Position, StockPurchase, APIStore } from '../api_store/apiStore';
import { Build } from '@mui/icons-material';

interface PortfolioState {
  isLoading: boolean;
  error: string | null;
  positions: Position[];
}

const initialState: PortfolioState = {
  isLoading: false,
  error: null,
  positions: [],
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

const portfolioSlice = createSlice({
  name: 'portfolio',
  initialState,
  reducers: {},
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
    });
  }
});

export default portfolioSlice.reducer;