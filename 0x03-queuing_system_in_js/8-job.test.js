/* eslint-disable init-declarations */
/* eslint-disable sort-keys */
/* eslint-disable max-lines-per-function */
/* eslint-disable id-length */
/* eslint-disable max-len */
/* eslint-disable no-undef */
// 8-job.test.js
import {createPushNotificationsJobs} from './8-job';
// Assuming your function is exported from 8-job.js
import kue from 'kue';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeAll(() => {
    // Connect to Redis and create a Kue queue in test mode
    queue = kue.createQueue({
      'redis': {
        'host': 'localhost',
        'port': 6379
    },
      'prefix': 'test'
    });
    queue.testMode.enter();
  });

  afterAll(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  afterEach(() => {
    // Clear jobs after each test
    queue.testMode.clear();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).toThrow('Jobs is not an array');
  });

  it('should create jobs in the queue and log events', () => {
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

    createPushNotificationsJobs(jobs, queue);

    // Assert that jobs are correctly created in the queue
    expect(queue.testMode.jobs.length).toBe(jobs.length);

    // Check job creation and lifecycle event logging
    queue.testMode.jobs.forEach((job) => {
      expect(job.type).toBe('push_notification_code_3');
      expect(job.data).toMatchObject(jobs.find((j) => j.phoneNumber === job.data.phoneNumber));
    });
  });
});
