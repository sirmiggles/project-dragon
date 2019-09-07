/*	
	==========================================================
	FILE:			unigames_schema.sql
	AUTHOR:			TABADERO, MIGUEL ARIES SAMBAT (22240204)
	(C):			2019
	DATE CREATED:	20/8/2019
	LAST MODIFIED:	22/8/2019
	==========================================================
	**!!	 WARNING	!!**
	**	SQL Script must be run using SQLCMD mode in SSMS	**
*/

#	:setvar DBName "unigames_schema"

/*
	==========================================================
					CREATING THE TABLES
	==========================================================
*/

CREATE DATABASE IF NOT EXISTS unigames;
USE  unigames;
DROP TABLE IF EXISTS
	Loan, ItemTag, Game, Book, CardGame, Miscellaneous, ItemGenre, ItemEquipment, MemberInterest,
    ItemMechanic, Mechanic, Transactions, Genre, Equipment, Tag, Interest, Reservations, Item,
    ItemType, NonMember, ClubMember, ClubRank, Collection, Users
;

#	Table for the Items	#
CREATE TABLE  Item  (
	 ItemID 			INT PRIMARY KEY NOT NULL AUTO_INCREMENT,				# 	PK for Items
     ItemTitle 			VARCHAR(256) NOT NULL,									#	Name/Title of the Item 
	 ItemType 			INT NOT NULL,											# 	FK from ItemType Table - Describes if it is a book, boardgame, etc.	(Mainly used for IF, Procedure)
	 ItemDescription	VARCHAR(1024) DEFAULT 'N/A',							#	General description of the Item
     ItemCondition 		ENUM('EXCELLENT','VERY GOOD','GOOD','FAIR','BAD'),		#	Item's condition
     Available 			BOOL NOT NULL DEFAULT TRUE,								#	Boolean for availability of the item 
	 Collection 		INT DEFAULT NULL,										#	FK from Collection Table - Describes which collection the item belongs to
	 Notes 				VARCHAR(1024) DEFAULT 'N/A'								#	Item notes, e.g. is the item missing pieces?
);

#	Reference Table for Games (MAIN STORAGE OF GAME INFORMATION)
CREATE TABLE  Game  (
	 GameID 		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,					#	PK for Game SubType Table
	 GameItemID 	INT UNIQUE NOT NULL,										#	FK from Item Table
	 MinPlayers 	INT DEFAULT 2,												#	Minimum number of players to be able to play a proper game
	 MaxPlayers 	INT DEFAULT 4,												#	Maximum number of players to be able to play a proper game
	 MinGameLength 	VARCHAR(16),												#	Minimum length of the game
     MaxGameLength 	VARCHAR(16)													#	Maximum length of the game
);

#	Reference Table for Books (MAIN STORAGE OF BOOK INFORMATION)
CREATE TABLE  Book  (
	 BookID 		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,					#	PK for Book SubType Table
	 BookItemID 	INT UNIQUE NOT NULL,										#	FK from Item Table
     ISBN			VARCHAR(16) DEFAULT NULL									#	ISBN of the book
);

#	Reference Table for Card Games (MAIN STORAGE OF CARD GAME INFORMATION)
CREATE TABLE CardGame	(
	CardGameID		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,					#	PK for the CardGame Table
    CardGameItemID	INT UNIQUE NOT NULL,										#	FK from the Item Table
    MinPlayers 	INT DEFAULT 2,													#	Minimum number of players to be able to play a proper game
	MaxPlayers 	INT DEFAULT 4													#	Maximum number of players to be able to play a proper game
);

#	Reference Table for Card Games (MAIN STORAGE OF CARD GAME INFORMATION)
CREATE TABLE Miscellaneous	(
	MiscID		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,						#	PK for the Miscellaneous Table
    MiscItemID	INT UNIQUE NOT NULL												#	FK from the Item Table
);

#	Reference Table for the Collection an Item belongs to
CREATE TABLE  Collection  (
	 CollectionID 		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,				#	PK for Collection Table					
	 CollectionName 	VARCHAR(32) NOT NULL									#	Name of the collection
);

#	Reference Table for Categories (Board Game, Book, etc)	#
CREATE TABLE  ItemType  (
	 TypeID 	INT PRIMARY KEY NOT NULL AUTO_INCREMENT ,				#	PK of the ItemType Table
	 TypeName 	VARCHAR(255) NOT NULL									#	Name of the category (should be updated w.r.t. SubTypes of the Item Table)
);

