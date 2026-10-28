class TimeSlot:
    def __init__(self, date_time):
        self.date_time = date_time
        self.is_available = True

class AppointmentRequest:
    def __init__(self, patient, slot):
        self.patient = patient
        self.slot = slot
        self.status = "Pending"  # Pending, Accepted, Declined

class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.upcoming_appointments = []

    def book_appointment(self, slot, N=5):
        # Alternative Flow: Maximum Appointment Limit Reached (N = 5)
        if len(self.upcoming_appointments) >= N:
            print(f"[Alternative Flow] Booking failed for {self.name}: Maximum limit of {N} upcoming appointments reached.")
            return False
        
        if not slot.is_available:
            print(f"[Error] Slot {slot.date_time} is not available.")
            return False

        # Main Flow: Create appointment request
        request = AppointmentRequest(self, slot)
        self.upcoming_appointments.append(request)
        slot.is_available = False
        print(f"[Main Flow] Request submitted for {self.name} at {slot.date_time}. Status: {request.status}")
        return True

class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name
        self.schedule = []

    def add_slot(self, slot):
        self.schedule.append(slot)

    def respond_to_request(self, request, accept=True):
        if accept:
            request.status = "Accepted"
            print(f"[UC3] Doctor {self.name} ACCEPTED the appointment request for {request.patient.name}.")
        else:
            request.status = "Declined"
            request.patient.upcoming_appointments.remove(request) # Free up slot & limit if declined
            request.slot.is_available = True
            print(f"[UC3] Doctor {self.name} DECLINED the appointment request for {request.patient.name}.")

# --- Program Execution Simulation ---
if __name__ == "__main__":
    print("=== Clinic Appointment System Simulation (N = 5) ===\n")
    
    doctor = Doctor("D1", "Dr. Ahmed")
    
    # Create 6 slots for testing
    slots = [
        TimeSlot("2026-11-01 10:00 AM"),
        TimeSlot("2026-11-01 11:00 AM"),
        TimeSlot("2026-11-02 02:00 PM"),
        TimeSlot("2026-11-03 09:00 AM"),
        TimeSlot("2026-11-04 10:00 AM"),
        TimeSlot("2026-11-05 11:00 AM")
    ]
    
    for s in slots:
        doctor.add_slot(s)

    patient = Patient("P1", "Nour Ahmed")

    print("--- 1. Booking up to N = 5 appointments ---")
    for i in range(5):
        patient.book_appointment(slots[i], N=5)

    print("\n--- 2. Attempting to book the 6th appointment (Triggering Alternative Flow) ---")
    patient.book_appointment(slots[5], N=5)

    print("\n--- 3. Doctor Responding to an Appointment Request ---")
    pending_request = patient.upcoming_appointments[0]
    doctor.respond_to_request(pending_request, accept=True)
    
    print("\nSimulation completed successfully.")
