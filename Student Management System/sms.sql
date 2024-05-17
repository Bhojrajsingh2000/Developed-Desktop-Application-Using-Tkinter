-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2024 at 12:09 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sms`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `dep` varchar(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `year` varchar(50) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `stid` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `division` varchar(50) NOT NULL,
  `roll` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `teacher` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`dep`, `course`, `year`, `semester`, `stid`, `name`, `division`, `roll`, `gender`, `dob`, `email`, `contact`, `address`, `teacher`) VALUES
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030112', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030114', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030115', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030116', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030117', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030118', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030119', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030120', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030121', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030122', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030123', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030124', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030125', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind'),
('Civil Department', 'B.Tech', '2021-2022', 'Semester 2', '22SCSE2030126', 'DEEPAK', '2nd', '22132030109', 'Male', '08/08/2003', '788', '9927038901', 'JARTALI', 'arvind');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
