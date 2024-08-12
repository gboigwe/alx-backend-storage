-- Creating a stored procedure ComputeAverageScoreForUser
-- that computes a student new correction
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN pro_user_id INT
)
BEGIN
    DECLARE var_avg_score DECIMAL(10,2);

    -- Compute the average score
    SELECT AVG(score) INTO var_avg_score
    FROM corrections
    WHERE user_id = pro_user_id;

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = var_avg_score
    WHERE id = pro_user_id;
END //

DELIMITER ;
