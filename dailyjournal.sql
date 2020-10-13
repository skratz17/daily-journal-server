CREATE TABLE `Moods` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `value` INTEGER NOT NULL,
  `label` TEXT NOT NULL
);

CREATE TABLE `Entries` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `date` TEXT NOT NULL,
  `entry` TEXT NOT NULL,
  `moodId` INTEGER NOT NULL,
  FOREIGN KEY(`moodId`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Concepts` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL
);

CREATE TABLE `EntryConcepts` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `entryId` INTEGER NOT NULL,
  `conceptId` INTEGER NOT NULL,
  FOREIGN KEY(`entryId`) REFERENCES `Entry`(`id`),
  FOREIGN KEY(`conceptId`) REFERENCES `Concept`(`id`)
);

INSERT INTO `Moods` VALUES (null, 0, "👿");
INSERT INTO `Moods` VALUES (null, 1, "🤬");
INSERT INTO `Moods` VALUES (null, 2, "😡");
INSERT INTO `Moods` VALUES (null, 3, "😭");
INSERT INTO `Moods` VALUES (null, 4, "😕");
INSERT INTO `Moods` VALUES (null, 5, "🙃");
INSERT INTO `Moods` VALUES (null, 6, "🙂");
INSERT INTO `Moods` VALUES (null, 7, "😀");
INSERT INTO `Moods` VALUES (null, 8, "😁");
INSERT INTO `Moods` VALUES (null, 9, "🤠");

INSERT INTO `Concepts` VALUES (null, "sqlite");
INSERT INTO `Concepts` VALUES (null, "python");
INSERT INTO `Concepts` VALUES (null, "classes");

INSERT INTO `Entries` VALUES (null, "2020-10-13", "Setting up the Daily Journal database in Python.", 8);
INSERT INTO `Entries` VALUES (null, "2020-10-12", "We started talking about classes and shit", 10);

INSERT INTO `EntryConcepts` VALUES (null, 1, 1);
INSERT INTO `EntryConcepts` VALUES (null, 1, 2);
INSERT INTO `EntryConcepts` VALUES (null, 2, 2);
INSERT INTO `EntryConcepts` VALUES (null, 2, 3);