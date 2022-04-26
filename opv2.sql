SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

Drop database opv2;
create database opv2;
use opv2;
--
-- Databáze: `opv2`
--

-- --------------------------------------------------------

-- --------------------------------------------------------

--
-- Struktura tabulky `den_praxe`
--

CREATE TABLE `den_praxe` (
  `Id_den` int(11) NOT NULL,
  `stav` enum('pracovni','vikend','vylouceny') DEFAULT 'pracovni',
  `praxe` int(11) DEFAULT NULL,
  `datum` date DEFAULT NULL,
  `nadpis` varchar(255) DEFAULT NULL,
  `pocet_hodin` int(11) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `znalost` varchar(255) DEFAULT NULL,
  `cinnost` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Struktura tabulky `firma`
--

CREATE TABLE `firma` (
  `Id_firma` int(11) NOT NULL,
  `stav` enum('schvalena','akceptovatelna','ceka_na_schvaleni','archiv') DEFAULT 'ceka_na_schvaleni',
  `nazev` varchar(30) NOT NULL,
  `ICO` int(20) NOT NULL,
  `mesto_vykon` varchar(50) DEFAULT NULL,
  `ulice_vykon` varchar(50) DEFAULT NULL,
  `psc_vykon` int(11) DEFAULT NULL,
  `mesto_sidlo` varchar(50) DEFAULT NULL,
  `ulice_sidlo` varchar(50) DEFAULT NULL,
  `psc_sidlo` int(11) DEFAULT NULL,
  `IT` tinyint(1) DEFAULT NULL,
  `ELE` tinyint(1) DEFAULT NULL,
  `PROJEKT` tinyint(1) DEFAULT NULL,
  `VOS` tinyint(1) DEFAULT NULL,
  `zastupce` varchar(20) DEFAULT NULL,
  `web` varchar(30) DEFAULT NULL,
  `cinnost` text DEFAULT NULL,
  `pomucky` text DEFAULT NULL,
  `poznamka` text DEFAULT NULL
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `firma`
--

INSERT INTO `firma` (`Id_firma`, `stav`, `nazev`, `ICO`, `mesto_vykon`, `ulice_vykon`, `psc_vykon`,`mesto_sidlo`, `ulice_sidlo`, `psc_sidlo`, `IT`, `ELE`, `PROJEKT`, `VOS`, `zastupce`, `web`) VALUES
(1, 'schvalena', 'Algorit', 123, 'Písek', 'Za Nádražím 2723', 39701, 'Písek', 'Za Nádražím 2723', 39701, 1, 1, 0, NULL, NULL, NULL),
(2, 'akceptovatelna', 'Seznam', 456, 'Praha', 'Radlická 3294/10', 15000, 'Praha', 'Radlická 3294/10', 15000, 0, 1, 1, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktura tabulky `instruktor`
--

CREATE TABLE `instruktor` (
  `Id_instruktor` int(11) NOT NULL,
  `stav` enum('aktivni','smazany') DEFAULT 'aktivni',
  `jmeno` varchar(20) NOT NULL,
  `prijmeni` varchar(20) NOT NULL,
  `firma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabulky `obor`
--

CREATE TABLE `obor` (
  `Id_obor` int(11) NOT NULL,
  `stav` enum('aktivni','smazany') DEFAULT 'aktivni',
  `nazev` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `obor`
--

INSERT INTO `obor` (`Id_obor`, `stav`, `nazev`) VALUES
(1, 'smazany', 'SPŠ Elektrotechnika - Komerční elektrotechnika'),
(2, 'aktivni', 'SPŠ Elektrotechnika - Elektronické řídící systémy'),
(3, 'smazany', 'SPŠ Elektrotechnika - Informační a komunikační technologie'),
(4, 'aktivni', 'SPŠ Elektrotechnika - Počítačové projektování'),
(5, 'aktivni', 'SPŠ Informační technologie - Operační systémy a programování SW aplikací'),
(6, 'smazany', 'SPŠ Informační technologie - Manažerská informatika'),
(7, 'smazany', 'VOŠ Přenos a zpracování informací');

-- --------------------------------------------------------

--
-- Struktura tabulky `opravneni`
--

CREATE TABLE `opravneni` (
  `Id_opravneni` int(11) NOT NULL,
  `nazev` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `opravneni`
--

INSERT INTO `opravneni` (`Id_opravneni`, `nazev`) VALUES
(1, 'Admin'),
(3, 'Ucitel'),
(2, 'Zak');

-- --------------------------------------------------------

--
-- Struktura tabulky `praxe`
--

CREATE TABLE `praxe` (
  `Id_praxe` int(11) NOT NULL,
  `firma` int(11) DEFAULT NULL,
  `zak` int(11) NOT NULL,
  `instruktor` int(11) DEFAULT NULL,
  `ucitel` int(11) DEFAULT NULL,
  `trida` int(11) NOT NULL,
  `od` date NOT NULL,
  `do` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabulky `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `session_id` varchar(255) DEFAULT NULL,
  `data` blob DEFAULT NULL,
  `expiry` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Struktura tabulky `trida`
--

CREATE TABLE `trida` (
  `Id_trida` int(11) NOT NULL,
  `nazev` varchar(5) NOT NULL,
  `rok_nastupu` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `trida`
--

INSERT INTO `trida` (`Id_trida`, `nazev`, `rok_nastupu`) VALUES
(1, 'C4', 2018),
(2, 'B4', 2018),
(3, 'A2', 2020),
(4, 'A3', 2019),
(5, 'C2', 2020),
(6, 'C3', 2019),
(7, 'A4', 2018),
(8, 'B3', 2019),
(9, 'B1', 2021),
(10, 'B2', 2020),
(11, 'A1', 2021),
(12, 'C1', 2021),
(13, 'V3', 2018),
(14, 'D1', 2021),
(15, 'D2', 2020),
(16, 'D3', 2019),
(17, 'D4', 2018);

-- --------------------------------------------------------

--
-- Struktura tabulky `uzivatel`
--

CREATE TABLE `uzivatel` (
  `Id_uzivatel` int(11) NOT NULL,
  `stav` enum('aktivni','smazany') DEFAULT 'aktivni',
  `jmeno` varchar(20) DEFAULT NULL,
  `prijmeni` varchar(20) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  `telefon` bigint(20) DEFAULT NULL,
  `dat_nar` date DEFAULT NULL,
  `opravneni` int(11) NOT NULL,
  `obor` int(11) DEFAULT NULL,
  `ulice` varchar(50) DEFAULT NULL,
  `mesto` varchar(50) DEFAULT NULL,
  `psc` int(5) DEFAULT NULL,
  `aktualni_trida` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `uzivatel`
--

INSERT INTO `uzivatel` (`Id_uzivatel`, `stav`, `jmeno`, `prijmeni`, `email`, `telefon`, `dat_nar`, `opravneni`, `obor`, `ulice`, `mesto`, `psc`, `aktualni_trida`) VALUES
(1, 'aktivni', 'Dominik', 'Smola', 'dsmola9@gmail.com', 1, '2021-12-14', 1, 5, NULL, NULL, NULL, NULL),
(213, 'aktivni', 'Dominik', 'Smola', 'dsmola@sps-pi.cz', NULL, NULL, 2, NULL, NULL, NULL, NULL, 8);



CREATE TABLE `tokens` (
  `token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `firma`
--
ALTER TABLE `firma`
  ADD PRIMARY KEY (`Id_firma`),
  ADD UNIQUE KEY `firma_ICO_uindex` (`ICO`);

--
-- Indexy pro tabulku `instruktor`
--
ALTER TABLE `instruktor`
  ADD PRIMARY KEY (`Id_instruktor`),
  ADD KEY `instruktor_firma_Id_firma_fk` (`firma`);

--
-- Indexy pro tabulku `obor`
--
ALTER TABLE `obor`
  ADD PRIMARY KEY (`Id_obor`),
  ADD UNIQUE KEY `obor_nazev_uindex` (`nazev`);

--
-- Indexy pro tabulku `opravneni`
--
ALTER TABLE `opravneni`
  ADD PRIMARY KEY (`Id_opravneni`),
  ADD UNIQUE KEY `opravneni_nazev_uindex` (`nazev`);

--
-- Indexy pro tabulku `praxe`
--
ALTER TABLE `praxe`
  ADD PRIMARY KEY (`Id_praxe`),
  ADD KEY `praxe_uzivatel_Id_uzivatel_fk` (`zak`),
  ADD KEY `praxe_firma_Id_firma_fk` (`firma`),
  ADD KEY `praxe_instruktor_Id_instruktor_fk` (`instruktor`);

--
-- Indexy pro tabulku `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `session_id` (`session_id`);

--
-- Indexy pro tabulku `trida`
--
ALTER TABLE `trida`
  ADD PRIMARY KEY (`Id_trida`);

--
-- Indexy pro tabulku `uzivatel`
--
ALTER TABLE `uzivatel`
  ADD PRIMARY KEY (`Id_uzivatel`),
  ADD UNIQUE KEY `uzivatel_email_uindex` (`email`),
  ADD UNIQUE KEY `uzivatel_telefon_uindex` (`telefon`),
  ADD KEY `uzivatel_opravneni_Id_opravneni_fk` (`opravneni`),
  ADD KEY `uzivatel_obor_Id_obor_fk` (`obor`),
  ADD KEY `uzivatel_trida_Id_trida_fk` (`aktualni_trida`);

--
-- Indexy pro tabulku `den_praxe`
--
ALTER TABLE `den_praxe`
  ADD PRIMARY KEY (`Id_den`),
  ADD KEY `den_praxe_praxe_Id_praxe_fk` (`praxe`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `firma`
--
ALTER TABLE `firma`
  MODIFY `Id_firma` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `instruktor`
--
ALTER TABLE `instruktor`
  MODIFY `Id_instruktor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `obor`
--
ALTER TABLE `obor`
  MODIFY `Id_obor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `opravneni`
--
ALTER TABLE `opravneni`
  MODIFY `Id_opravneni` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `praxe`
--
ALTER TABLE `praxe`
  MODIFY `Id_praxe` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `trida`
--
ALTER TABLE `trida`
  MODIFY `Id_trida` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `uzivatel`
--
ALTER TABLE `uzivatel`
  MODIFY `Id_uzivatel` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `den_praxe`
--
ALTER TABLE `den_praxe`
  MODIFY `Id_den` int(11) NOT NULL AUTO_INCREMENT;

--
-- Omezení pro exportované tabulky
--


--
-- Omezení pro exportované tabulky
--

--
-- Omezení pro tabulku `instruktor`
--
ALTER TABLE `instruktor`
  ADD CONSTRAINT `instruktor_firma_Id_firma_fk` FOREIGN KEY (`firma`) REFERENCES `firma` (`Id_firma`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Omezení pro tabulku `praxe`
--
ALTER TABLE `praxe`
  ADD CONSTRAINT `praxe_firma_Id_firma_fk` FOREIGN KEY (`firma`) REFERENCES `firma` (`Id_firma`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `praxe_instruktor_Id_instruktor_fk` FOREIGN KEY (`instruktor`) REFERENCES `instruktor` (`Id_instruktor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `praxe_uzivatel_Id_uzivatel_fk` FOREIGN KEY (`zak`) REFERENCES `uzivatel` (`Id_uzivatel`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `praxe_uzivatel_Id_uzivatel_fk_2` FOREIGN KEY (`ucitel`) REFERENCES `uzivatel` (`Id_uzivatel`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Omezení pro tabulku `uzivatel`
--
ALTER TABLE `uzivatel`
  ADD CONSTRAINT `uzivatel_obor_Id_obor_fk` FOREIGN KEY (`obor`) REFERENCES `obor` (`Id_obor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `uzivatel_opravneni_Id_opravneni_fk` FOREIGN KEY (`opravneni`) REFERENCES `opravneni` (`Id_opravneni`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `uzivatel_trida_Id_trida_fk` FOREIGN KEY (`aktualni_trida`) REFERENCES `trida` (`Id_trida`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Omezení pro tabulku `den_praxe`
--
ALTER TABLE `den_praxe`
  ADD CONSTRAINT `den_praxe_praxe_Id_praxe_fk` FOREIGN KEY (`praxe`) REFERENCES `praxe` (`Id_praxe`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
