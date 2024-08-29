package com.example.demo;
import org.springframework.core.io.InputStreamResource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
@RestController
@RequestMapping("/api/calculator")
public class CalculationController {
    @GetMapping("/coverage-csv")
    public ResponseEntity<InputStreamResource> downloadCodeCoverageCsv() throws IOException {
        // Path to the JaCoCo CSV file
        File csvFile = new File("target/site/jacoco/jacoco.csv");
        if (!csvFile.exists()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        InputStreamResource resource = new InputStreamResource(new FileInputStream(csvFile));
        HttpHeaders headers = new   HttpHeaders();
        headers.add(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=code-coverage-report.csv");
        headers.add(HttpHeaders.CONTENT_TYPE, "text/csv");
        return new ResponseEntity<>(resource, headers, HttpStatus.OK);
    }
}