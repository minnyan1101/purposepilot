export function userIdValidate(userId) {
  const regex = /^[a-zA-Z0-9_]{1,128}$/

  if (userId.match(regex)) {
    return [true, "" ]
  } else {
    return [false, "(a-z, A-Z, 0-9)の英数字と\"_\"アンダーバーのみ入力可能です" ]
  }
} 

export function passwordValidate(password){
  const length = password.length
  if (8 <= length && length <= 128) {
    return [true, "" ]
  } else {
    return [false, "パスワードは8~128文字以内で入力してください" ]
  }
}