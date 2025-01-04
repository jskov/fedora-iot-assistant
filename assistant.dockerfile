# For Podman Quad
# To be placed in /etc/containers/systemd/users/3000/assistant.container
#
# Debug rendering with:
#  /usr/lib/systemd/user-generators/podman-user-generator --dryrun
#
# sudo systemctl daemon-reload
# systemctl list-unit-files
# systemctl start assistant
#
# sudo systemctl --user -M assistant@ status assistant

[Service]
# Allows long image download time
TimeoutStartSec=900

# Implied by systemd users/3000
#User=assistant
#Group=assistant

# Wait for network startup - podman-user-wait-network-online.service should be added in Podman 5.3.0
# via https://github.com/containers/podman/pull/24305
# Without this container is started before networking which Podman fails on
# see https://www.reddit.com/r/podman/comments/1clo1ct/container_starting_before_network_is_up/
ExecStartPre=nm-online -s

[Container]
# This is 2024.10.4
Image = ghcr.io/home-assistant/home-assistant@sha256:408a5a63e3e9a89ceb6ecd98345e54c86073314b4d94e217cd54f7208307406d

AddDevice=/dev/ttyUSB0
ContainerName=assistant
Environment=TZ=Europe/Copenhagen
PublishPort=8123:8123
Volume=/opt/data/services/assistant:/config:Z,rw

GlobalArgs=--log-level=warn
PodmanArgs=--group-add=keep-groups --cap-add=CAP_NET_RAW,CAP_NET_BIND_SERVICE --cidfile=/var/run/user/3000/assistant.cid

[Unit]
# Cannot depend on root service. Instead relies on assistant-prep comes before podman-user-wait-network-online.service
#Requires=assistant-prep.service
#After=assistant-prep.service

[Install]
WantedBy=default.target
