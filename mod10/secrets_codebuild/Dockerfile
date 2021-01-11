FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
# Install apache and remove the list of packages downloaded from apt-get update
RUN apt-get update && \
    apt-get install -y apache2 && \
    rm -r /var/lib/apt/lists/*
    
# echo HTML string into the apache web root directory
RUN echo "<H1>Hello Secrets World!</H1>" > /var/www/html/index.html

EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]