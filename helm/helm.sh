# add a chart repo
helm repo add bitnami https://chartsd.bitnami.com/bitnami
helm repo list
# search repo
helm search repo kash # could search on hub w/ helm search hub wordpress
# install a chart/package and create a release/instance
helm install releasedapp bitnami/wordpress
helm status releasedapp
# inspect chart for prm values
helm show values bitnami/wordpress
# change said values
echo '{mariadb.auth.database: user0db, mariadb.auth.username: user0}' > values.yaml
helm install -f values.yaml bitnami/wordpress --generate-name  # could use --set
# upgrade/rollback
helm upgrade -f panda.yaml happy-panda bitnami/wordpress
helm rollback happy-panda 1
# uninstall
helm uninstall happy-panda
helm list --all


