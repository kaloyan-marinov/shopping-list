podman container rm -f \
    container-shopping-list-postgres \
    container-shopping-list

podman volume prune

podman network prune

podman image prune
