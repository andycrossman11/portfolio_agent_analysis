import { Card, CardContent, TextField, Button, Box } from "@mui/material";
import { Position } from "../../api_store/apiStore";
import { useState } from "react";
import { updatePosition } from "../../redux/portfolioSlice";
import { useDispatch } from "react-redux";
import { AppDispatch } from "../../redux/store";

interface StockCardProps {
  position: Position;
}

const PositionCard: React.FC<StockCardProps> = ({ position }) => {
    const dispatch: AppDispatch = useDispatch();
    const [editedPosition, setEditedPosition] = useState(position); // Track edited position

    // Handle input change for editing
    const handleInputChange = (field: string, value: string) => {
        setEditedPosition((prev) => ({ ...prev, [field]: value }));
    };

    const handleCancel = () => {
        setEditedPosition(position); // Revert to original position
      };
    
    const handleSave = () => {
        // Add logic to save changes (e.g., dispatch update action)
        console.log("Save", editedPosition);
        dispatch(updatePosition(editedPosition));
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
                    value={editedPosition.quantity}
                    onChange={(e) => handleInputChange("ticker", e.target.value)}
                    fullWidth
                    margin="normal"
                />
                <TextField
                    label="Quantity"
                    value={editedPosition.quantity}
                    onChange={(e) => handleInputChange("quantity", e.target.value)}
                    fullWidth
                    margin="normal"
                />
                <TextField
                    label="Total Price"
                    value={editedPosition.total_purchase_price}
                    onChange={(e) => handleInputChange("total_purchase_price", e.target.value)}
                    fullWidth
                    margin="normal"
                />
                <TextField
                    label="Purchased Date"
                    value={editedPosition.purchase_date}
                    onChange={(e) => handleInputChange("purchase_date", e.target.value)}
                    fullWidth
                    margin="normal"
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

export default PositionCard;
