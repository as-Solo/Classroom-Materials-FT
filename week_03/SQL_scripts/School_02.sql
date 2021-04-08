ALTER TABLE participant
ADD FOREIGN KEY(company)
REFERENCES client_(client_id)
ON DELETE SET NULL; #ON DELETE CASCADE lo haría, pero recorriendo cualquier tabla con relación