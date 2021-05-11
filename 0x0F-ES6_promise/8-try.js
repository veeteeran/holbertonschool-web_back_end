export default function divideFunction(numerator, denominator) {
  let result = 0;
  try {
    if (denominator === 0) {
      throw new Error('cannot divide by 0')
    }
    result = numerator / denominator
  }
  catch (error) {
    console.log(error)
  }

  return result
}