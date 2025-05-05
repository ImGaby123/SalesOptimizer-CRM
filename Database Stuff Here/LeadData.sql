INSERT INTO crm.company (
    company_id,
    company_name,
    industry,
    website,
    company_email,
    yrs_in_industry,
    created_at,
    updated_at
)
VALUES (
    1,
    'OpenAI Solutions',
    'Technology',
    'https://openai.com',
    'contact@openai.com',
    5,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);


INSERT INTO `crm`.`contact`
(`contact_id`, `company_id`, `first_name`, `last_name`, `job_title`, `email`, `phone_number`, `gender`, `created_at`, `updated_at`)
VALUES
(201, 1, 'Alice', 'Smith', 'Marketing Manager', 'alice.smith@example.com', '09171234567', 'Female', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(202, 1, 'Bob', 'Johnson', 'Sales Lead', 'bob.johnson@example.com', '09181234567', 'Male', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(203, 1, 'Charlie', 'Lee', 'Product Manager', 'charlie.lee@example.com', '09191234567', 'Male', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(204, 1, 'Diana', 'Evans', 'HR Specialist', 'diana.evans@example.com', '09201234567', 'Female', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(205, 1, 'Ethan', 'Wong', 'CTO', 'ethan.wong@example.com', '09211234567', 'Male', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);




INSERT INTO `crm`.`leads`
(`lead_id`, `company_id`, `contact_id`, `source_id`, `engagement_score`, `lead_score`, `lead_quality`, `created_at`, `updated_at`)
VALUES
(1, 1, 201, 301, 72, 7, 'High', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 1, 202, 302, 50, 4, 'Medium', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 1, 203, 303, 90, 9, 'Very High', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 1, 204, 304, 30, 2, 'Low', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 1, 205, 305, 65, 6, 'Medium', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 1, 206, 306, 85, 8, 'High', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 1, 207, 307, 15, 1, 'Very Low', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(8, 1, 208, 308, 45, 5, 'Medium', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(9, 1, 209, 309, 95, 10, 'Very High', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(10, 1, 210, 310, 55, 6, 'Medium', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
