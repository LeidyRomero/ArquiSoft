FROM ruby:2.3.1
MAINTAINER Steven Tarazona

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update -qq
RUN mkdir /clientes
WORKDIR /clientes
COPY Gemfile /clientes/Gemfile
COPY Gemfile.lock \clientes/Gemfile.lock
ENV BUNDLER_VERSION 2.0.1
RUN gem install bundler && bundle install --jobs 20 --retry 5
COPY . /clientes

EXPOSE 8080

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0", "-p", "8080"]
