from time import perf_counter


# Represents an appointment time slot
class TimeSlot:
    def __init__(self, date_time):
        self.date_time = date_time
        self.is_available = True


# Represents a patient's appointment request
class AppointmentRequest:
    def __init__(self, patient, slot):
        self.patient = patient
        self.slot = slot
        self.status = "Pending"


# Represents a patient's medical record
class MedicalRecord:
    def __init__(self, patient, medical_data):
        self.patient = patient
        self.medical_data = medical_data


# Represents a patient
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.upcoming_appointments = []

    # R2 and R4: Request an appointment within the limit
    def book_appointment(self, slot, N=5):

        # Check the maximum number of upcoming appointments
        if len(self.upcoming_appointments) >= N:
            print(
                f"[Alternative Flow] Booking failed for {self.name}: "
                f"Maximum limit of {N} upcoming appointments reached."
            )
            return None

        # Check whether the selected slot is available
        if not slot.is_available:
            print(
                f"[Error] Slot {slot.date_time} is not available."
            )
            return None

        # Create the appointment request
        request = AppointmentRequest(self, slot)

        self.upcoming_appointments.append(request)
        slot.is_available = False

        print(
            f"[UC2] Appointment request submitted for {self.name} "
            f"at {slot.date_time}. Status: {request.status}"
        )

        return request


# Represents a doctor
class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name
        self.schedule = []

    # Add an available time slot to the doctor's schedule
    def add_slot(self, slot):
        self.schedule.append(slot)

    # R1 and R6: Display available appointment times
    def view_available_slots(self):
        start_time = perf_counter()

        available_slots = [
            slot for slot in self.schedule
            if slot.is_available
        ]

        print(f"\nAvailable slots for Dr. {self.name}:")

        if available_slots:
            for slot in available_slots:
                print(slot.date_time)
        else:
            print("No available slots.")

        elapsed_time = perf_counter() - start_time

        print(f"Display time: {elapsed_time:.6f} seconds")

        if elapsed_time <= 2:
            print("[R6] Availability displayed within 2 seconds.")
        else:
            print("[R6] Performance requirement was not met.")

        return available_slots

    # R3: Accept or decline an appointment request
    def respond_to_request(self, request, accept=True):

        # Make sure the request belongs to this doctor's schedule
        if request.slot not in self.schedule:
            print("[Error] This request does not belong to this doctor.")
            return False

        # A request can only be processed once
        if request.status != "Pending":
            print("[Error] This request has already been processed.")
            return False

        if accept:
            request.status = "Accepted"

            print(
                f"[UC3] Dr. {self.name} ACCEPTED the appointment "
                f"request for {request.patient.name}."
            )

        else:
            request.status = "Declined"

            # Remove the declined request from upcoming appointments
            request.patient.upcoming_appointments.remove(request)

            # Make the time slot available again
            request.slot.is_available = True

            print(
                f"[UC3] Dr. {self.name} DECLINED the appointment "
                f"request for {request.patient.name}."
            )

        return True

    # R5: Only authorized staff can access medical data
    def view_medical_record(self, medical_record):
        print(
            f"[R5] Access granted to Dr. {self.name}. "
            f"Medical record for {medical_record.patient.name}: "
            f"{medical_record.medical_data}"
        )


# Main program
if __name__ == "__main__":

    N = 5

    print("=== Clinic Appointment System ===")
    print(f"Maximum upcoming appointments per patient: {N}")

    # Create a doctor
    doctor = Doctor("D1", "Ahmed")

    # Create six appointment slots
    slots = [
        TimeSlot("2026-11-01 10:00 AM"),
        TimeSlot("2026-11-01 11:00 AM"),
        TimeSlot("2026-11-02 02:00 PM"),
        TimeSlot("2026-11-03 09:00 AM"),
        TimeSlot("2026-11-04 10:00 AM"),
        TimeSlot("2026-11-05 11:00 AM")
    ]

    # Add slots to the doctor's schedule
    for slot in slots:
        doctor.add_slot(slot)

    # Create a patient
    patient = Patient("P1", "Nour Ahmed")

    # R1 and R6: View available appointment slots
    print("\n--- UC1: View Doctor Availability ---")
    doctor.view_available_slots()

    # R2 and R4: Book five appointments
    print("\n--- UC2: Book Five Appointments ---")

    for i in range(N):
        patient.book_appointment(slots[i], N)

    # Test the alternative flow
    print("\n--- Alternative Flow: Attempt to Book a Sixth Appointment ---")

    patient.book_appointment(slots[5], N)

    # R3: Doctor accepts the first request
    print("\n--- UC3: Doctor Accepts a Request ---")

    first_request = patient.upcoming_appointments[0]

    doctor.respond_to_request(first_request, accept=True)

    # R3: Doctor declines the second request
    print("\n--- UC3: Doctor Declines a Request ---")

    second_request = patient.upcoming_appointments[1]

    doctor.respond_to_request(second_request, accept=False)

    # Check that the declined slot is available again
    print("\n--- Checking Availability After Declining ---")

    doctor.view_available_slots()

    # R5: Demonstrate access to medical data by the doctor
    print("\n--- R5: Medical Data Access ---")

    medical_record = MedicalRecord(
        patient,
        "Sample medical data"
    )

    doctor.view_medical_record(medical_record)

    print("\nSimulation completed.")