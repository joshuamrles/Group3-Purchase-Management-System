--reset DATABASE
DELETE FROM PurchaseOrder_purchaseorderitem;
DELETE FROM Quotation_quotationitem;
DELETE FROM PurchaseOrder_purchaseorder;
DELETE FROM Quotation_quotation;
DELETE FROM app_item;
DELETE FROM app_person;
DELETE FROM app_vendor;

-- items data set
INSERT INTO app_item VALUES('PRO001', 'DESKTOP-SPEC(1060 graphic card)','Desktop for Designer');
INSERT INTO app_item VALUES('PRO002', 'HP ES 27" monitor screen','Screen for Designer');
INSERT INTO app_item VALUES('PRO003', 'DESKTOP i7 Intel','Desktop for Software');
INSERT INTO app_item VALUES('PRO004', 'HP ES 24" monitor screen','Standard Screen');
INSERT INTO app_item VALUES('PRO005', 'Colour Printer 3in1','Standard Printer');
INSERT INTO app_item VALUES('PRO006', 'Computer Set Asus','Standard set');

--staff data set
INSERT INTO app_person(user_id_id, person_id, person_name, person_address, person_phone_number,person_role) VALUES(1,'STAFF00001','Hafiz Ghani','Finance MMU, Persiaran Multimedia 63100 Cyberjaya Selangor','+60112345424','FINANCE');
INSERT INTO app_person(user_id_id, person_id, person_name, person_address, person_phone_number,person_role) VALUES(2,'STAFF00002','Muhamad Ghani','RnD MMU, Persiaran Multimedia 63100 Cyberjaya Selangor','+60156348724','MANAGER');


--vendor data set
INSERT INTO app_vendor VALUES('VEN1000001','Fujitsu(M) Sdn Bhd','+601999242241','Bangunan Emerio Cyberjaya, Level 2&3 Lingkaran Teknokrat 63000 Cyberjaya','muhamadhafiz.ghani@gmail.com');
INSERT INTO app_vendor VALUES('VEN1000003','Sepakat Teknologi Sdn Bhd','+603868211113','No.4 BlokB, Jalan Putra 2/1 Perdana, 63000 Cyberjaya','muhamadhafiz.ghani@gmail.com');
INSERT INTO app_vendor VALUES('VEN1000002','Ingeniworks Sdn Bhd','+60386880363','F-3-3 Blok F, Jalan Perdana 63000 Cyberjaya','muhamadhafiz.ghani@gmail.com');

--quotation data set
--1st quotation
INSERT INTO Quotation_quotation(quotation_id,person_id_id,vendor_id_id,description,total_price) VALUES('QUO100001','STAFF00001','VEN1000001','This valid till 3rd day from the issue date',5000.00);
INSERT INTO Quotation_quotationitem(quotation_id_id,item_id_id,quantity,unit_price,total_price,ref_id) VALUES('QUO100001','PRO002',1,2000.00,2000.00,'not applicable');
INSERT INTO Quotation_quotationitem(quotation_id_id,item_id_id,quantity,unit_price,total_price,ref_id) VALUES('QUO100001','PRO001',1,3000.00,3000.00,'not applicable');
--2nd quotation
INSERT INTO Quotation_quotation(quotation_id,person_id_id,vendor_id_id,description,total_price) VALUES('QUO100002','STAFF00001','VEN1000002','This valid till 3rd day from the issue date',4580.00);
INSERT INTO Quotation_quotationitem(quotation_id_id,item_id_id,quantity,unit_price,total_price,ref_id) VALUES('QUO100002','PRO003',1,3980.00,3980.00,'not applicable');
INSERT INTO Quotation_quotationitem(quotation_id_id,item_id_id,quantity,unit_price,total_price,ref_id) VALUES('QUO100002','PRO004',1,600.00,600.00,'not applicable');
--3rd quotation
INSERT INTO Quotation_quotation(quotation_id,person_id_id,vendor_id_id,description,total_price) VALUES('QUO100003','STAFF00001','VEN1000003','This valid till 3rd day from the issue date',6810.00);
INSERT INTO Quotation_quotationitem(quotation_id_id,item_id_id,quantity,unit_price,total_price,ref_id) VALUES('QUO100003','PRO005',1,1200.00,1200.00,'not applicable');
INSERT INTO Quotation_quotationitem(quotation_id_id,item_id_id,quantity,unit_price,total_price,ref_id) VALUES('QUO100003','PRO006',1,5610.00,5610.00,'not applicable');
