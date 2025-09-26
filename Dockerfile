# Dockerfile with intentional errors for demo purposes

# Using a non-existent base image
FROM nonexistent-base-image:latest

# Missing RUN keyword (this line will cause a syntax error)
apt-get update && apt-get install -y python3 python3-pip

# Wrong instruction name
INVALID_INSTRUCTION /app

# Typo in COPY instruction - destination path is wrong
COPY . /ap
WORKDIR /ap

# Multiple EXPOSE instructions with invalid syntax
EXPOSE 80 443
EXPOSE invalid-port
EXPOSE 

# Invalid CMD format
CMD python3 app.py --port=8080 --host=0.0.0.0

# Another invalid instruction
WRONG_COMMAND echo "This will fail"

# Missing quotes in ENV
ENV MY_VAR=this has spaces without quotes

# Invalid HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Wrong USER format
USER root:admin:extra