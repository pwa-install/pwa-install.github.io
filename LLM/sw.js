console.log('Service Worker 注册成功');
importScripts('https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm');

let handler;

self.addEventListener('activate', (event) => {
  handler = new ServiceWorkerMLCEngineHandler();
  console.log('Service Worker 已激活');
});

self.addEventListener('message', async (event) => {
  if (!handler) return;

  if (event.data.type === 'query') {
    try {
      const response = await handler.handle(event.data.text);
      event.source.postMessage({ response });
    } catch (error) {
      console.error('WebLLM 处理错误:', error);
      event.source.postMessage({ error: '处理失败' });
    }
  }
});
