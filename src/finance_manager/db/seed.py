import random
from datetime import datetime, timedelta
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.category_pattern import CategoryPattern
from finance_manager.models.person import Person
from finance_manager.models.transaction import Transaction
from finance_manager.models.transaction_category import TransactionCategory
from finance_manager.models.transaction_source import TransactionSource

_DATE_RANGE_START = datetime(2026, 1, 1)
_DATE_RANGE_END = datetime(2026, 8, 1)


async def seed(session: AsyncSession) -> None:
    people = [
        Person(first_name="Chase", last_name="McDonald"),
        Person(first_name="Hannah", last_name="McDonald"),
    ]

    session.add_all(people)
    await session.flush()

    sources = [
        TransactionSource(name="Chase Fidelity Checking", owner=people[0]),
        TransactionSource(name="hannah Fidelity Checking", owner=people[1]),
        TransactionSource(name="chase WF Credit", owner=people[0]),
        TransactionSource(name="hannah CB Credit", owner=people[1]),
        TransactionSource(name="hannah Discover Credit", owner=people[1]),
        TransactionSource(name="hannah HCB Checking", owner=people[1]),
        TransactionSource(name="Chase Bilt credit", owner=people[0]),
    ]
    session.add_all(sources)
    await session.flush()

    categories = [
        TransactionCategory(name="rent", description="For the place we live"),
        TransactionCategory(name="eating Out"),
        TransactionCategory(name="transfers"),
        TransactionCategory(name="chase Paycheck"),
        TransactionCategory(name="megan School"),
        TransactionCategory(name="car Insurance"),
        TransactionCategory(name="misc Income"),
        TransactionCategory(name="groceries"),
        TransactionCategory(name="hannah Paycheck"),
        TransactionCategory(name="Utilities"),
        TransactionCategory(name="gasoline"),
        TransactionCategory(name="automotive"),
        TransactionCategory(name="fun"),
        TransactionCategory(name="other"),
        TransactionCategory(name="sat Phone"),
        TransactionCategory(name="emergency"),
        TransactionCategory(name="exclude"),
        TransactionCategory(name="adventure"),
        TransactionCategory(name="gifts"),
        TransactionCategory(name="Ski Pass"),
        TransactionCategory(name="Laundry"),
    ]

    session.add_all(categories)
    await session.flush()

    patterns = [
        CategoryPattern(pattern="Integrated Mou", transaction_category=categories[0]),
        CategoryPattern(pattern="WAL-MART"),
    ]

    session.add_all(patterns)
    await session.flush()

    trans = make_trans(sources, categories)
    session.add_all(trans)
    await session.flush()


def make_tran(
    amount: Decimal, summary: str, category: TransactionCategory, source: TransactionSource
) -> Transaction:
    return Transaction(
        timestamp=random_timestamp(),
        amount=amount,
        summary=summary,
        transaction_category=category,
        transaction_source=source,
    )


def random_timestamp() -> datetime:
    return _DATE_RANGE_START + timedelta(
        seconds=random.randint(0, int((_DATE_RANGE_END - _DATE_RANGE_START).total_seconds()))
    )


