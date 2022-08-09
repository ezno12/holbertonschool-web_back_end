const kue = require('kue')
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}
queue.process('push_notification_code', (job, done) => {
    const { phoneNum, message } = job.data
    sendNotification(phoneNum, message)
    done();
})