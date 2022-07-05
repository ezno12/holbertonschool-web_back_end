import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((resualt) => { console.log(`${resualt[0].body} ${resualt[1].firstName} ${resualt[1].lastName}`); })
    .catch(() => { console.log('Signup system offline'); });
}
