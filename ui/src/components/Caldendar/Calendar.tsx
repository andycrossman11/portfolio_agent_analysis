import React, { useState } from "react";
import dayjs from "dayjs";
import { DateCalendar } from "@mui/x-date-pickers/DateCalendar";
import { Card, Typography } from "@mui/material";

interface CalendarProps {
  setSelectedAnalysis: (date: string) => void;
}

const CalendarComponent: React.FC<CalendarProps> = ({ setSelectedAnalysis }) => {
  const [selectedDate, setSelectedDate] = useState(dayjs());
  const today = dayjs();

  const handleDateChange = (newDate: dayjs.Dayjs | null) => {
    if (newDate) {
      setSelectedDate(newDate);
      setSelectedAnalysis(newDate.format("MM-DD-YYYY"));
    }
  };

  return (
    <Card sx={{ p: 4, backgroundColor: "#eae0f0", borderRadius: 3, width: '90%' }}>
      <Typography variant="h5" sx={{ fontWeight: "bold", mb: 2 }}>
        {selectedDate.format("ddd, MMM D")}
      </Typography>
      <DateCalendar
        value={selectedDate}
        onChange={handleDateChange}
        views={["year", "month", "day"]}
        shouldDisableDate={(date) => date.isAfter(today)}
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
  );
};

export default CalendarComponent;