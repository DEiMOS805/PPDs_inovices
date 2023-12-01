from dataclasses import dataclass
from datetime import datetime
import math


@dataclass
class Invoice:
    """Clase que representa una factura."""

    uuidFactura: str
    esManual: str
    nombreReceptor: str
    rfcReceptor: str
    nombreEmisor: str
    rfcEmisor: str
    fechaEmision: str
    monto: float
    montoPagado: float
    montoAPagar: float
    metodoPago: str
    vigencia: str
    divisaFactura: str
    divisaMovimiento: str
    estadoFactura: str
    idTransaccion: str
    montoTransaccion: float
    fechaTransaccion: str
    transaccionConcepto: str
    bancoEmisor: str
    cuentaEmisora: str
    bancoReceptor: str
    cuentaReceptora: str
    montoAbonado: float
    claveRastreo: str
    observaciones: str

    # Función para formatear los campos de fecha
    def __post_init__(self):
        if not isinstance(self.fechaEmision, str) and math.isnan(self.fechaEmision):
            self.fechaEmision = "NA"
        else:
            self.fechaEmision = datetime.strptime(self.fechaEmision, "%d/%m/%y")

        if not isinstance(self.fechaTransaccion, str) and math.isnan(self.fechaTransaccion):
            self.fechaTransaccion = "NA"
        else:
            self.fechaTransaccion = datetime.strptime(self.fechaTransaccion, "%d/%m/%y")

    def __str__(self):
        return f"Invoice(uuidFactura: {self.uuidFactura}, esManual: {self.esManual}, nombreReceptor: {self.nombreReceptor}, rfcReceptor: {self.rfcReceptor}, nombreEmisor: {self.nombreEmisor}, rfcEmisor: {self.rfcEmisor}, fechaEmision: {self.fechaEmision}, monto: {self.monto}, montoPagado: {self.montoPagado}, montoAPagar: {self.montoAPagar}, metodoPago: {self.metodoPago}, vigencia: {self.vigencia}, divisaFactura: {self.divisaFactura}, divisaMovimiento: {self.divisaMovimiento}, estadoFactura: {self.estadoFactura}, idTransaccion: {self.idTransaccion}, montoTransaccion: {self.montoTransaccion}, fechaTransaccion: {self.fechaTransaccion}, bancoEmisor: {self.bancoEmisor}, bancoEmisor: {self.bancoEmisor}, cuentaEmisora: {self.cuentaEmisora}, bancoReceptor: {self.bancoReceptor}, cuentaReceptora: {self.cuentaReceptora}, montoAbonado: {self.montoAbonado}, claveRastreo: {self.claveRastreo}, observaciones: {self.observaciones})"

    def __repr__(self):
        return f"Invoice(uuidFactura: {self.uuidFactura}, idTransaccion: {self.idTransaccion}, montoTransaccion: {self.montoTransaccion}, monto: {self.monto}, montoPagado: {self.montoPagado}, montoAPagar: {self.montoAPagar})"
