from pydantic import BaseModel, Field

class CriterionScore(BaseModel):
    score: int = Field(ge=0, le=2)
    count: int | None = None
    point_explanation: str | None = None

class Topic(BaseModel):
    score: int = Field(ge=0, le=2)
    clarity: str
    has_relevance_explanation: bool
    point_explanation: str | None = None

class Approaches(BaseModel):
    score: int = Field(ge=0, le=2)
    count: int | None = None
    definition_clarity: str
    point_explanation: str | None = None

class Ideas(BaseModel):
    score: int = Field(ge=0, le=2)
    count: int
    novelty: str
    implementation_clarity: str
    point_explanation: str | None = None

class Problems(BaseModel):
    score: int = Field(ge=0, le=2)
    count: int | None = None
    clarity: str
    point_explanation: str | None = None

class Criteria(BaseModel):
    topic_definition: Topic
    sources: CriterionScore
    approaches: Approaches
    problems: Problems
    ideas: Ideas

class Evaluation(BaseModel):
    total_score: int = Field(ge=0, le=10)
    criteria: Criteria
    total_point_explanation: str | None = None