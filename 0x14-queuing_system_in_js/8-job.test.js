const kue = require('kue');
const { expect } = require('chai');
const createPushNotificationsJobs = require('./8-job');

const queue = kue.createQueue();

afterEach(() => {
    queue.testMode.clear();
});

after(() => {
    queue.testMode.exit();
});

test('creates and enqueue jobs with valid data', () => {
    createPushNotificationsJobs([{ num: '06578890678', message: 'This is the code 1234 to verify your account' }], queue);
    expect(queue.testMode.jobs.length).to.eql(1);
    expect(queue.testMode.jobs[0].type).to.eql('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({ num: '06578890678', message: 'This is the code 1234 to verify your account' });
});

test('throw an Error for invalid Data', () => {
    expect(() => {
        createPushNotificationsJobs([], queue);
    }).to.throw('Jobs is not an array');
});
