from src.parsing.log_parser import parse_syslog

RAW_LOG = "data/raw/messages.log"
OUT_CSV = "data/processed/logs.csv"

def main():
    df = parse_syslog(RAW_LOG)
    df.to_csv(OUT_CSV, index=False)
    print(f"Parsed {len(df)} log entries")

if __name__ == "__main__":
    main()
