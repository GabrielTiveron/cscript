FROM python:3.7

RUN pip install jupyter \
    lark-parser

VOLUME /cscript

WORKDIR "/cscript"

EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
