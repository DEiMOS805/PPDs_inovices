from datetime import datetime
from random import sample
import argparse as ap
import pandas as pd
import calendar
import logging
import time
import sys

from get_data import get_movements, get_invoices


# Constants to control de tabu search algorithm
SOLUTIONS_NUM = 2                   # Number of candidates to search
MAX_SOLUTIONS_NUM = 5               # Maximum number of candidates to search
ITERATIONS = 1000                   # Number of iterations to make


if __name__ == "__main__":
    # Start time to measure total execution time
    start_time = time.time()

    # LOGGING CONFIGURATION
    # Define logging basic configuration
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define logging format
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

    # Define file handler
    file_handler = logging.FileHandler("./execution.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Define stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # GET DATA FROM COMMAND LINE
    # Define command line arguments
    logger.info("Getting data from command line...")
    argparser = ap.ArgumentParser()
    argparser.add_argument("--uuidFactura", type=str, help="uuidFactura to search for PDD invoices (string data type)")
    logger.info("Data from command line: %s", argparser.parse_args())
    logger.info("All data from command line was successfully obtained")

    # Parse command line arguments
    logger.info("Parsing command line arguments...")
    args = argparser.parse_args()
    logger.info("Command line arguments were successfully parsed")

    # Get values from command line arguments
    logger.info("Getting values from command line arguments...")
    uuidFactura = args.uuidFactura
    logger.info("Values from command line arguments: %s", uuidFactura)

    # TRANSFORM DATA TO WORK WITH
    # Load data from csv files (datasets)
    logger.info("Loading data from csv files...")
    movements_dataset = pd.read_csv("./data/PAQUETE_20231113/movimientos.csv")
    logger.info("Data from csv file: \"./data/PAQUETE_20231113/movimientos.csv\" loaded successfully")
    invoices_cxc_dataset = pd.read_csv("./data/PAQUETE_20231113/reportCXC.csv")
    logger.info("Data from csv file: \"./data/PAQUETE_20231113/reportCXC.csv\" loaded successfully")
    invoices_cxp_dataset = pd.read_csv("./data/PAQUETE_20231113/reportCXP.csv")
    logger.info("Data from csv file: \"./data/PAQUETE_20231113/reportCXP.csv\" loaded successfully")
    logger.info("All data from csv files was successfully loaded")

    # Transform data into our "movement" and "invoice" classes
    logger.info("Transforming data into our \"movement\" and \"invoice\" classes...")
    movements = get_movements(movements_dataset)
    logger.info("Data from data frame: \"movements_dataset\" transformed successfully")
    invoices_cxc = get_invoices(invoices_cxc_dataset)
    logger.info("Data from csv file: \"invoices_cxc\" transformed successfully")
    invoices_cxp = get_invoices(invoices_cxp_dataset)
    logger.info("Data from csv file: \"invoices_cxp\" transformed successfully")
    logger.info("All data was successfully transformed")
    # print(invoices_cxc[:2])

    # Make sure data was loaded correctly
    logger.info("Total movements found and loaded: %s", len(movements))
    logger.info("Total CxC invoices found and loaded: %s", len(invoices_cxc))
    logger.info("Total CxP invoices found and loaded: %s", len(invoices_cxp))

    # Filter PPD invoices from CXC and CXP invoices to reduce search space
    logger.info("Filtering PPD invoices from CXC and CXP invoices to reduce search space...")
    invoices_cxc = list(filter(lambda invoice: invoice.metodoPago == "PPD", invoices_cxc))
    invoices_cxp = list(filter(lambda invoice: invoice.metodoPago == "PPD", invoices_cxp))
    logger.info("PPD invoices from CXC and CXP invoices filtered successfully")

    # Make sure filter step worked
    logger.info("CxC invoices after \"PPD\" filter: %s", len(invoices_cxc))
    logger.info("CxP invoices after \"PPD\" filter: %s", len(invoices_cxp))

    # Filter movements in which the amount is 0.01
    logger.info("Removing movements in which the amount is $0.01...")
    movements = list(filter(lambda movement: movement.monto != 0.01, movements))
    logger.info(f"Movements after \"0.01\" filter: {len(movements)}")

    # Search for invoice target in CxC invoices
    logger.info("Searching for invoice target in CxC invoices...")
    invoice_target = list(filter(lambda invoice: invoice.uuidFactura == uuidFactura, invoices_cxc))
    # Validate if invoice target was found in CxC invoices
    if invoice_target == []:
        logger.warning("Invoice target not found in CxC invoices")
        # Search for invoice target in CxP invoices if not found in CxC invoices
        logger.info("Searching for invoice target in CxP invoices...")
        invoice_target == list(filter(lambda invoice: invoice.uuidFactura == uuidFactura, invoices_cxp))
        # Validate if invoice target was found in CxP invoices
        if invoice_target == []:
            logger.critical("Invoice target not found in CxP invoices")
            logger.info("Finishing process...")
            sys.exit()
        else:
            logger.info("Invoice target found in CxP invoices")
            # True if invoice target was found in CxC invoices, False otherwise
            invoice_issued = False # Search for egresses
    else:
        logger.info("Invoice target found in CxC invoices")
        invoice_issued = True # Search for incomes

    # Simplify access to invoice target data
    invoice_target = invoice_target[0]
    logger.debug("Invoice target data: %s", invoice_target)

    # Check if invoice target was already paid
    logger.info("Checking if invoice target was already paid...")
    if invoice_target.estadoFactura == "PAGADA":
        logger.info("Invoice target was already paid. Nothing to do.")
        logger.info("Finishing process...")
        sys.exit()

    # FILTER MOVEMENTS BY DATE
    # Define beginning and end dates
    logger.info("Filtering movements by date...")
    beginning_date = datetime(invoice_target.fechaEmision.year - 1, 1, 1)
    logger.info("Beginning date to make conciliation process: %s", beginning_date)
    end_date = datetime(invoice_target.fechaEmision.year, invoice_target.fechaEmision.month, calendar.monthrange(invoice_target.fechaEmision.year, invoice_target.fechaEmision.month)[1])
    logger.info("End date to make conciliation process: %s", end_date)

    # Make filter step
    logger.info("Filtering movements by date...")
    movements = list(filter(lambda movement: beginning_date <= movement.fecha <= end_date, movements))
    logger.info("Movements filtered by date successfully")
    logger.info("Total movements after date filter: %s", len(movements))

    # Filter movements by incomes or egresses
    logger.info("Filtering movements by incomes or egresses...")
    if invoice_issued:
        logger.info("Filtering movements by egresses...")
        movements = list(filter(lambda movement: movement.abono != 0, movements))
        logger.info("Movements filtered by egresses successfully")
        logger.info("Total movements after egresses filter: %s", len(movements))
    else:
        logger.info("Filtering movements by incomes...")
        movements = list(filter(lambda movement: movement.cargo != 0, movements))
        logger.info("Movements filtered by incomes successfully")
        logger.info("Total movements after incomes filter: %s", len(movements))

    # Filter movements by currency
    logger.info("Filtering movements by currency...")
    movements = list(filter(lambda movement: movement.moneda == invoice_target.divisaFactura, movements))
    logger.info("Movements filtered by currency successfully")
    # Make sure filter step worked
    logger.info("Total movements after currency filter: %s", len(movements))

    # FILTER MOVEMENTS BY AMOUNT
    # Search for movements with the same amount as invoice target
    logger.info("Searching for movements with the same amount as invoice target...")
    one_payment_movement = list(filter(lambda movement: movement.monto == invoice_target.monto, movements))
    logger.info("Movements with the same amount as invoice target searched finished.")

    # Movement found (to consider)
    if one_payment_movement != []:
        logger.info(f"Movement found with the same amount as invoice target: {one_payment_movement}")
        logger.info("Finishing process...")
        sys.exit()

    # Make Tabu Search Algorithm
    logger.warning("No movement found with the same amount as invoice target")
    logger.info("Searching for movements sets with a sum of amounts similars as invoice target...")
    logger.info("Tabu Search Algorithm started...")

    # Initialize variables
    better_movements_solution = []      # Better movements solution found so far
    smaller_difference = float("inf")   # Smaller difference between total amount of local movements and invoice target
    best_total = 0                      # Best total amount of local movements found so far
    tabu_list = []                      # List of movements to avoid (movement sets already explored)

    # Log variables
    logger.debug(f"Number of candidates to search: {SOLUTIONS_NUM}")
    logger.debug(f"Better movements solution: {better_movements_solution}")
    logger.debug(f"Smaller difference: {smaller_difference}")
    logger.debug(f"Tabu list: {tabu_list}")
    logger.info(f"Limit of iterations to make: {ITERATIONS}")
    logger.info(f"Range of combinations to search: [{SOLUTIONS_NUM}-{MAX_SOLUTIONS_NUM}]")

    # Variable to measure tabu search algorithm execution time
    start_search_time = time.time()

    # Tabu Search Algorithm
    for actual_solutions_num in range(SOLUTIONS_NUM, MAX_SOLUTIONS_NUM + 1):
        logger.debug(f"Actual solutions num: {actual_solutions_num}")

        for i in range(ITERATIONS):
            logger.debug(f"Iteration: {i} of the first for loop")

            # Get random movements from movements list
            logger.debug("Getting random movements from movements list...")
            local_solution = sample(movements, actual_solutions_num)
            logger.debug(f"Selected movements: {local_solution}")

            # Check if neighboor is already inside tabu list
            if sorted(local_solution, key=lambda movement: movement.monto) in tabu_list:
                logger.debug("Random solution is already in tabu list, passing to next iteration...")
                continue
            else:
                # Calculate total amount of local movements
                logger.debug("Random solution is not in tabu list. Calculating total amount of local movements...")
                total = sum(movement.monto for movement in local_solution)
                logger.debug(f"Total amount of local movements: {total}")
                # Calculate difference between total amount of local movements and invoice target
                local_difference = abs(total - invoice_target.monto)
                logger.debug(f"Difference between total amount of local movements and invoice target: {local_difference}")
                # Check if actual local solution is better than previous best local solution
                if local_difference <= smaller_difference:
                    logger.debug("Local solution is better than previous local solution. Updating variables...")
                    smaller_difference = local_difference
                    logger.debug(f"New smaller difference: {smaller_difference}")
                    best_total = total
                    logger.debug(f"New best total: {best_total}")
                    better_movements_solution = local_solution
                    logger.debug(f"New better movements solution: {better_movements_solution}")

                # Add neighboor to tabu list
                tabu_list.append(sorted(local_solution, key=lambda movement: movement.monto))
                # Limit tabu list to 10 elements to avoid memory overflow
                # if len(tabu_list) > 10:
                #     tabu_list.pop(0)

    # Variable to measure tabu search algorithm execution time
    end_search_time = time.time()
    logger.info(f"Search for movements sets took: {end_search_time - start_search_time:.3}s")

    # Print results
    logger.info(f"Better movements set: {better_movements_solution}")
    logger.info(f"Number of movements in better movements set: {len(better_movements_solution)}")
    logger.info(f"Total amount of better movements set: ${best_total:.2f}")
    logger.info(f"Amount to pay of the target invoice: ${invoice_target.monto:.2f}")

    # Print execution time
    finish_time = time.time()
    logger.info(f"Total execution time: {finish_time - start_time:.3f}s")
    logger.info("Finishing process...")
