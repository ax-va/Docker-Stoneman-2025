# build stage
FROM rust:1.83-slim-bookworm AS builder

WORKDIR /project

COPY project .
RUN cargo build --release

# runtime stage
FROM debian:bookworm-slim

WORKDIR /app

COPY --from=builder /project/target/release/rust-service /app

ENTRYPOINT ["./rust-service"]