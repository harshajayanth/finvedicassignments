package com.fnassignment.crud.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fnassignment.crud.model.Stock;
import com.fnassignment.crud.repos.StockRepository;

@Service
public class StockService {

	@Autowired
	private StockRepository stockrepository;
	
	public List<Stock> getAllStocks() {
		return stockrepository.findAll();
	}

	public Object getStockById(Long id) {
		return stockrepository.findById(id);
	}

	public void deleteStock(Long id) {
		stockrepository.deleteById(id);
	}

	public Stock addStock(Stock stock) {
		return stockrepository.save(stock);
	}

	public Object updateStock(Long id, Stock stockDetails) {
		Stock stock=stockrepository.findById(id)
				.orElseThrow(() -> new RuntimeException("Stock not found"));
		stock.setTicker(stockDetails.getTicker());
		stock.setCompanyName(stockDetails.getCompanyName());
		stock.setPrice(stockDetails.getPrice());
		return stock;
	}
	
}
