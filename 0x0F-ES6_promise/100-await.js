import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    return {
      'photo': await uploadPhoto(),
      'user': await createUser()
    }
  } catch {
    return {
      'photo': null,
      'user': null
    }
  }
}