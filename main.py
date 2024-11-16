from project.tasks import schedule_requests


def main():
    schedule_requests.delay()


if __name__ == '__main__':
    main()

