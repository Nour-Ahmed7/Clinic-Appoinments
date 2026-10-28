
# 2. Use Cases

## Actors

- **Patient:** Views a doctor's available days and times and requests an appointment.
- **Doctor:** Accepts or declines appointment requests.

## UC1: View Doctor Availability

- **Primary Actor:** Patient
- **Related Requirement:** R1
- **Precondition:** The system has the doctor's availability schedule.

### Main Flow

1. The Patient selects a Doctor.
2. The system retrieves the selected Doctor's available days and times.
3. The system displays the available appointment slots.

- **Postcondition:** The Patient can review the available slots.
- **Constraint:** Available appointment times must be displayed within 2 seconds (R6).

## UC2: Book Appointment

- **Primary Actor:** Patient
- **Related Requirements:** R2, R4
- **Preconditions:**
  - The Patient has selected an available time slot.
  - The Patient has fewer than N upcoming appointments.

### Main Flow

1. The Patient selects an available time slot.
2. The system checks the number of the Patient's upcoming appointments.
3. The system creates an appointment request for the selected slot.
4. The system informs the Patient that the request has been submitted and is awaiting the Doctor's decision.

### Alternative Flow: Maximum Appointment Limit Reached

1. At step 2, the system finds that the Patient already has N upcoming appointments.
2. The system does not create another appointment request.
3. The system informs the Patient that the maximum number of upcoming appointments has been reached.

- **Postcondition:** A request is created only if the Patient has fewer than N upcoming appointments.
- **Constraint:** N = 5 for this project.

## UC3: Respond to Appointment Request

- **Primary Actor:** Doctor
- **Related Requirement:** R3
- **Precondition:** An appointment request is waiting for the Doctor's decision.

### Main Flow

1. The Doctor views a pending appointment request.
2. The Doctor chooses to accept or decline the request.
3. The system records the Doctor's decision.
4. The system updates the appointment request status.
5. The system makes the result available to the Patient.

- **Postcondition:** The request has an accepted or declined status.

## System-Wide Constraints

- **R5 — Security:** Patient medical data must be accessible only to authorized staff.
- **R6 — Performance:** Available appointment times must be displayed within 2 seconds.
- **R7 — Usability:** The application must be usable on mobile phone screens.