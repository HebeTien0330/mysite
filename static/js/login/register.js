/**
 * @Author: tangchengqin
 * @Date: 2024/11/25 17:10:58
 * @LastEditors: tangchengqin
 * @LastEditTime: 2024/11/25 17:10:58
 * Description: 
 * Copyright: Copyright (©) 2024 Clarify. All rights reserved.
 */
function getInput() {
    let username = null;
    let password = null;
    let checkCode = null;
    $(".login_txtbx").each(function() {
        if ($(this).attr("placeholder") == "账号") {
            username = $(this).val();
        } else if ($(this).attr("placeholder") == "密码") {
            password = $(this).val();
        } else if ($(this).attr("placeholder") == "验证码") {
            checkCode = $(this).val();
        }
    });
    return { username, password, checkCode };
}


function register() {
    const { username, password, checkCode } = getInput();
    if (!canRegister(username, password, checkCode)) {
        alert("账号/密码/验证码错误，反正肯定有东西错了！");
        return;
    }
    network.request("login/register/", "post", { username, password }).then(res => {
        if (res.data.code == 200) {
            window.location.href = `${network.BASE_URL}login/`;
            return;
        } else if (res.data.code == 500) {
            alert(res.msg);
        }
    })
}

function canRegister(username, password, checkCode) {
    if (!validUsername(username)) {
        return false;
    }
    if (!validPassword(password)) {
        return false;
    }
    if (!validCheckCode(checkCode)) {
        return false;
    }
    return true;
}

function validUsername(username) {
    if (username.length < 6 || username.length > 10) {
        return false;
    }
    if (!isAlphanumeric(username)) {
        return false;
    }
    return true;
}

function validPassword(password) {
    if (password.length < 6 || password.length > 20) {
        return false;
    }
    if (!isAlphanumeric(password)) {
        return false;
    }
    return true;
}

function validCheckCode(checkCode) {
    if (checkCode != code) {
        return false;
    }
    return true;
}

function verifyCode() {
    const { checkCode } = getInput();
    if (!validCheckCode(checkCode)) {
        alert("验证码错误");
        return;
    }
    alert("验证码正确");
}

function isAlphanumeric(str) {
    // 正则表达式匹配数字和字母
    const regex = /^[a-zA-Z0-9]+$/;
    return regex.test(str);
}