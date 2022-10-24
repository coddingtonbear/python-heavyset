from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


HEX_COLOR = str
SECONDS = int
UNKNOWN = Any
WEIGHT_KG = float


class Exercise(BaseModel):
    id: UUID
    isUnilateral: bool
    selectedStatisticRaw: str
    disabledStatisticsRaw: list[str]
    isArchived: bool
    exerciseVolumeGroups: list[UNKNOWN]
    createdDate: datetime
    trainingMaxUnit: str
    notes: str | None
    lastPerformedDate: datetime
    isAssisted: bool
    baseWeightUnit: str
    isTimed: bool
    name: str
    shouldAutoFillBodyWeight: bool


class Prescription(BaseModel):
    trainingMaxUpdateOptionRaw: str
    intensity: int | None
    id: UUID
    minReps: int | None
    maxReps: int | None
    isSkipped: bool
    restDuration: SECONDS | None
    exercise: Exercise


class RoutineGroup(BaseModel):
    id: UUID
    minSets: int | None
    maxSets: int | None
    prescriptions: list[Prescription]


class Routine(BaseModel):
    id: str
    firstPerformedDate: datetime | None
    lastPerformedDate: datetime | None
    isUserGenerated: bool
    name: str
    groups: list[RoutineGroup]


class RoutineEnvelope(BaseModel):
    isRoot: bool
    childNodes: list[UNKNOWN]
    id: UUID
    hexCode: HEX_COLOR
    path: str
    name: str
    routine: Routine


class Routines(BaseModel):
    path: str
    id: UUID
    isRoot: bool
    name: str
    childNodes: list[RoutineEnvelope]


class WorkoutSet(BaseModel):
    exercise: Exercise
    prescription: Prescription | None
    updateDate: datetime
    id: UUID
    reps: int
    isPersonalRecord: bool
    notes: str | None
    unitString: str
    resistance: WEIGHT_KG
    baseResistance: WEIGHT_KG
    duration: SECONDS


class Workout(BaseModel):
    id: UUID
    name: str
    endDate: datetime
    startDate: datetime
    bodyweight: WEIGHT_KG
    sets: list[WorkoutSet]
    hexCode: HEX_COLOR | None
    routine: Routine | None
    exercises: list[Exercise]


class VolumeGroup(BaseModel):
    id: UUID
    name: str


class Plate(BaseModel):
    kilograms: WEIGHT_KG
    id: UUID
    massValue: float
    hexCode: HEX_COLOR
    itemTypeRaw: str
    massUnitString: str


class Bar(BaseModel):
    kilograms: WEIGHT_KG
    id: UUID
    massValue: float
    itemTypeRaw: str
    name: str
    massUnitString: str


class InventoryLocation(BaseModel):
    id: UUID
    name: str
    collars: list[UNKNOWN]
    bars: list[Bar]
    plates: list[Plate]


class HeavySetBackup(BaseModel):
    rootNode: Routines
    exercises: list[Exercise]
    workouts: list[Workout]
    volumeGroups: list[VolumeGroup]
    inventoryLocations: list[InventoryLocation]

    class Config:
        json_encoders = {
            UUID: lambda val: str(val).upper(),
            # Contrary to what the stdlib docs suggest, %Y
            # will not in all situations return a 4-digit year
            # so here we're just formatting our year manually.
            datetime: lambda val: f'{val.year:04}' + val.strftime('-%m-%dT%H:%M:%SZ')
        }
