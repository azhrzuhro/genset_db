-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 14, 2025 at 04:09 AM
-- Server version: 8.0.42
-- PHP Version: 8.3.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `genset`
--

-- --------------------------------------------------------

--
-- Table structure for table `sensor`
--

CREATE TABLE `sensor` (
  `id` int NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `oil_pressure` float NOT NULL,
  `coolant_temp` float NOT NULL,
  `engine_RPM` int NOT NULL,
  `vibration` int NOT NULL,
  `baterei` float NOT NULL,
  `fuel_level` int NOT NULL,
  `hours_meter` float NOT NULL,
  `genset_voltage` float NOT NULL,
  `genset_current` float NOT NULL,
  `genset_frekuensi` float NOT NULL,
  `genset_power` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sensor`
--

INSERT INTO `sensor` (`id`, `timestamp`, `oil_pressure`, `coolant_temp`, `engine_RPM`, `vibration`, `baterei`, `fuel_level`, `hours_meter`, `genset_voltage`, `genset_current`, `genset_frekuensi`, `genset_power`) VALUES
(1, '2025-07-12 09:37:16', 4, 72, 1520, 120, 13, 83, 1532, 220, 5, 50, 2300),
(2, '2025-07-12 15:02:16', 4, 74, 1524, 180, 13, 83, 1532, 220, 3, 50, 2350),
(3, '2025-07-12 15:02:40', 4, 74, 1524, 180, 13, 83, 1532, 220, 3, 50, 2350),
(4, '2025-07-12 15:02:41', 5, 74, 1520, 185, 13, 83, 1532, 220, 3, 50, 2350),
(5, '2025-07-12 15:02:42', 5, 75, 1521, 189, 13, 83, 1532, 220, 3, 50, 2350),
(6, '2025-07-12 15:02:43', 4, 74, 1518, 180, 13, 83, 1532, 220, 3, 50, 2350),
(7, '2025-07-12 15:02:44', 4, 75, 1519, 167, 13, 83, 1532, 222, 3, 50, 2350);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sensor`
--
ALTER TABLE `sensor`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
