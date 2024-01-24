FROM kkoldduck2/customui:v.1.1

WORKDIR /custom_ui

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt

COPY . .

ENV FLASK_APP=pybo
ENV APP_CONFIG_FILE=/custom_ui/config/development.py

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "flask", "run", "--host=0.0.0.0"]