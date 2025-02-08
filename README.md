# Rubber Band Muscle Simulator

An interactive React component that simulates and visualizes the behavior of rubber bands in different arrangements (series, parallel, and combined) and compares them to muscle responses.

![Rubber Band Simulator Preview](https://api.placeholder.com/800/400)

## Features

- Interactive drag interface to simulate pulling forces
- Three different rubber band arrangements:
  - Series
  - Parallel
  - Combined (both series and parallel)
- Real-time force and length measurements
- Muscle response comparisons for each arrangement
- Responsive design with clean UI

## Live Demo

```jsx
import React, { useState, useEffect } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const RubberBandSimulator = () => {
  const [pulling, setPulling] = useState(false);
  const [arrangement, setArrangement] = useState('series');
  const [stretch, setStretch] = useState(0);
  
  // Preview of key simulation logic
  const getForce = (arrangement, stretch) => {
    switch(arrangement) {
      case 'series':
        return stretch * 0.5; // Lower force, higher displacement
      case 'parallel':
        return stretch * 2; // Higher force, lower displacement
      case 'both':
        return stretch * 1; // Balanced response
      default:
        return stretch;
    }
  };

  // ... rest of the component code
};
```

## Installation

1. Install the required dependencies:
```bash
npm install @/components/ui
```

2. Copy the component into your project:
```bash
src/
  components/
    RubberBandSimulator.jsx
```

3. Import and use the component:
```jsx
import RubberBandSimulator from './components/RubberBandSimulator';

function App() {
  return (
    <div>
      <RubberBandSimulator />
    </div>
  );
}
```

## Usage

The simulator provides an interactive interface where users can:

1. Select the rubber band arrangement using the buttons:
   - Series
   - Parallel
   - Both (Combined)

2. Click and drag to simulate pulling the rubber bands

3. Observe:
   - Real-time force measurements
   - Length changes
   - Comparative analysis with muscle behavior

## Technical Details

- Built with React 18+
- Uses React Hooks for state management
- Styled with Tailwind CSS
- Components from shadcn/ui library
- No external physics engines required

## Educational Value

The simulator helps understand:
- Force-length relationships in elastic materials
- Parallel vs series force transmission
- Muscle biomechanics principles
- Basic physics of elastic elements
