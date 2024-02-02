import streamlit as st
import os

from key import key_to_cn, cn_to_key

config_file_path = '/home/ecs-assist-user/.steam/SteamApps/common/PalServer/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini'

def get_remote_ip() -> str:
    """Get remote ip."""

    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None

    return session_info.request.remote_ip

def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.split('OptionSettings=(', 1)[1].rsplit(')', 1)[0]
        items = content.split(',')
        for item in items:
            if '=' in item:
                key, value = item.split('=', 1)
                config[key.strip()] = value.strip()
    return config

def write_config(file_path, config):
    with open(file_path, 'w') as file:
        config_str = ', '.join([f'{key}={value}' for key, value in config.items()])
        file.write(f'[/Script/Pal.PalGameWorldSettings]\nOptionSettings=({config_str})')

def modify_config_ui(config):
    new_config = {}
    for key, value in config.items():
        cn_key = key_to_cn.get(key, key)
        if value.replace('.', '', 1).isdigit():
            new_value = st.number_input(cn_key, value=float(value))
        elif value.lower() in ['true', 'false']:
            new_value = st.selectbox(cn_key, [True, False], index=[True, False].index(eval(value.capitalize())))
        else:
            new_value = st.text_input(cn_key, value=value)
        new_config[cn_to_key.get(cn_key, cn_key)] = str(new_value)
    return new_config

def main():
    print(f"The remote ip is {get_remote_ip()}")
    st.title('editor')

    config = read_config(config_file_path)
    new_config = modify_config_ui(config)

    st.warning('提交修改会重启服务，请确保当前可中断游戏。')
    if st.button('提交修改'):
        os.system("systemctl stop pal-server")
        write_config(config_file_path, new_config)
        os.system("systemctl start pal-server")

        st.success('配置已更新！')

if __name__ == '__main__':
    main()
