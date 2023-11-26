/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [CustomerID]
      ,[Genre]
      ,[Age]
      ,[Annual Income (k$)]
      ,[Spending Score (1-100)]
  FROM [Mail Customer Database].[dbo].[Mall_Customers$]