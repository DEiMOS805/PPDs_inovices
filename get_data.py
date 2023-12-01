import pandas as pd
from movements import Movement
from invoice import Invoice


def get_movements(df):
    movements = []
    for index, row in df.iterrows():
        movements.append(
            Movement(
                row["idTransaccion"],
                row["Empresa"],
                row["Fecha"],
                row["Hora"],
                row["Cuenta"],
                row["Concepto"],
                row["Monto"],
                row["Cargo"],
                row["Abono"],
                row["Moneda"],
                row["MontoPosterior"],
                row["Referencia"],
                row["TipoCuenta"],
                row["ClaveRastreo"],
                row["TipoMovimiento"],
                row["BancoEmisor"],
                row["BancoReceptor"],
                row["CuentaEmisora"],
                row["CuentaReceptora"],
                row["AliasCuenta"],
                row["NombreEmisor"],
                row["RFCEmisor"],
                row["NombreReceptor"],
                row["RFCReceptor"],
                row["CEP_Dia"],
                row["CEP_Mes"],
                row["CEP_Anio"],
                row["CEP_Hora"],
                row["CEP_ClaveRastreo"],
                row["CEP_Amount"],
                row["CEP_IVA"],
                row["CEP_Concepto"],
                row["CEP_RFCReceptor"],
                row["CEP_NombreReceptor"],
                row["CEP_CuentaReceptora"],
                row["CEP_BancoReceptor"],
                row["CEP_RFCEmisor"],
                row["CEP_NombreEmisor"],
                row["CEP_CuentaEmisora"],
                row["CEP_BancoEmisor"],
                row["Categoria"],
            )
        )
    return movements


def get_invoices(df):
    invoices = []
    for index, row in df.iterrows():
        invoices.append(
            Invoice(
                row["UUIDFactura"],
                row["EsManual"],
                row["Nombre_Receptor"],
                row["RFC_Receptor"],
                row["Nombre_Emisor"],
                row["RFC_Emisor"],
                row["FechaEmision"],
                row["Monto"],
                row["MontoPagado"],
                row["MontoAPagar"],
                row["MetodoPago"],
                row["Vigencia"],
                row["DivisaFactura"],
                row["DivisaMovimiento"],
                row["EstadoFactura"],
                row["IdTransaccion"],
                row["MontoTransaccion"],
                row["FechaTransaccion"],
                row["TransaccionConcepto"],
                row["BancoEmisor"],
                row["CuentaEmisora"],
                row["BancoReceptor"],
                row["CuentaReceptora"],
                row["MontoAbonado"],
                row["ClaveRastreo"],
                row["Observaciones"],
            )
        )
    return invoices
