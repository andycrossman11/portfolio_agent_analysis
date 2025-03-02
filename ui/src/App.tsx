import React, { useEffect, useState } from 'react';
import Sidebar from './components/Sidebar/Sidebar';
import Calendar from './components/Caldendar/Calendar';
import PortfolioAnalysis from './components/PortfolioAnalysis/PortfolioAnalysis';
import './App.css';
import { useDispatch, useSelector } from 'react-redux';
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { fetchAnalyses } from './redux/portfolioSlice';
import { RootState, AppDispatch } from './redux/store';

const App: React.FC = () => {
  const dispatch: AppDispatch = useDispatch();
  const analyses = useSelector((state: RootState) => state.portfolio.analyses);
  const [selectedAnalysis, setSelectedAnalysis] = useState("");

  useEffect(() => {
    dispatch(fetchAnalyses());
  }, [dispatch]);

  const handleSelectAnalysis = (date: string) => {
    console.log(date);
    setSelectedAnalysis(() => {
      const analysis = analyses.find(a => a.analysis_date === date);
      return analysis ? analysis.llm_summary : `Sorry, no portfolio analysis for ${date}`;
    });
  }

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
        <div className="app" style={{ display: 'flex', touchAction: 'pan-y' }}>
          <div style={{ width: '25%' }}>
            <Sidebar />
          </div>
          <div className="main-content" style={{ width: '75%', display: 'flex', gap: '16px', touchAction: 'pan-y', overflowY: 'auto', overflowX: 'hidden', maxHeight: '100vh' }}>
            <Calendar setSelectedAnalysis={handleSelectAnalysis}/>
            <PortfolioAnalysis analysis={selectedAnalysis} />
          </div>
        </div>
    </LocalizationProvider>
  );
};

export default App;