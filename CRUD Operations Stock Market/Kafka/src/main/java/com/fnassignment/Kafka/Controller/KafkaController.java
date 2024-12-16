package com.fnassignment.Kafka.Controller;

import java.util.Collections;
import java.util.List;
import java.util.Properties;
import java.util.Set;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.AdminClientConfig;
import org.apache.kafka.clients.admin.NewTopic;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.fnassignment.Kafka.Model.OrderDTO;
import com.fnassignment.Kafka.Service.KafkaConsumerService;
import com.fnassignment.Kafka.Service.KafkaProducerService;

import jakarta.annotation.PostConstruct;


@Controller
@RestController
@RequestMapping("/api")
public class KafkaController {

    private static final Logger logger = LoggerFactory.getLogger(KafkaController.class);

    @Autowired
    private KafkaProducerService kafkaProducerService;
    
    @Autowired
    private KafkaConsumerService kafkaConsumerService;

    @Value("${kafka.server}")
    private String server;

    @Value("${kafka.topic}")
    private String topic;

    Properties props = new Properties();

    @PostConstruct
    public void ConnectKafka() {
        props.put(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG, server);

        try (AdminClient adminClient = AdminClient.create(props)) {
            Set<String> topics = adminClient.listTopics().names().get();
            logger.info("Connected to Kafka at {}. Topics: {}", server, topics);
        } catch (Exception e) {
            logger.error("Unable to Connect to Kafka Server: {}", e.toString());
        }
    }

    @PostMapping("/createTopic")
    public String createTopic() {
        try (AdminClient adminClient = AdminClient.create(props)) {
            Set<String> topics = adminClient.listTopics().names().get();

            if (topics.contains(topic)) {
                logger.info(topic + " Topic Already Exists");
                return topic + " Topic Already Exists";
            }

            NewTopic newTopic = new NewTopic(topic, 3, (short) 1);
            adminClient.createTopics(Collections.singleton(newTopic)).all().get();
            logger.info("Topic '{}' created successfully.", topic);
            return "Topic '" + topic + "' created successfully.";
        } catch (Exception e) {
            logger.error(e.toString());
            return "";
        }
    }

    @PostMapping("/produce")
    public String produce(@RequestParam("count") int count,@RequestBody OrderDTO orderDTO) {
        try {
            AdminClient adminClient = AdminClient.create(props);
            Set<String> topics = adminClient.listTopics().names().get();

            if (!topics.contains(topic)) {
                logger.info(topic + " Topic Doesn't Exist. Create A topic");
                return topic + " Topic Doesn't Exist. Create A topic";
            }

            String response = kafkaProducerService.produceOrder(count,orderDTO);
            return response;
        } catch (Exception e) {
            logger.error("Error producing message: {}", e.toString());
            return "Unable to produce";
        }
    }

	@GetMapping("/consumer")
	public String consumer() {
		String result=kafkaConsumerService.consumeOrder();
		return "Consumed Order" + " : " + result;
	}
	
}
