import React, { useState } from 'react';
import axios from 'axios';

const GenerateText = () => {
  const [start, setStart] = useState('');
  const [numSamples, setNumSamples] = useState(10);
  const [maxNewTokens, setMaxNewTokens] = useState(50);
  const [temperature, setTemperature] = useState(1.0);
  const [topK, setTopK] = useState(null);
  const [generatedText, setGeneratedText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/generate', {
        start,
        num_samples: numSamples,
        max_new_tokens: maxNewTokens,
        temperature,
        top_k: topK,
      });
      setGeneratedText(response.data.generated_text);
    } catch (error) {
      console.error('Error:', error);
      setGeneratedText('Error generating text');
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={start}
          onChange={(e) => setStart(e.target.value)}
          placeholder="Enter start text"
        />
        <input
          type="number"
          value={numSamples}
          onChange={(e) => setNumSamples(e.target.value)}
          placeholder="Number of samples"
        />
        <input
          type="number"
          value={maxNewTokens}
          onChange={(e) => setMaxNewTokens(e.target.value)}
          placeholder="Max new tokens"
        />
        <input
          type="number"
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
          placeholder="Temperature"
        />
        <input
          type="number"
          value={topK}
          onChange={(e) => setTopK(e.target.value)}
          placeholder="Top K"
        />
        <button type="submit">Generate</button>
      </form>
      {generatedText && <p>{generatedText}</p>}
    </div>
  );
};

export default GenerateText;