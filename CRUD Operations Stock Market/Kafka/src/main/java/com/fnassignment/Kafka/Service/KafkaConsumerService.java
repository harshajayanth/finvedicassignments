package com.fnassignment.Kafka.Service;

import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class KafkaConsumerService {
	

    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumerService.class);

    private final List<JSONObject> messages = new ArrayList<>();

    @KafkaListener(topics = "TradeOrder", groupId = "console-consumer-62622")
    public void consumeMessage(String message) {
        try {
            JSONObject jsonMessage = new JSONObject();
            jsonMessage.put("value", message);
            messages.add(jsonMessage);

            logger.info("Consumed message: {}", message);
        } catch (Exception e) {
            logger.error("Error while processing message: {}", e.getMessage(), e);
        }
    }
    
    public String consumeOrder() {
        return messages.toString() +" Count : "+ messages.size();
    }

}
