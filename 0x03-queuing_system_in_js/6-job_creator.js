import kue from 'kue';

const queue = kue.createQueue();
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code to verify your account',
  },
  {
    phoneNumber: '4153518782',
    message: 'This is the code to verify your account',
  },
];

jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code', jobData);

  job.on('complete', () => {
    console.log(`Notification job: ${job.id} completed`);
  });

  job.on('failed', (error) => {
    console.log(`Notification job ${job.id} failed: ${error}`);
  });

  job.on('progress', (progress) => {
    console.log(`Notification job: ${job.id} ${progress}% complete`);
  });

  job.save((error) => {
    if (error) {
      console.error(`Error creating job: ${error}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });
});

console.log('Job creator is running ...');