def make_trans(
    sources: list[TransactionSource], categories: list[TransactionCategory]
) -> list[Transaction]:
    trans: list[Transaction] = []
    trans.append(
        make_tran(
            Decimal("33.34"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("33.34"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1425.49"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("512.08"), "WHITWORTH DPT DEPOSIT 5097773222 WA", categories[4], sources[4]
        )
    )
    trans.append(
        make_tran(Decimal("1390.30"), "ONLINE ACH PAYMENT THANK YOU", categories[2], sources[2])
    )
    trans.append(
        make_tran(Decimal("698.29"), "GEICO *AUTO 800-841-3000 DC", categories[5], sources[2])
    )
    trans.append(
        make_tran(Decimal("2070.69"), "ONLINE ACH PAYMENT THANK YOU", categories[2], sources[6])
    )
    trans.append(
        make_tran(
            Decimal("125.72"), "CASHBACK BONUS REDEMPTION PYMT/STMT CRDT", categories[6], sources[4]
        )
    )
    trans.append(
        make_tran(Decimal("1449.14"), "INTERNET PAYMENT - THANK YOU", categories[2], sources[4])
    )
    trans.append(
        make_tran(Decimal("53.10"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("7500.00"),
            "TRANSFERRED TO VS 242-650231-1 CURRENT CONTRIBUTION (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("1131.21"), "TRANSFERRED FROM TRANSFER (Cash)", categories[2], sources[0])
    )
    trans.append(
        make_tran(
            Decimal("68.92"),
            "GLENWOOD SPR*UTILITY 970-384-6455 CO766X7GHGRH",
            categories[9],
            sources[4],
        )
    )
    trans.append(
        make_tran(
            Decimal("2.50"),
            "TYL*GLENWOOD SERV FEE 972-713-3700 TX766X7GHGRHFEE",
            categories[9],
            sources[4],
        )
    )
    trans.append(
        make_tran(Decimal("1131.21"), "TRANSFERRED TO TRANSFER (Cash)", categories[2], sources[1])
    )
    trans.append(
        make_tran(
            Decimal("5000.00"),
            "TRANSFERRED TO VS 258-183612-1 CURRENT CONTRIBUTION (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("49.42"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1390.30"),
            "DIRECT DEBIT WELLS FARGO CACCPYMT (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("2070.69"),
            "DIRECT DEBIT WELLS FARGO CACCPYMT (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1000.00"),
            "FID BKG SVC LLC MONEYLINE Z28570799 1TBPY",
            categories[2],
            sources[5],
        )
    )
    trans.append(
        make_tran(
            Decimal("1000.00"),
            "Electronic categories[12]ds Transfer Paid (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1449.14"), "DIRECT DEBIT DISCOVER E-PAYMENT (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(Decimal("18.00"), "MASABI RFTA GLENWOOD SPRICO", categories[10], sources[6])
    )
    trans.append(make_tran(Decimal("1879.96"), "CK # 1026", categories[11], sources[5]))
    trans.append(
        make_tran(Decimal("42.59"), "TST*SLOPE & HATCH Glenwood SpriCO", categories[1], sources[2])
    )
    trans.append(
        make_tran(Decimal("94.37"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("43.62"), "PHILLIPS 66 - ALTA CONVENGLENWOOD SPRICO", categories[10], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("17.32"), "RAGGED MOUNTAIN SPORTS CARBONDALE CO", categories[12], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("41.52"), "WAL-MART #1095 GLENWOOD SPRICO", categories[13], sources[2])
    )
    trans.append(
        make_tran(Decimal("47.95"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("25.00"), "CASH BACK REDEMPTION REF 190905174", categories[6], sources[2])
    )
    trans.append(
        make_tran(Decimal("20.78"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1802.41"),
            "DIRECT DEPOSIT Kimley-Horn CORP CRED (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1425.36"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("63.50"), "MEOW WOLF MEOWWOLF.COM NM", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("86.32"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("9.00"), "MASABI RFTA GLENWOOD SPRICO", categories[10], sources[6])
    )
    trans.append(
        make_tran(Decimal("3.64"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(
            Decimal("130.08"), "RAGGED MOUNTAIN SPORTS CARBONDALE CO", categories[12], sources[4]
        )
    )
    trans.append(
        make_tran(Decimal("2.95"), "BIG JOHNS ACE HDWE GLENWOOD SPRICO", categories[12], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("65.93"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("2000.00"), "DIRECT DEBIT UGIFT529 GIFT (Cash)", categories[4], sources[1]
        )
    )
    trans.append(
        make_tran(Decimal("43.43"), "STINKER #317 GLENWOOD SPRICO", categories[10], sources[4])
    )
    trans.append(
        make_tran(Decimal("0.96"), "BIG JOHNS ACE HDWE GLENWOOD SPRICO", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("117.59"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("23.55"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("1900.00"), "BPS*BILT RENT NEW YORK NY", categories[0], sources[6])
    )
    trans.append(make_tran(Decimal("2.49"), "BPS*BILT RENT NEW YORK NY", categories[0], sources[6]))
    trans.append(
        make_tran(Decimal("18.00"), "MASABI RFTA GLENWOOD SPRICO", categories[10], sources[6])
    )
    trans.append(make_tran(Decimal("250.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(
        make_tran(
            Decimal("1425.35"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("10.20"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn CORP CRED (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("36.91"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("36.91"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("31.25"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("31.25"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("13.34"), "CITY-MARKET #0437 BUENA VISTA CO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("45.55"), "SHELL OIL 57444284905 MINTURN CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(Decimal("4.92"), "CITY-MARKET #0437 BUENA VISTA CO", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("1188.27"), "ONLINE ACH PAYMENT THANK YOU", categories[2], sources[2])
    )
    trans.append(
        make_tran(Decimal("9.00"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(Decimal("1965.49"), "ONLINE ACH PAYMENT THANK YOU", categories[2], sources[6])
    )
    trans.append(
        make_tran(Decimal("76.56"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("413.76"), "INTERNET PAYMENT - THANK YOU", categories[2], sources[4])
    )
    trans.append(
        make_tran(Decimal("1107.72"), "TRANSFERRED TO TRANSFER (Cash)", categories[2], sources[0])
    )
    trans.append(
        make_tran(
            Decimal("83.50"),
            "GLENWOOD SPR*UTILITY 970-384-6455 COTYLX16045672",
            categories[9],
            sources[4],
        )
    )
    trans.append(
        make_tran(
            Decimal("2.92"),
            "TYL*GLENWOOD SERV FEE 972-713-3700 TXTYLX16045788",
            categories[9],
            sources[4],
        )
    )
    trans.append(
        make_tran(
            Decimal("2500.00"),
            "TRANSFERRED TO VS 258-183612-1 CURRENT CONTRIBUTION (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("1107.72"), "TRANSFERRED FROM TRANSFER (Cash)", categories[2], sources[1])
    )
    trans.append(
        make_tran(
            Decimal("1188.27"),
            "DIRECT DEBIT WELLS FARGO CACCPYMT (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1965.49"),
            "DIRECT DEBIT WELLS FARGO CACCPYMT (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("413.76"), "DIRECT DEBIT DISCOVER E-PAYMENT (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("196.73"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("50.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(
        make_tran(
            Decimal("40.71"), "MAVERIK #05032 GLENWOO GLENWOOD SPRICO", categories[10], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("30.45"),
            "DIRECT DEPOSIT Kimley-Horn EDI PYMNTS (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("102.50"), "THE KNOT REGISTRY THEKNOT.COM/RMD", categories[18], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("57.46"), "RALPHS #0221 SAN CLEMENTE CA", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("42.00"), "RPS GRAND JUNCTION GRAND JCT CO", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("64.46"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("95.72"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("25.00"), "CASH BACK REDEMPTION REF 193005098", categories[6], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("36.82"), "ALTA CONVENIENCE 6019 GLENWOOD SPRICO", categories[10], sources[4]
        )
    )
    trans.append(
        make_tran(
            Decimal("1425.36"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("20.83"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("25.10"), "USPS PO 0737080538 GLENWOOD SPRICO", categories[18], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn CORP CRED (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("7.63"), "BIG JOHNS ACE HDWE GLENWOOD SPRICO", categories[12], sources[4])
    )
    trans.append(
        make_tran(Decimal("24.71"), "TST*SLOPE & HATCH Glenwood SpriCO", categories[1], sources[2])
    )
    trans.append(
        make_tran(Decimal("12.74"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("111.22"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(Decimal("22.50"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(make_tran(Decimal("1000.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(
        make_tran(
            Decimal("1809.45"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("47.20"), "PHILLIPS 66 - ALTA CONVENGLENWOOD SPRICO", categories[10], sources[6]
        )
    )
    trans.append(
        make_tran(
            Decimal("537.46"),
            "PT *VALLEY VIEW HOSPITAL 970-384-6890 CO",
            categories[15],
            sources[2],
        )
    )
    trans.append(
        make_tran(
            Decimal("598.00"), "STEAMBOAT MTN RESERVAT STEAMBOAT SPRCO", categories[16], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("60.13"), "SQ *HODGE POTTERY New Castle CO", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("104.80"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[4])
    )
    trans.append(
        make_tran(
            Decimal("8.81"), "RAGGED MOUNTAIN SPORTS CARBONDALE CO", categories[12], sources[2]
        )
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("1900.00"),
            "DIRECT DEBIT Integrated MouWEB PMTS (Cash)",
            categories[0],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1425.36"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("91.87"), "ALTARD STATE/VOWD 100", categories[17], sources[3]))
    trans.append(
        make_tran(
            Decimal("2.49"), "DIRECT DEBIT AppFolio, Inc.WEB PMTS (Cash)", categories[0], sources[0]
        )
    )
    trans.append(
        make_tran(
            Decimal("30.20"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("30.20"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("27.29"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("27.29"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("13.73"), "WASH BY U NEW CASTLE CO", categories[11], sources[2]))
    trans.append(make_tran(Decimal("86.07"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("43.74"), "REPLAY SPORTS GWS", categories[12], sources[3]))
    trans.append(
        make_tran(Decimal("42.89"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[2])
    )
    trans.append(
        make_tran(Decimal("550.29"), "INTERNET PAYMENT - THANK YOU", categories[2], sources[4])
    )
    trans.append(
        make_tran(Decimal("12.56"), "SQ *ALPENGLOW BOOKS &amp; GIF", categories[12], sources[3])
    )
    trans.append(make_tran(Decimal("64.54"), "TST*ROSIS LITTLE BAVARI", categories[1], sources[3]))
    trans.append(make_tran(Decimal("95.00"), "ANNUAL MEMBERSHIP FEE", categories[13], sources[3]))
    trans.append(make_tran(Decimal("109.87"), "Payment Thank You - Web", categories[2], sources[3]))
    trans.append(
        make_tran(
            Decimal("3000.00"), "TRANSFERRED TO VS Z24-421958-1 (Cash)", categories[2], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("1028.81"), "TRANSFERRED FROM TRANSFER (Cash)", categories[2], sources[0])
    )
    trans.append(
        make_tran(Decimal("15.99"), "FREETAXUSACOM 877-269-9027 UT", categories[13], sources[2])
    )
    trans.append(
        make_tran(Decimal("15.99"), "FREETAXUSACOM 877-269-9027 UT", categories[13], sources[4])
    )
    trans.append(
        make_tran(
            Decimal("109.87"), "DIRECT DEBIT CHASE CREDIT CEPAY (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(Decimal("1028.81"), "TRANSFERRED TO TRANSFER (Cash)", categories[2], sources[1])
    )
    trans.append(
        make_tran(
            Decimal("1392.14"), "TRANSFERRED TO VS Z30-618311-1 (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("42.89"),
            "DIRECT DEBIT WF Credit CardAUTO PAY (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("270.00"), "DIRECT DEBIT IRS USATAXPYMT (Cash)", categories[16], sources[0]
        )
    )
    trans.append(
        make_tran(
            Decimal("550.29"), "DIRECT DEBIT DISCOVER E-PAYMENT (Cash)", categories[2], sources[1]
        )
    )
    trans.append(make_tran(Decimal("39.00"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("784.00"),
            "DIRECT DEPOSIT IRS TREAS 3 TAX REF (Cash)",
            categories[16],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("54.30"), "CIRCLE K # 44112", categories[10], sources[3]))
    trans.append(make_tran(Decimal("79.80"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("50.64"), "PHILLIPS 66 - ALTITUDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("10.73"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("50.00"), "DIRECT DEBIT VENMO PAYMENT (Cash)", categories[18], sources[0])
    )
    trans.append(
        make_tran(
            Decimal("606.00"),
            "DIRECT DEPOSIT CO DEPT REVECOSTTAXRFD (Cash)",
            categories[16],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("599.00"),
            "DIRECT DEPOSIT CO DEPT REVECOSTTAXRFD (Cash)",
            categories[16],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("25.00"), "CASH BACK REDEMPTION REF 195186395", categories[6], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1508.69"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("20.83"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("26.83"),
            "DIRECT DEPOSIT Kimley-Horn EDI PYMNTS (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("60.81"), "MAVERIK #5208", categories[10], sources[3]))
    trans.append(make_tran(Decimal("2.96"), "TYL*GLENWOOD SERV FEE", categories[9], sources[3]))
    trans.append(make_tran(Decimal("20.10"), "Etsy.com*SkySugarPierc", categories[17], sources[3]))
    trans.append(make_tran(Decimal("104.42"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("84.59"), "GLENWOOD SPR*UTILITY", categories[9], sources[3]))
    trans.append(make_tran(Decimal("32.81"), "TARGET        00020297", categories[18], sources[3]))
    trans.append(make_tran(Decimal("40.30"), "LOVE'S #0517 OUTSIDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("9.88"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("124.35"), "eBay O*16-14360-60413", categories[13], sources[3]))
    trans.append(make_tran(Decimal("20.00"), "Hanging Lake", categories[12], sources[3]))
    trans.append(make_tran(Decimal("9.88"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(make_tran(Decimal("86.31"), "AMAZON MKTPL*BP4BN7RU0", categories[17], sources[3]))
    trans.append(make_tran(Decimal("19.00"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(make_tran(Decimal("17.66"), "AMAZON MKTPL*BP0LE2R10", categories[17], sources[3]))
    trans.append(make_tran(Decimal("38.48"), "BRFACTORY.COM", categories[17], sources[3]))
    trans.append(make_tran(Decimal("136.98"), "CHACOS.COM", categories[17], sources[3]))
    trans.append(
        make_tran(
            Decimal("163.78"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("100.00"),
            "Cash eWithdrawal in Branch 03/20/2026 10:30 AM 205 E MEADOWS DR GLENWOOD SPRINGS CO",
            categories[20],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("118.34"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("428.00"), "PT *VALLEY VIEW HOSPITAL", categories[15], sources[3])
    )
    trans.append(make_tran(Decimal("50.17"), "RAGGED MOUNTAIN SPORTS", categories[12], sources[3]))
    trans.append(make_tran(Decimal("42.61"), "PHILLIPS 66 - ALTITUDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("2.50"), "AMAZON MKTPLACE PMTS Amzn.com/billWA", categories[17], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("2.49"), "DIRECT DEBIT AppFolio, Inc.WEB PMTS (Cash)", categories[0], sources[0]
        )
    )
    trans.append(
        make_tran(
            Decimal("1900.00"),
            "DIRECT DEBIT Integrated MouWEB PMTS (Cash)",
            categories[0],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1475.06"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("813.96"), "SUNLIGHT MTN WEBSITE", categories[19], sources[3]))
    trans.append(
        make_tran(Decimal("328.40"), "UNITED      0162388644446", categories[16], sources[3])
    )
    trans.append(make_tran(Decimal("2.41"), "GLENWOOD SPRINGS ARC THR", categories[12], sources[3]))
    trans.append(make_tran(Decimal("3.19"), "WAL-MART #1095", categories[12], sources[3]))
    trans.append(make_tran(Decimal("484.27"), "Etsy.com*PerluxGold", categories[17], sources[3]))
    trans.append(make_tran(Decimal("112.22"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("35.27"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("35.27"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("34.85"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("34.85"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("428.00"), "PT *VALLEY VIEW HOSPITAL", categories[15], sources[3])
    )
    trans.append(
        make_tran(Decimal("1593.43"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[2])
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("1593.43"),
            "DIRECT DEBIT WF Credit CardAUTO PAY (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("47.20"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[6])
    )
    trans.append(
        make_tran(Decimal("3380.60"), "Payment Thank You - Web", categories[2], sources[3])
    )
    trans.append(
        make_tran(Decimal("15.99"), "INTERNET PAYMENT - THANK YOU", categories[2], sources[4])
    )
    trans.append(make_tran(Decimal("65.14"), "GLENWOOD SPR*UTILITY", categories[9], sources[3]))
    trans.append(make_tran(Decimal("63.22"), "PHILLIPS 66 - ALTITUDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("2.50"), "TYL*GLENWOOD SERV FEE", categories[9], sources[3]))
    trans.append(make_tran(Decimal("35.25"), "RAGGED MOUNTAIN SPORTS", categories[12], sources[3]))
    trans.append(make_tran(Decimal("109.37"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("8.62"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(
            Decimal("599.01"), "TRANSFERRED TO VS Z24-421958-1 (Cash)", categories[2], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("694.10"), "TRANSFERRED TO TRANSFER (Cash)", categories[2], sources[0])
    )
    trans.append(
        make_tran(
            Decimal("-15.99"), "DIRECT DEBIT DISCOVER E-PAYMENT (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("2510.67"), "TRANSFERRED TO VS Z30-618311-1 (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("3380.60"), "DIRECT DEBIT CHASE CREDIT CEPAY (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(Decimal("694.10"), "TRANSFERRED FROM TRANSFER (Cash)", categories[2], sources[1])
    )
    trans.append(
        make_tran(
            Decimal("47.20"),
            "DIRECT DEBIT WF Credit CardAUTO PAY as of 2026-04-03 (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("167.68"),
            "302 RIVERSIDE SIMPLY AUTOGLENWOOD SPRICO",
            categories[11],
            sources[2],
        )
    )
    trans.append(
        make_tran(
            Decimal("1508.70"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("29.73"),
            "DIRECT DEPOSIT Kimley-Horn EDI PYMNTS (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("14.25"), "USPS PO 0737080538", categories[17], sources[3]))
    trans.append(make_tran(Decimal("66.23"), "NEPAL RESTAURANT", categories[1], sources[3]))
    trans.append(make_tran(Decimal("3.43"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("108.00"), "BELLY UP ASPEN", categories[12], sources[3]))
    trans.append(make_tran(Decimal("78.10"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("59.69"), "CIRCLE K # 40682", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("20.83"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(Decimal("2.19"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("20.72"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("484.27"), "Etsy.com*PerluxGold", categories[17], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(make_tran(Decimal("6.24"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("47.71"), "SHELL OIL 57444276505", categories[10], sources[3]))
    trans.append(make_tran(Decimal("40.99"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("122.38"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("13.88"), "EXXON PALISADE", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("228.29"), "JIMS AUTOMOTIVE SERVICE I", categories[11], sources[3])
    )
    trans.append(
        make_tran(Decimal("19.62"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(make_tran(Decimal("79.81"), "AUTOZONE #4062", categories[18], sources[3]))
    trans.append(
        make_tran(Decimal("49.08"), "KING SOOPERS #0657 FUEL Q", categories[10], sources[3])
    )
    trans.append(
        make_tran(
            Decimal("1508.69"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("2.25"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(Decimal("25.62"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(make_tran(Decimal("654.47"), "Etsy.com*JBJewelryHous", categories[17], sources[3]))
    trans.append(
        make_tran(Decimal("2.25"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(Decimal("83.04"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1900.00"),
            "DIRECT DEBIT Integrated MouWEB PMTS (Cash)",
            categories[0],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("2.49"), "DIRECT DEBIT AppFolio, Inc.WEB PMTS (Cash)", categories[0], sources[0]
        )
    )
    trans.append(
        make_tran(
            Decimal("1802.41"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("66.19"), "MAVERIK 5032", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("31.17"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("31.17"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("32.35"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("32.35"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("20.83"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[2])
    )
    trans.append(make_tran(Decimal("42.67"), "TST*SLOPE &amp; HATCH", categories[1], sources[3]))
    trans.append(make_tran(Decimal("46.80"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("3.43"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("59.05"), "PHILLIPS 66 - ALTITUDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("19.35"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("1513.29"), "Payment Thank You - Web", categories[2], sources[3])
    )
    trans.append(
        make_tran(
            Decimal("20.83"),
            "DIRECT DEBIT WF Credit CardAUTO PAY (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1350.29"), "TRANSFERRED TO VS Z24-421958-1 (Cash)", categories[2], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("204.22"), "TRANSFERRED FROM TRANSFER (Cash)", categories[2], sources[0])
    )
    trans.append(
        make_tran(Decimal("204.22"), "TRANSFERRED TO TRANSFER (Cash)", categories[2], sources[1])
    )
    trans.append(
        make_tran(
            Decimal("1513.29"), "DIRECT DEBIT CHASE CREDIT CEPAY (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("1949.48"), "TRANSFERRED TO VS Z30-618311-1 (Cash)", categories[2], sources[1]
        )
    )
    trans.append(make_tran(Decimal("58.55"), "GLENWOOD SPR*UTILITY", categories[9], sources[3]))
    trans.append(make_tran(Decimal("2.50"), "TYL*GLENWOOD SERV FEE", categories[9], sources[3]))
    trans.append(
        make_tran(Decimal("34.01"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1508.68"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("68.21"), "PHILLIPS 66 - ALTITUDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("79.32"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(
            Decimal("630.00"), "DIRECT DEPOSIT VENMO CASHOUT (Cash)", categories[2], sources[0]
        )
    )
    trans.append(make_tran(Decimal("50.43"), "SQ *HIGH ALPINE BREWERY", categories[1], sources[3]))
    trans.append(make_tran(Decimal("45.32"), "MCGILL'S AT CRESTED BUT", categories[1], sources[3]))
    trans.append(make_tran(Decimal("51.19"), "CITY MARKET FUEL 0447", categories[10], sources[3]))
    trans.append(make_tran(Decimal("18.36"), "CITY MARKET #0219 FUEL", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("20.83"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(Decimal("45.55"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("139.20"),
            "DIRECT DEPOSIT Kimley-Horn EDI PYMNTS (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("14.48"), "RIFLE FAST BREAK RIFLE CO", categories[10], sources[2])
    )
    trans.append(make_tran(Decimal("39.92"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("96.03"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("327.57"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1508.69"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("67.78"), "LOVE'S #0007 OUTSIDE", categories[10], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(make_tran(Decimal("16.23"), "WHOLEFDS BLT #10298", categories[16], sources[3]))
    trans.append(
        make_tran(Decimal("17.90"), "WAL-MART #1095 GLENWOOD SPRICO", categories[17], sources[2])
    )
    trans.append(
        make_tran(Decimal("17.98"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(make_tran(Decimal("106.27"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(
            Decimal("1950.00"),
            "DIRECT DEBIT Integrated MouWEB PMTS (Cash)",
            categories[0],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("2.49"), "DIRECT DEBIT AppFolio, Inc.WEB PMTS (Cash)", categories[0], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("16.47"), "QDOBA - SKYPORT 303-3429000 CO", categories[1], sources[2])
    )
    trans.append(
        make_tran(Decimal("7.50"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("19.99"),
            "GOOGLE *GOOGLE ONE G.CO/HELPPAY#CAP1LXVLA0",
            categories[13],
            sources[4],
        )
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("2.00"), "RDM AIRPORT PARKING REDMOND OR", categories[11], sources[2])
    )
    trans.append(
        make_tran(Decimal("396.28"), "MENS WEARHOUSE #2664 BEND OR", categories[16], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("33.06"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("33.06"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("32.66"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("32.66"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("30.32"), "CIRCLE K # 44112", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("20.83"), "GOOGLE *Google One 855-836-3987 CA", categories[13], sources[2]
        )
    )
    trans.append(make_tran(Decimal("34.18"), "Robins", categories[1], sources[3]))
    trans.append(make_tran(Decimal("53.22"), "PHILLIPS 66 - ALTA CON", categories[10], sources[3]))
    trans.append(make_tran(Decimal("6.55"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("357.49"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[2])
    )
    trans.append(make_tran(Decimal("22.50"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("66.69"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("357.49"),
            "DIRECT DEBIT WF Credit CardAUTO PAY (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("130.87"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("1508.70"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(make_tran(Decimal("958.15"), "Payment Thank You - Web", categories[2], sources[3]))
    trans.append(
        make_tran(
            Decimal("19.99"), "CASHBACK BONUS REDEMPTION PYMT/STMT CRDT", categories[6], sources[4]
        )
    )
    trans.append(
        make_tran(
            Decimal("469.63"), "TRANSFERRED TO VS Z32-184732-1 (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("469.63"), "TRANSFERRED FROM VS Z28-570799-1 (Cash)", categories[2], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("1.50"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("80.30"), "PAYPAL *BORAH GEAR 208-484-6357 MT", categories[12], sources[2]
        )
    )
    trans.append(make_tran(Decimal("103.26"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("22.52"), "TST* SWEET COLORADOUGH GL", categories[1], sources[3])
    )
    trans.append(make_tran(Decimal("57.15"), "GLENWOOD SPR*UTILITY", categories[9], sources[3]))
    trans.append(make_tran(Decimal("2.50"), "TYL*GLENWOOD SERV FEE", categories[9], sources[3]))
    trans.append(make_tran(Decimal("253.06"), "LOWES #01905*", categories[13], sources[3]))
    trans.append(
        make_tran(Decimal("62.82"), "STINKER #317 GLENWOOD SPRICO", categories[10], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("958.15"), "DIRECT DEBIT CHASE CREDIT CEPAY (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("2765.47"), "TRANSFERRED TO VS Z30-618311-1 (Cash)", categories[2], sources[1]
        )
    )
    trans.append(make_tran(Decimal("310.24"), "AIRBNB * HMWDDCTCCH", categories[17], sources[3]))
    trans.append(
        make_tran(
            Decimal("400.00"), "DIRECT DEPOSIT VENMO CASHOUT (Cash)", categories[2], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("25.00"), "CASH BACK REDEMPTION REF 201734844", categories[2], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("15.95"), "200047-Meow Wolf-GMP-Park720-5043620 CO", categories[12], sources[2]
        )
    )
    trans.append(make_tran(Decimal("2.75"), "RTD Denver Denver CO", categories[10], sources[2]))
    trans.append(
        make_tran(Decimal("1.75"), "PUBLIC WORKS-PRKG METR DENVER CO", categories[12], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("51.14"), "MAVERIK #05204 IDAHO S IDAHO SPRINGSCO", categories[10], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("32.11"), "TST* LUCKY BIRD - MILK MADENVER CO", categories[1], sources[2])
    )
    trans.append(make_tran(Decimal("42.12"), "ASGEIR REYKJAVIK IS", categories[12], sources[2]))
    trans.append(make_tran(Decimal("104.01"), "BAYMONT INN AND SUITES", categories[12], sources[3]))
    trans.append(make_tran(Decimal("56.82"), "EB *WHEELAND BROTHERS-", categories[18], sources[3]))
    trans.append(
        make_tran(Decimal("37.39"), "SQ *JAFFA KITCHEN Basalt CO", categories[1], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("590.16"),
            "DIRECT DEPOSIT Kimley-Horn EDI PYMNTS (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("20.83"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(Decimal("2.25"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(Decimal("10.19"), "CITY-MARKET #0433 EL JEBEL CO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("91.62"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("4.31"), "SCOOTER'S CAR WASH", categories[11], sources[3]))
    trans.append(
        make_tran(Decimal("416.70"), "PHYSICIANS AT VALLEY VIEW", categories[15], sources[3])
    )
    trans.append(
        make_tran(Decimal("1.50"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(Decimal("74.58"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(make_tran(Decimal("3.12"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("77.71"), "PHILLIPS 66 - ALTITUDE", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("196.00"), "USPS PO 0737080538 GLENWOOD SPRICO", categories[13], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("51.03"), "SHELL OIL 57443812201 SILVERTHORNE CO", categories[10], sources[2]
        )
    )
    trans.append(make_tran(Decimal("4.65"), "WHOLEFDS BLT #10298", categories[7], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("1470.22"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("36.04"), "CO MOTOR VEH SERV EMV DENVER CO", categories[17], sources[2])
    )
    trans.append(make_tran(Decimal("120.60"), "Cardinal Pathology", categories[15], sources[3]))
    trans.append(make_tran(Decimal("117.16"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(
        make_tran(Decimal("102.60"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("13.97"), "SCOOTER'S CAR WASH GLENWOOD SPGSCO", categories[11], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("597.65"),
            "302 RIVERSIDE SIMPLY AUTOGLENWOOD SPRICO",
            categories[11],
            sources[2],
        )
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("58.96"), "CITY MARKET 447 CARBONDALE CO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("62.54"), "CITY MARKET FUEL 0447 CARBONDALE CO", categories[10], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("19.46"), "SQ *SAN JUAN SODA COMPANYPagosa SpringCO", categories[12], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("2.49"), "DIRECT DEBIT AppFolio, Inc.WEB PMTS (Cash)", categories[0], sources[0]
        )
    )
    trans.append(
        make_tran(
            Decimal("1950.00"),
            "DIRECT DEBIT Integrated MouWEB PMTS (Cash)",
            categories[0],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("20.00"), "SQ *HINSDALE COUNTY HISTOLake City CO", categories[12], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("40.74"), "TST*SLOPE &amp; HATCH Glenwood SpriCO", categories[1], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("62.77"), "CITY MARKET #0219 FUEL GUNNISON CO", categories[10], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("8.09"), "LAKE CITY BAKERY LAKE CITY CO", categories[1], sources[2])
    )
    trans.append(
        make_tran(Decimal("40.74"), "TST*SLOPE & HATCH Glenwood SpriCO", categories[1], sources[2])
    )
    trans.append(
        make_tran(Decimal("61.36"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1802.40"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("33.80"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("33.80"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("36.85"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("36.85"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("839.54"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[2])
    )
    trans.append(
        make_tran(Decimal("692.84"), "GEICO *AUTO 800-841-3000 DC", categories[5], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("1508.68"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("130.87"),
            "DIRECT DEPOSIT BRANCH MESSEP2P Hannah Rhude WEB (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("20.61"), "WHOLEFDS BLT #10298", categories[7], sources[3]))
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("839.54"),
            "DIRECT DEBIT WF Credit CardAUTO PAY (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(Decimal("10.00"), "RAINBOW AUTO WASH & STORA", categories[11], sources[2])
    )
    trans.append(
        make_tran(Decimal("8.25"), "RAINBOW AUTO WASH & STORASALIDA CO", categories[11], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("338.29"), "UNITED 0162118006820UNITED.COM TX", categories[16], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("338.29"), "UNITED 0162118006819UNITED.COM TX", categories[16], sources[2]
        )
    )
    trans.append(make_tran(Decimal("57.07"), "LOVE'S #0115 OUTSIDE", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("1728.42"), "Payment Thank You - Web", categories[2], sources[3])
    )
    trans.append(make_tran(Decimal("56.01"), "GLENWOOD SPR*UTILITY", categories[9], sources[3]))
    trans.append(make_tran(Decimal("2.50"), "TYL*GLENWOOD SERV FEE", categories[9], sources[3]))
    trans.append(
        make_tran(
            Decimal("4149.31"), "TRANSFERRED TO VS Z24-421958-1 (Cash)", categories[2], sources[0]
        )
    )
    trans.append(
        make_tran(Decimal("242.64"), "TRANSFERRED FROM TRANSFER (Cash)", categories[2], sources[0])
    )
    trans.append(
        make_tran(Decimal("242.64"), "TRANSFERRED TO TRANSFER (Cash)", categories[2], sources[1])
    )
    trans.append(
        make_tran(
            Decimal("1728.42"), "DIRECT DEBIT CHASE CREDIT CEPAY (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(
            Decimal("2430.42"), "TRANSFERRED TO VS Z30-618311-1 (Cash)", categories[2], sources[1]
        )
    )
    trans.append(
        make_tran(Decimal("84.98"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("327.64"), "REI.COM 800-426-4840 800-426-4840 WA", categories[12], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("36.91"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(Decimal("12.40"), "Maroon Bells Breckenridge CO", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("66.00"), "CIRCLEK #2744112 GLENWOOD SPRICO", categories[10], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("57.90"), "RAGGED MOUNTAIN SPORTS CARBONDALE CO", categories[12], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("20.83"), "ZOLEO USA Inc. SEATTLE WA", categories[14], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("285.10"), "MOUNTAIN VILLAGE RESORT STANLEY ID", categories[12], sources[2]
        )
    )
    trans.append(make_tran(Decimal("123.07"), "CITY-MARKET #0405", categories[7], sources[3]))
    trans.append(make_tran(Decimal("73.00"), "SP MONTELLE INTIMATE", categories[12], sources[3]))
    trans.append(
        make_tran(Decimal("45.79"), "JOCKEY INTERNATIONAL  INC", categories[12], sources[3])
    )
    trans.append(make_tran(Decimal("626.62"), "CHECK RECEIVED (Cash)", categories[6], sources[1]))
    trans.append(make_tran(Decimal("1000.00"), "CHECK RECEIVED (Cash)", categories[6], sources[1]))
    trans.append(
        make_tran(Decimal("75.00"), "CASH BACK REDEMPTION REF 204321291", categories[2], sources[2])
    )
    trans.append(
        make_tran(Decimal("2.78"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(Decimal("89.42"), "American Eagle Outfitters", categories[12], sources[3])
    )
    trans.append(make_tran(Decimal("300.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(make_tran(Decimal("1000.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(
        make_tran(
            Decimal("1898.93"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("22.14"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(make_tran(Decimal("18.00"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("1508.70"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("126.15"),
            "DIRECT DEPOSIT Kimley-Horn EDI PYMNTS (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("15.99"), "LOWES #01905* GLENWOOD SPRICO", categories[12], sources[2])
    )
    trans.append(make_tran(Decimal("10.92"), "TARGET T-2029", categories[12], sources[3]))
    trans.append(make_tran(Decimal("2500.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(make_tran(Decimal("7500.00"), "CHECK RECEIVED (Cash)", categories[6], sources[0]))
    trans.append(
        make_tran(
            Decimal("46.40"),
            "MAVERIK #00651 POCATEL POCATELLO ID651007763930 199",
            categories[10],
            sources[4],
        )
    )
    trans.append(
        make_tran(
            Decimal("48.77"),
            "MAVERIK #05012 RIFLE RIFLE CO501201817631 199",
            categories[10],
            sources[4],
        )
    )
    trans.append(
        make_tran(Decimal("44.66"), "MAVERIK #806 GREEN RIVER WY", categories[10], sources[4])
    )
    trans.append(
        make_tran(
            Decimal("25.00"), "MOUNTAIN VILLAGE RESORT STANLEY ID", categories[12], sources[2]
        )
    )
    trans.append(make_tran(Decimal("39.52"), "STINKER #88 CHALLIS ID", categories[10], sources[4]))
    trans.append(
        make_tran(Decimal("83.44"), "TST*STANLEY SUPPER CLUB Stanley ID", categories[1], sources[2])
    )
    trans.append(
        make_tran(Decimal("4.65"), "LOWES #01906* IDAHO FALLS ID", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("98.57"), "WAL-MART #5494 IDAHO FALLS ID", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("36.37"), "PINEDALE SUPER CENTER PINEDALE WY", categories[10], sources[4])
    )
    trans.append(
        make_tran(Decimal("55.49"), "WALMART FUEL 05494 IDAHO FALLS ID", categories[10], sources[4])
    )
    trans.append(
        make_tran(Decimal("2.17"), "LOWES #01906* IDAHO FALLS ID", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("35.80"), "24 HOUR C STORE ROCK SPRINGS WY", categories[10], sources[4])
    )
    trans.append(
        make_tran(
            Decimal("2.49"), "DIRECT DEBIT AppFolio, Inc.WEB PMTS (Cash)", categories[0], sources[0]
        )
    )
    trans.append(
        make_tran(
            Decimal("1950.00"),
            "DIRECT DEBIT Integrated MouWEB PMTS (Cash)",
            categories[0],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("29.74"), "RAGGED MOUNTAIN SPORTS CARBONDALE CO", categories[12], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("16.14"), "LOWES #01905* GLENWOOD SPRICO", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("134.48"), "WINMAR CABINS 180-05116038 CO", categories[12], sources[2])
    )
    trans.append(
        make_tran(Decimal("53.10"), "CITY-MARKET #0405 GLENWOOD SPRICO", categories[7], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("14.74"), "SCOOTER'S CAR WASH GLENWOOD SPGSCO", categories[11], sources[2]
        )
    )
    trans.append(
        make_tran(
            Decimal("1508.68"),
            "DIRECT DEPOSIT TYLER TECHNOPAYROLL (Cash)",
            categories[3],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("1898.93"),
            "DIRECT DEPOSIT Kimley-Horn PAYROLL (Cash)",
            categories[8],
            sources[1],
        )
    )
    trans.append(
        make_tran(Decimal("3.75"), "MASABI RFTA 970-925-8484 CO", categories[10], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("15.38"), "SQ *TWIN LAKES GENERAL STTWIN LAKES CO", categories[1], sources[2]
        )
    )
    trans.append(make_tran(Decimal("3.75"), "MASABI RFTA", categories[10], sources[3]))
    trans.append(
        make_tran(
            Decimal("44.63"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("44.63"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[0],
        )
    )
    trans.append(
        make_tran(
            Decimal("36.14"),
            "REINVESTMENT FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(
        make_tran(
            Decimal("36.14"),
            "DIVIDEND RECEIVED FIDELITY GOVERNMENT MONEY MARKET (SPAXX) (Cash)",
            categories[2],
            sources[1],
        )
    )
    trans.append(make_tran(Decimal("8.82"), "SAFEWAY #2817 SALIDA CO", categories[7], sources[2]))
    trans.append(
        make_tran(Decimal("3160.51"), "AUTOMATIC PAYMENT - THANK YOU", categories[2], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("39.00"), "TST* INDY PASS PIES NEW TWIN LAKES CO", categories[1], sources[2]
        )
    )
    trans.append(
        make_tran(Decimal("100.00"), "SCANGA MEAT CO SALIDA CO", categories[18], sources[2])
    )
    trans.append(
        make_tran(
            Decimal("3160.51"),
            "DIRECT DEBIT WF Credit CardAUTO PAY (Cash)",
            categories[2],
            sources[0],
        )
    )

    return trans
