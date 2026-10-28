# 2. Use Cases

## Actors

* **Patient:** Can view doctors, check available appointment slots, book appointments, and cancel upcoming appointments.
* **Doctor:** Can view their upcoming appointments.

## UC1: View Doctors

* **Primary Actor:** Patient
* **Precondition:** The system is available.
* **Main Flow:**

  1. The Patient opens the list of doctors.
  2. The system displays the available doctors and their specialties.
* **Postcondition:** The Patient can choose a doctor.

## UC2: View Available Appointment Slots

* **Primary Actor:** Patient
* **Precondition:** The system contains the selected Doctor's schedule.
* **Main Flow:**

  1. The Patient selects a Doctor.
  2. The system retrieves the Doctor's appointment slots.
  3. The system displays the available slots.
* **Postcondition:** The Patient can select an available slot.

## UC3: Book Appointment

* **Primary Actor:** Patient
* **Preconditions:**

  * The selected appointment slot is available.
  * The Patient has fewer than N upcoming appointments.
* **Main Flow:**

  1. The Patient selects an available slot.
  2. The system checks the slot's availability.
  3. The system checks the Patient's number of upcoming appointments.
  4. The system creates the appointment.
  5. The system displays a booking confirmation.
* **Alternative Flow — Slot Is No Longer Available:**

  1. At step 2, the system discovers that another Patient has already booked the slot.
  2. The system does not create the appointment.
  3. The system displays an error message and asks the Patient to choose another slot.
* **Postcondition:** The appointment is created only if all booking conditions are satisfied.

## UC4: Cancel Appointment

* **Primary Actor:** Patient
* **Precondition:** The Patient has an upcoming appointment.
* **Main Flow:**

  1. The Patient selects an upcoming appointment.
  2. The Patient requests cancellation.
  3. The system cancels the appointment.
  4. The system makes the appointment slot available again.
  5. The system displays a cancellation confirmation.
* **Postcondition:** The appointment is cancelled and its slot becomes available.

## UC5: View Upcoming Appointments

* **Primary Actor:** Doctor
* **Precondition:** The Doctor has appointments recorded in the system.
* **Main Flow:**

  1. The Doctor requests to view upcoming appointments.
  2. The system retrieves the Doctor's upcoming appointments.
  3. The system displays the appointments.
* **Postcondition:** The Doctor can review their upcoming appointments.
