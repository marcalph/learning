# my nix learning journey
- follow the 'zero to nix' from determinate systems
### runing a program
``` shell
echo "Hello Nix" | nix run "nixpkgs#cowsay"
```

### nix dev env
enable a nix dev env
``` shell
nix develop "github:DeterminateSystems/zero-to-nix#example"
```

just run a simple command from a nix env and exit
``` shell
nix develop "github:DeterminateSystems/zero-to-nix#example" --command git help
```

### builds

``` shell
nix build "nixpkgs#python3Packages.pip"
./result/bin/pip --help
```

> find * -type l >> .gitignore


