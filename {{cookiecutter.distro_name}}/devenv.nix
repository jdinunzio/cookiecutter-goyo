{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    version = "{{cookiecutter.python_version}}";
    venv = {
      enable = true;
    };
    uv = {
      enable = true;
    };
  };
}
