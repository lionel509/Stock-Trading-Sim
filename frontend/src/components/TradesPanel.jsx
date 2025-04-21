import React from 'react';

export default function TradesPanel({ trades }) {
  return (
    <div className="trades-panel">
      <h3>Trades</h3>
      <ul>
        {trades.map((t, i) => (
          <li key={i}>
            {t.side.toUpperCase()} {t.quantity} @ ${t.price}
          </li>
        ))}
      </ul>
    </div>
  );
}