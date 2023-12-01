from dataclasses import dataclass


@dataclass
class Bitacora:
    idInvoice: str
    idEvent: str
    aditionalData: dict
    amount: float
    amountPaidAfterMatch: float
    amountPaidBeforeMatch: float
    amountToPaidAfterMatch: float
    amountToPaidBeforeMatch: float
    amountToPay: float
    eventType: str
    hasMatchAfterMatch: bool
    hasMatchBeforeMatch: bool
    idBussinessGroup: str
    idTransaction: str
    matchMethod: str
    needReviewAfterMatch: bool
    needRevisionBeforeMatch: bool
    paymentMethod: str
    resource: str
    result: str
    stateAfterMatch: str
    stateBeforeMatch: str

    def __str__(self):
        return f"Bitacora(idInvoice: {self.idInvoice}, idEvent: {self.idEvent}, aditionalData: {self.aditionalData}, amount: {self.amount}, amountPaidAfterMatch: {self.amountPaidAfterMatch}, amountPaidBeforeMatch: {self.amountPaidBeforeMatch}, amountToPaidAfterMatch: {self.amountToPaidAfterMatch}, amountToPaidBeforeMatch: {self.amountToPaidBeforeMatch}, amountToPay: {self.amountToPay}, eventType: {self.eventType}, hasMatchAfterMatch: {self.hasMatchAfterMatch}, hasMatchBeforeMatch: {self.hasMatchBeforeMatch}, idBussinessGroup: {self.idBussinessGroup}, idTransaction: {self.idTransaction}, matchMethod: {self.matchMethod}, needReviewAfterMatch: {self.needReviewAfterMatch}, needRevisionBeforeMatch: {self.needRevisionBeforeMatch}, paymentMethod: {self.paymentMethod}, resource: {self.resource}, result: {self.result}, stateAfterMatch: {self.stateAfterMatch}, stateBeforeMatch: {self.stateBeforeMatch})"

    def __repr__(self):
        return str(self)
