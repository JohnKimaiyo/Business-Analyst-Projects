/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [BusinessEntityID]
      ,[NationalIDNumber]
      ,[LoginID]
      ,[OrganizationNode]
      ,[OrganizationLevel]
      ,[JobTitle]
      ,[BirthDate]
      ,[MaritalStatus]
      ,[Gender]
      ,[HireDate]
      ,[SalariedFlag]
      ,[VacationHours]
      ,[SickLeaveHours]
      ,[CurrentFlag]
      ,[rowguid]
      ,[ModifiedDate]

	  ,CASE
	  WHEN VacationHours > 50 THEN 'Over Time Rquiere'
	  WHEN VacationHours < 50 THEN 'Over time not required'
	  END AS Over_Time_Status
  FROM [AdventureWorks2019].[HumanResources].[Employee]