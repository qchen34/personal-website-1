import React, { useState } from 'react';
import axios from 'axios';
import './GenerateText.css'; // Import the CSS file for styling

// 根据环境设置 API 基础 URL
const API_BASE_URL = process.env.NODE_ENV === 'development' 
  ? 'http://localhost:5001'
  : 'https://api.chenqiwei.org';

const GenerateText = () => {
  const [generatedTexts, setGeneratedTexts] = useState({});
  const [isLoading, setIsLoading] = useState({});

  const handleGenerate = async (model) => {
    setIsLoading(prev => ({ ...prev, [model]: true }));
    try {
      // 确保传递正确的模型路径
      console.log("Sending request for model:", model); // 添加日志
      const response = await axios.post(`${API_BASE_URL}/generate`, {
        model: model  // 例如: "out-shakespeare-char-2000"
      });
      
      console.log("Response:", response.data); // 添加日志
      
      setGeneratedTexts(prev => ({
        ...prev,
        [model]: response.data.generated_text || response.data.error
      }));
    } catch (error) {
      console.error('Error:', error);
      setGeneratedTexts(prev => ({
        ...prev,
        [model]: `Error: ${error.message}`
      }));
    } finally {
      setIsLoading(prev => ({ ...prev, [model]: false }));
    }
  };

  const handleClear = (model) => {
    setGeneratedTexts(prev => {
      const newTexts = { ...prev };
      delete newTexts[model];
      return newTexts;
    });
  };

  const models = [
    {
      section: "Shakespeare Text Generator",
      description: "This model is trained on Shakespeare's text dataset.",
      variants: [
        { 
          title: "Model with 2000 Iterations", 
          id: "out-shakespeare-char-2000"  // 确保这个ID与实际目录名称匹配
        },
        { 
          title: "Model with 4000 Iterations", 
          id: "out-shakespeare-char-4000"
        },
        { 
          title: "Model with 8000 Iterations", 
          id: "out-shakespeare-char-8000"
        }
      ]
    },
    {
      section: "Jordan Peterson Text Generator",
      description: "This model is trained on Jordan Peterson's lectures and writings.",
      variants: [
        { 
          title: "Model with 2000 Iterations", 
          id: "out-peterson-char-2000"
        },
        { 
          title: "Model with 4000 Iterations", 
          id: "out-peterson-char-4000"
        },
        { 
          title: "Model with 8000 Iterations", 
          id: "out-peterson-char-8000"
        }
      ]
    }
  ];

  return (
    <div className="container">
      {models.map((modelSection, index) => (
        <div key={index} className="section">
          <h1>{modelSection.section}</h1>
          <p>{modelSection.description}</p>
          <div className="models-grid">
            {modelSection.variants.map((variant) => (
              <div key={variant.id} className="model-block">
                <h2>{variant.title}</h2>
                <div className="button-container">
                  <button
                    className="generate-btn"
                    onClick={() => handleGenerate(variant.id)}
                    disabled={isLoading[variant.id]}
                  >
                    {isLoading[variant.id] ? 'Generating...' : 'Generate'}
                  </button>
                  <button
                    className="clear-btn"
                    onClick={() => handleClear(variant.id)}
                    disabled={!generatedTexts[variant.id]}
                  >
                    Clear
                  </button>
                </div>
                {generatedTexts[variant.id] && (
                  <div className="output">
                    <h3>Generated Text:</h3>
                    <p>{generatedTexts[variant.id]}</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default GenerateText;