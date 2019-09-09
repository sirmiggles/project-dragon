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

--	:setvar DBName "unigames_schema"

/*
	==========================================================
					CREATING THE TABLES
	==========================================================
*/

USE [unigames]

DROP TABLE IF EXISTS
	[Loan], [Transactions], [Game], [Book], [Genre],
	[Member], [Rank], [Item], [Type], [Collection]

PRINT 'TABLES DELETED'
GO

--	Table for the Items	--
CREATE TABLE [dbo].[Item] (
	[ItemID]		INT PRIMARY KEY IDENTITY NOT NULL,					--	Primary Key for Items
	[Type]			INT NOT NULL,										--	Item Type - book, boardgame, etc.	(FK) (Mainly used for IF, Procedure)
	[Available]		TINYINT NOT NULL DEFAULT 0,							--	Is the item available? 0 = True, 1 = False
	[Collection]	INT DEFAULT 0,										--	Which collection the item belongs to (FK)
	[Notes]			VARCHAR DEFAULT 'N/A'								--	Item notes, e.g. is the item missing pieces?
)

--	Reference Table for Games (MAIN STORAGE OF GAME INFORMATION)
CREATE TABLE [dbo].[Game] (
	[GameID]		INT PRIMARY KEY IDENTITY,							--	Primary Key for Game SubType Table
	[GameItemID]	INT UNIQUE NOT NULL,								--	FK for Item Table
	[GameName]		VARCHAR(256) NOT NULL,								--	Game's name
	[GameGenre]		INT DEFAULT 0,										--	Default is '0' which is 'N/A'
	[Description]	VARCHAR(1024) DEFAULT 'N/A',						--	Description of the game
	[Condition]		TINYINT DEFAULT 0,									--	Game's condition
	[MinPlayers]	INT DEFAULT 2,										--	Minimum number of players to be able to play a proper game
	[MaxPlayers]	INT DEFAULT 4,										--	Maximum number of players to be able to play a proper game
	[AveGameLength]	VARCHAR(32),										--	Average length of the game
	[Notes]			VARCHAR(256) DEFAULT 'N/A'							--	Missing pieces, damage, etc. 
)

--	Reference Table for Books (MAIN STORAGE OF BOOK INFORMATION)
CREATE TABLE [dbo].[Book] (
	[BookID]		INT PRIMARY KEY IDENTITY,
	[BookItemID]		INT UNIQUE NOT NULL,
	[BookName]		VARCHAR(256) NOT NULL,
	[BookGenre]		INT DEFAULT 0,
	[Description]	VARCHAR(1024) DEFAULT 'N/A',
	[Condition]		TINYINT DEFAULT 0,
	[Notes]			VARCHAR(256) DEFAULT 'N/A'
)

--	Reference Table for the Collection an Item belongs in
CREATE TABLE [dbo].[Collection] (
	[CollectionID]		INT PRIMARY KEY IDENTITY,
	[CollectionName]	VARCHAR(32) NOT NULL
)

--	Reference Table for Categories (Board Game, Book, etc)	--
CREATE TABLE [dbo].[Type] (
	[TypeID]	INT PRIMARY KEY IDENTITY NOT NULL,
	[TypeName]	VARCHAR(255) NOT NULL									--	Name of the category
)

--	Reference Table for Genres (Family, RPG, TCG, etc.)
CREATE TABLE [dbo].[Genre] (
	[GenreID]		INT PRIMARY KEY IDENTITY NOT NULL,
	[GenreName]		VARCHAR(255) NOT NULL								--	Name of the genre
)

--	Table containing member data (raw - no logins yet)
CREATE TABLE [dbo].[Member] (
	[MemberID]		INT PRIMARY KEY IDENTITY NOT NULL,
	[FirstName]		VARCHAR(255) NOT NULL,
	[Surname]		VARCHAR(255) NOT NULL,
	[Paid]			TINYINT DEFAULT 1,									--	Has the member paid? 0 = True, 1 = False
	[Rank]			INT DEFAULT 0,										--	Member permissions [MySQL has enums]
	[PrefPronoun]	VARCHAR(8) DEFAULT 'N/A',
)

--	Reference Table for Permissions	(Ordinary, GK, Committee, etc.)
CREATE TABLE [dbo].[Rank] (
	[RankID]		INT PRIMARY KEY IDENTITY NOT NULL,
	[Name]	VARCHAR(32)	NOT NULL
)

