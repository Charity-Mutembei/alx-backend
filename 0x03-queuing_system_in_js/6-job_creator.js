/* eslint-disable no-shadow */
/* eslint-disable no-magic-numbers */
/* eslint-disable sort-keys */
/* eslint-disable sort-vars */
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue(),

// Sample data for the job
 jobData = {
  'phoneNumber': '1234567890',
  'message': 'This is a test notification message'
},

// Create a job in the queue
 job = queue.create('push_notification_code', jobData);

// Event handlers for job lifecycle
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (err) {
    console.error('Error creating job:', err);
  } else {
    // Start processing the job
    queue.process('push_notification_code', (job, done) => {
      // Simulate job processing time
      setTimeout(() => {
        console.log(`Sending notification to ${
            job.data.phoneNumber}: ${job.data.message}`);
        done();
      }, 3000);
      // Simulating a 3-second job processing time
    });
  }
});
