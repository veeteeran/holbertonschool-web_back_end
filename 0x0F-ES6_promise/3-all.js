import { uploadPhoto, createUser } from './utils.js'

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto,
    createUser
  ])
  .then(messages => console.log(messages))
  .catch(console.log("Signup system offline"))
}
