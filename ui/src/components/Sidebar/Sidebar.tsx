// components/Sidebar.tsx
import React from 'react';
import { Drawer, List, ListItem, ListItemText, ListItemIcon, Button, Typography } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

interface SidebarProps {
  positions: { id: number; name: string }[];
}

const Sidebar: React.FC<SidebarProps> = ({ positions }) => {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: 240,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: 240,
          boxSizing: 'border-box',
          backgroundColor: '#f4f4f4',
          padding: 2,
        },
      }}
    >
      <Typography variant="h6" sx={{ mb: 2 }}>
        Positions
      </Typography>
      <List>
        {positions.map((position) => (
          <ListItem key={position.id} sx={{ mb: 1 }}>
            <ListItemText primary={position.name} />
            <ListItemIcon>
              <Button onClick={() => console.log('edit')}><EditIcon /></Button>
              <Button onClick={() => console.log('delete')}><DeleteIcon /></Button>
            </ListItemIcon>
          </ListItem>
        ))}
      </List>
      <Button
        variant="contained"
        color="primary"
        startIcon={<AddIcon />}
        onClick={() => console.log('add')}
        sx={{ mt: 2 }}
      >
        Add Position
      </Button>
    </Drawer>
  );
};

export default Sidebar;