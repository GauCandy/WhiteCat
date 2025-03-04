import disnake
from disnake.ext import commands
import json
import os
import lang_custom

Guild = './Data/guilds/{guild_id}.json'



async def execute(message: disnake.Message, bot: commands.Bot, lang: str):
    lang_get = lang_custom.lang(lang).group("remove_reply").get_text  
    guild_id = str(message.guild.id)
    guild_file_path = Guild.format(guild_id=guild_id)

    if not os.path.exists(guild_file_path):
        await message.channel.send(lang_get("guild_data_not_found"))
        return

    try:
        with open(guild_file_path, 'r', encoding='utf-8') as f:
            guild_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Lỗi khi đọc file JSON của server: {e}")
        await message.channel.send(lang_get("error_reading_file"))
        return

    content = message.content.strip().split()
    if len(content) < 2:
        await message.channel.send(lang_get("provide_command_name"))
        return

    command_name = content[1]
    user_id = str(message.author.id)

    command_found = False
    can_delete = False
    for command in guild_data["autoreply"]:
        if command["name"] == command_name:
            command_found = True
            allow_edit = guild_data.get("allow_member_edit", False)
            allow_edit_ids = guild_data.get("allow_edit_id", [])
            
            if user_id == command.get("Owner") or user_id in allow_edit_ids or (allow_edit and user_id == command.get("Owner")):
                can_delete = True
            break

    if not command_found:
        await message.channel.send(lang_get("command_not_found").format(reply=command_name))
        return
    
    if not can_delete:
        await message.channel.send(lang_get("no_permission"))
        return

    view = disnake.ui.View()
    no_button = ConfirmButton(lang_get("cancel"), disnake.ButtonStyle.danger, command_name, guild_data, guild_file_path, False, message.author.id, lang)
    yes_button = ConfirmButton(lang_get("confirm"), disnake.ButtonStyle.success, command_name, guild_data, guild_file_path, True, message.author.id, lang)
    view.add_item(no_button)
    view.add_item(yes_button)
    await message.channel.send(lang_get("confirm_delete").format(reply=command_name), view=view)

class ConfirmButton(disnake.ui.Button):
    def __init__(self, label, style, command_name, guild_data, guild_file_path, confirm, user_id, lang):
        super().__init__(label=label, style=style)
        self.command_name = command_name
        self.guild_data = guild_data
        self.guild_file_path = guild_file_path
        self.confirm = confirm
        self.user_id = user_id
        self.lang = lang

    async def callback(self, interaction: disnake.MessageInteraction):
        lang_get = lang_custom.lang(self.lang).group("remove_reply").get_text  # Đẩy self.lang vào đây cho mỗi lần gọi

        if interaction.user.id != self.user_id:
            await interaction.response.send_message(lang_get("no_permission"), ephemeral=True)
            return

        if self.confirm:
            try:
                with open(self.guild_file_path, 'r', encoding='utf-8') as f:
                    guild_data = json.load(f)
                
                command_exists = False
                for command in guild_data["autoreply"]:
                    if command["name"] == self.command_name:
                        command_exists = True
                        guild_data["autoreply"].remove(command)
                        break
                
                if not command_exists:
                    await interaction.message.edit(content=lang_get("command_not_found").format(reply=self.command_name), view=None)
                    return
                
                with open(self.guild_file_path, 'w', encoding='utf-8') as f:
                    json.dump(guild_data, f, ensure_ascii=False, indent=4)
                
                await interaction.message.edit(content=lang_get("command_deleted").format(reply=self.command_name), view=None)
            except Exception as e:
                print(f"Lỗi khi ghi file JSON của server: {e}")
                await interaction.message.edit(content=lang_get("error_occurred"), view=None)
        else:
            await interaction.message.edit(content=lang_get("delete_cancelled"), view=None)
