import { uploadPhoto, createUser } from './utils';

export default async function () {
  let obj = {
    photo: null,
    user: null,
  };
  try {
    obj = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
    return obj;
  } catch (error) {
    return obj;
  }
}
