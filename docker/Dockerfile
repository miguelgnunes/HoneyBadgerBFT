#RUN git clone https://github.com/amiller/HoneyBadgerBFT.git
#COPY ../ /
FROM honeybadger-base
RUN git clone https://github.com/miguelgnunes/HoneyBadgerBFT.git && cd HoneyBadgerBFT && git checkout another-dev && git pull origin another-dev && git log | head

COPY ./start.sh /
CMD sh /start.sh
