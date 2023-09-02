-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-09-2023 a las 01:03:20
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbsigpogac`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asesoria_constructiva`
--

CREATE TABLE `asesoria_constructiva` (
  `SK_ASESORIA` int(11) NOT NULL,
  `NM_TIEMPO` int(11) NOT NULL,
  `ST_UNIDAD_ASESORIA` varchar(50) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_empleado`
--

CREATE TABLE `asignacion_empleado` (
  `SK_ASIG_EMPLEADO` int(11) NOT NULL,
  `SK_PROYECTO_id` int(11) NOT NULL,
  `FK_USUARIO_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `asignacion_empleado`
--

INSERT INTO `asignacion_empleado` (`SK_ASIG_EMPLEADO`, `SK_PROYECTO_id`, `FK_USUARIO_id`) VALUES
(1, 1, 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_equipo`
--

CREATE TABLE `asignacion_equipo` (
  `SK_ASIG_EQUIPO` int(11) NOT NULL,
  `FK_EQUIPO_id` int(11) NOT NULL,
  `SK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_material`
--

CREATE TABLE `asignacion_material` (
  `SK_ASIG_MATERIAL` int(11) NOT NULL,
  `ST_DESCRIPCION` varchar(50) DEFAULT NULL,
  `SK_MATERIAL_id` int(11) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Administrador'),
(2, 'Empleado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(3, 1, 1),
(4, 1, 2),
(5, 1, 3),
(6, 1, 4),
(7, 1, 5),
(8, 1, 6),
(9, 1, 7),
(10, 1, 8),
(11, 1, 9),
(12, 1, 10),
(13, 1, 11),
(14, 1, 12),
(15, 1, 13),
(16, 1, 14),
(17, 1, 15),
(18, 1, 16),
(19, 1, 17),
(20, 1, 18),
(21, 1, 19),
(22, 1, 20),
(23, 1, 21),
(24, 1, 22),
(25, 1, 23),
(26, 1, 24),
(27, 1, 25),
(28, 1, 26),
(29, 1, 27),
(30, 1, 28),
(31, 1, 29),
(32, 1, 30),
(33, 1, 31),
(34, 1, 32),
(35, 1, 33),
(36, 1, 34),
(37, 1, 35),
(38, 1, 36),
(39, 1, 37),
(40, 1, 38),
(41, 1, 39),
(42, 1, 40),
(43, 1, 41),
(44, 1, 42),
(45, 1, 43),
(46, 1, 44),
(47, 1, 45),
(48, 1, 46),
(49, 1, 47),
(50, 1, 48),
(51, 1, 49),
(52, 1, 50),
(53, 1, 51),
(54, 1, 52),
(55, 1, 53),
(56, 1, 54),
(57, 1, 55),
(58, 1, 56),
(59, 1, 57),
(60, 1, 58),
(61, 1, 59),
(62, 1, 60),
(63, 1, 61),
(64, 1, 62),
(65, 1, 63),
(66, 1, 64),
(67, 1, 65),
(68, 1, 66),
(69, 1, 67),
(70, 1, 68),
(71, 1, 69),
(72, 1, 70),
(73, 1, 71),
(74, 1, 72),
(75, 1, 73),
(76, 1, 74),
(77, 1, 75),
(78, 1, 76),
(79, 1, 77),
(80, 1, 78),
(81, 1, 79),
(82, 1, 80),
(83, 1, 81),
(84, 1, 82),
(85, 1, 83),
(86, 1, 84),
(87, 1, 85),
(88, 1, 86),
(89, 1, 87),
(90, 1, 88),
(91, 1, 89),
(92, 1, 90),
(93, 1, 91),
(94, 1, 92),
(95, 1, 93),
(96, 1, 94),
(97, 1, 95),
(98, 1, 96),
(99, 1, 97),
(100, 1, 98),
(101, 1, 99),
(102, 1, 100),
(103, 1, 101),
(104, 1, 102),
(105, 1, 103),
(106, 1, 104),
(1, 2, 40),
(2, 2, 44);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add usuario', 6, 'add_usuario'),
(22, 'Can change usuario', 6, 'change_usuario'),
(23, 'Can delete usuario', 6, 'delete_usuario'),
(24, 'Can view usuario', 6, 'view_usuario'),
(25, 'Can add documento usuario', 7, 'add_documentousuario'),
(26, 'Can change documento usuario', 7, 'change_documentousuario'),
(27, 'Can delete documento usuario', 7, 'delete_documentousuario'),
(28, 'Can view documento usuario', 7, 'view_documentousuario'),
(29, 'Can add cliente', 8, 'add_cliente'),
(30, 'Can change cliente', 8, 'change_cliente'),
(31, 'Can delete cliente', 8, 'delete_cliente'),
(32, 'Can view cliente', 8, 'view_cliente'),
(33, 'Can add tipo equipo', 9, 'add_tipoequipo'),
(34, 'Can change tipo equipo', 9, 'change_tipoequipo'),
(35, 'Can delete tipo equipo', 9, 'delete_tipoequipo'),
(36, 'Can view tipo equipo', 9, 'view_tipoequipo'),
(37, 'Can add equipo', 10, 'add_equipo'),
(38, 'Can change equipo', 10, 'change_equipo'),
(39, 'Can delete equipo', 10, 'delete_equipo'),
(40, 'Can view equipo', 10, 'view_equipo'),
(41, 'Can add material', 11, 'add_material'),
(42, 'Can change material', 11, 'change_material'),
(43, 'Can delete material', 11, 'delete_material'),
(44, 'Can view material', 11, 'view_material'),
(45, 'Can add estado proyecto', 12, 'add_estadoproyecto'),
(46, 'Can change estado proyecto', 12, 'change_estadoproyecto'),
(47, 'Can delete estado proyecto', 12, 'delete_estadoproyecto'),
(48, 'Can view estado proyecto', 12, 'view_estadoproyecto'),
(49, 'Can add proyecto', 13, 'add_proyecto'),
(50, 'Can change proyecto', 13, 'change_proyecto'),
(51, 'Can delete proyecto', 13, 'delete_proyecto'),
(52, 'Can view proyecto', 13, 'view_proyecto'),
(53, 'Can add tipo servicio', 14, 'add_tiposervicio'),
(54, 'Can change tipo servicio', 14, 'change_tiposervicio'),
(55, 'Can delete tipo servicio', 14, 'delete_tiposervicio'),
(56, 'Can view tipo servicio', 14, 'view_tiposervicio'),
(57, 'Can add transporte', 15, 'add_transporte'),
(58, 'Can change transporte', 15, 'change_transporte'),
(59, 'Can delete transporte', 15, 'delete_transporte'),
(60, 'Can view transporte', 15, 'view_transporte'),
(61, 'Can add senializacion vial', 16, 'add_senializacionvial'),
(62, 'Can change senializacion vial', 16, 'change_senializacionvial'),
(63, 'Can delete senializacion vial', 16, 'delete_senializacionvial'),
(64, 'Can view senializacion vial', 16, 'view_senializacionvial'),
(65, 'Can add renta equipo', 17, 'add_rentaequipo'),
(66, 'Can change renta equipo', 17, 'change_rentaequipo'),
(67, 'Can delete renta equipo', 17, 'delete_rentaequipo'),
(68, 'Can view renta equipo', 17, 'view_rentaequipo'),
(69, 'Can add renta desimetro', 18, 'add_rentadesimetro'),
(70, 'Can change renta desimetro', 18, 'change_rentadesimetro'),
(71, 'Can delete renta desimetro', 18, 'delete_rentadesimetro'),
(72, 'Can view renta desimetro', 18, 'view_rentadesimetro'),
(73, 'Can add levantamiento topografico', 19, 'add_levantamientotopografico'),
(74, 'Can change levantamiento topografico', 19, 'change_levantamientotopografico'),
(75, 'Can delete levantamiento topografico', 19, 'delete_levantamientotopografico'),
(76, 'Can view levantamiento topografico', 19, 'view_levantamientotopografico'),
(77, 'Can add factura', 20, 'add_factura'),
(78, 'Can change factura', 20, 'change_factura'),
(79, 'Can delete factura', 20, 'delete_factura'),
(80, 'Can view factura', 20, 'view_factura'),
(81, 'Can add estructura metalica', 21, 'add_estructurametalica'),
(82, 'Can change estructura metalica', 21, 'change_estructurametalica'),
(83, 'Can delete estructura metalica', 21, 'delete_estructurametalica'),
(84, 'Can view estructura metalica', 21, 'view_estructurametalica'),
(85, 'Can add concreto', 22, 'add_concreto'),
(86, 'Can change concreto', 22, 'change_concreto'),
(87, 'Can delete concreto', 22, 'delete_concreto'),
(88, 'Can view concreto', 22, 'view_concreto'),
(89, 'Can add asignacion material', 23, 'add_asignacionmaterial'),
(90, 'Can change asignacion material', 23, 'change_asignacionmaterial'),
(91, 'Can delete asignacion material', 23, 'delete_asignacionmaterial'),
(92, 'Can view asignacion material', 23, 'view_asignacionmaterial'),
(93, 'Can add asignacion equipo', 24, 'add_asignacionequipo'),
(94, 'Can change asignacion equipo', 24, 'change_asignacionequipo'),
(95, 'Can delete asignacion equipo', 24, 'delete_asignacionequipo'),
(96, 'Can view asignacion equipo', 24, 'view_asignacionequipo'),
(97, 'Can add asignacion empleado', 25, 'add_asignacionempleado'),
(98, 'Can change asignacion empleado', 25, 'change_asignacionempleado'),
(99, 'Can delete asignacion empleado', 25, 'delete_asignacionempleado'),
(100, 'Can view asignacion empleado', 25, 'view_asignacionempleado'),
(101, 'Can add asesoria constructiva', 26, 'add_asesoriaconstructiva'),
(102, 'Can change asesoria constructiva', 26, 'change_asesoriaconstructiva'),
(103, 'Can delete asesoria constructiva', 26, 'delete_asesoriaconstructiva'),
(104, 'Can view asesoria constructiva', 26, 'view_asesoriaconstructiva');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `SK_CLIENTE` int(11) NOT NULL,
  `ST_NOMBRE_CLIENTE` varchar(100) NOT NULL,
  `ST_DOC_CLIENTE` varchar(75) NOT NULL,
  `ST_NIT_CLIENTE` varchar(17) NOT NULL,
  `BN_TIPO_CLIENTE` tinyint(1) NOT NULL,
  `FC_INGRESO_CLIENTE` datetime(6) NOT NULL,
  `FK_USUARIO_id` bigint(20) NOT NULL,
  `BN_ESTA_ACTIVO` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`SK_CLIENTE`, `ST_NOMBRE_CLIENTE`, `ST_DOC_CLIENTE`, `ST_NIT_CLIENTE`, `BN_TIPO_CLIENTE`, `FC_INGRESO_CLIENTE`, `FK_USUARIO_id`, `BN_ESTA_ACTIVO`) VALUES
(1, 'Platanares S.A. de C.V.', '205123-3', '0614-011010-106-4', 1, '2023-06-06 03:12:39.362647', 1, 0),
(2, '2323', '13212232-1', '2132-132132-132-1', 0, '2023-06-13 03:27:48.031180', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `concreto`
--

CREATE TABLE `concreto` (
  `SK_CONCRETO` int(11) NOT NULL,
  `ST_TIPO_DOC_CONCRETO` varchar(25) NOT NULL,
  `ST_DOC_CONCRETO` varchar(100) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-05-31 02:13:06.020313', '1', 'Administrador', 1, '[{\"added\": {}}]', 3, 1),
(2, '2023-05-31 02:13:16.829592', '2', 'Empleado', 1, '[{\"added\": {}}]', 3, 1),
(3, '2023-06-10 04:15:35.826400', '2', 'Empleado', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1),
(4, '2023-06-10 04:16:43.510167', '1', 'Administrador', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'Administrador', 'documentousuario'),
(6, 'Administrador', 'usuario'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(8, 'Cliente', 'cliente'),
(4, 'contenttypes', 'contenttype'),
(10, 'Equipo', 'equipo'),
(9, 'Equipo', 'tipoequipo'),
(11, 'Material', 'material'),
(26, 'Proyecto', 'asesoriaconstructiva'),
(25, 'Proyecto', 'asignacionempleado'),
(24, 'Proyecto', 'asignacionequipo'),
(23, 'Proyecto', 'asignacionmaterial'),
(22, 'Proyecto', 'concreto'),
(12, 'Proyecto', 'estadoproyecto'),
(21, 'Proyecto', 'estructurametalica'),
(20, 'Proyecto', 'factura'),
(19, 'Proyecto', 'levantamientotopografico'),
(13, 'Proyecto', 'proyecto'),
(18, 'Proyecto', 'rentadesimetro'),
(17, 'Proyecto', 'rentaequipo'),
(16, 'Proyecto', 'senializacionvial'),
(14, 'Proyecto', 'tiposervicio'),
(15, 'Proyecto', 'transporte'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-05-30 23:55:45.471580'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-05-30 23:55:46.245849'),
(3, 'auth', '0001_initial', '2023-05-30 23:55:49.254214'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-05-30 23:55:50.262942'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-05-30 23:55:50.373906'),
(6, 'auth', '0004_alter_user_username_opts', '2023-05-30 23:55:50.495592'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-05-30 23:55:50.591414'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-05-30 23:55:50.658702'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-05-30 23:55:50.737282'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-05-30 23:55:50.800854'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-05-30 23:55:50.914206'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-05-30 23:55:51.106094'),
(13, 'auth', '0011_update_proxy_permissions', '2023-05-30 23:55:51.214263'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-05-30 23:55:51.286256'),
(15, 'Administrador', '0001_initial', '2023-05-30 23:55:56.659100'),
(16, 'Cliente', '0001_initial', '2023-05-30 23:55:57.898511'),
(17, 'Equipo', '0001_initial', '2023-05-30 23:55:59.227223'),
(18, 'Material', '0001_initial', '2023-05-30 23:55:59.752960'),
(19, 'Proyecto', '0001_initial', '2023-05-30 23:56:20.437080'),
(20, 'admin', '0001_initial', '2023-05-30 23:56:22.948422'),
(21, 'admin', '0002_logentry_remove_auto_add', '2023-05-30 23:56:23.048556'),
(22, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-30 23:56:23.111634'),
(23, 'sessions', '0001_initial', '2023-05-30 23:56:23.662639'),
(24, 'Cliente', '0002_cliente_bn_esta_activo', '2023-06-01 01:06:53.309364'),
(25, 'Administrador', '0002_alter_usuario_fc_nacimiento_and_more', '2023-06-02 02:44:27.382369'),
(26, 'Equipo', '0002_equipo_bn_estado_equipo', '2023-06-02 02:44:28.072497'),
(27, 'Material', '0002_material_bn_estado_material', '2023-06-02 02:44:28.635913'),
(28, 'Equipo', '0003_equipo_fc_ingreso', '2023-06-06 02:57:15.891482'),
(29, 'Equipo', '0004_equipo_st_img_equipo_alter_equipo_sk_tipo_equipo_and_more', '2023-06-06 03:13:47.865319'),
(30, 'Administrador', '0003_alter_usuario_st_dui_usuario_and_more', '2023-06-10 15:04:45.741864'),
(31, 'Material', '0003_alter_material_st_descripcion_material_and_more', '2023-06-10 15:04:45.806065'),
(32, 'Administrador', '0003_usuario_bn_estado_usuario_and_more', '2023-06-10 18:00:33.506537'),
(33, 'Administrador', '0004_alter_usuario_st_afp_usuario_and_more', '2023-06-11 17:22:16.581881'),
(34, 'Equipo', '0005_rename_sk_tipo_equipo_equipo_fk_tipo_equipo_and_more', '2023-06-11 17:22:49.654072'),
(35, 'Cliente', '0003_rename_sk_usuario_cliente_fk_usuario', '2023-06-11 17:27:28.242442'),
(36, 'Proyecto', '0002_rename_sk_proyecto_asesoriaconstructiva_fk_proyecto_and_more', '2023-06-11 17:28:09.199879'),
(37, 'Administrador', '0005_rename_sk_usuario_documentousuario_fk_usuario', '2023-06-11 17:34:15.814698');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('cboiqxxt6goc2por91cdiixip93m7qwn', '.eJxVjE0OwiAYBe_C2hCBAuLSvWcg31-laiAp7cp4d23ShW7fzLyXyrAuJa9d5jyxOiujDr8bAj2kboDvUG9NU6vLPKHeFL3Trq-N5XnZ3b-DAr186yBkQjySSUOk5JFtSETkOZIVND4Fj4DGueEUE1g7BoeIY0wMgoMj9f4A5xA4Zg:1qBkRX:Z5HBj4TESvC65CLaSb4R-815B9R1rO2tSUH4jUZkhI8', '2023-07-04 23:07:23.084699'),
('cmavbuow476pzif2abcescsabm3s5xvd', '.eJxVjEEOgjAQRe_StWkYhnZGl-45QzPttIIaSCisjHdXEha6_e-9_zJBtnUIW81LGNVcDKA5_Y5R0iNPO9G7TLfZpnlalzHaXbEHrbafNT-vh_t3MEgdvnXpHAJFOiM1bcHSKYEAZlBE76RlVmDPHhtKDJAkMlH2Hpx2TC6Z9wfYjTbE:1q9GSG:ii0U6IcAlKCFU8MQJLDmEq0AYR0S-VGFdIBO3YCkTe0', '2023-06-28 02:41:52.330577'),
('lsvl674ip8notu05xxee3q76tq5jolgt', '.eJxVjMsOwiAUBf-FtSECBbwu3fsN5D6oVA0kpV0Z_12bdKHbMzPnpRKuS0lrz3OaRJ2VserwOxLyI9eNyB3rrWludZkn0puid9r1tUl-Xnb376BgL986ZDYhHtnAEBk8iQ3AzF4i20zGQ_CEZJwbThHQ2jE4IhojCGYaHKv3BwupOJg:1qHPdi:kBfxoxFZmEIEmZwKQp4CrKe1WcGD4nMQwsE-LXHlGQ8', '2023-07-20 14:07:22.711837'),
('mtqblnlbnpq6fmjyfoou5bsbaowinmd1', '.eJxVjMsOwiAUBf-FtSECBbwu3fsN5D6oVA0kpV0Z_12bdKHbMzPnpRKuS0lrz3OaRJ2VserwOxLyI9eNyB3rrWludZkn0puid9r1tUl-Xnb376BgL986ZDYhHtnAEBk8iQ3AzF4i20zGQ_CEZJwbThHQ2jE4IhojCGYaHKv3BwupOJg:1qbWwG:Qr3b4omTDwXjGpxWXOueHgdbBf3uH44fiB-VY-3arG8', '2023-09-14 01:57:40.541742'),
('v1ohnz7tvamv9x60z3irvwzf44appv8q', '.eJxVjMsOwiAUBf-FtSECBbwu3fsN5D6oVA0kpV0Z_12bdKHbMzPnpRKuS0lrz3OaRJ2VserwOxLyI9eNyB3rrWludZkn0puid9r1tUl-Xnb376BgL986ZDYhHtnAEBk8iQ3AzF4i20zGQ_CEZJwbThHQ2jE4IhojCGYaHKv3BwupOJg:1qC81R:y8AC9fqDR6moOG0BzjzHm0FZh86-wwTx8mRT8qgxGXY', '2023-07-06 00:18:01.157145'),
('ygm1307a7kcc082kat85lfc0439xoaod', '.eJxVjE0OwiAYBe_C2hCBAuLSvWcg31-laiAp7cp4d23ShW7fzLyXyrAuJa9d5jyxOiujDr8bAj2kboDvUG9NU6vLPKHeFL3Trq-N5XnZ3b-DAr186yBkQjySSUOk5JFtSETkOZIVND4Fj4DGueEUE1g7BoeIY0wMgoMj9f4A5xA4Zg:1q4u7V:yknPMiT5kmXrj23CfPhScppx1RdZZhHbWPk38eAgO-4', '2023-06-16 02:02:25.559864');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `SK_EQUIPO` int(11) NOT NULL,
  `ST_NOMBRE_EQUIPO` varchar(50) NOT NULL,
  `ST_DESCRIPCION_EQUIPO` varchar(120) NOT NULL,
  `FK_TIPO_EQUIPO_id` int(11) NOT NULL,
  `BN_ESTADO_EQUIPO` tinyint(1) NOT NULL,
  `FC_INGRESO` date NOT NULL,
  `ST_IMG_EQUIPO` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `equipo`
--

INSERT INTO `equipo` (`SK_EQUIPO`, `ST_NOMBRE_EQUIPO`, `ST_DESCRIPCION_EQUIPO`, `FK_TIPO_EQUIPO_id`, `BN_ESTADO_EQUIPO`, `FC_INGRESO`, `ST_IMG_EQUIPO`) VALUES
(1, 'Pick Up Frontier', 'Pick Up Frontier 2023 color gris. Placa ABC123', 1, 1, '2023-06-06', 'img_equipo/default.jpg'),
(2, '1213213', 'Decoblock fino intemperie blanco hueso 40kg. Decoblock fino, blanco hueso, intemperie, mezcla para repello.', 2, 1, '2023-06-11', 'img_equipo/default.jpg'),
(3, '1234', 'Pick Up Frontier 2023 color gris. Placa ABC123', 1, 1, '2023-06-11', 'img_equipo/Nissan_Frontier.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_proyecto`
--

CREATE TABLE `estado_proyecto` (
  `SK_ESTADO_PROYECTO` int(11) NOT NULL,
  `ST_ESTADO_PROYECTO` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estado_proyecto`
--

INSERT INTO `estado_proyecto` (`SK_ESTADO_PROYECTO`, `ST_ESTADO_PROYECTO`) VALUES
(1, 'Registrado'),
(2, 'En ejecución'),
(3, 'Completado'),
(4, 'Finalizado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estructura_metalica`
--

CREATE TABLE `estructura_metalica` (
  `SK_ESTRUCTURA_METALICA` int(11) NOT NULL,
  `ST_TIPO_DOC_CONCRETO` varchar(25) NOT NULL,
  `ST_DOC_CONCRETO` varchar(100) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `SK_FACTURA` int(11) NOT NULL,
  `ST_FACTURA` varchar(100) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `levantamiento_topografico`
--

CREATE TABLE `levantamiento_topografico` (
  `SK_LEVANTAMIENTO_TOPOGRAFICO` int(11) NOT NULL,
  `NM_AREA` decimal(10,2) NOT NULL,
  `ST_UNIDAD_LEVANTAMIENTO` varchar(50) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `material`
--

CREATE TABLE `material` (
  `SK_MATERIAL` int(11) NOT NULL,
  `ST_NOMBRE_MATERIAL` varchar(60) NOT NULL,
  `ST_DESCRIPCION_MATERIAL` varchar(120) NOT NULL,
  `BN_ESTADO_MATERIAL` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `material`
--

INSERT INTO `material` (`SK_MATERIAL`, `ST_NOMBRE_MATERIAL`, `ST_DESCRIPCION_MATERIAL`, `BN_ESTADO_MATERIAL`) VALUES
(1, 'Decoblock fino intemperie blanco hueso', 'Decoblock fino intemperie blanco hueso 40kg. Decoblock fino, blanco hueso, intemperie, mezcla para repello.', 0),
(2, 'Cemento Holcim Maestro', 'Cemento Holcim Maestro es un cemento para trabajos de albañilería; tiene adición de caliza e inclusor de aire.', 1),
(4, '21321', '132', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `SK_PROYECTO` int(11) NOT NULL,
  `ST_DIRECCION_PROYECTO` varchar(120) NOT NULL,
  `NM_LATITUD_PROYECTO` double NOT NULL,
  `NM_LONGITUD_PROYECTO` double NOT NULL,
  `ST_DESCRIPCION_PROYECTO` varchar(120) NOT NULL,
  `FC_INGRESO_PROYECTO` datetime(6) NOT NULL,
  `FK_CLIENTE_id` int(11) NOT NULL,
  `FK_ESTADO_PROYECTO_id` int(11) NOT NULL,
  `FK_TIPO_SERVICIO_id` int(11) NOT NULL,
  `FK_USUARIO_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`SK_PROYECTO`, `ST_DIRECCION_PROYECTO`, `NM_LATITUD_PROYECTO`, `NM_LONGITUD_PROYECTO`, `ST_DESCRIPCION_PROYECTO`, `FC_INGRESO_PROYECTO`, `FK_CLIENTE_id`, `FK_ESTADO_PROYECTO_id`, `FK_TIPO_SERVICIO_id`, `FK_USUARIO_id`) VALUES
(1, 'San Salvador, El Salvador.', 13.7072, -89.2047, 'Recarpeteo de calles principales', '2023-06-11 15:26:18.000000', 1, 1, 1, 1),
(2, 'San Salvador, El Salvador.', 13.7072, -89.2047, 'Recarpeteo de calles principales', '2023-06-11 15:26:18.000000', 1, 3, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `renta_desimetro`
--

CREATE TABLE `renta_desimetro` (
  `SK_RENTA_DESIMETRO` int(11) NOT NULL,
  `FC_SALIDA_DESIMETRO` datetime(6) NOT NULL,
  `FC_ENTRADA_DESIMETRO` datetime(6) NOT NULL,
  `ST_NOMBRE_TECNICO` varchar(50) NOT NULL,
  `ST_OBSERVACION_DESIMETRO` varchar(120) DEFAULT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `renta_equipo`
--

CREATE TABLE `renta_equipo` (
  `SK_RENTA_EQUIPO` int(11) NOT NULL,
  `FC_SALIDA_EQUIPO` datetime(6) NOT NULL,
  `FC_ENTRADA_EQUIPO` datetime(6) NOT NULL,
  `ST_TIPO_USO` varchar(100) NOT NULL,
  `ST_OBSERVACION_EQUIPO` varchar(120) DEFAULT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `senializacion_vial`
--

CREATE TABLE `senializacion_vial` (
  `SK_SENIALIZACION_VIAL` int(11) NOT NULL,
  `ST_ESPECIFICACION_VIAL` varchar(120) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_equipo`
--

CREATE TABLE `tipo_equipo` (
  `SK_TIPO_EQUIPO` int(11) NOT NULL,
  `ST_TIPO_EQUIPO` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_equipo`
--

INSERT INTO `tipo_equipo` (`SK_TIPO_EQUIPO`, `ST_TIPO_EQUIPO`) VALUES
(3, 'Equipo hiidraulico'),
(2, 'Herramientas'),
(1, 'Vehiculo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_servicio`
--

CREATE TABLE `tipo_servicio` (
  `SK_TIPO_SERVICIO` int(11) NOT NULL,
  `ST_TIPO_SERVICIO` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_servicio`
--

INSERT INTO `tipo_servicio` (`SK_TIPO_SERVICIO`, `ST_TIPO_SERVICIO`) VALUES
(1, 'Concreto y asfalto'),
(2, 'Renta de Equipo para terracería'),
(3, 'Renta de densímetro nuclear'),
(4, 'Transporte'),
(5, 'Levantamiento topográfico'),
(6, 'Estructuras metálicas'),
(7, 'Señalización vial'),
(8, 'Asesorías constructivas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transporte`
--

CREATE TABLE `transporte` (
  `SK_TRANSPORTE` int(11) NOT NULL,
  `NM_VOLUMEN` decimal(10,2) NOT NULL,
  `ST_UNIDAD_TRANSPORTE` varchar(50) NOT NULL,
  `FK_PROYECTO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `ST_DUI_USUARIO` varchar(10) NOT NULL,
  `ST_NIT_USUARIO` varchar(17) DEFAULT NULL,
  `ST_AFP_USUARIO` varchar(12) DEFAULT NULL,
  `ST_ISSS_USUARIO` varchar(9) DEFAULT NULL,
  `FC_NACIMIENTO` date NOT NULL,
  `FC_INGRESO_USUARIO` datetime(6) NOT NULL,
  `BN_ESTADO_USUARIO` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `ST_DUI_USUARIO`, `ST_NIT_USUARIO`, `ST_AFP_USUARIO`, `ST_ISSS_USUARIO`, `FC_NACIMIENTO`, `FC_INGRESO_USUARIO`, `BN_ESTADO_USUARIO`) VALUES
(1, 'pbkdf2_sha256$320000$uJ85nIukxkr2ZDCViMa5TK$OtHycPxyRxJXAFIPhJGGGgivG41/E9TYpNYzZkrjWW4=', '2023-06-20 23:07:22.979333', 1, 'Kevin24', 'Kevin Alejandro', 'Agreda Lemus', 'kevin.ale24@gmail.com', 1, 0, '2023-05-31 00:00:08.605631', '13213243-1', '2321-321312-321-1', '122222222222', '111111111', '2000-09-14', '2023-05-31 00:00:08.605631', 1),
(2, 'pbkdf2_sha256$320000$uJ85nIukxkr2ZDCViMa5TK$OtHycPxyRxJXAFIPhJGGGgivG41/E9TYpNYzZkrjWW4=', '2023-06-13 02:26:25.671710', 0, 'navarro', 'Gerardo', 'Navarro', 'ng20002@ues.edu.sv', 1, 1, '2023-05-31 00:02:51.961756', '12323123-2', '1312-321321-321-3', '131312321321', '121321312', '2005-06-10', '2023-05-31 00:02:51.961756', 0),
(3, 'pbkdf2_sha256$320000$NohoNriXUv0YwIhJjomP3T$kxQQUQqRhfOVHRVbKm/BaDaP8YGEk9o54pEVAGTAqeE=', '2023-05-31 02:07:52.351620', 0, 'mey', 'Meybel', 'Guardado', 'mey@gmail.com', 1, 0, '2023-05-31 00:03:31.640396', '12132432-4', '1323-213213-123-2', '111111111111', '111111111', '2005-06-12', '2023-05-31 00:03:31.640396', 1),
(4, 'pbkdf2_sha256$320000$h8amltyVaLNsMOhCrL9LF0$8WLrjji3ustkAl/myfAj273NpLVufgLQls524zlLOqA=', NULL, 0, 'Alexander', 'Edwin', 'Hernández', 'oxxa@gmail.com', 1, 0, '2023-05-31 00:05:03.477971', '11111111-1', '1111-111111-111-1', '111232132131', '123213213', '2005-06-12', '2023-05-31 00:05:03.477971', 1),
(8, 'pbkdf2_sha256$320000$Ap5wrFJ8Y4ouXaxdZXMC0P$/yO8cYVUyX8hyaaSIfBbFnslt/gWY4U8tafHJAe0GUw=', NULL, 0, 'marvin', 'Marvin', 'Ortiz', 'ortiz@gmail.com', 1, 1, '2023-05-31 00:16:09.026669', '12321321-3', '2131-231221-321-3', '123213213213', '111111111', '2005-06-12', '2023-05-31 00:16:09.026669', 1),
(9, 'pbkdf2_sha256$320000$RXSXOXrmbWYtxHV5ys5R5f$qX3RLTLPnw0iqa0m8Tk82etBODcZHnGsjZRCOMP5MgU=', NULL, 0, 'carlos', 'Carlos', 'Perez', 'dsadsa@gsfddgg.com', 1, 1, '2023-05-31 02:32:45.118427', '13223123-1', '1321-321312-321-3', '132132432432', NULL, '2005-06-12', '2023-05-31 02:32:45.118427', 1),
(10, 'pbkdf2_sha256$320000$VgTIv6JqdspMVrWphoILyW$Q/FlIkMQXSBB8VzOG+bty0mGbPEAPNacVN42MxUVX4Y=', '2023-06-01 01:10:46.684795', 0, 'KevinAg', 'Kevin', 'Agreda', 'kevin.ale4@gmail.com', 0, 1, '2023-06-01 01:10:30.137150', '12423424-2', '2132-4', '132132132131', '323123123', '2005-06-12', '2023-06-01 01:10:30.137150', 0),
(11, 'pbkdf2_sha256$320000$6VkKVWQ09XllO0CKzEU8Pp$qOPmBwymTeTX9CSPsyjjOEJW72r78CxHaq8bgasIGro=', NULL, 0, 'Kevin2', 'Gerardo Ernesto', 'Navarro Gochez', 'kevin.a24@gmail.com', 1, 1, '2023-06-06 03:17:53.371402', '13213123-1', '2131-231232-131-3', NULL, NULL, '2005-06-02', '2023-06-06 03:17:53.371402', 1),
(12, 'pbkdf2_sha256$320000$uJ85nIukxkr2ZDCViMa5TK$OtHycPxyRxJXAFIPhJGGGgivG41/E9TYpNYzZkrjWW4=', '2023-08-31 01:57:40.151780', 1, 'Kevin', 'Kevin', 'Agreda', 'aa20009@ues.edu.sv', 1, 1, '2023-06-06 03:17:53.371402', '06132123-1', NULL, NULL, NULL, '2005-06-12', '2023-06-06 03:17:53.371402', 1),
(13, 'pbkdf2_sha256$320000$eslHUVtdDWPkYPbPqRKeul$IONMwD++Hh8nrswRj9V4/ZlG0ZoMhar4AHIqtBZW5Lk=', '2023-06-14 03:20:34.851842', 0, 'DCarranza', 'Daniel', 'Carranza', 'dcarranza@gmail.com', 0, 1, '2023-06-11 17:42:26.974428', '12222222-2', '1232-320007-565-6', NULL, NULL, '2005-06-02', '2023-06-11 17:42:26.974428', 1),
(14, 'pbkdf2_sha256$320000$HT8aiPrnjtUYZfeO6geggz$cgMN0S+0ZDL5177KWD3NvHyEIJyrIlEmi4gL8aeB4Uw=', '2023-06-14 00:38:37.126096', 0, 'Mey2', 'Meybel', 'Guardado', 'mp20031@gmail.com', 0, 1, '2023-06-11 17:46:44.771760', '22222222-2', NULL, NULL, NULL, '2005-06-12', '2023-06-11 17:46:44.771760', 1),
(15, 'pbkdf2_sha256$320000$fN2RnZGc8O2cG0oTz3iwWF$ASjR83otJvjSINAOuBfexfvpfJNRLWWyIbFI51vzAac=', NULL, 0, 'Kevin123', 'sdfddsf', 'edf', '2432432@gmail.com', 1, 1, '2023-06-21 02:43:27.202033', '23423432-4', '3243-243243-241-1', NULL, NULL, '2005-06-09', '2023-06-21 02:43:27.202033', 1),
(16, 'pbkdf2_sha256$320000$bWRUVEhw0XYOENkQO60xyx$gQWuEDcB2n3ASRhXpIKIgRmTvWdijgkvqmXpLc0uV1c=', NULL, 0, 'Prueba1', 'Meybel1', '122432', 'kevin.ale224@gmail.com', 1, 1, '2023-06-21 02:44:21.313555', '21343243-4', '2143-424334-223-4', '343242343243', '243432432', '2005-06-01', '2023-06-21 02:44:21.313555', 1),
(17, 'pbkdf2_sha256$320000$A7UWcCspgyUaKFGnA52F1a$MNhp20J9vnK8roO62lML5nqxLaFKxPbPVTd+nTq1Plw=', NULL, 0, '1111', '111', '1111', 'edff34323@gmail.com', 1, 1, '2023-06-21 02:55:56.062461', '11111113-2', '2324-234343-243-4', NULL, NULL, '2005-06-08', '2023-06-21 02:55:56.062461', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_documento`
--

CREATE TABLE `usuario_documento` (
  `SK_DOC_USUARIO` int(11) NOT NULL,
  `ST_TIPO_DOC_USUARIO` varchar(50) NOT NULL,
  `ST_DOC_USUARIO` varchar(100) NOT NULL,
  `FK_USUARIO_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario_documento`
--

INSERT INTO `usuario_documento` (`SK_DOC_USUARIO`, `ST_TIPO_DOC_USUARIO`, `ST_DOC_USUARIO`, `FK_USUARIO_id`) VALUES
(1, 'DUI', 'doc_usuario/WhatsApp_Image_2023-02-13_at_8.46.43_PM.jpeg', 8),
(2, 'NIT', 'doc_usuario/mapa-turistico-de-el-salvador.jpg', 9),
(3, 'DUI', 'doc_usuario/el-salvador-mapa-politico-con-la-capital-san-salvador-las-fronteras-nacional_Dk2Xzo8.jpg', 9),
(4, 'NIT', 'doc_usuario/NIT.pdf', 1),
(6, 'DUI', 'doc_usuario/DUI_Xg6pMZJ.pdf', 13),
(7, 'NIT', 'doc_usuario/NIT_RiZxZOr.pdf', 10),
(8, 'DUI', 'doc_usuario/DUI_YEF4Bi0.jpg', 14),
(9, 'NIT', 'doc_usuario/NIT_3yvlbe1.pdf', 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_groups`
--

CREATE TABLE `usuario_groups` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario_groups`
--

INSERT INTO `usuario_groups` (`id`, `usuario_id`, `group_id`) VALUES
(11, 1, 1),
(16, 3, 1),
(17, 4, 1),
(18, 8, 1),
(19, 9, 1),
(9, 11, 1),
(21, 12, 1),
(23, 13, 2),
(24, 15, 1),
(25, 16, 1),
(26, 17, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_user_permissions`
--

CREATE TABLE `usuario_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asesoria_constructiva`
--
ALTER TABLE `asesoria_constructiva`
  ADD PRIMARY KEY (`SK_ASESORIA`),
  ADD KEY `asesoria_constructiv_FK_PROYECTO_id_082571ca_fk_proyecto_` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `asignacion_empleado`
--
ALTER TABLE `asignacion_empleado`
  ADD PRIMARY KEY (`SK_ASIG_EMPLEADO`),
  ADD KEY `asignacion_empleado_SK_PROYECTO_id_fa8ad7dc_fk_proyecto_` (`SK_PROYECTO_id`),
  ADD KEY `asignacion_empleado_FK_USUARIO_id_cbd1789a_fk_usuario_id` (`FK_USUARIO_id`);

--
-- Indices de la tabla `asignacion_equipo`
--
ALTER TABLE `asignacion_equipo`
  ADD PRIMARY KEY (`SK_ASIG_EQUIPO`),
  ADD KEY `asignacion_equipo_SK_PROYECTO_id_b36858b9_fk_proyecto_` (`SK_PROYECTO_id`),
  ADD KEY `asignacion_equipo_FK_EQUIPO_id_7761936b_fk_equipo_SK_EQUIPO` (`FK_EQUIPO_id`);

--
-- Indices de la tabla `asignacion_material`
--
ALTER TABLE `asignacion_material`
  ADD PRIMARY KEY (`SK_ASIG_MATERIAL`),
  ADD KEY `asignacion_material_SK_MATERIAL_id_245d30c9_fk_material_` (`SK_MATERIAL_id`),
  ADD KEY `asignacion_material_FK_PROYECTO_id_897da730_fk_proyecto_` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`SK_CLIENTE`),
  ADD UNIQUE KEY `ST_NOMBRE_CLIENTE` (`ST_NOMBRE_CLIENTE`),
  ADD UNIQUE KEY `ST_DOC_CLIENTE` (`ST_DOC_CLIENTE`),
  ADD UNIQUE KEY `ST_NIT_CLIENTE` (`ST_NIT_CLIENTE`),
  ADD KEY `cliente_FK_USUARIO_id_9bb34782_fk_usuario_id` (`FK_USUARIO_id`);

--
-- Indices de la tabla `concreto`
--
ALTER TABLE `concreto`
  ADD PRIMARY KEY (`SK_CONCRETO`),
  ADD KEY `concreto_FK_PROYECTO_id_7797d277_fk_proyecto_SK_PROYECTO` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_usuario_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`SK_EQUIPO`),
  ADD UNIQUE KEY `ST_NOMBRE_EQUIPO` (`ST_NOMBRE_EQUIPO`),
  ADD KEY `equipo_FK_TIPO_EQUIPO_id_0d2bd282_fk_tipo_equipo_SK_TIPO_EQUIPO` (`FK_TIPO_EQUIPO_id`);

--
-- Indices de la tabla `estado_proyecto`
--
ALTER TABLE `estado_proyecto`
  ADD PRIMARY KEY (`SK_ESTADO_PROYECTO`);

--
-- Indices de la tabla `estructura_metalica`
--
ALTER TABLE `estructura_metalica`
  ADD PRIMARY KEY (`SK_ESTRUCTURA_METALICA`),
  ADD KEY `estructura_metalica_FK_PROYECTO_id_4cb153cd_fk_proyecto_` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`SK_FACTURA`),
  ADD KEY `factura_FK_PROYECTO_id_90feabd6_fk_proyecto_SK_PROYECTO` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `levantamiento_topografico`
--
ALTER TABLE `levantamiento_topografico`
  ADD PRIMARY KEY (`SK_LEVANTAMIENTO_TOPOGRAFICO`),
  ADD KEY `levantamiento_topogr_FK_PROYECTO_id_75a65ed5_fk_proyecto_` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `material`
--
ALTER TABLE `material`
  ADD PRIMARY KEY (`SK_MATERIAL`),
  ADD UNIQUE KEY `ST_NOMBRE_MATERIAL` (`ST_NOMBRE_MATERIAL`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`SK_PROYECTO`),
  ADD KEY `proyecto_FK_CLIENTE_id_545d6051_fk_cliente_SK_CLIENTE` (`FK_CLIENTE_id`),
  ADD KEY `proyecto_FK_ESTADO_PROYECTO_i_70004694_fk_estado_pr` (`FK_ESTADO_PROYECTO_id`),
  ADD KEY `proyecto_FK_TIPO_SERVICIO_id_eecf0903_fk_tipo_serv` (`FK_TIPO_SERVICIO_id`),
  ADD KEY `proyecto_FK_USUARIO_id_ec11ee20_fk_usuario_id` (`FK_USUARIO_id`);

--
-- Indices de la tabla `renta_desimetro`
--
ALTER TABLE `renta_desimetro`
  ADD PRIMARY KEY (`SK_RENTA_DESIMETRO`),
  ADD KEY `renta_desimetro_FK_PROYECTO_id_e86ee1df_fk_proyecto_SK_PROYECTO` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `renta_equipo`
--
ALTER TABLE `renta_equipo`
  ADD PRIMARY KEY (`SK_RENTA_EQUIPO`),
  ADD KEY `renta_equipo_FK_PROYECTO_id_2f0c7d3b_fk_proyecto_SK_PROYECTO` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `senializacion_vial`
--
ALTER TABLE `senializacion_vial`
  ADD PRIMARY KEY (`SK_SENIALIZACION_VIAL`),
  ADD KEY `senializacion_vial_FK_PROYECTO_id_c3a00a57_fk_proyecto_` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `tipo_equipo`
--
ALTER TABLE `tipo_equipo`
  ADD PRIMARY KEY (`SK_TIPO_EQUIPO`),
  ADD UNIQUE KEY `ST_TIPO_EQUIPO` (`ST_TIPO_EQUIPO`);

--
-- Indices de la tabla `tipo_servicio`
--
ALTER TABLE `tipo_servicio`
  ADD PRIMARY KEY (`SK_TIPO_SERVICIO`);

--
-- Indices de la tabla `transporte`
--
ALTER TABLE `transporte`
  ADD PRIMARY KEY (`SK_TRANSPORTE`),
  ADD KEY `transporte_FK_PROYECTO_id_e272dde3_fk_proyecto_SK_PROYECTO` (`FK_PROYECTO_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `ST_DUI_USUARIO` (`ST_DUI_USUARIO`),
  ADD UNIQUE KEY `usuario_email_de9343f9_uniq` (`email`),
  ADD UNIQUE KEY `ST_NIT_USUARIO` (`ST_NIT_USUARIO`),
  ADD UNIQUE KEY `ST_AFP_USUARIO` (`ST_AFP_USUARIO`);

--
-- Indices de la tabla `usuario_documento`
--
ALTER TABLE `usuario_documento`
  ADD PRIMARY KEY (`SK_DOC_USUARIO`),
  ADD KEY `usuario_documento_FK_USUARIO_id_8a409ec7_fk_usuario_id` (`FK_USUARIO_id`);

--
-- Indices de la tabla `usuario_groups`
--
ALTER TABLE `usuario_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_groups_usuario_id_group_id_2e3cd638_uniq` (`usuario_id`,`group_id`),
  ADD KEY `usuario_groups_group_id_c67c8651_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `usuario_user_permissions`
--
ALTER TABLE `usuario_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_user_permissions_usuario_id_permission_id_3db58b8c_uniq` (`usuario_id`,`permission_id`),
  ADD KEY `usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asesoria_constructiva`
--
ALTER TABLE `asesoria_constructiva`
  MODIFY `SK_ASESORIA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asignacion_empleado`
--
ALTER TABLE `asignacion_empleado`
  MODIFY `SK_ASIG_EMPLEADO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `asignacion_equipo`
--
ALTER TABLE `asignacion_equipo`
  MODIFY `SK_ASIG_EQUIPO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asignacion_material`
--
ALTER TABLE `asignacion_material`
  MODIFY `SK_ASIG_MATERIAL` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `SK_CLIENTE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `concreto`
--
ALTER TABLE `concreto`
  MODIFY `SK_CONCRETO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `equipo`
--
ALTER TABLE `equipo`
  MODIFY `SK_EQUIPO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `estado_proyecto`
--
ALTER TABLE `estado_proyecto`
  MODIFY `SK_ESTADO_PROYECTO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `estructura_metalica`
--
ALTER TABLE `estructura_metalica`
  MODIFY `SK_ESTRUCTURA_METALICA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `SK_FACTURA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `levantamiento_topografico`
--
ALTER TABLE `levantamiento_topografico`
  MODIFY `SK_LEVANTAMIENTO_TOPOGRAFICO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `material`
--
ALTER TABLE `material`
  MODIFY `SK_MATERIAL` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `SK_PROYECTO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `renta_desimetro`
--
ALTER TABLE `renta_desimetro`
  MODIFY `SK_RENTA_DESIMETRO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `renta_equipo`
--
ALTER TABLE `renta_equipo`
  MODIFY `SK_RENTA_EQUIPO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `senializacion_vial`
--
ALTER TABLE `senializacion_vial`
  MODIFY `SK_SENIALIZACION_VIAL` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_equipo`
--
ALTER TABLE `tipo_equipo`
  MODIFY `SK_TIPO_EQUIPO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipo_servicio`
--
ALTER TABLE `tipo_servicio`
  MODIFY `SK_TIPO_SERVICIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `transporte`
--
ALTER TABLE `transporte`
  MODIFY `SK_TRANSPORTE` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `usuario_documento`
--
ALTER TABLE `usuario_documento`
  MODIFY `SK_DOC_USUARIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuario_groups`
--
ALTER TABLE `usuario_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `usuario_user_permissions`
--
ALTER TABLE `usuario_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asesoria_constructiva`
--
ALTER TABLE `asesoria_constructiva`
  ADD CONSTRAINT `asesoria_constructiv_FK_PROYECTO_id_082571ca_fk_proyecto_` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `asignacion_empleado`
--
ALTER TABLE `asignacion_empleado`
  ADD CONSTRAINT `asignacion_empleado_FK_USUARIO_id_cbd1789a_fk_usuario_id` FOREIGN KEY (`FK_USUARIO_id`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `asignacion_empleado_SK_PROYECTO_id_fa8ad7dc_fk_proyecto_` FOREIGN KEY (`SK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `asignacion_equipo`
--
ALTER TABLE `asignacion_equipo`
  ADD CONSTRAINT `asignacion_equipo_FK_EQUIPO_id_7761936b_fk_equipo_SK_EQUIPO` FOREIGN KEY (`FK_EQUIPO_id`) REFERENCES `equipo` (`SK_EQUIPO`),
  ADD CONSTRAINT `asignacion_equipo_SK_PROYECTO_id_b36858b9_fk_proyecto_` FOREIGN KEY (`SK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `asignacion_material`
--
ALTER TABLE `asignacion_material`
  ADD CONSTRAINT `asignacion_material_FK_PROYECTO_id_897da730_fk_proyecto_` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`),
  ADD CONSTRAINT `asignacion_material_SK_MATERIAL_id_245d30c9_fk_material_` FOREIGN KEY (`SK_MATERIAL_id`) REFERENCES `material` (`SK_MATERIAL`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_FK_USUARIO_id_9bb34782_fk_usuario_id` FOREIGN KEY (`FK_USUARIO_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `concreto`
--
ALTER TABLE `concreto`
  ADD CONSTRAINT `concreto_FK_PROYECTO_id_7797d277_fk_proyecto_SK_PROYECTO` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD CONSTRAINT `equipo_FK_TIPO_EQUIPO_id_0d2bd282_fk_tipo_equipo_SK_TIPO_EQUIPO` FOREIGN KEY (`FK_TIPO_EQUIPO_id`) REFERENCES `tipo_equipo` (`SK_TIPO_EQUIPO`);

--
-- Filtros para la tabla `estructura_metalica`
--
ALTER TABLE `estructura_metalica`
  ADD CONSTRAINT `estructura_metalica_FK_PROYECTO_id_4cb153cd_fk_proyecto_` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_FK_PROYECTO_id_90feabd6_fk_proyecto_SK_PROYECTO` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `levantamiento_topografico`
--
ALTER TABLE `levantamiento_topografico`
  ADD CONSTRAINT `levantamiento_topogr_FK_PROYECTO_id_75a65ed5_fk_proyecto_` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD CONSTRAINT `proyecto_FK_CLIENTE_id_545d6051_fk_cliente_SK_CLIENTE` FOREIGN KEY (`FK_CLIENTE_id`) REFERENCES `cliente` (`SK_CLIENTE`),
  ADD CONSTRAINT `proyecto_FK_ESTADO_PROYECTO_i_70004694_fk_estado_pr` FOREIGN KEY (`FK_ESTADO_PROYECTO_id`) REFERENCES `estado_proyecto` (`SK_ESTADO_PROYECTO`),
  ADD CONSTRAINT `proyecto_FK_TIPO_SERVICIO_id_eecf0903_fk_tipo_serv` FOREIGN KEY (`FK_TIPO_SERVICIO_id`) REFERENCES `tipo_servicio` (`SK_TIPO_SERVICIO`),
  ADD CONSTRAINT `proyecto_FK_USUARIO_id_ec11ee20_fk_usuario_id` FOREIGN KEY (`FK_USUARIO_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `renta_desimetro`
--
ALTER TABLE `renta_desimetro`
  ADD CONSTRAINT `renta_desimetro_FK_PROYECTO_id_e86ee1df_fk_proyecto_SK_PROYECTO` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `renta_equipo`
--
ALTER TABLE `renta_equipo`
  ADD CONSTRAINT `renta_equipo_FK_PROYECTO_id_2f0c7d3b_fk_proyecto_SK_PROYECTO` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `senializacion_vial`
--
ALTER TABLE `senializacion_vial`
  ADD CONSTRAINT `senializacion_vial_FK_PROYECTO_id_c3a00a57_fk_proyecto_` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `transporte`
--
ALTER TABLE `transporte`
  ADD CONSTRAINT `transporte_FK_PROYECTO_id_e272dde3_fk_proyecto_SK_PROYECTO` FOREIGN KEY (`FK_PROYECTO_id`) REFERENCES `proyecto` (`SK_PROYECTO`);

--
-- Filtros para la tabla `usuario_documento`
--
ALTER TABLE `usuario_documento`
  ADD CONSTRAINT `usuario_documento_FK_USUARIO_id_8a409ec7_fk_usuario_id` FOREIGN KEY (`FK_USUARIO_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `usuario_groups`
--
ALTER TABLE `usuario_groups`
  ADD CONSTRAINT `usuario_groups_group_id_c67c8651_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `usuario_groups_usuario_id_161fc80c_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `usuario_user_permissions`
--
ALTER TABLE `usuario_user_permissions`
  ADD CONSTRAINT `usuario_user_permiss_permission_id_a8893ce7_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `usuario_user_permissions_usuario_id_693d9c50_fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
