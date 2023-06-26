import hydra
from typing import Any
from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig, OmegaConf

@dataclass
class MySQLConfig:
    host: str = "localhost"
    port: int = 3306
    mysql: Any = "hello"


cs = ConfigStore.instance()
# Registering the Config class with the name 'config'.
cs.store(name="codeconfig", node=MySQLConfig, group="db")



@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

    assert cfg.node.loompa == 10          # attribute style access
    assert cfg["node"]["loompa"] == 10    # dictionary style access

    assert cfg.node.zippity == 10         # Value interpolation
    assert isinstance(cfg.node.zippity, int)  # Value interpolation type
    assert cfg.node.do == "oompa 10"      # string interpolation

    cfg.node.waldo                        # raises an exception

if __name__ == "__main__":
    my_app()
