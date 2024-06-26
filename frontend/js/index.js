document.addEventListener("DOMContentLoaded", function () {
    const logoutLink = document.getElementById('logout'); // 获取退出链接
  
    // 退出功能
    function logout(event) {
      event.preventDefault(); // 阻止默认跳转行为
      localStorage.removeItem('token'); // 移除 token
      alert('您已成功退出'); // 显示退出提示（可选）
      // 这里可以添加额外的退出逻辑，例如重定向到登录页面
    }
  
    // 为退出链接添加事件监听器
    logoutLink.addEventListener('click', logout);
  });