#	Table containing Genres (Family, RPG, TCG, etc.)
CREATE TABLE  Genre  (
	 GenreID 		INT PRIMARY KEY NOT NULL AUTO_INCREMENT ,			#	PK of the Genre Table
	 GenreName 		VARCHAR(255) NOT NULL								#	Name of the genre
);

#	Link Table between Genres and Items
CREATE TABLE ItemGenre	(
	GenreID		INT NOT NULL,											#	FK from the Genre Table
	ItemID 		INT NOT NULL											#	FK from the Item Table
);

#	Table containing names of various (game) mechanics of an Item
CREATE TABLE  Mechanic  (
	MechanicID				INT PRIMARY KEY NOT NULL AUTO_INCREMENT,				#	PK for the Mechanics Table
    MechanicName			VARCHAR(255) NOT NULL,									#	Name of the Mechanic
    MechanicDescription		VARCHAR(1024) NOT NULL									#	Brief description of what the mechanic entails
);

#	Link Table between Item and Mechanic
CREATE TABLE  ItemMechanic  (
	ItemID 			INT NOT NULL,												#	FK from the Item Table	
	MechanicID		INT NOT NULL												#	FK from the Mechanic Table					
);

#	Table containing information about Equipment
CREATE TABLE Equipment	(
	EquipmentID		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,			#	PK of the Equipment Table
    EquipmentName	VARCHAR(255) NOT NULL,								#	Name of the Equipment Item
	Notes			VARCHAR(1024) DEFAULT 'N/A'							#	Extra Notes on the Equipment
);

#	Link Table between Equipment and Item
CREATE TABLE ItemEquipment	(
	ItemID			INT NOT NULL,												#	FK from the Item Table
    EquipmentID		INT NOT NULL											#	FK from the Equipment Table
);

#	Table containing member data (raw - no logins yet)
CREATE TABLE  ClubMember  (
	 MemberID 			INT PRIMARY KEY NOT NULL AUTO_INCREMENT,				#	PK of the ClubMember Table
	 FirstName 			VARCHAR(255) NOT NULL,									#	First Name of the member
	 Surname 			VARCHAR(255) NOT NULL,									#	Surname of the member
     PreferredName 		VARCHAR(255),											#   Preferred name - to be updated by a trigger to equal FirstName if NULL
	 PreferredPronoun 	VARCHAR(8) DEFAULT 'N/A',								#	Preferred pronoun of member
     MemberRank 		INT NOT NULL,											#	FK from ClubRank Table - Member permissions and status 
     GuildMember   	 	BOOLEAN DEFAULT FALSE,									#	Guild Membership (also for non-students!)
     UniversityID		VARCHAR(8) DEFAULT NULL,								#	UWA Student or Staff ID			
     JoinDate      	 	DATETIME DEFAULT NOW(),									#   Datetime when member is added to the Table
     Email				VARCHAR(255) NOT NULL,									#   Email address is mandatory (can be changed)
     PhoneNumber		VARCHAR(20) NOT NULL,									# 	Phone Number of the member
     Incidents			VARCHAR(255) DEFAULT 'N/A',								#   Comments about previous bad behaviour
     UserID				INT NOT NULL											#	FK from Users Table
);

CREATE TABLE NonMember	(
	NonMemberID			INT PRIMARY KEY NOT NULL AUTO_INCREMENT,				#	PK of the NonMember Table
    FirstName			VARCHAR(255) NOT NULL,									#	First Name 
    Surname 			VARCHAR(255) NOT NULL,									#	Surname 			
	OrganizationName 	VARCHAR(255) DEFAULT NULL,								#	Name of the club or Organization
    Email				VARCHAR(255) NOT NULL,									#   Email address of the non-member or organization
	PhoneNumber			VARCHAR(20) NOT NULL,									# 	Phone Number of the non-member or organization
    UserID				INT NOT NULL											#	FK from Users Table
);

#	Table which generalizes a user and represents both members and non-members/organizations
CREATE TABLE Users	(
	UserID			INT PRIMARY KEY NOT NULL AUTO_INCREMENT						#	PK of the Users Table
);

#	Table which contains various possible member interests
CREATE TABLE Interest (
	InterestID		INT PRIMARY KEY NOT NULL AUTO_INCREMENT ,					#	PK for Interest Table
	InterestName	VARCHAR(32)													#	Name of the interest ('Card Games', 'RPGs', etc.)
);

