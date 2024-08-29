package com.example.demo;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest


class DemoApplicationTests {
	private final CalculatorService calculatorService = new CalculatorService();
	@Test
	public void testAdd() {
		assertEquals(5, calculatorService.add(2, 3));
		assertEquals(0, calculatorService.add(0, 0));
	}
	@Test
	public void testSubtract() {
		assertEquals(1, calculatorService.subtract(3, 2));
		assertEquals(-5, calculatorService.subtract(0, 5));
	}
	@Test
	public void testMultiply() {
		assertEquals(6, calculatorService.multiply(2, 3));
		assertEquals(0, calculatorService.multiply(0, 10));
	}
}