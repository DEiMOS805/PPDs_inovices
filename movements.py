from dataclasses import dataclass
from datetime import datetime
import math


@dataclass
class Movement:
    """Clase que representa un movimiento bancario."""

    idTransaccion: str
    empresa: str
    fecha: str
    hora: str
    cuenta: str
    concepto: str
    monto: float
    cargo: float
    abono: float
    moneda: str
    montoPosterior: float
    referencia: str
    tipoCuenta: str
    claveRastreo: str
    tipoMovimiento: str
    bancoEmisor: str
    bancoReceptor: str
    cuentaEmisora: str
    cuentaReceptora: str
    aliasCuenta: str
    nombreEmisor: str
    rfcEmisor: str
    nombreReceptor: str
    rfcReceptor: str
    cepDia: str
    cepMes: str
    cepAnio: str
    cepHora: str
    cepClaveRastreo: str
    cepAmount: str
    cepIva: str
    cepConcepto: str
    cepRfcReceptor: str
    cepNombreReceptor: str
    cepCuentaReceptora: str
    cepBancoReceptor: str
    cepRfcEmisor: str
    cepNombreEmisor: str
    cepCuentaEmisora: str
    cepBancoEmisor: str
    categoria: str

    # Función para formatear los campos de fecha
    def __post_init__(self):
        if not isinstance(self.fecha, str) and math.isnan(self.fecha):
            self.fecha = "NA"
        else:
            self.fecha = datetime.strptime(self.fecha, "%d/%m/%y")

    def __str__(self):
        return f"Movimiento(idTransaccion: {self.idTransaccion}, empresa: {self.empresa}, fecha: {self.fecha}, hora: {self.hora}, cuenta: {self.cuenta}, concepto: {self.concepto}, monto: ${self.monto}, cargo: ${self.cargo}, abono: ${self.abono}, moneda: {self.moneda}, montoPosterior: ${self.montoPosterior}, referencia: {self.referencia}, tipoCuenta: {self.tipoCuenta}, claveRastreo: {self.claveRastreo}, tipoMovimiento: {self.tipoMovimiento}, bancoEmisor: {self.bancoEmisor}, bancoReceptor: {self.bancoReceptor}, cuentaEmisora: {self.cuentaEmisora}, cuentaReceptora: {self.cuentaReceptora}, aliasCuenta: {self.aliasCuenta}, nombreEmisor: {self.nombreEmisor}, rfcEmisor: {self.rfcEmisor}, nombreReceptor: {self.nombreReceptor}, rfcReceptor: {self.rfcReceptor}, cepDia: {self.cepDia}, cepMes: {self.cepMes}, cepAnio: {self.cepAnio}, cepHora: {self.cepHora}, cepClaveRastreo: {self.cepClaveRastreo}, cepAmount: {self.cepAmount}, cepIva: {self.cepIva}, cepConcepto: {self.cepConcepto}, cepRfcReceptor: {self.cepRfcReceptor}, cepNombreReceptor: {self.cepNombreReceptor}, cepCuentaReceptora: {self.cepCuentaReceptora}, cepBancoReceptor: {self.cepBancoReceptor}, cepRfcEmisor: {self.cepRfcEmisor}, cepNombreEmisor: {self.cepNombreEmisor}, cepCuentaEmisora: {self.cepCuentaEmisora}, cepBancoEmisor: {self.cepBancoEmisor}, categoria: {self.categoria})"

    def __repr__(self):
        return f"Movimiento(idTransaccion: {self.idTransaccion}, monto: ${self.monto}, cargo: ${self.cargo}, abono: ${self.abono})"
