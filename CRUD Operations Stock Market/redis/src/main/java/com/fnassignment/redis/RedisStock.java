package com.fnassignment.redis;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import redis.clients.jedis.Jedis;


@RestController
@RequestMapping("/api/stockexchange")
public class RedisStock {
	
	private static int TTL_SECONDS=60;

	 private Jedis getJedisConnection() {
	        Jedis jedis = new Jedis("localhost", 6379); // Replace with your Redis host and port
	        return jedis;
	    }
	 
	 @Autowired
	 private RedisModel redisModel;
    //INSERT INTO REDIS

	@PostMapping
    public void insertStock(@RequestBody RedisModel redisModel){
		Jedis jedis = getJedisConnection();
        jedis.hset(redisModel.getSymbol(),"price",String.valueOf(redisModel.getPrice()));
        jedis.hset(redisModel.getSymbol(),"stockName",String.valueOf(redisModel.getStockName()));
        jedis.expire(redisModel.getSymbol(), TTL_SECONDS);
    }

    // READ FROM REDIS
    @GetMapping("/{symbol}")
    public void getStock(@PathVariable String symbol){
		Jedis jedis = getJedisConnection();
    	if(jedis.exists(symbol)) {
        String price=jedis.hget(symbol, "price");
        String stockName=jedis.hget(symbol,"stockName");
        System.out.println("Stock : "+stockName+" Price : "+price);
    	}
    	else {
            System.out.println(symbol+"expired");
    	}
    }

    //Update Redis

    @PutMapping
    public void updateStock(@RequestBody RedisModel redisModel){
		Jedis jedis = getJedisConnection();
        jedis.hset(redisModel.getSymbol(), "price",String.valueOf(redisModel.getPrice()));
        String stockName=jedis.hget(redisModel.getSymbol(),"stockName");
        jedis.expire(redisModel.getSymbol(), TTL_SECONDS);
        System.out.println("Stock : "+stockName+" Price Updated: "+jedis.hget(redisModel.getSymbol(),"price"));
    }

    @DeleteMapping("/{symbol}")
    //Delete Stock
    public void deleteStock(@PathVariable String symbol){
		Jedis jedis = getJedisConnection();
        jedis.del(symbol);
        System.out.println("Stock Deleted");
    }

}
