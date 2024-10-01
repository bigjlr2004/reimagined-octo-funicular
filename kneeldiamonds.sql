CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` TEXT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` FLOAT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL, 
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
	FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),    
	FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)    

);

INSERT INTO `Metals`VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals`VALUES (null, '14K Gold', 736.40);
INSERT INTO `Metals`VALUES (null, '24K Gold', 1258.90);
INSERT INTO `Metals`VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metals`VALUES (null, 'Palladium', 1241);

INSERT INTO `Sizes`VALUES (null, .5, 405);
INSERT INTO `Sizes`VALUES (null, .75, 782);
INSERT INTO `Sizes`VALUES (null, 1, 1470);
INSERT INTO `Sizes`VALUES (null, 1.5, 1997);
INSERT INTO `Sizes`VALUES (null, 2, 3638);

INSERT INTO `Styles`VALUES (null, 'Classic', 500);
INSERT INTO `Styles`VALUES (null, 'Modern', 710);
INSERT INTO `Styles`VALUES (null, 'Vintage', 965);

INSERT INTO `Orders`VALUES (null, 4, 1, 1);
INSERT INTO `Orders`VALUES (null, 5, 2, 2);
INSERT INTO `Orders`VALUES (null, 2, 3, 5);
INSERT INTO `Orders`VALUES (null, 3, 1, 3);
INSERT INTO `Orders`VALUES (null, 1, 2, 4);
INSERT INTO `Orders`VALUES (null, 5, 3, 5);



-- SELECT ALL ORDERS
 SELECT
            id,
            metal_Id,
            size_Id,
            style_Id
        FROM Orders