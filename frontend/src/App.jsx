import React, { useState, useEffect } from 'react';
import CandleChart from './components/CandleChart';
import SimulationControls from './components/SimulationControls';
import TradesPanel from './components/TradesPanel';
import Panel from './components/Panel';
import { getCandles, startSimulation } from './api/api';

export default function App() {
  const [candles, setCandles] = useState([]);
  const [trades, setTrades] = useState([]);
  const [running, setRunning] = useState(false);

  const fetchCandles = async () => {
    const data = await getCandles('AAPL', '1m');
    setCandles(data);
  };

  useEffect(() => {
    fetchCandles();
    const interval = setInterval(fetchCandles, 60000);
    return () => clearInterval(interval);
  }, []);

  const handleStart = async () => {
    setRunning(true);
    const result = await startSimulation();
    setTrades(result.trades);
    setRunning(false);
  };

  return (
    <div className="app-container">
      <Panel>
        <CandleChart data={candles} trades={trades} />
      </Panel>
      <Panel>
        <SimulationControls onStart={handleStart} running={running} />
        <TradesPanel trades={trades} />
      </Panel>
    </div>
  );
}