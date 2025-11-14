{ pkgs, lib, config, inputs, ... }:

{
  packages = [
  ];

  languages.python = {
    enable = true;
    version = "3.13";
    venv = {
      enable = true;
      requirements = "pipenv";
    };
    uv = {
      enable = true;
    };
  };
}
