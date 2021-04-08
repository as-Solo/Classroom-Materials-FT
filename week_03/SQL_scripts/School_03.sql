ALTER TABLE participant
ADD FOREIGN KEY(company)
REFERENCES client_(client_id)
ON DELETE SET NULL;