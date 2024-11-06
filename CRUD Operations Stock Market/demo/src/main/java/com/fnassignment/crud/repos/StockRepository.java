package com.fnassignment.crud.repos;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.fnassignment.crud.model.Stock;

@Repository
public interface StockRepository extends JpaRepository<Stock, Long> {
}

