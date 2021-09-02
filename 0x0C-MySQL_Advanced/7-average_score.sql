-- 7. Average score
-- compute and store the average score for a student
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score)
                     FROM corrections
                     WHERE corrections.user_id = user_id);

    UPDATE users
        SET average_score = avg_score
        WHERE id = user_id;
END; //
DELIMITER ;