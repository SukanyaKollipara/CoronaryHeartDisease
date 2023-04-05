# File to create a structure for the input to the ML model
# This way the attributes of the class patientData can be used as features of the data.

from pydantic import BaseModel


# Class which describes patient data measurements
# Contains 11 attibutes/inputs
class patientData(BaseModel):
    sysBP: int
    glucose: int
    age:int
    cigsPerDay: int
    totChol: int
    diaBP: int
    prevalentHyp: int
    male: int
    BPMeds: int
    diabetes: int