package com.fnassignment.Kafka.Model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class OrderDTO {

    @JsonProperty("StockName")
    private String stockName;

    @JsonProperty("StockSymbol")
    private String stockSymbol;

    @JsonProperty("price")
    private double price;
    
    @JsonProperty("Capital")
    private String Capital;

    // Getters and Setters
    public String getStockName() {
        return stockName;
    }

    public void setStockName(String stockName) {
        this.stockName = stockName;
    }

    public String getStockSymbol() {
        return stockSymbol;
    }

    public void setStockSymbol(String stockSymbol) {
        this.stockSymbol = stockSymbol;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
    
    public void setCapital(String Capital) {
        this.Capital = Capital;
    }

    public String getCapital() {
        return Capital;
    }
    
}
