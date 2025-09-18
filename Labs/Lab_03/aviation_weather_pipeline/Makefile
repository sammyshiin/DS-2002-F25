.PHONY: all fetch analyze clean
all: analyze

fetch:
	@echo "Grabbing METAR data..."
	@./fetch_metars.sh
	@echo "Done fetching. Check out raw_metars/"

analyze: fetch
	@echo "Crunching the METAR files into a CSV..."
	@./analyze_data.sh
	@echo "All set. Your weather_report.csv is ready."
	@echo "Pipeline completed successfully!"

clean:
	@echo "Starting cleanup: removing generated data..."
	@rm -rf raw_metars weather_report.csv
	@echo "Cleanup complete"
