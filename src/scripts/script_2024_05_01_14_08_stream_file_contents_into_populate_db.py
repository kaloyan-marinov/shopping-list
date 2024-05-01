"""
(1)
create an input file, which follows the following structure:
```
<category_name_1>
<item_name_1>
<category_name_2>
<item_name_2>
...
```

a sample input file,
which corresponds to the rows
written into the database by `src/scripts/script_2024_05_01_10_03_populate_db.py`,
looks like so:
```
vegetable
broccoli
household
hand soap
hygiene
toothpaste
```

(2)
execute this script by issuing
```
(venv) $ PYTHONPATH=. \
    python \
    src/scripts/script_2024_05_01_14_08_stream_file_contents_into_populate_db.py \
    --input-file=<specify-absolute-path-to-input-file>
```
"""

import argparse
import logging

from src import Category, Item, app, db

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

handler_1 = logging.StreamHandler()
handler_1.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"),
)

logger.addHandler(handler_1)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog=__name__,
    )
    arg_parser.add_argument(
        "--input-file",
        type=str,
        required=True,
    )

    args = arg_parser.parse_args()
    logger.debug("args.input_file = %s", args.input_file)

    c_name_2_category_id = {}

    with app.app_context(), open(args.input_file, mode="r") as input_file:
        category_name = next(input_file)
        item_name = next(input_file)

        while True:
            c_name = category_name.rstrip()
            i_name = item_name.rstrip()
            logger.info(c_name)
            logger.info(i_name)
            logger.info("")

            if c_name not in c_name_2_category_id:
                c = Category(name=c_name)
                db.session.add(c)
                db.session.commit()
                c_name_2_category_id[c_name] = c.id
            category_id = c_name_2_category_id[c_name]
            i = Item(name=item_name, category_id=category_id)
            db.session.add(i)
            db.session.commit()

            try:
                category_name = next(input_file)
                item_name = next(input_file)
            except StopIteration as e:
                logger.info(f"{e = }")
                logger.info(e)
                break
