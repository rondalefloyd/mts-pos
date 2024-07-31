
            self.salesCursor.execute("""
            WITH RankedProduct AS (
                SELECT
                    P.Name,
                    P.Barcode,
                    P.ExpiryDate,
                    PT.Name,
                    B.Name,
                    S.Name,
                    SG.Name,
                    PP.Capital,
                    PP.Price,
                    PP.DiscountAmount,
                    PP.EffectiveDate,
                    CASE WHEN PM.PromoId > 0 THEN True ELSE False END,
                    CASE WHEN ST.StockId > 0 THEN True ELSE False END,
                    ST.Available,
                    PP.UpdateTs,
                    ROW_NUMBER() OVER(PARTITION BY P.Name, B.Name, S.Name, SG.Name ORDER BY PP.ProductPriceId DESC, PP.UpdateTs DESC) AS RowNumber
                FROM ProductPrice AS PP
                LEFT JOIN Product AS P ON P.ProductId = PP.ProductId
                LEFT JOIN ProductType AS PT ON PT.ProductTypeId = P.ProductTypeId
                LEFT JOIN Brand AS B ON B.BrandId = P.BrandId
                LEFT JOIN Supplier AS S ON S.SupplierId = P.SupplierId
                LEFT JOIN SalesGroup AS SG ON SG.SalesGroupId = P.SalesGroupId
                LEFT JOIN Promo AS PM ON PM.PromoId = PP.PromoId
                LEFT JOIN Stock AS ST ON ST.ProductId = P.ProductId
                WHERE
                    (P.Name LIKE ? OR
                    P.Barcode LIKE ? OR
                    P.ExpiryDate LIKE ? OR
                    PT.Name LIKE ? OR
                    B.Name LIKE ? OR
                    S.Name LIKE ? OR
                    PP.Capital LIKE ? OR
                    PP.Price LIKE ? OR
                    PP.DiscountAmount LIKE ? OR
                    PM.PromoId LIKE ? OR
                    ST.StockId LIKE ? OR
                    ST.Available LIKE ? OR
                    PP.UpdateTs LIKE ?) AND
                    SG.Name = ? AND
                    PP.Price >= 0 AND
                    PP.DiscountAmount >= 0 AND
                    PP.EffectiveDate <= CURRENT_DATE
                ORDER BY PP.ProductPriceId DESC, PP.UpdateTs DESC
            )
            SELECT * FROM RankedProduct
            WHERE RowNumber = 1
            LIMIT ?
            OFFSET ?
            """, ("%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                orderType,
                rowCount,
                offset))  

            productData = self.salesCursor.fetchall()

            return productData