import { Card, CardContent, Typography, IconButton, TextField, Button, Box } from "@mui/material";
import { Edit, Delete, Cancel } from "@mui/icons-material";
import { Position } from "../../api_store/apiStore";
import { useSwipeable } from "react-swipeable";
import { motion } from "framer-motion";
import { useState } from "react";
import { deletePosition, updatePosition } from "../../redux/portfolioSlice";
import { useDispatch } from "react-redux";
import { AppDispatch } from "../../redux/store";

interface StockCardProps {
  position: Position;
}

const PositionCard: React.FC<StockCardProps> = ({ position }) => {
    const dispatch: AppDispatch = useDispatch();
    const [swipedLeft, setSwipedLeft] = useState(false);

    const swipeHandlers = useSwipeable({
        onSwipedLeft: () => setSwipedLeft(true), // Trigger when swiped left
        onSwipedRight: () => setSwipedLeft(false), // Reset on swipe right
        trackMouse: true,
    });

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
        {...swipeHandlers}>
            <CardContent sx={{ padding: 1 }}>
                <Typography variant="h6">{position.ticker}</Typography>
                <Typography variant="body2">Quantity: {position.quantity}</Typography>
                <Typography variant="body2">
                Total Price: ${position.total_purchase_price.toFixed(2)}
                </Typography>
                <Typography variant="body2">
                Purchased: {new Date(position.purchase_date).toISOString().split("T")[0]}
                </Typography>
            </CardContent>

            {/*Right Swipe View*/}
            <motion.div
                style={{
                position: "absolute",
                top: 0,
                right: 0,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100%",
                width: "100%",
                backgroundColor: "#fff",
                borderLeft: "1px solid #ddd",
                zIndex: 10
                }}
                initial={{ x: "100%" }}
                animate={{ x: swipedLeft ? 0 : "100%" }}
                transition={{ type: "spring", stiffness: 200, damping: 20 }}
            >
                <Box sx={{ display: "flex", gap: 1 }}>
                    <IconButton color="primary" onClick={() => {setSwipedLeft(false);}}>
                        <Edit />
                    </IconButton>
                    <IconButton color="secondary" onClick={() => dispatch(deletePosition(position.id))}>
                        <Delete />
                    </IconButton>
                    <IconButton color="default" onClick={() => setSwipedLeft(false)}>
                        <Cancel />
                    </IconButton>
                </Box>
            </motion.div>
        </Card>
    );
};

export default PositionCard;
