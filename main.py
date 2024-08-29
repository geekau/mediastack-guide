def define_env(env):
    # Project-related variables
    env.variables['COMPOSE_PROJECT_NAME']       = 'mediastack'
    env.variables['DOCKER_SUBNET']              = '172.28.10.0/24'
    env.variables['DOCKER_GATEWAY']             = '172.28.10.1'
    env.variables['LOCAL_SUBNET']               = '192.168.1.0/24'
    env.variables['LOCAL_DOCKER_IP']            = '192.168.1.10'
    env.variables['TP_THEME']                   = 'nord'
    env.variables['PLEX_CLAIM']                 = ''
    
    # SMTP Relay
    env.variables['SMTP_USERNAME']              = 'user@localhost'
    env.variables['SMTP_PASSWORD']              = 'password'
    env.variables['SMTP_PORT']                  = '25'

    # Folder paths
    env.variables['FOLDER_FOR_DATA']            = '/mediastackdata'
    env.variables['FOLDER_FOR_MEDIA']           = '/mediastack'
    
    # PUID and PGID
    env.variables['PUID']                       = '1000'
    env.variables['PGID']                       = '1000'
    env.variables['UMASK']                      = '0022'

    # VPN Provider Settings
    env.variables['VPN_TYPE']                   = 'openvpn'
    env.variables['VPN_SERVICE_PROVIDER']       = 'VPN provider name'
    env.variables['VPN_USERNAME']               = '<username from VPN provider>'
    env.variables['VPN_PASSWORD']               = '<password from VPN provider>'

    env.variables['SERVER_COUNTRIES']           = ''
    env.variables['SERVER_REGIONS']             = ''
    env.variables['SERVER_CITIES']              = ''
    env.variables['SERVER_HOSTNAMES']           = ''
    env.variables['SERVER_CATEGORIES']          = ''
    env.variables['OPENVPN_CUSTOM_CONFIG']      = ''
    env.variables['VPN_ENDPOINT_IP']            = ''
    env.variables['VPN_ENDPOINT_PORT']          = ''
    env.variables['WIREGUARD_PUBLIC_KEY']       = ''
    env.variables['WIREGUARD_PRIVATE_KEY']      = ''
    env.variables['WIREGUARD_PRESHARED_KEY']    = ''
    env.variables['WIREGUARD_ADDRESSES']        = ''

    # Timezone
    env.variables['TIMEZONE']                   = 'Europe/Zurich'
    
    # Application ports
    env.variables['QBIT_PORT']                  = '6881'
    env.variables['FLARESOLVERR_PORT']          = '8191'
    env.variables['WEBUI_PORT_TDARR']           = '8265'
    env.variables['TDARR_SERVER_PORT']          = '8266'
    env.variables['WEBUI_PORT_BAZARR']          = '6767'
    env.variables['WEBUI_PORT_DDNS_UPDATER']    = '8000'
    env.variables['WEBUI_PORT_HEIMDALL']        = '2080'
    env.variables['WEBUI_PORT_HOMEPAGE']        = '3000'
    env.variables['WEBUI_PORT_JELLYFIN']        = '8096'
    env.variables['WEBUI_PORT_JELLYSEERR']      = '5055'
    env.variables['WEBUI_PORT_LIDARR']          = '8686'
    env.variables['WEBUI_PORT_MYLAR3']          = '8090'
    env.variables['WEBUI_PORT_PLEX']            = '32400'
    env.variables['WEBUI_PORT_PORTAINER']       = '9000'
    env.variables['WEBUI_PORT_PROWLARR']        = '9696'
    env.variables['WEBUI_PORT_QBITTORRENT']     = '8200'
    env.variables['WEBUI_PORT_RADARR']          = '7878'
    env.variables['WEBUI_PORT_READARR']         = '8787'
    env.variables['WEBUI_PORT_SONARR']          = '8989'
    env.variables['WEBUI_PORT_SABNZBD']         = '8100'
    env.variables['WEBUI_PORT_WHISPARR']        = '6969'

    # Reverse Proxy ports
    env.variables['REVERSE_PROXY_PORT_HTTP']    = '80'
    env.variables['REVERSE_PROXY_PORT_HTTPS']   = '443'
    
    # SWAG settings
    env.variables['URL']                        = 'your-domain-name-goes-here.com'
    env.variables['SUBDOMAINS']                 = 'wildcard'
    env.variables['VALIDATION']                 = 'dns'
    env.variables['DNSPLUGIN']                  = 'cloudflare'
    env.variables['CERTPROVIDER']               = ''
    env.variables['PROPAGATION']                = ''
    env.variables['DUCKDNSTOKEN']               = ''
    env.variables['EMAIL']                      = ''
    env.variables['ONLY_SUBDOMAINS']            = 'false'
    env.variables['EXTRA_DOMAINS']              = ''
    env.variables['STAGING']                    = 'false'

    # Cloudflare Tunnel
    env.variables['CF_ZONE_ID']                 = ''
    env.variables['CF_ACCOUNT_ID']              = ''
    env.variables['CF_API_TOKEN']               = ''
    env.variables['CF_TUNNEL_NAME']             = ''
    env.variables['CF_TUNNEL_TOKEN']            = ''
