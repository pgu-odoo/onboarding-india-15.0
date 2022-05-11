One2many field:
1. here appointment_id is One2many field hence its links between patient and appointment model . so whatever data present in  the appointment model(between same patient_id), its automatically shown in the Appointment page of patient model.
2. whatever you do update delete or create, it links with each other
3. if you have to avoid data linking -- put attr in <tree create='0' delete='0' edit='0'>