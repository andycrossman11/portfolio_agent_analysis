import { Card, CardContent, TextField, Button, Box } from "@mui/material";
import { Position } from "../../api_store/apiStore";
import { useState } from "react";
import { setEditingIndex } from "../../redux/portfolioSlice";
import { useDispatch } from "react-redux";
import { AppDispatch } from "../../redux/store";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import dayjs, { Dayjs } from "dayjs";

interface StockCardProps {
    position: Position;
    updatePosition: (position: Position) => void;
}

const UpdateCard: React.FC<StockCardProps> = ({ position, updatePosition }) => {
    const dispatch: AppDispatch = useDispatch();
    const [editedPosition, setEditedPosition] = useState(position); // Track edited stock

    // Handle input change for editing
    const handleInputChange = (field: string, value: string | number) => {
        setEditedPosition((prev) => ({ ...prev, [field]: value }));
    };

    const handleCancel = () => {
        dispatch(setEditingIndex(-1));
    };
    
    const handleSave = () => {
        updatePosition(editedPosition);
        dispatch(setEditingIndex(-1));
    };

    return (
        <Card sx={{ 
            boxShadow: "none",
            backgroundColor: "transparent",
            borderTop: "1px solid #ddd",
            borderBottom: "1px solid #ddd",
            borderRadius: 0,
            width: "100%",
            overflow: "hidden", // Ensure no scrolling for the card
            position: "relative", // Important for absolute positioning of the buttons
        }} 
        >
            <CardContent sx={{ padding: 1 }}>
                <TextField
                    label="Ticker"
                    value={editedPosition.ticker}
                    onChange={(e) => handleInputChange("ticker", e.target.value)}
                    fullWidth
                    margin="normal"
                />
                <TextField
                    label="Quantity"
                    type="number"
                    value={editedPosition.quantity}
                    onChange={(e) => handleInputChange("quantity", parseFloat(e.target.value))}
                    fullWidth
                    margin="normal"
                />
                <TextField
                    label="Share Price"
                    type="number"
                    value={editedPosition.purchase_share_price}
                    onChange={(e) => handleInputChange("purchase_share_price", parseFloat(e.target.value))}
                    fullWidth
                    margin="normal"
                />
                <DatePicker
                    label="Purchase Date"
                    value={editedPosition.purchase_date ? dayjs(editedPosition.purchase_date) : null}
                    onChange={(date: Dayjs | null) => {
                        handleInputChange("purchase_date", date ? date.format("MM-DD-YYYY") : "");
                    }}
                    slotProps={{ textField: { fullWidth: true, margin: "normal" } }}
                />
                {/* Action buttons */}
                <Box sx={{ display: "flex", gap: 1, mt: 2 }}>
                <Button variant="contained" color="primary" onClick={handleSave}>
                    Save
                </Button>
                <Button variant="outlined" color="secondary" onClick={handleCancel}>
                    Cancel
                </Button>
                </Box>
            </CardContent>
        </Card>
    );
};

export default UpdateCard;
