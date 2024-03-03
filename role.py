import discord
import os
from dotenv import load_dotenv
load_dotenv()
chemrole = os.getenv("APCHEMROLE")

class Role(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="AP Chemistry",custom_id="APCHEM", style=discord.ButtonStyle.blurple, emoji="🧪")
    async def apchem(self,interaction:discord.Interaction,button):
        role = discord.utils.get(interaction.guild.roles, name="ap chem")
        if role in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Chemistry!", ephemeral=True)
            return
        await interaction.user.remove_roles(role)
        await interaction.response.send_message("Removed AP Chemistry!", ephemeral=True)
        
    @discord.ui.button(label="AP Biology",custom_id="APBIO", style=discord.ButtonStyle.green, emoji="🧬")
    async def apbio(self,interaction:discord.Interaction,button):
        role = discord.utils.get(interaction.guild.roles, name="ap bio")
        if role in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Biology!", ephemeral=True)
            return
        await interaction.user.remove_roles(role)
        await interaction.response.send_message("Removed AP Biology!", ephemeral=True)
        
    @discord.ui.button(label="AP Physics Mechanics",custom_id="APPHYSM", style=discord.ButtonStyle.red, emoji="⚙️")
    async def apphysm(self,interaction:discord.Interaction,button):
        role = discord.utils.get(interaction.guild.roles, name="physics mech")
        if role in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Physics Mechanics!", ephemeral=True)
            return
        await interaction.user.remove_roles(role)
        await interaction.response.send_message("Removed AP Physics Mechanics!", ephemeral=True)
        
    @discord.ui.button(label="AP Physics Electricity And Magnetism",custom_id="APPHYSENM", style=discord.ButtonStyle.red, emoji="⚡")
    async def apphysenm(self,interaction:discord.Interaction,button):
        role = discord.utils.get(interaction.guild.roles, name="physics enm")
        if role in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Physics Electricity And Magnetism!", ephemeral=True)
            return
        await interaction.user.remove_roles(role)
        await interaction.response.send_message("Removed AP Physics Electricity And Magnetism!", ephemeral=True)
    
    @discord.ui.button(label="AP Computer Science Principles", custom_id="APCSP", style=discord.ButtonStyle.red, emoji="💻")
    async def apcsp(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="ap csp")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP Computer Science Principles!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Computer Science Principles!", ephemeral=True)

    @discord.ui.button(label="AP Computer Science A", custom_id="APCSA", style=discord.ButtonStyle.red, emoji="🖥️")
    async def apcsa(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="ap csa")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP Computer Science A!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Computer Science A!", ephemeral=True)

    @discord.ui.button(label="AP Calculus AB", custom_id="APCALCAB", style=discord.ButtonStyle.red, emoji="📈")
    async def apcalcab(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="calc ab")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP Calculus AB!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Calculus AB!", ephemeral=True)

    @discord.ui.button(label="AP Calculus BC", custom_id="APCALCBC", style=discord.ButtonStyle.red, emoji="📊")
    async def apcalcbc(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="calc bc")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP Calculus BC!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP Calculus BC!", ephemeral=True)
            
    @discord.ui.button(label="Honors Humanities", custom_id="HUMANITIES", style=discord.ButtonStyle.gray, emoji="📚")
    async def humanities(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="humanities")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed Honors Humanities!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added Honors Humanities!", ephemeral=True)

    @discord.ui.button(label="AP World History", custom_id="APWORLD", style=discord.ButtonStyle.gray, emoji="🌍")
    async def apworld(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="ap world")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP World History!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP World History!", ephemeral=True)

    @discord.ui.button(label="AP US History", custom_id="APUSH", style=discord.ButtonStyle.gray, emoji="🇺🇸")
    async def apush(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="apush")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP US History!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP US History!", ephemeral=True)

    @discord.ui.button(label="AP English Language", custom_id="APEL", style=discord.ButtonStyle.gray, emoji="📝")
    async def apel(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="apel")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP English Language!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP English Language!", ephemeral=True)

    @discord.ui.button(label="AP English Literature", custom_id="APLIT", style=discord.ButtonStyle.gray, emoji="📖")
    async def aplit(self, interaction: discord.Interaction, button):
        role = discord.utils.get(interaction.guild.roles, name="ap lit")
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Removed AP English Literature!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Added AP English Literature!", ephemeral=True)

    @discord.ui.button(label="Honors Principles Of Engineering", custom_id="HPOE", style=discord.ButtonStyle.red, emoji="📐")
    async def hpoe(self, interaction: discord.Interaction, button):
            role = discord.utils.get(interaction.guild.roles, name="hpoe")
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message("Removed Honors Principles Of Engineering!", ephemeral=True)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message("Added Honors Principles Of Engineering!", ephemeral=True)
