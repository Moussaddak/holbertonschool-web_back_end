function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw (new Error('Jobs is not an array'));
    }
    jobs.forEach((jobInfo) => {
        const job = queue.create('push_notification_code_3', jobInfo).save(error => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        });
        job.on('complete', () => console.log(`Notification job ${job.id} completed`));
        job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
        job.on('progress', (percentage) => console.log(`Notification job ${job.id} ${percentage}% complete`));
    });
}

module.exports = createPushNotificationsJobs;
