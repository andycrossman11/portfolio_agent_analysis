// components/Sidebar.tsx
import React, { useEffect } from 'react';
import { Drawer, List, ListItem, Button, Typography, Divider } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../../redux/store';
import { fetchPositions } from '../../redux/portfolioSlice';
import PositionCard from '../PositionCard/PositionCard';


const Sidebar: React.FC = () => {
  const dispatch: AppDispatch = useDispatch();
  const positions = useSelector((state: RootState) => state.portfolio.positions);

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
            <PositionCard position={position} />
          </ListItem>
          {index < positions.length - 1 && (
            <Divider sx={{ backgroundColor: '#e0e0e0' }} />
          )}
        </React.Fragment>
      ))}
      </List>
      <Button
        variant="contained"
        color="primary"
        startIcon={<AddIcon />}
        onClick={() => console.log('add')}
        sx={{ mt: 2, mr: 2, ml: 2 }}
      >
        Add Position
      </Button>
    </Drawer>
  );
};

export default Sidebar;