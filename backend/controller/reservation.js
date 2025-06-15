import errorHandler from '../error/error.js';
import {Reservation} from '../models/reservationSchema.js';

export const sendReservation = async (req,res,next) =>{
    const {firstName, lastName, email, phone, date, time} = req.body;
    if(!firstName || !lastName || !email || !phone || !date || !time){
        return next(new errorHandler('Please provide all the required fields', 400));
    }
    try{
        await Reservation.create(firstName, lastName, email, phone, date, time);
        res.status(200),json({
            success:true,
            message:'Reservation sent successfully',
        })
    }
    catch(error){
        if(error.name === "ValidationError"){
           const validationErrors = Object.values(error.errors).map((err)=>err.message);
           return next(new errorHandler(validationErrors.join(', '), 400));

    }


}
};
