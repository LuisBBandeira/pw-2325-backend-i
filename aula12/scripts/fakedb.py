#Creates a fake json file that should represent an actual DB
import json
from faker import Faker

fake = Faker()

if __name__ == "__main__":
    total_rows=20

    result = [
        dict(
            id=fake.isbn10(),
            name=" ".join(fake.words(nb=2)),
            price=fake.pricetag(),
            enabled=True,
            sku=100
        )
        for _ in range(total_rows)
    ]

    with open("db.json","w") as file:
        file.writelines(json.dumps(result, indent=2))