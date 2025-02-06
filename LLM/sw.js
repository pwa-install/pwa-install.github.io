importScripts('https://cdn.jsdelivr.net/npm/web-llm'); // 导入 WebLLM

let model;

// 初始化 WebLLM
async function loadLLM() {
  model = await webllm.load_model('TinyLlama');
  console.log('WebLLM 模型加载完成');
}

self.addEventListener('install', (event) => {
  event.waitUntil(loadLLM());
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker 已激活');
});

self.addEventListener('message', async (event) => {
  if (!model) return;

  if (event.data.type === 'query') {
    const response = await model.generate(event.data.text);
    event.source.postMessage({ response });
  }
});
