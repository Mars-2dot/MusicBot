/*
 * Copyright 2018 John Grosh <john.a.grosh@gmail.com>.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.mars.MusicBot.commands.admin;

import com.jagrosh.jdautilities.command.CommandEvent;
import com.jagrosh.jdautilities.commons.utils.FinderUtil;
import com.mars.MusicBot.Bot;
import com.mars.MusicBot.commands.AdminCommand;
import com.mars.MusicBot.settings.Settings;
import com.mars.MusicBot.utils.FormatUtil;
import net.dv8tion.jda.api.entities.TextChannel;

import java.util.List;

public class SettcCmd extends AdminCommand 
{
    public SettcCmd(Bot bot)
    {
        this.name = "settc";
        this.help = "sets the text channel for music commands";
        this.arguments = "<channel|NONE>";
        this.aliases = bot.getConfig().getAliases(this.name);
    }
    
    @Override
    protected void execute(CommandEvent event) 
    {
        if(event.getArgs().isEmpty())
        {
            event.reply(event.getClient().getError()+" Please include a text channel or NONE");
            return;
        }
        Settings s = event.getClient().getSettingsFor(event.getGuild());
        if(event.getArgs().equalsIgnoreCase("none"))
        {
            s.setTextChannel(null);
            event.reply(event.getClient().getSuccess()+" Music commands can now be used in any channel");
        }
        else
        {
            List<TextChannel> list = FinderUtil.findTextChannels(event.getArgs(), event.getGuild());
            if(list.isEmpty())
                event.reply(event.getClient().getWarning()+" No Text Channels found matching \""+event.getArgs()+"\"");
            else if (list.size()>1)
                event.reply(event.getClient().getWarning()+FormatUtil.listOfTChannels(list, event.getArgs()));
            else
            {
                s.setTextChannel(list.get(0));
                event.reply(event.getClient().getSuccess()+" Music commands can now only be used in <#"+list.get(0).getId()+">");
            }
        }
    }
    
}