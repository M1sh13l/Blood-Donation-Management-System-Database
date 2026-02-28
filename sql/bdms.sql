-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2024 at 08:49 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bdms`
--

-- --------------------------------------------------------

--
-- Table structure for table `bloodcondition`
--

CREATE TABLE `bloodcondition` (
  `TID` varchar(15) NOT NULL,
  `BloodCondition` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bloodcondition`
--

INSERT INTO `bloodcondition` (`TID`, `BloodCondition`) VALUES
('T00200', 'bloodclot'),
('T00200', 'leukemia'),
('T00100', 'Safe'),
('T00300', 'Flu');

-- --------------------------------------------------------

--
-- Table structure for table `blooddonation`
--

CREATE TABLE `blooddonation` (
  `DonationID` varchar(15) NOT NULL,
  `Start_Time` varchar(10) DEFAULT NULL,
  `End_Time` varchar(10) DEFAULT NULL,
  `QuantityBlood` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `DID` varchar(15) DEFAULT NULL,
  `CID` varchar(15) DEFAULT NULL,
  `TID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blooddonation`
--

INSERT INTO `blooddonation` (`DonationID`, `Start_Time`, `End_Time`, `QuantityBlood`, `Date`, `DID`, `CID`, `TID`) VALUES
('D100100', '9:30 am', '10:00 am', 420, '2024-05-05', 'D0000001', 'C1000', 'T00100'),
('D200200', '12:45 pm', '1:30 pm', 350, '2023-06-12', 'D0000003', 'C3000', 'T00200'),
('D300300', '11:15 am', '12:30 pm', 400, '2023-12-26', 'D0000003', 'C1000', 'T00400'),
('D400400', '1:30 pm', '2:00 pm', 370, '2023-10-24', 'D0000002', 'C2000', 'T00300');

-- --------------------------------------------------------

--
-- Table structure for table `bloodtest`
--

CREATE TABLE `bloodtest` (
  `TestID` varchar(15) NOT NULL,
  `Date` date NOT NULL,
  `BloodType` varchar(3) NOT NULL,
  `DID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bloodtest`
--

INSERT INTO `bloodtest` (`TestID`, `Date`, `BloodType`, `DID`) VALUES
('T00100', '2024-05-01', 'O+', 'D0000001'),
('T00200', '2023-12-31', 'AB+', 'D0000003'),
('T00300', '2023-10-20', 'A-', 'D0000002'),
('T00400', '2023-06-17', 'AB+', 'D0000003');

-- --------------------------------------------------------

--
-- Table structure for table `blood_donation_center`
--

CREATE TABLE `blood_donation_center` (
  `CenterID` varchar(15) NOT NULL,
  `Cname` varchar(50) NOT NULL,
  `Location` varchar(100) NOT NULL,
  `DID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blood_donation_center`
--

INSERT INTO `blood_donation_center` (`CenterID`, `Cname`, `Location`, `DID`) VALUES
('C1000', 'Central Blood Bank', 'Ulaishah, Riyadh 12746', 'D0000001'),
('C2000', 'JHAH Blood Bank', 'Gharb Al Dhahran, Dhahran 34465', 'D0000002'),
('C3000', 'Blood Bank King Faisal Specialist Hospital', 'Al-Rawda, Jeddah 23433', 'D0000003');

-- --------------------------------------------------------

--
-- Table structure for table `donor`
--

CREATE TABLE `donor` (
  `DonorID` varchar(15) NOT NULL,
  `Fname` varchar(50) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `DOB` date NOT NULL,
  `BloodType` varchar(3) NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Donation_History` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donor`
--

INSERT INTO `donor` (`DonorID`, `Fname`, `Lname`, `Gender`, `DOB`, `BloodType`, `Address`, `PhoneNumber`, `Email`, `Donation_History`) VALUES
('D0000001', 'Mashael', 'Saeed', 'F', '2005-12-26', 'O+', 'Al-Rawda', '0546312456', 'mmsaeed@effat.edu.sa', 'None'),
('D0000002', 'Samir', 'Hamid', 'M', '1999-01-03', 'A-', 'Abhor', '0546784321', 'srhamid@gmail.com', '2nd time'),
('D0000003', 'Fatima', 'Al-Qahtani', 'F', '2002-09-11', 'AB+', 'Al Faisaliyyah', '0554436779', 'Fatima_Qahtan@gmail.com', '3rd time');

-- --------------------------------------------------------

--
-- Table structure for table `healthcondition`
--

CREATE TABLE `healthcondition` (
  `DID` varchar(15) NOT NULL,
  `Health_Condition` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `healthcondition`
--

INSERT INTO `healthcondition` (`DID`, `Health_Condition`) VALUES
('D0000001', 'Healthy'),
('D0000002', 'Allergies'),
('D0000003', 'Asthma');

-- --------------------------------------------------------

--
-- Table structure for table `medicalhistory`
--

CREATE TABLE `medicalhistory` (
  `RID` varchar(15) NOT NULL,
  `Medical_History` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medicalhistory`
--

INSERT INTO `medicalhistory` (`RID`, `Medical_History`) VALUES
('R000001', 'allergies and family medical history'),
('R000002', 'allergies and family medical history'),
('R000003', 'Past Surgeries');

-- --------------------------------------------------------

--
-- Table structure for table `phlebotomist`
--

CREATE TABLE `phlebotomist` (
  `PhlebotomistID` varchar(15) NOT NULL,
  `Fname` varchar(50) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `CID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `phlebotomist`
--

INSERT INTO `phlebotomist` (`PhlebotomistID`, `Fname`, `Lname`, `Gender`, `DOB`, `Address`, `PhoneNumber`, `Email`, `CID`) VALUES
('P10000', 'Ahmad', 'Hazim', 'M', '1993-05-24', 'Al-Nasim, Riyadh', '0567855433', 'AhziM24@hotmail.com', 'C1000'),
('P20000', 'Mai', 'Kamel', 'F', '1979-02-14', 'Al-Rawda, Jeddah', '0558823167', 'MaiMai14@hotmail.com', 'C3000'),
('P30000', 'Khaled', 'Medhat', 'M', '1971-03-10', 'Taybah, Dammam', '0555667779', 'KMkm2@hotmail.com', 'C2000');

-- --------------------------------------------------------

--
-- Table structure for table `recipient`
--

CREATE TABLE `recipient` (
  `RecipientID` varchar(15) NOT NULL,
  `Fname` varchar(50) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) NOT NULL,
  `Email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recipient`
--

INSERT INTO `recipient` (`RecipientID`, `Fname`, `Lname`, `Gender`, `DOB`, `Address`, `PhoneNumber`, `Email`) VALUES
('R000001', 'Lana', 'Ray', 'F', '1997-02-16', 'Al-Nasim', '0566442891', 'Lanadr@hotmail.com'),
('R000002', 'Lama', 'Ray', 'F', '2000-07-21', 'Al-Nasim', '0566442892', 'Lamadr@hotmail.com'),
('R000003', 'Yousef', 'Khaled', 'M', '1995-11-03', 'Al-Hamra', '0567878122', 'YouKl12@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `register_appointment`
--

CREATE TABLE `register_appointment` (
  `SID` varchar(15) NOT NULL,
  `DID` varchar(15) NOT NULL,
  `App_Time` varchar(10) NOT NULL,
  `APP_Date` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register_appointment`
--

INSERT INTO `register_appointment` (`SID`, `DID`, `App_Time`, `APP_Date`) VALUES
('S0000001', 'D0000001', '9:00 am', '2024-05-05'),
('S0000003', 'D0000003', '12:00 pm', '2024-5-4'),
('S0000004', 'D0000002', '1:00 pm', '2023-10-24');

-- --------------------------------------------------------

--
-- Table structure for table `related`
--

CREATE TABLE `related` (
  `RID` varchar(15) NOT NULL,
  `DID` varchar(15) NOT NULL,
  `Type_of_Relation` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `related`
--

INSERT INTO `related` (`RID`, `DID`, `Type_of_Relation`) VALUES
('R000001', 'D0000001', 'None'),
('R000002', 'D0000002', 'None'),
('R000003', 'D0000003', 'Brother-in-law');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `StaffID` varchar(15) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Role` varchar(50) NOT NULL,
  `CID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`StaffID`, `Name`, `DOB`, `Address`, `PhoneNumber`, `Email`, `Role`, `CID`) VALUES
('S0000001', 'Hana', '1982-10-05', 'Al Amoudiya, Riyadh', '0554321178', 'HanaA12@gmail.com', 'Receptionist', 'C1000'),
('S0000002', 'Seif', '1990-06-02', 'Ar Rawabi, Riyadh', '0554325561', 'Seif_f12@gmail.com', 'Phelobotmists assistant', 'C1000'),
('S0000003', 'Sarah', '2001-10-07', 'Al Fayhaa, Jeddah', '0555425663', 'SarahK-22@gmail.com', 'Nurse', 'C3000'),
('S0000004', 'Amir', '1978-08-12', 'Olaya, Al Khobar', '0566663312', 'Asa33@gmail.com', 'Receptionist', 'C2000');

-- --------------------------------------------------------

--
-- Table structure for table `track`
--

CREATE TABLE `track` (
  `PID` varchar(15) NOT NULL,
  `TID` varchar(15) NOT NULL,
  `DID` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `track`
--

INSERT INTO `track` (`PID`, `TID`, `DID`) VALUES
('P10000', 'T00100', 'D0000001'),
('P20000', 'T00200', 'D0000003'),
('P30000', 'T00300', 'D0000002');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blooddonation`
--
ALTER TABLE `blooddonation`
  ADD PRIMARY KEY (`DonationID`),
  ADD KEY `DID` (`DID`),
  ADD KEY `CID` (`CID`),
  ADD KEY `TID` (`TID`);

--
-- Indexes for table `bloodtest`
--
ALTER TABLE `bloodtest`
  ADD PRIMARY KEY (`TestID`),
  ADD KEY `DID` (`DID`);

--
-- Indexes for table `blood_donation_center`
--
ALTER TABLE `blood_donation_center`
  ADD PRIMARY KEY (`CenterID`),
  ADD KEY `DID` (`DID`);

--
-- Indexes for table `donor`
--
ALTER TABLE `donor`
  ADD PRIMARY KEY (`DonorID`);

--
-- Indexes for table `healthcondition`
--
ALTER TABLE `healthcondition`
  ADD PRIMARY KEY (`DID`,`Health_Condition`);

--
-- Indexes for table `medicalhistory`
--
ALTER TABLE `medicalhistory`
  ADD PRIMARY KEY (`RID`,`Medical_History`);

--
-- Indexes for table `phlebotomist`
--
ALTER TABLE `phlebotomist`
  ADD PRIMARY KEY (`PhlebotomistID`),
  ADD KEY `CID` (`CID`);

--
-- Indexes for table `recipient`
--
ALTER TABLE `recipient`
  ADD PRIMARY KEY (`RecipientID`);

--
-- Indexes for table `register_appointment`
--
ALTER TABLE `register_appointment`
  ADD PRIMARY KEY (`SID`,`DID`),
  ADD KEY `DID` (`DID`);

--
-- Indexes for table `related`
--
ALTER TABLE `related`
  ADD PRIMARY KEY (`RID`,`DID`),
  ADD KEY `DID` (`DID`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`StaffID`),
  ADD KEY `CID` (`CID`);

--
-- Indexes for table `track`
--
ALTER TABLE `track`
  ADD PRIMARY KEY (`PID`,`TID`,`DID`),
  ADD KEY `TID` (`TID`),
  ADD KEY `DID` (`DID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `blooddonation`
--
ALTER TABLE `blooddonation`
  ADD CONSTRAINT `blooddonation_ibfk_1` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`),
  ADD CONSTRAINT `blooddonation_ibfk_2` FOREIGN KEY (`CID`) REFERENCES `blood_donation_center` (`CenterID`),
  ADD CONSTRAINT `blooddonation_ibfk_3` FOREIGN KEY (`TID`) REFERENCES `bloodtest` (`TestID`);

--
-- Constraints for table `bloodtest`
--
ALTER TABLE `bloodtest`
  ADD CONSTRAINT `bloodtest_ibfk_1` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`);

--
-- Constraints for table `blood_donation_center`
--
ALTER TABLE `blood_donation_center`
  ADD CONSTRAINT `blood_donation_center_ibfk_1` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`);

--
-- Constraints for table `healthcondition`
--
ALTER TABLE `healthcondition`
  ADD CONSTRAINT `healthcondition_ibfk_1` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`);

--
-- Constraints for table `medicalhistory`
--
ALTER TABLE `medicalhistory`
  ADD CONSTRAINT `medicalhistory_ibfk_1` FOREIGN KEY (`RID`) REFERENCES `recipient` (`RecipientID`);

--
-- Constraints for table `phlebotomist`
--
ALTER TABLE `phlebotomist`
  ADD CONSTRAINT `phlebotomist_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `blood_donation_center` (`CenterID`);

--
-- Constraints for table `register_appointment`
--
ALTER TABLE `register_appointment`
  ADD CONSTRAINT `register_appointment_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `staff` (`StaffID`),
  ADD CONSTRAINT `register_appointment_ibfk_2` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`);

--
-- Constraints for table `related`
--
ALTER TABLE `related`
  ADD CONSTRAINT `related_ibfk_1` FOREIGN KEY (`RID`) REFERENCES `recipient` (`RecipientID`),
  ADD CONSTRAINT `related_ibfk_2` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`);

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `blood_donation_center` (`CenterID`);

--
-- Constraints for table `track`
--
ALTER TABLE `track`
  ADD CONSTRAINT `track_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `phlebotomist` (`PhlebotomistID`),
  ADD CONSTRAINT `track_ibfk_2` FOREIGN KEY (`TID`) REFERENCES `bloodtest` (`TestID`),
  ADD CONSTRAINT `track_ibfk_3` FOREIGN KEY (`DID`) REFERENCES `donor` (`DonorID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