#	Link Table to Member Interests
CREATE TABLE MemberInterest (
	MemberID 		INT NOT NULL,												#	FK from the ClubMember Table
	InterestID		INT NOT NULL												# 	FK from the Interest Table
);

#	Reference Table for Membership Status and Permissions	
CREATE TABLE  ClubRank  (
	 RankID 		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,					#	PK for the ClubRank Table
	 RankName 		VARCHAR(32)	NOT NULL										#	Name of membership rank ('Ordinary Member', 'Gatekeeper', etc.)
);

#	Transaction Table for Borrowings (Main Library Table)
CREATE TABLE  Transactions  (
	 TransactionID  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,					#	PK for the Transactions Table
	 BorrowerID 	INT NOT NULL,												#	FK from Users Table - Which member borrowed it?
	 ApproverID 	INT NOT NULL,												#	FK from Users Table - Which member approved the transaction?
	 DateBorrowed 	DATETIME NOT NULL,											#	Date which the item was borrowed
     DueDate		DATETIME NOT NULL, 											#	Date when the item is due to be returned
	 ReturnConfirmerID 	INT DEFAULT NULL,										#	FK from Users Table - Which member confirmed the item return? (default NULL, as it may have not been returned)
     DateReturned 	DATETIME DEFAULT NULL										#	Date which item was returned (default NULL, as it may have not been returned)
);

#	Table for Tracking Item Borrowings
CREATE TABLE   Loan  (
	 LoanID 					INT PRIMARY KEY NOT NULL AUTO_INCREMENT,		#	PK for the Loan Table
	 LoanTransactionID 			INT NOT NULL,									#	FK from Transaction Table - ID of the transaction that the Item was borrowed in
	 LoanItemID 				INT NOT NULL									#	FK from Item Table - ID of the Item that was borrowed
);

#	Table for Tracking Item Reservations
CREATE TABLE   Reservations  (
	ReservationID				INT PRIMARY KEY NOT NULL AUTO_INCREMENT,		#	PK for the Reservations Table								
	UserID						INT NOT NULL,									#	FK from Users Table - ID of user who wants to reserve an item
    ItemID						INT NOT NULL UNIQUE,							#	FK from Items Table - ID of item to be borrowed
    StartDate					DATETIME NOT NULL,								#	Earliest date where item shall no longer be borrowed to another user
    ExpiryDate					DATETIME NOT NULL								#	Latest date until reservation expires
    );

#	Reference Table for the Tags
CREATE TABLE   Tag  (
	 TagID 						INT PRIMARY KEY NOT NULL AUTO_INCREMENT,		#	PK for the Tag Table - Tag Identifier
	 TagName 					VARCHAR(32) NOT NULL							#	Tag name/descriptor for the tag
);

#	Link Table for Items and Tags
CREATE TABLE   ItemTag  (
	 TagID 			INT NOT NULL,												#	FK from Tag Table - ID of the tag
	 ItemID 		INT NOT NULL												#	FK from Item Table - ID of the item to be tagged
);

/*
	======================================================
	MAKING THE FOREIGN KEY LINKS FOR THE DB
	======================================================
*/

#	Link Club-Members and Non-Members to Borrower Table
ALTER TABLE ClubMember ADD CONSTRAINT FK_MemberBorrower
	FOREIGN KEY (UserID) REFERENCES Users(UserID)
    ON UPDATE CASCADE;
    
ALTER TABLE NonMember ADD CONSTRAINT FK_NonMemberBorrower
	FOREIGN KEY (UserID) REFERENCES Users(UserID)
    ON UPDATE CASCADE;
    
    
