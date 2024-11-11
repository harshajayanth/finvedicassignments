package com.fnassignment.redis;

import redis.clients.jedis.Jedis;

public class RedisStock {

    //INSERT INTO REDIS

    public void insertStock(Jedis jedis,String symbol,String stockName,double price){
        jedis.hset(symbol,"price",String.valueOf(price));
        jedis.hset(symbol,"stockName",String.valueOf(stockName));
    }

    // READ FROM REDIS

    public void getStock(Jedis jedis,String symbol){
        String price=jedis.hget(symbol, "price");
        String stockName=jedis.hget(symbol,"stockName");
        System.out.println("Stock : "+stockName+" Price : "+price);
    }

    //Update Redis

    public void updateStock(Jedis jedis,String symbol,double price){
        jedis.hset(symbol, "price",String.valueOf(price));
        String stockName=jedis.hget(symbol,"stockName");
        System.out.println("Stock : "+stockName+" Price Updated: "+jedis.hget(symbol,"price"));
    }

    //Delete Stock
    public void deleteStock(Jedis jedis,String symbol){
        jedis.del(symbol);
        System.out.println("Stock Deleted");
    }

}
