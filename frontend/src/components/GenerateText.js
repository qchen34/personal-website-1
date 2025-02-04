import React, { useState } from 'react';
import axios from 'axios';
import './GenerateText.css'; // Import the CSS file for styling

const GenerateText = () => {
  const [generatedText2000, setGeneratedText2000] = useState('');
  const [generatedText4000, setGeneratedText4000] = useState('');
  const [generatedText8000, setGeneratedText8000] = useState('');

  const handleSubmit = async (e, model, setGeneratedText) => {
    e.preventDefault();
    try {
      const response = await axios.post('https://api.chenqiwei.org/generate', { model });
      console.log('Response from backend:', response.data);
      if (response.data.error) {
        console.error('Backend error:', response.data.error);
        setGeneratedText(`Error: ${response.data.error}`);
      } else {
        setGeneratedText(response.data.generated_text);
      }
    } catch (error) {
      console.error('Request error:', error);
      console.error('Error response:', error.response?.data);
      setGeneratedText(`Error: ${error.response?.data?.error || error.message}`);
    }
  };

  const handleClear = (setGeneratedText) => {
    setGeneratedText('');
  };

  return (
    <div className="container">
      <div className="card">
        <h1>Generate Text</h1>
        <p>This model is trained on Shakespeare's text dataset.</p>
        <div className="model-block">
          <h2>Model with 2000 Iterations</h2>
          <form onSubmit={(e) => handleSubmit(e, 'out-shakespeare-char-2000', setGeneratedText2000)}>
            <button type="submit">Generate</button>
            <button type="button" onClick={() => handleClear(setGeneratedText2000)}>Clear</button>
          </form>
          {generatedText2000 && (
            <div className="output">
              <h2>Generated Text</h2>
              <p>{generatedText2000}</p>
            </div>
          )}
        </div>
        <div className="model-block">
          <h2>Model with 4000 Iterations</h2>
          <form onSubmit={(e) => handleSubmit(e, 'out-shakespeare-char-4000', setGeneratedText4000)}>
            <button type="submit">Generate</button>
            <button type="button" onClick={() => handleClear(setGeneratedText4000)}>Clear</button>
          </form>
          {generatedText4000 && (
            <div className="output">
              <h2>Generated Text</h2>
              <p>{generatedText4000}</p>
            </div>
          )}
        </div>
        <div className="model-block">
          <h2>Model with 8000 Iterations</h2>
          <form onSubmit={(e) => handleSubmit(e, 'out-shakespeare-char-8000', setGeneratedText8000)}>
            <button type="submit">Generate</button>
            <button type="button" onClick={() => handleClear(setGeneratedText8000)}>Clear</button>
          </form>
          {generatedText8000 && (
            <div className="output">
              <h2>Generated Text</h2>
              <p>{generatedText8000}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default GenerateText;