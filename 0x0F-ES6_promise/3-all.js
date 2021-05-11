import { uploadPhoto, createUser } from './utils.js'

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto(),
    createUser()
  ])
    .then(messages => {
      messages.forEach(message => console.log(
      message.body, message.firstName, message.lastName
    ))
  })
  .catch(console.log("Signup system offline"))
}
