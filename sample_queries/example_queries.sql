-- 1. View all donors
SELECT * FROM donor;

-- 2. Find all donors with blood type O+
SELECT * FROM donor
WHERE BloodType = 'O+';

-- 3. Show all donations with donor names
SELECT d.Fname, d.Lname, bd.DonationID, bd.Date, bd.QuantityBlood
FROM donor d
JOIN blooddonation bd ON d.DonorID = bd.DID;

-- 4. Count total donations per donor
SELECT DID, COUNT(*) AS TotalDonations
FROM blooddonation
GROUP BY DID;

-- 5. Show donors and their health conditions
SELECT d.Fname, d.Lname, hc.Health_Condition
FROM donor d
JOIN healthcondition hc ON d.DonorID = hc.DID;

-- 6. Show phlebotomist and the tests they handled
SELECT p.Fname, p.Lname, t.TID
FROM phlebotomist p
JOIN track t ON p.PhlebotomistID = t.PID;

-- 7. List recipients and their medical history
SELECT r.Fname, r.Lname, mh.Medical_History
FROM recipient r
JOIN medicalhistory mh ON r.RecipientID = mh.RID;

-- 8. Show all donation centers and assigned staff
SELECT c.Cname, s.Name, s.Role
FROM blood_donation_center c
JOIN staff s ON c.CenterID = s.CID;
