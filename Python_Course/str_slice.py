def main():
    today = "Today is Monday!"
    
    # Single character indexing
    print("Single character indexing:")
    print(f"Character at index 9: {today[9]}")
    
    # String slicing examples
    print("\nString slicing examples:")
    print(f"Word 'Monday': {today[9:15]}")
    print(f"Word 'day': {today[12:15]}")
    print(f"Word 'is': {today[6:8]}")
    print(f"Word 'Today': {today[:5]}")
    print(f"Word 'is Monday': {today[6:15]}")
    print(f"Word 'To': {today[:2]}")
    print(f"Word 'Mon': {today[9:12]}")

if __name__ == "__main__":
    main()
