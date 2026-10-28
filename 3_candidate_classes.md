# Candidate Classes Identification

Based on the requirements and use cases, candidate classes are identified using Noun-Verb analysis and categorized into Explicit, Inferred, and Rejected classes.

## 1. Explicit Classes
These are classes directly mentioned in the requirements and use cases as domain entities.

* **Patient**
  * **Supporting Evidence:** Mentioned in R1, R2, R4, UC1, UC2. Represents the user who views availability and books appointments.
* **Doctor**
  * **Supporting Evidence:** Mentioned in R1, R3, UC1, UC3. Represents the medical professional who has an availability schedule and accepts/declines requests.
* **Appointment / AppointmentRequest**
  * **Supporting Evidence:** Mentioned in R2, R3, R4, UC2, UC3. Represents the booking request submitted by a patient and managed by a doctor.

## 2. Inferred Classes
These are classes not explicitly named as nouns in a sentence, but logically required to fulfill the functional requirements and system behavior.

* **TimeSlot / AvailabilitySchedule**
  * **Supporting Evidence:** Required by R1 and UC1 ("doctor's available days and times", "available time slot"). Represents specific blocks of time when a doctor can take appointments.
* **AppointmentManager / ClinicSystem**
  * **Supporting Evidence:** Required by R2 and UC2 to check the patient's upcoming appointment count against the limit ($N = 5$).

## 3. Rejected Classes
These are nouns mentioned or implied in the user interface or technical infrastructure descriptions, but excluded from the domain model because they deal with UI or implementation details rather than business logic.

* **Screen / MobileScreen**
  * **Reason for Rejection:** R7 mentions mobile phone screens, which is a UI implementation detail and usability constraint, not a domain business class.
* **Database / SystemStorage**
  * **Reason for Rejection:** Data persistence is an infrastructure concern, handled separately from domain objects.
* **Button / NotificationPopup**
  * **Reason for Rejection:** These are UI components used to inform the user (as in UC2 step 4), not core domain entities.
