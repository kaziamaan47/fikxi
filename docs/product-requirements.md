# Fikxi - Product Requirements Document

## Version

v0.1.0

## Product Summary

Fikxi is a multilingual local services marketplace for Mumbai that connects customers with verified skilled workers.

Customers can post service jobs with their budget, location, preferred time, and job details. Workers can browse nearby jobs, bid or negotiate, accept bookings, complete jobs, and receive payment after customer confirmation.

Fikxi supports English, Hindi, and Marathi to make the platform accessible for customers and workers who may not be comfortable with English-heavy applications.

---

## Target Users

### 1. Customers

Customers are people who need local services completed from home or nearby locations.

Examples:
- AC repair
- Electrician work
- Plumbing
- Home repairs
- Courier delivery
- Car repair
- Car service

### 2. Workers

Workers are skilled or semi-skilled service providers.

Examples:
- AC technicians
- Electricians
- Plumbers
- Delivery workers
- Mechanics
- Home repair workers

### 3. Companies

Companies may need multiple verified workers for larger jobs, events, maintenance, delivery, or temporary labour.

### 4. Admin Team

Admins manage platform safety, worker verification, disputes, jobs, users, and payments.

---

## Core Problem

Customers often struggle to find trusted local workers quickly.

Workers often struggle to find consistent work, negotiate fair prices, and access customers directly.

Many existing digital platforms are not designed for workers who prefer Hindi, Marathi, voice-based guidance, or simple interfaces.

---

## Product Goals

1. Help customers post local service jobs easily.
2. Help workers find suitable jobs nearby.
3. Allow price negotiation between customers and workers.
4. Build trust through worker verification.
5. Support English, Hindi, and Marathi.
6. Provide clear scheduling for upcoming jobs.
7. Track job progress from posting to completion.
8. Support secure payment flow through Fikxi.

---

## MVP Scope

The first version of Fikxi will include:

### Customer Features

- Customer registration
- Customer login
- Create a job post
- Add job category
- Add job title and description
- Add location
- Add preferred date and time
- Add budget
- View posted jobs
- View worker bids
- Accept a worker bid
- Track job status
- Mark job as completed
- Rate and review worker

### Worker Features

- Worker registration
- Worker login
- Create worker profile
- Select skills/categories
- View available jobs
- View job details
- Submit bid
- Accept scheduled booking
- View upcoming jobs
- Track earnings placeholder
- View verification status

### Admin Features

- View all users
- View all workers
- View worker verification status
- Approve or reject worker verification
- View all jobs
- View job disputes placeholder

### Language Features

- English interface
- Hindi interface
- Marathi interface
- Language switcher

---

## Out of Scope for MVP

These features will not be built in the first version:

- Real payment gateway integration
- Real Aadhaar verification
- Real-time chat
- Mobile app
- Voice assistant
- AI job matching
- Company bulk hiring portal
- Background check integration
- SMS/WhatsApp notifications

These can be added after the core platform works.

---

## Main Job Flow

### Step 1: Customer Posts Job

Customer creates a job with:

- Category
- Title
- Description
- Location
- Budget
- Preferred date
- Preferred time

### Step 2: Workers Browse Jobs

Workers see available jobs based on category and location.

### Step 3: Worker Sends Bid

Worker can submit:

- Proposed price
- Message to customer
- Available date and time

### Step 4: Customer Accepts Bid

Customer reviews worker profile and accepts one bid.

### Step 5: Job Gets Scheduled

The job becomes scheduled with:

- Customer
- Worker
- Date
- Time
- Agreed price

### Step 6: Worker Completes Job

Worker marks job as completed.

### Step 7: Customer Confirms Completion

Customer confirms satisfaction and rates the worker.

### Step 8: Payment Status Updates

For MVP, payment will be tracked as a status only.

Example statuses:

- Pending
- Held by Fikxi
- Released to worker
- Refunded

---

## Job Statuses

A job can have the following statuses:

1. Open
2. Bidding
3. Scheduled
4. In Progress
5. Completed
6. Cancelled
7. Disputed

---

## Worker Verification Statuses

A worker can have the following verification statuses:

1. Not Submitted
2. Pending Review
3. Verified
4. Rejected
5. Suspended

---

## Payment Statuses

A payment can have the following statuses:

1. Not Started
2. Pending
3. Held
4. Released
5. Refunded
6. Failed

---

## Initial Service Categories

1. AC Repair and Service
2. Electrician
3. Plumbing
4. Home Repair
5. Courier and Local Delivery
6. Car Repair
7. Car Service

---
---

## Customer Job Posting Experience

The first valuable action after login is posting a job.

The customer home screen should focus on one primary action:

**Post a Job**

The job posting process should be completed in under 60 seconds.

Fikxi will use a step-by-step wizard instead of one long form.

### Job Posting Wizard

1. Choose service category
2. Choose subcategory
3. Describe the problem
4. Add photos
5. Choose preferred date and time
6. Add budget or request quotations
7. Review and post job

### Design Principle

The customer should never need technical knowledge to request a service.


## Success Criteria for MVP

The MVP is successful if:

1. A customer can create an account.
2. A worker can create an account.
3. A customer can post a job.
4. A worker can view available jobs.
5. A worker can bid on a job.
6. A customer can accept a bid.
7. The job can move through statuses.
8. The customer can rate the worker.
9. Admin can view users, workers, and jobs.
10. The interface supports English, Hindi, and Marathi.