package com.fnassignment.crud.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Stock {
	
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private Long Id;
	
	private String ticker;
	private String companyName;
	private int price;
	
	
	public Long getId() {
		return Id;
	}
	
	public void setId(Long Id) {
		this.Id=Id;
	}
	
	 public String getTicker() {
	        return ticker;
	    }

	    public void setTicker(String ticker) {
	        this.ticker = ticker;
	    }

	    public String getCompanyName() {
	        return companyName;
	    }

	    public void setCompanyName(String companyName) {
	        this.companyName = companyName;
	    }

	    public int getPrice() {
	        return price;
	    }

	    public void setPrice(int price) {
	        this.price = price;
	    }
}
