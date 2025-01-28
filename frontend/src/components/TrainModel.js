import React, { useState } from 'react';
import axios from 'axios';

const TrainModel = () => {
  const [iters, setIters] = useState(600000);
  const [learningRate, setLearningRate] = useState(6e-4);
  const [status, setStatus] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/train', {
        iters,
        learning_rate: learningRate,
      });
      setStatus(response.data.status);
      setError('');
    } catch (error) {
      console.error('Error:', error);
      setStatus('Error starting training');
      setError(error.response ? error.response.data.error : 'Unknown error');
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          value={iters}
          onChange={(e) => setIters(e.target.value)}
          placeholder="Number of iterations"
        />
        <input
          type="number"
          value={learningRate}
          onChange={(e) => setLearningRate(e.target.value)}
          placeholder="Learning rate"
        />
        <button type="submit">Train</button>
      </form>
      {status && <p>{status}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default TrainModel;