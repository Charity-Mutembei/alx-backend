/* eslint-disable no-ternary */
/* eslint-disable multiline-ternary */
/* eslint-disable sort-vars */
/* eslint-disable no-magic-numbers */
/* eslint-disable one-var */
/* eslint-disable no-unused-vars */
/* eslint-disable require-await */
/* eslint-disable no-plusplus */
/* eslint-disable max-statements */
import express from 'express';
import kue from 'kue';
import {promisify} from 'util';
import redis from 'redis';


const app = express(),
 port = 1245,

// Redis client setup
 redisClient = redis.createClient(),
 getAsync = promisify(redisClient.get).bind(redisClient),
 setAsync = promisify(redisClient.set).bind(redisClient),

// Function to reserve seats in Redis
 reserveSeat = async (number) => {
  await setAsync('available_seats', number.toString());
},

// Function to get current available seats from Redis
 getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');


return seats ? parseInt(seats, 10) : 0;
};

// Initialize available seats and reservation status
reserveSeat(50);
// Set initial available seats to 50
let reservationEnabled = true;

// Kue setup
const queue = kue.createQueue();

// Route to get number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();

  res.json({numberOfAvailableSeats});
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({'status': 'Reservation are blocked'});

return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({'status': 'Reservation failed'});
    } else {
      res.json({'status': 'Reservation in process'});
    }
  });
});

// Route to process the queue and reserve seats
app.get('/process', async (req, res) => {
  res.json({'status': 'Queue processing'});

  queue.process('reserve_seat', async (job, done) => {
    try {
      let currentSeats = await getCurrentAvailableSeats();

      if (currentSeats === 0) {
        reservationEnabled = false;
        throw new Error('Not enough seats available');
      }

      currentSeats--;
      await reserveSeat(currentSeats);

      if (currentSeats === 0) {
        reservationEnabled = false;
      }

      console.log(`Seat reservation job ${job.id} completed`);
      done();
    } catch (error) {
      console.error(`Seat reservation job ${job.id} failed: ${error.message}`);
      done(error);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
