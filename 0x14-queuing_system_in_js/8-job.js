module.exports = function createPushNotificationsJobs(jobs, queue) {
    if(!Array.isArray(jobs)) { throw Error('Jobs is not an array')}
    jobs.forEach((jobItem) => {
        const job = queue('push_notification_code_3', jobItem).save(() => {
            if( !err ) console.log( `Notification job created: ${job.id}` );
          })
          job.on('completed', () => { console.log('Notification job completed')})
          job.on('failing', () => { console.log('Notification job failed')})
          job.on('progress', (progress) => { console.log(`Notification job JOB_ID ${progress}% complete`)})
    })
}