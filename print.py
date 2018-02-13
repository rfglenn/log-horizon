from db import Session
from model import Interval

def main():
	session = Session()

	for interval in session.query(Interval).all():
		print(interval)

if __name__ == '__main__':
	main()
