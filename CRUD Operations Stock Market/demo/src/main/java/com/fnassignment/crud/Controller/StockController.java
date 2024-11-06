package com.fnassignment.crud.Controller;

import com.fnassignment.crud.model.Stock;
import com.fnassignment.crud.service.StockService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/stocks")
public class StockController {

    @Autowired
    private StockService stockService;

    // Get all stocks
    @GetMapping
    public List<Stock> getAllStocks() {
        return stockService.getAllStocks();
    }

    // Get a stock by ID
    @GetMapping("/{id}")
    public ResponseEntity<Object> getStockById(@PathVariable Long id) {
        return ResponseEntity.ok(stockService.getStockById(id));
        
    }

    // Create a new stock
    @PostMapping
    public Stock createStock(@RequestBody Stock stock) {
        return stockService.addStock(stock);
    }

    // Update an existing stock
    @PutMapping("/{id}")
    public ResponseEntity<String> updateStock(@PathVariable Long id, @RequestBody Stock stockDetails) {
    	stockService.updateStock(id, stockDetails);
        return ResponseEntity.ok("Updated");
    }

    // Delete a stock
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStock(@PathVariable Long id) {
        stockService.deleteStock(id);
        return ResponseEntity.noContent().build();
    }
}
