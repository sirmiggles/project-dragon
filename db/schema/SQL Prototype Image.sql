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
	 Loan ,  Transactions ,  Game ,  Book ,  Genre , ClubMember ,  ClubRank ,  Item ,  ItemType ,  Collection, Tag, ItemTag
;

#	Table for the Items	#
CREATE TABLE  Item  (
	 ItemID 		INT PRIMARY KEY NOT NULL AUTO_INCREMENT,			# Primary Key for Items
	 ItemType 			INT NOT NULL,										# Item Type - book, boardgame, etc.	(FK) (Mainly used for IF, Procedure)
	 Available 		TINYINT NOT NULL DEFAULT 0,							#	Is the item available? 0 = True, 1 = False
	 Collection 	INT DEFAULT 0,										#	Which collection the item belongs to (FK)
	 Notes 			VARCHAR(1024) DEFAULT 'N/A'							#	Item notes, e.g. is the item missing pieces?
);

#	Reference Table for Games (MAIN STORAGE OF GAME INFORMATION)
CREATE TABLE  Game  (
	 GameID 		INT PRIMARY KEY AUTO_INCREMENT,						#	Primary Key for Game SubType Table
	 GameItemID 	INT UNIQUE NOT NULL,								#	FK for Item Table
	 GameName 		VARCHAR(256) NOT NULL,								#	Game's name
	 GameGenre 		INT DEFAULT 0,										#	Default is '0' which is 'N/A'
	 GameDescription 	VARCHAR(1024) DEFAULT 'N/A',					#	Description of the game
	 GameCondition 		TINYINT DEFAULT 0,								#	Game's condition
	 MinPlayers 	INT DEFAULT 2,										#	Minimum number of players to be able to play a proper game
	 MaxPlayers 	INT DEFAULT 4,										#	Maximum number of players to be able to play a proper game
	 AveGameLength 	VARCHAR(32),										#	Average length of the game
	 Notes 			VARCHAR(256) DEFAULT 'N/A'							#	Missing pieces, damage, etc. 
);

#	Reference Table for Books (MAIN STORAGE OF BOOK INFORMATION)
CREATE TABLE  Book  (
	 BookID 		INT PRIMARY KEY  AUTO_INCREMENT,
	 BookItemID 		INT UNIQUE NOT NULL,
	 BookName 		VARCHAR(256) NOT NULL,
	 BookGenre 		INT DEFAULT 0,
	 BookDescription 	VARCHAR(1024) DEFAULT 'N/A',
	 BookCondition 		TINYINT DEFAULT 0,
	 Notes 			VARCHAR(256) DEFAULT 'N/A'
);

#	Reference Table for the Collection an Item belongs in
CREATE TABLE  Collection  (
	 CollectionID 		INT PRIMARY KEY  AUTO_INCREMENT,
	 CollectionName 	VARCHAR(32) NOT NULL
);

#	Reference Table for Categories (Board Game, Book, etc)	#
CREATE TABLE  ItemType  (
	 TypeID 	INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
	 TypeName 	VARCHAR(255) NOT NULL									#	Name of the category
);

#	Reference Table for Genres (Family, RPG, TCG, etc.)
CREATE TABLE  Genre  (
	 GenreID 		INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
	 GenreName 		VARCHAR(255) NOT NULL								#	Name of the genre
);

#	Table containing member data (raw - no logins yet)
CREATE TABLE  ClubMember  (
	 MemberID 		INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
	 FirstName 		VARCHAR(255) NOT NULL,
	 Surname 		VARCHAR(255) NOT NULL,
	 Paid 			TINYINT DEFAULT 1,									#	Has the member paid? 0 = True, 1 = False
	 MemberRank 			INT DEFAULT 0,										#	Member permissions  MySQL has enums 
	 PrefPronoun 	VARCHAR(8) DEFAULT 'N/A'
);

#	Reference Table for Permissions	(Ordinary, GK, Committee, etc.)
CREATE TABLE  ClubRank  (
	 RankID 		INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
	 Name 	VARCHAR(32)	NOT NULL
);

