# Project Structure

src
    This folder contains *all* the source code of this distribution.

src/{{cookiecutter.package_name}}
    Root package of this distribution. All source code is a module or subpackage of {{cookiecutter.package_name}}.

    {%if cookiecutter.use_clean_architecture == "y" %}
    This package uses Clean Architecture, a layered model on which the lower layers are used to build the
    upper ones. Lower layers **must not** reference upper layers. This is the basic structure:

        domains:
            models
            constants
            exceptions
        application:
            interfaces
            usecases
            constants
            exceptions
        infrastructure:
            adapters
            utilities
        presentation:
            scripts

    **Domain:** Define the basic models and entities of the project. The data structures in the domain space
    are difined here, together with its associated constants, enums and exceptions.

    **Application:** Define the business logic of the application. Business logic is implemented in use cases.
    use cases use models, entities, constants and exceptions defined in the domain model. It also might need
    other support classes to interact with the external world. Those interactions are reflected in the
    application's interface, which makes it abstract and pluggable.

    **Infastructure:** Here the _adapters_ are defined, the concrete implementation of the application's
    interfaces.

    **Presentation:** Contains all the executables of this package. This includes python and shell scripts,
    cron jobs, AWS lambda definitions, etc.
    {% endif %}
tests
    Test folder. All the test code lives here. Notice that for test work properly, this distribution must have been
    installed. It's recommended to install this distribution in development mode (see README).

tests/unit
    Unit test package. All tests in this package *must* be unitary: they must test only code in this distribution. In
    particular, unit tests *must not* depend on external components, like DBMS, web servers, or any external
    application. Unit tests must be fast, and the test suite must run under a few seconds. This package should
    follow the same module structure than {{cookiecutter.package_name}}.

tests/integration
    Integration test package. The purpose of integration tests is to test the interoperation of the current distribution
    with external components, like DBMS, web servers, or any external application. Every external dependency *must* be
    run locally.

docs
    Documentation folder.

docs/adr
    Folder for Architectural Decision Records. Every ADR must reside in its own file.

docs/build
    This folder contains the documents built from the rst or markdown sources.

scripts
    This folder contain helpful scripts required to build the project, its docker image, and deployment. *NO application
    code* should reside in this folder.