--	Transaction Table for Borrowings (Main Library Table)
CREATE TABLE [dbo].[Transactions] (
	[TransactionID] INT PRIMARY KEY IDENTITY NOT NULL,					--	Identifier for the transaction
	[BorrowerID]	INT NOT NULL,										--	Which member borrowed it?
	[ApproverID]	INT NOT NULL,										--	Which member approved the transaction?
	[DateBorrowed]	DATETIME NOT NULL,									--	Date which the item was borrowed
	[ReturnConfirmerID]	INT NOT NULL,									--	Which member confirmed the item return?
	[DateReturned]	DATETIME NOT NULL,									--	Date which item was returned
)

--	Table for Tracking Item Borrowings
CREATE TABLE [dbo].[Loan] (
	[LoanID]					INT PRIMARY KEY IDENTITY NOT NULL,		--	Identifier for the Borrowing
	[LoanTransactionID]			INT NOT NULL,							--	The Transaction that the Item was borrowed for
	[LoanItemID]				INT NOT NULL							--	The Item that was borrowed
)

--	Reference Table for the Tags
CREATE TABLE [dbo].[Tag] (
	[TagID]						INT PRIMARY KEY IDENTITY NOT NULL,		--	Tag Identifier
	[TagName]					VARCHAR(32) NOT NULL					--	Tag name/descriptor for the tag
)

--	Link Table for Items and Tags
CREATE TABLE [dbo].[ItemTag] (
	[ItemTagID]			INT PRIMARY KEY IDENTITY NOT NULL,
	[LinkTag]			INT NOT NULL,
	[TaggedItem]		INT NOT NULL
)

PRINT 'TABLES CREATED' 
/*
	======================================================
	MAKING THE FOREIGN KEY LINKS FOR THE DB
	======================================================
*/

--	Link subclasses to Item Table (Polymorphic Association)
ALTER TABLE [Game] ADD CONSTRAINT [FK_GameItemID]
	FOREIGN KEY ([GameItemID]) REFERENCES Item([ItemID])

ALTER TABLE [Book] ADD CONSTRAINT [FK_BookItemID]
	FOREIGN KEY ([BookItemID]) REFERENCES Item([ItemID])

--	Link Item to the Categories, Genre
ALTER TABLE [Item] ADD CONSTRAINT [FK_Type]
	FOREIGN KEY ([Type]) REFERENCES Type([TypeID])

ALTER TABLE [Item] ADD CONSTRAINT [FK_Collection]
	FOREIGN KEY ([Collection]) REFERENCES Collection([CollectionID])

ALTER TABLE [Game] ADD CONSTRAINT [FK_GameGenre]
	FOREIGN KEY ([GameGenre]) REFERENCES Genre([GenreID])

ALTER TABLE [Book] ADD CONSTRAINT [FK_BookGenre]
	FOREIGN KEY ([BookGenre]) REFERENCES Genre([GenreID])


--	Link Members to the Ranks
ALTER TABLE [Member] ADD CONSTRAINT [FK_Rank]
	FOREIGN KEY ([Rank]) REFERENCES Rank([RankID])

--	Link the transaction table to the members and items
ALTER TABLE [Transactions] ADD CONSTRAINT [FK_BorrowerID]
	FOREIGN KEY ([BorrowerID]) REFERENCES Member([MemberID])

ALTER TABLE [Transactions] ADD CONSTRAINT [FK_ApproverID]
	FOREIGN KEY ([ApproverID]) REFERENCES Member([MemberID])

ALTER TABLE [Transactions] ADD CONSTRAINT [FK_ReturnConfirmerID]
	FOREIGN KEY ([ReturnConfirmerID]) REFERENCES Member([MemberID])

--	Link the inventory to the transactions and item table
ALTER TABLE [Loan] ADD CONSTRAINT [FK_LoanTransactionID]
	FOREIGN KEY ([LoanTransactionID]) REFERENCES Transactions([TransactionID])

ALTER TABLE [Loan] ADD CONSTRAINT [FK_LoanItemID]
	FOREIGN KEY ([LoanItemID]) REFERENCES Item([ItemID])

--	Link the Tag and Items
ALTER TABLE [ItemTag] ADD CONSTRAINT [FK_ItemTagTag]
	FOREIGN KEY ([LinkTag]) REFERENCES Tag([TagID])

ALTER TABLE [ItemTag] ADD CONSTRAINT [FK_ItemTagItem]
	FOREIGN KEY ([TaggedItem]) REFERENCES Item([ItemID])









