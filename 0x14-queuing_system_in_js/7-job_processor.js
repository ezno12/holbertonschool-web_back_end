const kue = require('kue')
const queue = kue.createQueue();

const blacklistedPhoneNUmber = [ 4153518780, 4153518781]

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100)
    if (blacklistedPhoneNUmber.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`))
        return
    }
    job.progess(50,100)
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
    done();
}

job.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNum, message } = job.data
    sendNotification(phoneNum, message, job, done)})