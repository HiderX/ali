async function handleLogin(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const loginData = {
        username: formData.get('username'),
        password: formData.get('password')
    };
    try {
        const response = await fetch('http://122.51.185.92/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginData)
        });
        const result = await response.json();
        if (response.ok && result.token) {
            alert('Login successful');
            // 将 token 存储到 localStorage
            localStorage.setItem('token', result.token);
            window.location.href = './index.html'; // 重定向
        } else {
            handleErrors(result);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
}

async function handleRegister(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const registerData = {
        name: formData.get('name'),
        password: formData.get('password'),
        age: Number(formData.get('age')),
        email: formData.get('email'),
        re_password: formData.get('repassword'),
        agreement: formData.get('agreement') === 'on'
    };
    try {
        const response = await fetch('http://122.51.185.92/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(registerData)
        });
        const result = await response.json();
        if (response.ok && result.msg === 'ok') {
            window.location.href = './login.html';
        } else {
            handleErrors(result.msg);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
}

function handleErrors(result) {
    // 根据需要处理错误消息
    let errorMsg = '';
    if (typeof result === 'string') {
        errorMsg = result;
    } else if (typeof result === 'object' && result.msg) {
        errorMsg = result.msg;
    } else if (typeof result === 'object') {
        errorMsg = Object.entries(result).map(([key, value]) => `${value}`).join('\n');
    } else {
        errorMsg = 'An unknown error occurred';
    }
    alert(`${errorMsg}`);
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('login').addEventListener('submit', handleLogin);
    document.getElementById('register').addEventListener('submit', handleRegister);
});

//点击网页后，播放音乐
function playAudio() {
    var audioPlayer = document.getElementById('audio-player');
    audioPlayer.play();
};

// 获取表单和链接的引用
const loginForm = document.getElementById('login');
const registerForm = document.getElementById('register');
const registerLink = document.getElementById('register_btn');
const loginLink = document.getElementById('login_btn');
const exitLink = document.getElementById('exit');

// 点击"立即注册"链接时切换表单显示状态
registerLink.addEventListener('click', function (event) {
    event.preventDefault(); // 阻止链接默认行为
    loginForm.classList.remove('show');
    registerForm.classList.add('show');
});

// 点击"返回登录界面"链接时切换表单显示状态
loginLink.addEventListener('click', function (event) {
    event.preventDefault(); // 阻止链接默认行为
    registerForm.classList.remove('show');
    loginForm.classList.add('show');
});

exitLink.addEventListener('click', function (event) {
    event.preventDefault();
    registerForm.remove('show');
    loginForm.remove('show');
})