#	Transaction Table for Borrowings (Main Library Table)
CREATE TABLE  Transactions  (
	 TransactionID  INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,					#	Identifier for the transaction
	 BorrowerID 	INT NOT NULL,										#	Which member borrowed it?
	 ApproverID 	INT NOT NULL,										#	Which member approved the transaction?
	 DateBorrowed 	DATETIME NOT NULL,									#	Date which the item was borrowed
	 ReturnConfirmerID 	INT NOT NULL,									#	Which member confirmed the item return?
	 DateReturned 	DATETIME NOT NULL								#	Date which item was returned
);

#	Table for Tracking Item Borrowings
CREATE TABLE   Loan  (
	 LoanID 					INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,		#	Identifier for the Borrowing
	 LoanTransactionID 			INT NOT NULL,							#	The Transaction that the Item was borrowed for
	 LoanItemID 				INT NOT NULL							#	The Item that was borrowed
);

#	Reference Table for the Tags
CREATE TABLE   Tag  (
	 TagID 						INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,		#	Tag Identifier
	 TagName 					VARCHAR(32) NOT NULL					#	Tag name/descriptor for the tag
);

#	Link Table for Items and Tags
CREATE TABLE   ItemTag  (
	 ItemTagID 			INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
	 LinkTag 			INT NOT NULL,
	 TaggedItem 		INT NOT NULL
);

/*
	======================================================
	MAKING THE FOREIGN KEY LINKS FOR THE DB
	======================================================
*/

#	Link subclasses to Item Table (Polymorphic Association)
ALTER TABLE  Game  ADD CONSTRAINT  FK_GameItemID 
	FOREIGN KEY ( GameItemID ) REFERENCES Item( ItemID );

ALTER TABLE  Book  ADD CONSTRAINT  FK_BookItemID 
	FOREIGN KEY ( BookItemID ) REFERENCES Item( ItemID );

#	Link Item to the Categories, Genre
ALTER TABLE  Item  ADD CONSTRAINT  FK_ItemType 
	FOREIGN KEY ( ItemType ) REFERENCES ItemType( TypeID );

ALTER TABLE  Item  ADD CONSTRAINT  FK_Collection 
	FOREIGN KEY ( Collection ) REFERENCES Collection( CollectionID );

ALTER TABLE  Game  ADD CONSTRAINT  FK_GameGenre 
	FOREIGN KEY ( GameGenre ) REFERENCES Genre( GenreID );

ALTER TABLE  Book  ADD CONSTRAINT  FK_BookGenre 
	FOREIGN KEY ( BookGenre ) REFERENCES Genre( GenreID );


#	Link Members to the Ranks
ALTER TABLE  ClubMember  ADD CONSTRAINT  FK_Rank 
	FOREIGN KEY ( MemberRank ) REFERENCES ClubRank( RankID );

#	Link the transaction table to the members and items
ALTER TABLE  Transactions  ADD CONSTRAINT  FK_BorrowerID 
	FOREIGN KEY ( BorrowerID ) REFERENCES ClubMember( MemberID );

ALTER TABLE  Transactions  ADD CONSTRAINT  FK_ApproverID 
	FOREIGN KEY ( ApproverID ) REFERENCES ClubMember( MemberID );

ALTER TABLE  Transactions  ADD CONSTRAINT  FK_ReturnConfirmerID 
	FOREIGN KEY ( ReturnConfirmerID ) REFERENCES ClubMember( MemberID );

#	Link the inventory to the transactions and item table
ALTER TABLE  Loan  ADD CONSTRAINT  FK_LoanTransactionID 
	FOREIGN KEY ( LoanTransactionID ) REFERENCES Transactions( TransactionID );

ALTER TABLE  Loan  ADD CONSTRAINT  FK_LoanItemID 
	FOREIGN KEY ( LoanItemID ) REFERENCES Item( ItemID );

#	Link the Tag and Items
ALTER TABLE  ItemTag  ADD CONSTRAINT  FK_ItemTagTag 
	FOREIGN KEY ( LinkTag ) REFERENCES Tag( TagID );

ALTER TABLE  ItemTag  ADD CONSTRAINT  FK_ItemTagItem 
	FOREIGN KEY ( TaggedItem ) REFERENCES Item( ItemID );







