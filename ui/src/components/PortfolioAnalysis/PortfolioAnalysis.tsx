import React from 'react';
import { Card, Typography } from '@mui/material';
import ReactMarkdown from 'react-markdown';
import { Box } from '@mui/system';

interface PortfolioAnalysisProps {
  analysis: string
}

const PortfolioAnalysis: React.FC<PortfolioAnalysisProps> = ({ analysis }) => {
  return (
    <Card sx={{ p: 4, backgroundColor: "#eae0f0", borderRadius: 3, width: '90%', maxHeight: '100%', overflowY: 'auto' }}>
      <Typography variant="h5" sx={{ fontWeight: "bold", mb: 2 }}>
        Portfolio Analysis
      </Typography>
      <Box sx={{ color: "#665" }}>
        <ReactMarkdown>
          {analysis}
        </ReactMarkdown>
      </Box>
    </Card>
  );
};

export default PortfolioAnalysis;