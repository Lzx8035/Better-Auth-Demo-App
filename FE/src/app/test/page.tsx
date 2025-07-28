"use client";

import { useState } from "react";

export default function TestPage() {
  const [result, setResult] = useState<string>("");

  const testFlaskAPI = async () => {
    try {
      console.log("测试Flask API...");
      const response = await fetch("http://127.0.0.1:5000", {
        credentials: "include",
        mode: "cors",
      });
      console.log(response);
      console.log("响应状态:", response.status);
      console.log("响应头:", response.headers);

      if (response.ok) {
        const data = await response.json();
        setResult(JSON.stringify(data, null, 2));
        console.log("Flask响应:", data);
      } else {
        setResult(`错误: ${response.status} ${response.statusText}`);
      }
    } catch (error) {
      setResult(`网络错误: ${error}`);
      console.error("网络错误:", error);
    }
  };

  const testLoginAPI = async () => {
    try {
      console.log("测试登录API...");
      const response = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: "lea@example.com",
          password: "123456",
        }),
        credentials: "include",
        mode: "cors",
      });

      console.log("登录响应状态:", response.status);
      console.log("登录响应头:", response.headers);

      if (response.ok) {
        const data = await response.json();
        setResult(JSON.stringify(data, null, 2));
      } else {
        const errorText = await response.text();
        setResult(`登录错误: ${response.status} - ${errorText}`);
      }
    } catch (error) {
      setResult(`登录网络错误: ${error}`);
      console.error("登录网络错误:", error);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">API 测试页面</h1>

      <div className="space-y-4">
        <button
          type="button"
          onClick={testFlaskAPI}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          测试Flask健康检查
        </button>

        <button
          type="button"
          onClick={testLoginAPI}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          测试登录API
        </button>
      </div>

      {result && (
        <div className="mt-4">
          <h2 className="font-bold">结果:</h2>
          <pre className="bg-gray-100 text-black p-4 rounded mt-2 whitespace-pre-wrap">
            {result}
          </pre>
        </div>
      )}
    </div>
  );
}
