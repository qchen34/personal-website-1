import React, { useState } from 'react';
import axios from 'axios';
import './GenerateText.css'; // Import the CSS file for styling

const GenerateText = () => {
  const [generatedText, setGeneratedText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5001/generate', {});
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

  const handleClear = () => {
    setGeneratedText('');
  };

  return (
    <div className="container">
      <div className="card">
        <h1>Generate Text</h1>
        <p>This model is trained on Shakespeare's text dataset. With 2000 iterations. </p>
        <form onSubmit={handleSubmit}>
          <button type="submit">Generate</button>
          <button type="button" onClick={handleClear}>Clear</button>
        </form>
        {generatedText && (
          <div className="output">
            <h2>Generated Text</h2>
            <p>{generatedText}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default GenerateText;