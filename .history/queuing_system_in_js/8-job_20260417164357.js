import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  // Guard clause required by task: jobs must be an array.
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Create one queue job per input payload.
  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  }
}

export default createPushNotificationsJobs;
