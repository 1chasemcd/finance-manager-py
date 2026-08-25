import csv
from datetime import datetime
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.person import Person
from finance_manager.models.transaction import Transaction
from finance_manager.models.transaction_category import TransactionCategory
from finance_manager.models.transaction_source import TransactionSource

chase = Person(first_name="Chase", last_name="McDonald")
hannah = Person(first_name="Hannah", last_name="McDonald")


async def create_data(session: AsyncSession, file_path: str) -> None:

    session.add_all([chase, hannah])

    categories: dict[str, TransactionCategory] = {}
    sources: dict[str, TransactionSource] = {}

    trans: list[Transaction] = []

    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            tran = Transaction()
            tran.timestamp = datetime.strptime(row[0], "%m/%d/%Y")
            tran.amount = Decimal(row[1])
            tran.summary = row[2]
            tran.transaction_category = get_or_add_category(session, categories, row[3])
            tran.transaction_source = get_or_add_source(session, sources, row[4])

            trans.append(tran)

    session.add_all(trans)
    await session.commit()


def get_or_add_category(
    session: AsyncSession, categories: dict[str, TransactionCategory], name: str
) -> TransactionCategory:
    if name in categories:
        return categories[name]
    cat = TransactionCategory(name=name)
    categories[name] = cat
    session.add(cat)
    return cat


def get_or_add_source(
    session: AsyncSession, sources: dict[str, TransactionSource], name: str
) -> TransactionSource:
    if name in sources:
        return sources[name]
    owner = chase if "chase" in name.lower() else hannah
    src = TransactionSource(name=name, owner=owner)
    sources[name] = src
    session.add(src)
    return src
