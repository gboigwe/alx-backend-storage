DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_weighted_s FLOAT;
    DECLARE total_weighted INT;

    -- Calculate the total weighted score and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_weighted_s, total_weighted
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = 
        CASE 
            WHEN total_weighted > 0 THEN total_weighted_s / total_weight
            ELSE 0
        END
    WHERE id = user_id;
END //

DELIMITER ;
