# OCPI Playground

⚠️ This project is still a WIP under active development ⚠️

This project aims to be a demonstration of OCPI servers topologies. It can be
used as an integration example of the
[`py-ocpi`](https://github.com/TECHS-Technological-Solutions/ocpi/tree/master)
server implementation, or to build OCPI-related services.

## Dependencies

This project requires the following dependencies to be installed in your
operating system:

- Docker
- Docker compose
- GNU Make

## Getting started

Once you've cloned the project, it can be bootstrapped using the eponym GNU Make
target:

```
$ make bootstrap
```

Now that application docker image has been built, you can start the whole stack
using:

```
$ make run
```

Depending on the OCPI server you want to explore, you may take a look and test
its HTTP API at:

- CPO: [http://localhost:8010](http://localhost:8010)
- eMSP: [http://localhost:8011](http://localhost:8011)

To run tests and linters, there are commands for that! You can list them using:

```
$ make help
```

## License

This work is released under the MIT License (see [LICENSE](./LICENSE)).
