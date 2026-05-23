-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2024 at 07:29 PM
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
-- Database: `logipack`
--

-- --------------------------------------------------------

--
-- Table structure for table `paquete`
--

CREATE TABLE `paquete` (
  `id` int(11) NOT NULL,
  `numeroenvio` varchar(20) NOT NULL,
  `peso` float NOT NULL,
  `nomdestino` varchar(50) NOT NULL,
  `dirdestino` varchar(100) NOT NULL,
  `entregado` tinyint(1) DEFAULT NULL,
  `observaciones` varchar(200) DEFAULT NULL,
  `idsucursal` int(11) NOT NULL,
  `idtransporte` int(11) DEFAULT NULL,
  `idrepartidor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `paquete`
--

INSERT INTO `paquete` (`id`, `numeroenvio`, `peso`, `nomdestino`, `dirdestino`, `entregado`, `observaciones`, `idsucursal`, `idtransporte`, `idrepartidor`) VALUES
(1, '040f6c1a', 0, 'PRUEBA1', 'PRUEBA1', 0, 'PRUEBA1', 20, 3, NULL),
(2, '7f257eb1', 0, 'PRUEBA2', 'PRUEBA2', 0, 'PRUEBA2', 10, 1, NULL),
(3, '8504c64e', 0, 'TEST3', 'direccion ejemplo norte 3', 0, 'obs ejemplo 3', 10, 4, NULL),
(4, 'a436dcc0', 0, 'TEST4', 'direccion ejemplo sur 4', 0, 'obs ejemplo 4', 10, 4, NULL),
(5, 'a68487e8', 0, 'TEST5', 'TEST5', 0, 'TEST5', 10, 2, NULL),
(6, '97ea3a4e', 21, 'Sabino', 'JOFRE 1245 NORTE', 0, 'paquete con cinta azul, tratar con cuidado articulo fragil', 10, 5, NULL),
(7, '0aa2cb91', 0, 'TEST_NOMBRE_1', 'TEST_DIRECCION_1', 0, 'TEST_OBS_1', 10, 6, NULL),
(8, '396b7fc6', 0, 'TEST_NOMBRE_2', 'TEST_DIRECCION_2', 0, 'TEST_OBS_2', 10, NULL, NULL),
(9, '5973e7a3', 0, 'TEST_NOMBRE_3', 'TEST_DIRECCION_3', 0, 'TEST_OBS_3', 10, 8, NULL),
(10, '728a312d', 0, 'TEST_NOMBRE_4', 'TEST_DIRECCION_4', 0, 'TEST_OBS_4', 10, NULL, NULL),
(11, '17fe791b', 12, 'Juan Perez', 'JOFRE 1245 NORTE', 0, 'el cliente llamo para avisar que lo trae mañana y lo dejo señado', 10, 9, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `paquete`
--
ALTER TABLE `paquete`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numeroenvio` (`numeroenvio`),
  ADD KEY `idsucursal` (`idsucursal`),
  ADD KEY `idtransporte` (`idtransporte`),
  ADD KEY `idrepartidor` (`idrepartidor`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `paquete`
--
ALTER TABLE `paquete`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `paquete`
--
ALTER TABLE `paquete`
  ADD CONSTRAINT `paquete_ibfk_1` FOREIGN KEY (`idsucursal`) REFERENCES `sucursal` (`id`),
  ADD CONSTRAINT `paquete_ibfk_2` FOREIGN KEY (`idtransporte`) REFERENCES `transporte` (`id`),
  ADD CONSTRAINT `paquete_ibfk_3` FOREIGN KEY (`idrepartidor`) REFERENCES `repartidor` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
