{ pkgs, lib, config, inputs, ... }:

{
  packages = [
    pkgs.uv
  ];
  languages.python = {
    enable = true;
    version = "3.13";
    venv = {
      enable = true;
      requirements = "cookiecutter";
    };
  };
}
