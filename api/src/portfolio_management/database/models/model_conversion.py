from .db_models import AnalysisSchema, PositionSchema
from .pydantic_model_map import Analysis, Position
from abc import ABC, abstractmethod

class ModelConversion(ABC):
    @abstractmethod
    def pydantic_to_sqlalchemy(self):
        pass

    @abstractmethod
    def sqlalchemy_to_pydantic(self):
        pass


class PositionModelConversion(ModelConversion):
    @staticmethod
    def pydantic_to_sqlalchemy(position: Position) -> PositionSchema:
        return PositionSchema(
            id=position.id,
            ticker=position.ticker,
            quantity=position.quantity,
            total_purchase_price=position.total_purchase_price,
            purchase_date=position.purchase_date,
        )

    @staticmethod
    def sqlalchemy_to_pydantic(position_data: PositionSchema) -> Position:
        return Position(
            id=position_data.id,
            ticker=position_data.ticker,
            quantity=position_data.quantity,
            total_purchase_price=position_data.total_purchase_price,
            purchase_date=position_data.purchase_date,
        )

class AnalysisModelConversion(ModelConversion):
    @staticmethod
    def pydantic_to_sqlalchemy(analysis: Analysis) -> AnalysisSchema:
        return AnalysisSchema(
            llm_summary=analysis.llm_summary,
            analysis_date=analysis.analysis_date
        )

    @staticmethod
    def sqlalchemy_to_pydantic(analysis_data: AnalysisSchema) -> Analysis:
        return Analysis(
            llm_summary=analysis_data.llm_summary,
            analysis_date=analysis_data.analysis_date
        )
