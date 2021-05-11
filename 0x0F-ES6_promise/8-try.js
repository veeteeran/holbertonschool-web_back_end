export default function divideFunction(numerator, denominator) {
  try {
    const result = numerator / denominator
    throw new Error('cannot divide by 0')
  }
  catch (error) {
    console.log(error)
  }

  return result
}