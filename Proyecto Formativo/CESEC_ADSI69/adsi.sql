-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 01, 2022 at 03:54 PM
-- Server version: 5.7.33
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `adsi`
--

-- --------------------------------------------------------

--
-- Table structure for table `carrusel`
--

CREATE TABLE `carrusel` (
  `id` int(4) NOT NULL,
  `img` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `url` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `carrusel`
--

INSERT INTO `carrusel` (`id`, `img`, `descripcion`, `url`, `fecha_inicio`, `fecha_fin`, `estado`) VALUES
(1, 'slide1.jpg', 'Ingresa tus dispositivos', '#', '2022-05-01', '2022-05-12', 1),
(2, 'slide2.jpg', 'La mejor gestion', '#', '2022-05-01', '2022-05-31', 1),
(3, 'slide3.jpg', 'otra pagina mas', '#', '2022-05-01', '2022-05-12', 1),
(4, 'slide4.jpg', 'pagina 4', '#', '2022-05-01', '2022-05-12', 1);

-- --------------------------------------------------------

--
-- Table structure for table `equipos`
--

CREATE TABLE `equipos` (
  `id` int(4) NOT NULL,
  `serie` varchar(50) DEFAULT NULL,
  `id_Marca` int(1) DEFAULT NULL,
  `detalle` text,
  `id_Usuario` int(4) DEFAULT NULL,
  `estado` int(1) DEFAULT NULL,
  `img` varchar(250) NOT NULL,
  `Qr` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ficha`
--

CREATE TABLE `ficha` (
  `id_Ficha` int(10) NOT NULL,
  `codigo` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `marca`
--

CREATE TABLE `marca` (
  `id_Marca` int(10) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rol`
--

CREATE TABLE `rol` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tipodocumento`
--

CREATE TABLE `tipodocumento` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `id_tipo` int(10) NOT NULL,
  `numeroDocumento` varchar(50) NOT NULL,
  `id_Rol` int(10) DEFAULT NULL,
  `contrasena` varchar(50) NOT NULL,
  `estado` int(1) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `img` varchar(50) DEFAULT NULL,
  `Qr` varchar(50) DEFAULT NULL,
  `telefono` varchar(50) NOT NULL,
  `ficha` int(10) DEFAULT NULL,
  `id_centro` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `id_tipo`, `numeroDocumento`, `id_Rol`, `contrasena`, `estado`, `correo`, `img`, `Qr`, `telefono`, `ficha`, `id_centro`) VALUES
(1, 'bienestar', 'CTA', 1, '1', 4, '123456', 1, 'bbienestarCTA@misena.edu.co', '', '', '', 0, 0),
(2, 'Andres', 'Vera', 1, '1004701817', 2, '1', 1, 'ciberandresoficial@gmail.com', '', '', '3007550860', 2278769, 1),
(3, 'Alejandro', 'Duque Padilla', 1, '1004701816', NULL, '1', NULL, 'kofla1234@outlook.com', NULL, NULL, '144141', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `carrusel`
--
ALTER TABLE `carrusel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numeroDocumento` (`numeroDocumento`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `carrusel`
--
ALTER TABLE `carrusel`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
