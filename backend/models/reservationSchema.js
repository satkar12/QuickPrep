import mongoose from 'mongoose';
import validator from 'validator';//for the validation of email

const reservationSchema = new mongoose.Schema({
    firstName:{
        type:String,
        required:true,
        minlength:[2, 'First name must be at least 3 characters Long'],
        maxlength:[30,'First name must be at most 30 characters Long'],
    },
    secondName:{
        type:String,
        required:true,
        minlength:[3,'second name must be at least 3 characters Long'],
        maxlength:[30,'Second name must be at most 30 characters Long'],
    },
    email:{
        type:String,
        required:true,
        validate:[validator.isEmail, 'Please provide a valid email'],
    },
    phone:{
        type:String,
        required:true,
        validate:[validator.isMobilePhone, 'Please provide a valid phone number'],
    },
    time:{
        type:String,
        required:true,
    },
    date:{
        type:Date,
        required:true,

    }
});
export const Reservation = mongoose.model('Reservation',reservationSchema );