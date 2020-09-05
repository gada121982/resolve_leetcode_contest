// problen https://leetcode.com/problems/roman-to-integer/
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let queue = []
  let result = 'not result'
  let flag = true



  let string_number = ''
  let so_du = null
  let so_nguyen = x
  let is_smaller_than_0 = false;

  if (so_nguyen < 0) {
    so_nguyen = Math.abs(so_nguyen)
    is_smaller_than_0 = true
  }


  while (flag === true) {
    so_du = so_nguyen % 10
    so_nguyen = Math.floor(so_nguyen / 10)

    queue.push(so_du)

    if (so_nguyen === 0) {
      flag = false
    }
  }


  if (is_smaller_than_0) {
    string_number += '-'
  }

  for (let i = 0; i < queue.length; i++) {
    string_number += queue[i]
  }



  result = parseInt(string_number)

  if (result < Math.pow(-2, 31) || result > Math.pow(2, 31) - 1) {
    return 0
  }

  return result
};
