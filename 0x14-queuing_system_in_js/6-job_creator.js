const kue = require('kue');

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

const queue = kue.createQueue();

let job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`)
    })
    .on('complete', () => console.log('Notification job completed'))
    .on('failed', () => console.log('Notification job failed'));
