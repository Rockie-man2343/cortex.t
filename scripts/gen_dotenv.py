def get_user_input(prompt, default=None):
    if default:
        value = input(f"{prompt} (default: {default}): ").strip()
        return value if value else default
    return input(f"{prompt}: ").strip()


def generate_dotenv():
    print("Please enter values for your .env file")
    print("Press Enter to accept default values where available")
    print("-" * 50)

    # Get user inputs
    env_vars = {
        "WALLET_NAME": get_user_input("--wallet.name", "default"),
        "WALLET_HOTKEY": get_user_input("--wallet.hotkey", "default"),
        "NETUID": get_user_input("--netuid", "18"),
        "SUBTENSOR_NETWORK": get_user_input("--subtensor.network", "finney"),
        "AXON_PORT": get_user_input("--axon.port", "8000"),
        "OPENAI_API_KEY": get_user_input("--openai.api-key", ""),
    }

    # Write to .env file
    with open(".env", "w") as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")

    print("\n.env file has been generated successfully!")


if __name__ == "__main__":
    try:
        generate_dotenv()
    except KeyboardInterrupt:
        print("\nExiting without saving...")
