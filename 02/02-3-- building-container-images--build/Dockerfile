FROM diamol/node:2e

ENV TARGET=blog.sixeyed.com
ENV METHOD=HEAD
ENV INTERVAL=3000

WORKDIR /app
COPY app .

CMD ["node", "/app/app.js"]