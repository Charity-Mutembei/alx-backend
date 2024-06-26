/* eslint-disable arrow-parens */
/* eslint-disable sort-keys */
/* eslint-disable one-var */
import kue from 'kue';

// Function to create push notification jobs
const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Process each job in the jobs array
  jobs.forEach(jobData => {
    // Create a job in the 'push_notification_code_3' queue
    const job = queue.create('push_notification_code_3', jobData);

    // Event handlers for job lifecycle
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
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

    // Save the job to the queue
    job.save();
  });
};

// Example usage:
const jobs = [
  {
    'phoneNumber': '4153518780',
    'message': 'Notification 1'
},
  {
    'phoneNumber': '4153518781',
    'message': 'Notification 2'
},
  {
    'phoneNumber': '4153518743',
    'message': 'Notification 3'
}
];

// Create a Kue queue
const queue = kue.createQueue();

// Call createPushNotificationsJobs with jobs array and queue
createPushNotificationsJobs(jobs, queue);
