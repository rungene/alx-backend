import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  }
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();  
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()  
  });
  it('display a error message if jobs is not an array', () => {
    try {
      createPushNotificationsJobs({phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'}, queue);
    } catch (error) {
      expect(error.message).to.equal('Jobs is not an array');
    }
  });
  it('create two new jobs to the queue', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'});
    expect(queue.testMode.jobs[1].data).to.eql({phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account'});
  });
});
