function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  } else {
    jobs.forEach((jobData) => {
      const job = queue.create('push_notification_code_3', jobData);
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
      job.on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      });
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
      job.save((err) => {
        if (err) {
          console.error(`Error creating job: ${err}`);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }
      });
    });
  }
}

module.exports = createPushNotificationsJobs;
