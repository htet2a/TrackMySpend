from config.config_loader import load_yaml
from utils.logger import get_logger


def main():
    logger = get_logger()

    config = load_yaml("config.yaml")
    categories = load_yaml("categories.yaml")
    stores = load_yaml("stores.yaml")

    app_name = config["application"]["name"]
    version = config["application"]["version"]

    category_count = len(categories["categories"])
    store_count = len(stores.get("stores", {}))

    logger.info("Application started")

    print(f"{app_name} {version}")
    print(f"Categories loaded: {category_count}")
    print(f"Stores loaded: {store_count}")
    print("TrackMySpend started successfully")


if __name__ == "__main__":
    main()