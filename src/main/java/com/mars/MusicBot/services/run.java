package com.mars.MusicBot.services;

import com.mars.MusicBot.JMusicBot;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;

@Service
public class run {
    @PostConstruct
    public void start(){
        JMusicBot.startBot();
    }
}
