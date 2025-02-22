// App.tsx
import React, { useState } from 'react';
import Sidebar from './components/Sidebar/Sidebar';
import Calendar from './components/Caldendar/Calendar';
import PortfolioAnalysis from './components/PortfolioAnalysis/PortfolioAnalysis';
import './App.css';
import { Provider } from 'react-redux';
import { store } from './redux/store';

const App: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState<Date>(new Date());
  const [positions, setPositions] = useState<{ id: number; name: string }[]>([]);

  return (
    <Provider store={store}>
      <div className="app">
          <Sidebar
            positions={positions}
        />
        <div className="main-content" style={{ display: 'flex', gap: '16px' }}>
          <Calendar />
          <PortfolioAnalysis date={selectedDate} />
        </div>
      </div>
    </Provider>
  );
};

export default App;