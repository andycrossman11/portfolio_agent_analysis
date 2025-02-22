import React from 'react';
import { Card, Typography } from '@mui/material';

interface PortfolioAnalysisProps {
  date: Date;
}

const PortfolioAnalysis: React.FC<PortfolioAnalysisProps> = ({ date }) => {
  return (
    <Card sx={{ p: 4, backgroundColor: "#eae0f0", borderRadius: 3, width: '90%' }}>
      <Typography variant="h5" sx={{ fontWeight: "bold", mb: 2 }}>
        Portfolio Analysis
      </Typography>
      <Typography variant="body2" sx={{ color: "#665" }}>
        A dialog is a type of modal window that appears in front of app content to provide critical information, or prompt for a decision to be made.
      </Typography>
    </Card>
  );
};

export default PortfolioAnalysis;