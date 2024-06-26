/* eslint-disable no-magic-numbers */
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue(),

// Function to send notifications
 sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${
    phoneNumber}, with message: ${message}`);
};

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  // Extract data from the job
  const {phoneNumber, message} = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message);

  // Simulate job processing completion
  setTimeout(() => {
    done();
  }, 1000);
  // Simulating a 1-second job processing time
});
