import React from 'react';
import { Button } from '@shadcn/ui/button';

export default function SimulationControls({ onStart, running }) {
  return (
    <div className="controls">
      <Button onClick={onStart} disabled={running}>
        {running ? 'Running...' : 'Start Simulation'}
      </Button>
    </div>
  );
}