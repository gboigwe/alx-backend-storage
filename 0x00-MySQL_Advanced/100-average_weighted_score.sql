-- An script that createe stored procedure
-- that computes and store the average weighted score
-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE total_weighted_s FLOAT;
    SET total_weighted_s = (SELECT SUM(score * weight) / SUM(weight)
                        FROM users AS U
                        JOIN corrections as C ON U.id=C.user_id
                        JOIN projects AS P ON C.project_id=P.id
                        WHERE U.id=user_id);
    UPDATE users SET average_score = total_weighted_s WHERE id=user_id;
END
$$
DELIMITER ;
