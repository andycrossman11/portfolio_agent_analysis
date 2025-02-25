import React, { useState } from 'react';
import Sidebar from './components/Sidebar/Sidebar';
import Calendar from './components/Caldendar/Calendar';
import PortfolioAnalysis from './components/PortfolioAnalysis/PortfolioAnalysis';
import './App.css';
import { Provider } from 'react-redux';
import { store } from './redux/store';
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date>(new Date());

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Provider store={store}>
        <div className="app" style={{ display: 'flex', touchAction: 'pan-y' }}>
          <div style={{ width: '25%' }}>
            <Sidebar />
          </div>
          <div className="main-content" style={{ width: '75%', display: 'flex', gap: '16px', touchAction: 'pan-y', overflowY: 'auto', overflowX: 'hidden', maxHeight: '100vh' }}>
            <Calendar />
            <PortfolioAnalysis date={selectedDate} />
          </div>
        </div>
      </Provider>
    </LocalizationProvider>
  );
};

export default App;