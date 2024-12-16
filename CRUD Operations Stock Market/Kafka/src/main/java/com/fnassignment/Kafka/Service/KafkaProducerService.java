package com.fnassignment.Kafka.Service;

import java.util.Properties;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import com.fnassignment.Kafka.Model.OrderDTO;


@Service
public class KafkaProducerService {
	
    private static final Logger logger = LoggerFactory.getLogger(KafkaProducerService.class);
	
	@Value("${kafka.server}")
	private String server;
	
	@Value("${kafka.topic}")
	private String topic;

	public String produceOrder(int count,OrderDTO dto) {
		
		Properties props=new Properties();
		props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,server);
		props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,StringSerializer.class.getName());
		props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,StringSerializer.class.getName());
		
		String key=dto.getStockSymbol();
		
		JSONObject value=new JSONObject();
		value.put("StockName",dto.getStockName());
		value.put("price",dto.getPrice());
		value.put("Capital",dto.getCapital());
		
		logger.info("{}",dto.getStockSymbol());
		
		
		try(KafkaProducer<String,String> producer=new KafkaProducer<>(props)){
			
			ProducerRecord<String,String> record=new ProducerRecord(topic,key,value.toString());
			
			for(int i=0;i<=count;i++) {
				producer.send(record);
			}
		}
		
		return "Kafka Item Produced : " + key+ " - " + value;
		
	}

}
