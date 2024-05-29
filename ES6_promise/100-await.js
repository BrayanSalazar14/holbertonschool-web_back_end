import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
    const data = {}
    try {
        data.photo = await uploadPhoto()
        data.user = await createUser()
    }
    catch {
        data.photo = null
        data.photo = null
    }
    return data
    // return {
    //     photo: await uploadPhoto(),
    //     user: await createUser()
    // }
}