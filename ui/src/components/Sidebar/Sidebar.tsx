// components/Sidebar.tsx
import React, { useEffect, useState } from 'react';
import { Drawer, List, ListItem, Button, Typography, Divider } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../../redux/store';
import { fetchPositions, createPosition, updatePosition, setEditingIndex, setSwipeIndex } from '../../redux/portfolioSlice';
import PositionCard from '../PositionCard/PositionCard';
import UpdateCard from '../UpdateCard/UpdateCard';
import { createEmptyPosition, Position, StockPurchase } from '../../api_store/apiStore';


const Sidebar: React.FC = () => {
  const dispatch: AppDispatch = useDispatch();
  const positions = useSelector((state: RootState) => state.portfolio.positions);
  const editIndex = useSelector((state: RootState) => state.portfolio.editingIndex);

  const handleAddPosition = (position: Position) => {
    const { id, ...rest } = position;
    const newPurchase: StockPurchase = { ...rest } as StockPurchase;
    dispatch(createPosition(newPurchase));
  };

  const handleUpdatePosition = (position: Position) => {
    dispatch(updatePosition(position));
  };

  useEffect(() => {
    dispatch(fetchPositions());
  }
  , []);

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: '25%',
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: '25%',
          boxSizing: 'border-box',
          backgroundColor: '#f4f4f4'
        },
      }}
    >
      <Typography variant="h6" sx={{ mb: 2 , mt:1, ml:2}}>
        Positions
      </Typography>
      <List sx={{ width: '100%' }}>
      {positions.map((position, index) => (
        <React.Fragment key={position.id}>
          <ListItem sx={{ padding: 0, paddingTop: 0, paddingBottom: 0, width: "100%" }}>
            {editIndex === index ? (
              <UpdateCard position={position} updatePosition={handleUpdatePosition}/>
                ) : (
              <PositionCard position={position} index={index}/>
            )}
          </ListItem>
          {index < positions.length - 1 && (
            <Divider sx={{ backgroundColor: '#e0e0e0' }} />
          )}
        </React.Fragment>
      ))}
      </List>
      {editIndex === positions.length 
        ? 
          <UpdateCard position={createEmptyPosition()} updatePosition={handleAddPosition} />
        :
          <Button
            variant="contained"
            color="primary"
            startIcon={<AddIcon />}
            onClick={() => {dispatch(setSwipeIndex(-1)); dispatch(setEditingIndex(positions.length));}}
            sx={{ mt: 2, mr: 2, ml: 2 }}
          >
            Add Position
          </Button>
      }
    </Drawer>
  );
};

export default Sidebar;