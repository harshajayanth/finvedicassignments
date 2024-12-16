package com.fnassignment.redis;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;


import redis.clients.jedis.Jedis;

@SpringBootApplication
public class RedisApplication {
	
	public static void main(String[] args) {
		SpringApplication.run(RedisApplication.class, args);
		
		 try(Jedis jedis=connectToRedis()){
		            
			        RedisModel model = new RedisModel();
			        RedisStock stock=new RedisStock();
			        
			        model.setSymbol("APL");
			        model.setStockName("Apple");
			        model.setPrice(150.00);
			        
			        stock.insertStock(model);
			        stock.getStock(model.getSymbol());
			        
			        model.setPrice(900.00);
			        stock.updateStock(model);
			        
			        stock.getStock(model.getSymbol());

		          //  redisStock.deleteStock(jedis,"APL");

		          //  redisStock.getStock(jedis,"APL");


	        }
		 finally {
			 System.out.print("");
		 }
	}
	
	  private static final String REDIS_HOST="localhost";
	  private static final int REDIS_PORT=6379;

	  	@Bean
	    public static Jedis connectToRedis() {
	        try {
	            Jedis jedis = new Jedis(REDIS_HOST, REDIS_PORT);
	            System.out.println("Successfully connected to Redis at " + REDIS_HOST + ":" + REDIS_PORT);
	            return jedis;
	        } catch (Exception e) {
	            System.out.println("Failed to connect to Redis: " + e.getMessage());
	            return null; 
	        }
	    }
}
