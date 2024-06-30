package com.mars.MusicBot.services;

import com.mars.MusicBot.JMusicBot;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;

@Service
@RequiredArgsConstructor
public class run {

    private final JMusicBot jMusicBot;

    @PostConstruct
    public void start(){
        jMusicBot.startBot();
    }
}
