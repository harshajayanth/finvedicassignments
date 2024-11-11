package com.fnassignment.redis;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import redis.clients.jedis.Jedis;

@SpringBootApplication
public class RedisApplication {

	public static void main(String[] args) {
		SpringApplication.run(RedisApplication.class, args);
		
		 try(Jedis jedis=connecttoRedis()){
	            System.out.println("Connected to Redis : " + jedis);

	            RedisStock redisStock=new RedisStock();

	            redisStock.insertStock(jedis,"APL","Apple",150.00);

	            redisStock.getStock(jedis,"APL");

	            redisStock.updateStock(jedis, "APL",600.000);

	            redisStock.getStock(jedis,"APL");

	            redisStock.deleteStock(jedis,"APL");

	            redisStock.getStock(jedis,"APL");

	        }
	        catch(Exception e){
	            System.out.print("Connection Failed");
	        }
	}
	
	  private static final String REDIS_HOST="localhost";
	    private static final int REDIS_PORT=6379;

	    private static Jedis connecttoRedis(){
	        return new Jedis(REDIS_HOST,REDIS_PORT);
	    }

}
