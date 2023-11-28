-- ROW_NUMBER() does just what it sounds like—displays the number of a given row. It starts are 1 and numbers the rows according to the ORDER BY part of the window statement. ROW_NUMBER() does not require you to specify a variable within the parentheses:
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [DepartmentID]
      ,[Name]
      ,[GroupName]
      ,[ModifiedDate],
	  ROW_NUMBER() OVER(ORDER BY ModifiedDate) AS row_number
  FROM [AdventureWorks2019].[HumanResources].[Department]
  WHERE ModifiedDate < '2009'