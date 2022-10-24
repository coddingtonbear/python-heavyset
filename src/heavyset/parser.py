from typing import Any

from pydantic import BaseModel


UUID = str
HEX_COLOR = str
ISO_DATE = str
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
    createdDate: ISO_DATE
    trainingMaxUnit: str
    notes: str | None
    lastPerformedDate: ISO_DATE
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
    firstPerformedDate: ISO_DATE | None
    lastPerformedDate: ISO_DATE | None
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
    updateDate: ISO_DATE
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
    endDate: ISO_DATE
    startDate: ISO_DATE
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

