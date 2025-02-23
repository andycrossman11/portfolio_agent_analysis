import React, { useState } from 'react';
import Sidebar from './components/Sidebar/Sidebar';
import Calendar from './components/Caldendar/Calendar';
import PortfolioAnalysis from './components/PortfolioAnalysis/PortfolioAnalysis';
import './App.css';
import { Provider } from 'react-redux';
import { store } from './redux/store';

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date>(new Date());

  return (
    <Provider store={store}>
      <div className="app" style={{ display: 'flex' }}>
        <div style={{ width: '25%' }}>
          <Sidebar />
        </div>
        <div className="main-content" style={{ width: '75%', display: 'flex', gap: '16px' }}>
          <Calendar />
          <PortfolioAnalysis date={selectedDate} />
        </div>
      </div>
    </Provider>
  );
};

export default App;