import uvicorn

if __name__ == "__main__":
	print("Entered twilight zone")
	uvicorn.run("app:app", host="127.0.0.1", port=3333, reload=True)

