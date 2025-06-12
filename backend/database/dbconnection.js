import mongoose from 'mongoose';


export const dbconnection =() =>{
    mongoose.connect(process.env.MONGO_URI, {
        dbName:"pdf-summerizer"
}).then(()=>{
    console.log("Database connected successfully");
}).catch((err)=>{
    console.log("Some error occured while connecting to database", err);
})};