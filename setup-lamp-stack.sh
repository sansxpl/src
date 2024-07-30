#!/bin/bash

# Function to remove existing LAMP components
remove_lamp() {
    echo "Removing existing LAMP components..."

    sudo apt-get remove --purge -y apache2 apache2-utils apache2-bin apache2.2-common
    sudo apt-get remove --purge -y mysql-server mysql-client mysql-common
    sudo apt-get remove --purge -y php libapache2-mod-php php-mysql
    sudo apt-get remove --purge -y php-mbstring php-xmlrpc php-soap php-gd php-xml php-intl php-cli php-ldap php-zip php-curl

    sudo apt-get autoremove -y
    sudo apt-get autoclean

    sudo rm -rf /etc/apache2 /etc/mysql /var/www/html
    echo "Existing LAMP components removed."
}

# Function to install LAMP stack
install_lamp() {
    echo "Updating package list..."
    sudo apt-get update -y

    echo "Installing Apache..."
    sudo apt-get install -y apache2

    echo "Installing MySQL..."
    sudo apt-get install -y mariadb-server

    sudo systemctl start apache2
    sudo systemctl start mariadb

    echo "Securing MySQL installation..."
    sudo mysql_secure_installation

    echo "Installing PHP 8.2..."
    sudo add-apt-repository ppa:ondrej/php -y
    sudo apt-get update -y
    sudo apt-get install -y php8.2 libapache2-mod-php8.2 php8.2-mysql

    echo "Installing PHP Extensions..."
    sudo apt-get install -y php8.2-mbstring php8.2-xmlrpc php8.2-soap php8.2-gd php8.2-xml php8.2-intl php8.2-cli php8.2-ldap php8.2-zip php8.2-curl

    echo "Replacing php.ini with pre-configured version..."
    curl -o /tmp/php.ini https://raw.githubusercontent.com/sansxpl/src/main/php.ini
    sudo mv /tmp/php.ini /etc/php/8.2/apache2/php.ini

    echo "Restarting Apache to apply changes..."
    sudo systemctl restart apache2

    echo "Testing LAMP Server..."
    echo "<?php phpinfo(); ?>" > /var/www/html/info.php

    if check_lamp "http://localhost/index.html"; then
        echo "Apache2 successfully installed"
    else
        echo "Apache2 installation failed"
    fi

    if check_lamp "http://localhost/info.php"; then
        echo "PHP successfully installed"
    else
        echo "PHP installation failed"
    fi

    echo "Renaming index.html..."
    sudo mv /var/www/html/index.html /var/www/html/_index.html

    echo "Chmoding var/www"
    chmod 777 /var/www/html

    echo "LAMP stack installed successfully."
}

# Function to check LAMP
check_lamp() {
    local url=$1
    local response=$(curl -s -o /dev/null -w "%{http_code}" $url)

    if [ "$response" == "200" ]; then
        return 0
    else
        return 1
    fi
}

# Main script execution
remove_lamp
install_lamp

echo "LAMP stack setup is complete."
