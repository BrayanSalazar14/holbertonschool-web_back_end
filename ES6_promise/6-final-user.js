import signUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUser(firstName, lastName), uploadPhoto(fileName)])
    .then((promise) => promise.map((result) => ({ status: result.status, value: result.status === 'fulfilled' ? result.value : `${result.reason}` })));
}
