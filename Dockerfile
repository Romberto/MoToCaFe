FROM ubuntu:latest
LABEL authors="romberto"

ENTRYPOINT ["top", "-b"]