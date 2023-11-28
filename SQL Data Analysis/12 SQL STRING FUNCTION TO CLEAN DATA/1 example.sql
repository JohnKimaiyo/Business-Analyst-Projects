/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [DepartmentID]
      ,[Name]
      ,[GroupName]
      ,LEFT([ModifiedDate],11) AS CLEANED_DATE
  FROM [AdventureWorks2019].[HumanResources].[Department]