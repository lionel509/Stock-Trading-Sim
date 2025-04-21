import React from 'react';
import {
  ResponsiveContainer,
  ComposedChart,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Line,
  Bar,
} from 'recharts';

export default function CandleChart({ data, trades }) {
  // transform data for Recharts
  const chartData = data.map(d => ({
    time: d.Date,
    open: d.Open,
    high: d.High,
    low: d.Low,
    close: d.Close,
  }));

  return (
    <ResponsiveContainer width="100%" height={400}>
      <ComposedChart data={chartData}>
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <CartesianGrid strokeDasharray="3 3" />
        <Bar dataKey="close" barSize={1} />
        <Line type="monotone" dataKey="high" stroke="#8884d8" dot={false} />
        {/* Render buy/sell markers */}
        {trades.map((t, i) => (
          <Line
            key={i}
            type="monotone"
            dataKey={() => t.price}
            stroke={t.side === 'buy' ? 'green' : 'red'}
            dot={{ r: 4 }}
          />
        ))}
      </ComposedChart>
    </ResponsiveContainer>
  );
}