import kue from 'kue';

const queue = kue.createQueue();

const blacklisted = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
  try {
    if (blacklisted.includes(phoneNumber)) {
      throw new Error(`Phone number ${phoneNumber} is blacklisted`);
    }
    const progress = job.progress();
    if (progress === 0.5) {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      setTimeout(()=> {
        done();  
      }, 1000);
    }
  } catch (error) {
    console.error(error.message);
    done(error);
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running ...');
