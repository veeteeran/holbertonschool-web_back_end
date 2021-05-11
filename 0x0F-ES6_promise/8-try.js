export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0')
  }
  try {
    const result = numerator / denominator
  }
  catch (error) {
    console.log(error)
  }

  return result
}