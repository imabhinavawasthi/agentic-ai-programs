def call_gemini(**geminiInput):
    try:
        print("Model:", geminiInput["model"])
        print("Prompt:", geminiInput["prompt"])
        print("Cost:", geminiInput["token"]+100)
    except KeyError as e:
        print("Please provide all the input:", e)
    except Exception as e:
        print("Error Occurred:", e)
    finally:
        print("Call Done")


call_gemini(
    model="3.8-pro",
    prompt="What is Python?",
    token=100
)