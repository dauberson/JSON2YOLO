import os
from pathlib import Path
from typing import List

from loguru import logger


# 1, 2 -> 0
# 0, 3, 4 -> None

def replace_annotations(replaceable_ids: List[str], new_class_id: str, annotations_path: Path):
    for filename in os.listdir(annotations_path):
        if not filename.endswith(".txt"):
            continue
        with open(annotations_path / filename, mode="r") as file:
            logger.info(f"Reading annotations from {filename}")
            new_annotation = ""
            for line in file.readlines():
                if line[0] in replaceable_ids:
                    logger.info(f"Replacing {line[0]} to {new_class_id}")
                    new_annotation += f"{new_class_id}{line[1:]}"
                else:
                    new_annotation += line
        with open(annotations_path / filename, mode="w") as file:
            file.truncate(0)
            file.writelines(new_annotation)


def remove_annotations(class_id_to_delete: List[str], annotations_path: Path):
    for filename in os.listdir(annotations_path):
        if not filename.endswith(".txt"):
            continue
        with open(annotations_path / filename, mode="r") as file:
            logger.info(f"Reading annotations from {filename}")
            new_annotation = ""
            for line in file.readlines():
                if line[0] not in class_id_to_delete:
                    new_annotation += line
        with open(annotations_path / filename, mode="w") as file:
            file.truncate(0)
            file.writelines(new_annotation)


if __name__ == '__main__':
    remove_annotations(
        class_id_to_delete=["3", "4", "0"],
        annotations_path=Path("/Users/daubersonmol/Documents/yolo-copel-data/labels")
    )
    replace_annotations(
        replaceable_ids=["1", "2"],
        new_class_id="0",
        annotations_path=Path("/Users/daubersonmol/Documents/yolo-copel-data/labels")
    )
