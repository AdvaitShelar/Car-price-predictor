import streamlit as st 
import pickle
import pandas as pd

company=['Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota','Renault', 'Honda','Datsun', 'Mitsubishi', 'Tata', 'Volkswagen','Chevrolet', 'Mini', 'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force',  'Mercedes', 'Land', 'Jaguar', 'Jeep', 'Volvo']

names=['Hyundai Santro Xing', 'Mahindra Jeep CL550', 'Hyundai Grand i10','Ford EcoSport Titanium', 
       'Ford Figo', 'Hyundai Eon','Ford EcoSport Ambiente', 'Maruti Suzuki Alto','Skoda Fabia Classic', 'Maruti Suzuki Stingray','Hyundai Elite i20', 'Mahindra Scorpio SLE', 'Audi A8', 'Audi Q7',
       'Mahindra Scorpio S10', 'Hyundai i20 Sportz','Maruti Suzuki Vitara', 'Mahindra Bolero DI',
       'Maruti Suzuki Swift', 'Maruti Suzuki Wagon', 'Toyota Innova 2.0','Renault Lodgy 85', 
       'Skoda Yeti Ambition', 'Maruti Suzuki Baleno','Renault Duster 110', 'Renault Duster 85', 
       'Honda City 1.5','Maruti Suzuki Dzire', 'Honda Amaze', 'Honda Amaze 1.5','Honda City', 
       'Datsun Redi GO', 'Maruti Suzuki SX4','Mitsubishi Pajero Sport', 'Honda City ZX', 
       'Tata Indigo eCS', 'Volkswagen Polo Highline', 'Chevrolet Spark LS','Renault Duster 110PS', 
       'Mini Cooper S', 'Skoda Fabia 1.2L','Renault Duster', 'Mahindra Scorpio S4', 
       'Mahindra Scorpio VLX','Mahindra Quanto C8', 'Ford EcoSport', 'Honda Brio',
       'Volkswagen Vento Highline', 'Hyundai i20 Magna','Toyota Corolla Altis', 
       'Hyundai Verna Transform', 'BMW 3 Series','Maruti Suzuki A', 'Toyota Etios GD', 
       'Ford Figo Diesel','Chevrolet Beat LT', 'BMW 7 Series', 'Mahindra XUV500 W8','Hyundai i10 Magna', 'Hyundai Verna Fluidic','Maruti Suzuki Ertiga', 'Honda Amaze 1.2', 'Hyundai i20 Asta',
       'Maruti Suzuki Eeco', 'Maruti Suzuki Esteem', 'Maruti Suzuki Ritz','Toyota Etios Liva',
       'Chevrolet Spark', 'Nissan Micra XV','Chevrolet Beat', 'Ford EcoSport Trend', 'Tata Indica V2',
       'Hindustan Motors Ambassador', 'Toyota Innova 2.5','Volkswagen Jetta Highline', 
       'Volkswagen Polo Comfortline','Volkswagen Polo', 'Mahindra Scorpio', 'Nissan Sunny',
       'Renault Kwid', 'Chevrolet Spark LT', 'Fiat Punto Emotion', 'Hyundai i10 Sportz', 
       'Chevrolet Beat LS', 'Tata Indigo CS','Hyundai Eon Era', 'Mahindra XUV500', 'Ford Fiesta', 'Hyundai i20', 'Hyundai Fluidic Verna', 'Fiat Petra ELX', 'Maruti Suzuki Ciaz',
       'Maruti Suzuki Zen', 'Hyundai Creta 1.6', 'Mahindra Scorpio SLX','Tata Nano Cx', 
       'Tata Sumo Victa', 'Volkswagen Passat Diesel', 'Renault Scala RxL', 'Hyundai i20 Active', 'Mahindra Xylo E4','Mahindra Jeep MM', 'Mahindra Bolero SLE', 'Force Motors Force',
       'Toyota Etios', 'Honda City VX', 'Mahindra Thar CRDe','Audi A4 1.8', 'Mercedes Benz GLA', 
       'Land Rover Freelander', 'Renault Kwid RXT', 'Tata Aria Pleasure', 'Mercedes Benz B',
       'Datsun GO T', 'Honda Jazz VX', 'Chevrolet Tavera Neo','Hyundai Eon Sportz', 'Tata Sumo Gold', 'Chevrolet Enjoy 1.4','Nissan Terrano XL', 'Maruti Suzuki Maruti', 'Renault Kwid 1.0',
       'Hyundai Accent GLX', 'Mahindra TUV300 T4', 'Honda Accord','Mahindra Scorpio 2.6', 
       'Honda Mobilio', 'Skoda Laura','Tata Manza Aura', 'Chevrolet Sail UVA', 'Audi A4 2.0',
       'Hyundai Elantra SX', 'Mahindra KUV100 K8', 'Hyundai i10','Hyundai Accent', 'Hyundai Verna', 'Toyota Fortuner','Mahindra Bolero Power', 'Skoda Rapid Elegance','Tata Vista Quadrajet', 'Chevrolet Beat Diesel','Hyundai Verna 1.4', 'Maruti Suzuki Versa', 'Tata Indigo LX',
       'Volkswagen Vento Konekt', 'Mercedes Benz C', 'Maruti Suzuki Omni','Hyundai Sonata Transform', 'Honda Jazz S', 'Mahindra Scorpio W','Honda Brio V', 'Mahindra TUV300 T8', 'Nissan X Trail',
       'Ford Ikon 1.3', 'Toyota Fortuner 3.0', 'Tata Manza ELAN','Mercedes Benz A', 'Tata Indigo LS', 'Hyundai Verna 1.6','BMW 5 Series', 'Skoda Superb 1.8', 'Audi Q3 2.0','Ford Figo Duratorq', 'Mahindra Logan Diesel', 'Tata Nano GenX','Honda City SV', 'Ford Figo Petrol', 
       'Toyota Corolla H2', 'Hyundai Xcent Base', 'Hyundai Accent Executive', 'Tata Zest XE',
       'Mahindra XUV500 W6', 'Tata Tigor Revotron', 'Maruti Suzuki 800', 'Honda Mobilio S', 
       'Tata Indica', 'Honda Brio VX', 'Tata Nano Lx', 'Jaguar XE XE', 'Hyundai Eon Magna', 
       'Hyundai Eon D', 'Maruti Suzuki Estilo', 'Mahindra Scorpio Vlx','Mitsubishi Lancer 1.8', 
       'Ford Fiesta SXi', 'Audi A6 2.0','Hyundai Getz Prime', 'Hyundai Santro', 'Chevrolet Beat PS',
       'BMW X1 xDrive20d', 'Tata Nano', 'Chevrolet Cruze LTZ','Mahindra XUV500 W10', 
       'Hyundai Accent GLE', 'Force Motors One','Chevrolet Spark 1.0', 'Renault Duster 85PS', 
       'Chevrolet Enjoy','Jeep Wrangler Unlimited', 'Hyundai Verna VGT', 'Maruti Suzuki Celerio', 
       'Tata Zest Quadrajet', 'Hyundai i10 Era', 'Tata Indigo Marina', 'Hyundai Xcent SX', 
       'Tata Nano LX', 'Mahindra Xylo E8', 'Tata Manza Aqua', 'Tata Venture EX','Skoda Octavia Classic', 'Ford Ikon 1.6', 'Nissan Sunny XL','Volkswagen Polo Trendline', 'Hyundai Elantra 1.8',
       'Tata Indica eV2', 'Jaguar XF 2.2', 'Audi Q5 2.0', 'BMW X1 sDrive20d', 'Maruti Suzuki S',
       'Volkswagen Vento Comfortline', 'Mahindra KUV100', 'Volkswagen Jetta Comfortline', 
       'Volvo S80 Summum', 'BMW X1', 'Renault Duster RxL', 'Honda WR V', 'Mahindra Scorpio LX',
       'Audi A3 Cabriolet', 'Hyundai Santro AE', 'Mahindra Xylo D2', 'Hyundai Getz GLE', 
       'Nissan Micra XL', 'Chevrolet Tavera LS', 'Tata Tiago Revotron', 'Tata Tiago Revotorq', 
       'Ford Fusion 1.4', 'Fiat Linea Emotion', 'Toyota Corolla', 'Tata Sumo Grande',
       'Volkswagen Polo Highline1.2L', 'Hyundai Creta', 'Tata Bolt XM', 'Datsun Go Plus', 
       'Ford Endeavor 4x4', 'Mahindra Logan', 'Chevrolet Sail 1.2', 'Tata Manza', 'Toyota Etios G',
       'Toyota Qualis', 'Mahindra Quanto C4', 'Hyundai i20 Select', 'Hyundai Getz', 'Skoda Fabia', 
       'Tata Zest XM']

years=[2007, 2006, 2014, 2012, 2013, 2016, 2015, 2010, 2017, 2008, 2018,
       2011, 2019, 2009, 2005, 2000, 2003, 2004, 1995, 2002, 2001]

fuels=['Petrol', 'Diesel', 'LPG']

st.title('Car Price Predictor')

selected_brand= st.selectbox('Select the car company', sorted(company))

selected_model= st.selectbox('Select the car model', sorted(names))

selected_year= st.selectbox('Select the year of purchase', sorted(years))

selected_fuel_type= st.selectbox('Select the fuel type', fuels)

kms_travelled= st.number_input('Enter the number of kilometers traveled')

model=pickle.load(open('LinearRegression.pkl','rb'))

if st.button('Predict Price'):
    
    input_df= pd.DataFrame({'company':[selected_brand], 'name':[selected_model], 'year':[selected_year], 'fuel_type':[selected_fuel_type], 'kms_driven':[kms_travelled]})
    
    st.table(input_df)
    
    result=model.predict(input_df)[0]
    
    st.header(result)