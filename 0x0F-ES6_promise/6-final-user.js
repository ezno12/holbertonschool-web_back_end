import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
  // eslint-disable-next-line consistent-return
    .then((data) => {
      if (data[0] === 'fulfilled') {
        return data;
      }
    })
    .catch((err) => console.log(err));
}
