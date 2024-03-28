# my nix learning journey
- follow the 'zero to nix' from determinate systems
### runing a program
```bash
echo "Hello Nix" | nix run "nixpkgs#cowsay"
```

### nix dev env
enable a nix dev env
```bash
nix develop "github:DeterminateSystems/zero-to-nix#example"
```

just run a simple command from a nix env and exit
```bash
nix develop "github:DeterminateSystems/zero-to-nix#example" --command git help
```

### builds

```bash
nix build "nixpkgs#python3Packages.pip"
./result/bin/pip --help
```

> find * -type l >> .gitignore

```bash
mkdir nix-rust-pkg && cd nix-rust-pkg
nix flake init --template "github:DeterminateSystems/zero-to-nix#rust-pkg"
```

### search 

```bash
nix search nixpkgs cargo #--json
```

```bash
nix flake show github:nix-community/nixpkgs-wayland
```

### flake

use flakehub to generate a flake (dev envs not package for now)
```bash
git clone --depth=1 --branch=master https://github.com/DeterminateSystems/fh-init-example-project
cd fh-init-example-project
nix run "https://flakehub.com/f/DeterminateSystems/fh/*.tar.gz" -- init
# respond to the prompts
nix flake show
```