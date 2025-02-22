import React, { useState } from "react";
import dayjs from "dayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DateCalendar } from "@mui/x-date-pickers/DateCalendar";
import { Card, Typography } from "@mui/material";

const CalendarComponent: React.FC = () => {
  const [selectedDate, setSelectedDate] = useState(dayjs());
  const today = dayjs();

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Card sx={{ p: 4, backgroundColor: "#eae0f0", borderRadius: 3, width: '90%' }}>
        <Typography variant="h5" sx={{ fontWeight: "bold", mb: 2 }}>
          {selectedDate.format("ddd, MMM D")}
        </Typography>
        <DateCalendar
          value={selectedDate}
          onChange={(newDate) => setSelectedDate(newDate)}
          views={["year", "month", "day"]}
          shouldDisableDate={(date) => date.isAfter(today) || date.day() === 0 || date.day() === 6}
          sx={{
            backgroundColor: "white",
            borderRadius: 2,
            width: '70%',
            height: '100%',
            '& .MuiPickersDay-root': {
              fontSize: '1.5rem', 
              margin: '0.25rem',
            },
            '& .MuiTypography-root': {
              fontSize: '1.5rem', 
              margin: '0.25rem'
            },
          }}
        />
      </Card>
    </LocalizationProvider>
  );
};

export default CalendarComponent;