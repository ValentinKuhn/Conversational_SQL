FROM postgres:16.0
ENV POSTGRES_DB example_posts
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password
ADD init.sql /docker-entrypoint-initdb.d/
