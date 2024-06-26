/* eslint-disable max-params */
/* eslint-disable no-magic-numbers */
/* eslint-disable one-var */
import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = [
'4153518780',
'4153518781'
];

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track initial progress
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail job with an error
    // eslint-disable-next-line newline-after-var
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
    done(error);
  } else {
    // Update progress to 50%
    job.progress(50, 100);
    // Log notification message
    console.log(`Sending notification to ${phoneNumber
        }, with message: ${message}`);
    // Simulate job completion
    setTimeout(() => {
      done();
    }, 1000);
    // Simulating a 1-second job processing time
  }
};

// Create a Kue queue with concurrency of 2
const queue = kue.createQueue({
  'concurrency': 2
});

// Process jobs in the 'push_notification_code_2' queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from the job
  const {phoneNumber, message} = job.data;

  // Call sendNotification function with job data
  sendNotification(phoneNumber, message, job, done);
});