#	Link Reservations to users
ALTER TABLE Reservations ADD CONSTRAINT FK_UsersReservation
	FOREIGN KEY (UserID) REFERENCES Users(UserID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    
ALTER TABLE Reservations ADD CONSTRAINT FK_ItemReservation
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
    ON DELETE CASCADE ON UPDATE CASCADE;


#	Link subclasses to Item Table (Polymorphic Association)
ALTER TABLE  Game  ADD CONSTRAINT  FK_GameItemID 
	FOREIGN KEY ( GameItemID ) REFERENCES Item( ItemID )
    ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE  Book  ADD CONSTRAINT  FK_BookItemID 
	FOREIGN KEY ( BookItemID ) REFERENCES Item( ItemID )
    ON DELETE CASCADE ON UPDATE CASCADE;
    
ALTER TABLE  CardGame  ADD CONSTRAINT  FK_GardGameItemID 
	FOREIGN KEY ( CardGameItemID ) REFERENCES Item( ItemID )
    ON DELETE CASCADE ON UPDATE CASCADE;
    
ALTER TABLE  Miscellaneous  ADD CONSTRAINT  FK_MiscellaneousItemID 
	FOREIGN KEY ( MiscItemID ) REFERENCES Item( ItemID )
    ON DELETE CASCADE ON UPDATE CASCADE;


#	Link Item to the Categories, Genre
ALTER TABLE  Item  ADD CONSTRAINT  FK_ItemType 
	FOREIGN KEY ( ItemType ) REFERENCES ItemType( TypeID )
    ON UPDATE CASCADE;

ALTER TABLE  Item  ADD CONSTRAINT  FK_Collection 
	FOREIGN KEY ( Collection ) REFERENCES Collection( CollectionID )
    ON UPDATE CASCADE;
    
#	Link Item to Genre
ALTER TABLE  ItemGenre ADD CONSTRAINT FK_ItemItemGenre
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
    ON UPDATE CASCADE ON DELETE CASCADE;
    
ALTER TABLE  ItemGenre ADD CONSTRAINT FK_ItemGenreGenre
	FOREIGN KEY	(GenreID) REFERENCES Genre(GenreID)
    ON UPDATE CASCADE ON DELETE CASCADE;


#	Link Item to Mechanic
ALTER TABLE  ItemMechanic ADD CONSTRAINT FK_ItemItemMechanic
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
    ON UPDATE CASCADE ON DELETE CASCADE;
    
ALTER TABLE  ItemMechanic ADD CONSTRAINT FK_ItemMechanicMechanic
	FOREIGN KEY	(MechanicID) REFERENCES Mechanic(MechanicID)
    ON UPDATE CASCADE ON DELETE CASCADE;
    

#	Link Item to Equipment
ALTER TABLE  ItemEquipment ADD CONSTRAINT FK_ItemItemEquipment
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
    ON UPDATE CASCADE ON DELETE CASCADE;
    
ALTER TABLE  ItemEquipment ADD CONSTRAINT FK_ItemEquipmentEquipment
	FOREIGN KEY	(EquipmentID) REFERENCES Equipment(EquipmentID)
    ON UPDATE CASCADE ON DELETE CASCADE;    

#	Link Members to the Ranks
ALTER TABLE  ClubMember  ADD CONSTRAINT  FK_Rank 
	FOREIGN KEY ( MemberRank ) REFERENCES ClubRank( RankID )
    ON UPDATE CASCADE;


#	Link the transaction table to the members and items
ALTER TABLE  Transactions  ADD CONSTRAINT  FK_BorrowerID 
	FOREIGN KEY ( BorrowerID ) REFERENCES Users( UserID )
    ON UPDATE CASCADE;

ALTER TABLE  Transactions  ADD CONSTRAINT  FK_ApproverID 
	FOREIGN KEY ( ApproverID ) REFERENCES Users( UserID )
    ON UPDATE CASCADE;

ALTER TABLE  Transactions  ADD CONSTRAINT  FK_ReturnConfirmerID 
	FOREIGN KEY ( ReturnConfirmerID ) REFERENCES Users( UserID )
    ON UPDATE CASCADE;


#	Link the inventory to the transactions and item table
ALTER TABLE  Loan  ADD CONSTRAINT  FK_LoanTransactionID 
	FOREIGN KEY ( LoanTransactionID ) REFERENCES Transactions( TransactionID )
    ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE  Loan  ADD CONSTRAINT  FK_LoanItemID 
	FOREIGN KEY ( LoanItemID ) REFERENCES Item( ItemID )
    ON DELETE CASCADE ON UPDATE CASCADE;


#	Link the Tag and Items
ALTER TABLE  ItemTag  ADD CONSTRAINT  FK_ItemTagTag 
	FOREIGN KEY ( TagID ) REFERENCES Tag( TagID )
    ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE  ItemTag  ADD CONSTRAINT  FK_ItemTagItem 
	FOREIGN KEY ( ItemID ) REFERENCES Item( ItemID )
    ON DELETE CASCADE ON UPDATE CASCADE;
    
    
#	Link the Members and their interests
ALTER TABLE MemberInterest ADD CONSTRAINT FK_MIMember
	FOREIGN KEY ( MemberID ) REFERENCES ClubMember(MemberID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    
ALTER TABLE MemberInterest ADD CONSTRAINT FK_MIInterest
	FOREIGN KEY (InterestID) REFERENCES Interest(InterestID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    
 
 /*
	==========================================================
					TRIGGERS FOR INSERTION
	==========================================================
*/
    
#Trigger to encrypt the email address and phone number of a Club Member    
DELIMITER ++
CREATE TRIGGER EncryptMember 
BEFORE UPDATE ON ClubMember 
FOR EACH ROW BEGIN
    SET NEW.Email = ENCRYPT(NEW.Email, 'key');
    SET NEW.PhoneNumber = ENCRYPT(NEW.PhoneNumber, 'key');
END++
DELIMITER ;


#Trigger to encrypt the email address and phone number of a Non-Member    
DELIMITER ++
CREATE TRIGGER EncryptNonMember
BEFORE UPDATE ON NonMember 
FOR EACH ROW BEGIN
    SET NEW.Email = ENCRYPT(NEW.Email, 'key');
    SET NEW.PhoneNumber = ENCRYPT(NEW.PhoneNumber, 'key');
END++
DELIMITER ;
    
    
    
/*
	==========================================================
					INSERTING TEST DATA
	==========================================================
*/

INSERT INTO ClubRank VALUES (NULL,'Regular Member');
INSERT INTO ClubRank VALUES (NULL,'Gatekeeper');
INSERT INTO ClubRank VALUES (NULL,'Committee Member');

INSERT INTO Interest VALUES (NULL,'Card Games');
INSERT INTO Interest VALUES (NULL,'RPGs');
INSERT INTO Interest VALUES (NULL,'War Games');
INSERT INTO Interest VALUES (NULL,'Board Games');

INSERT INTO Users VALUES (NULL);
INSERT INTO ClubMember VALUES (NULL, 'John', 'Rupert', NULL, DEFAULT, 1, FALSE, 22559471, DEFAULT, 'john.rupert@hello.bye', '0452587195', DEFAULT, 1);
INSERT INTO Users VALUES (NULL);
INSERT INTO ClubMember VALUES (NULL, 'Jake', 'Bonsonby', NULL, DEFAULT, 3, TRUE, 20718595, DEFAULT, 'jake.bonsonby@au.revoir', '0449527195', 'Destroyed several items in 2017', 2);
INSERT INTO Users VALUES (NULL);
INSERT INTO ClubMember VALUES (NULL, 'Alberta', 'Frederiksen', NULL, DEFAULT, 2, FALSE, 20182019, DEFAULT, 'alberta.frederiksen@bon.jour', '0478985195', DEFAULT, 3);
INSERT INTO Users VALUES (NULL);
INSERT INTO ClubMember VALUES (NULL, 'Ilanah', 'Johnson', NULL, DEFAULT, 1, TRUE, 20172018, DEFAULT, 'ilanah.johnson@guten.tag', '0452498565', DEFAULT, 4);

INSERT INTO MemberInterest VALUES (1,1);
INSERT INTO MemberInterest VALUES (1,2);
INSERT INTO MemberInterest VALUES (1,4);
INSERT INTO MemberInterest VALUES (2,3);
INSERT INTO MemberInterest VALUES (3,2);
INSERT INTO MemberInterest VALUES (3,3);
INSERT INTO MemberInterest VALUES (3,4);
INSERT INTO MemberInterest VALUES (4,1);
INSERT INTO MemberInterest VALUES (4,4);


/*
	==========================================================
					TEST QUERIES
	==========================================================
*/

/*Which Members have which interests?
SELECT ClubMember.MemberID, FirstName, Surname, InterestName 
FROM ClubMember JOIN MemberInterest ON (ClubMember.MemberID = MemberInterest.MemberID)
				JOIN Interest ON (MemberInterest.InterestID = Interest.InterestID)
ORDER BY ClubMember.MemberID;

#Which Members have which rank?
SELECT ClubMember.MemberID, FirstName, Surname, RankName
FROM ClubMember JOIN ClubRank ON (ClubMember.MemberRank = ClubRank.RankID )
ORDER BY ClubMember.MemberID;


